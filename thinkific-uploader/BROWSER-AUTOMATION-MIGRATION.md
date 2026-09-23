# Browser-automation migration plan — Thinkific tooling

_Drafted 2026-06-30 after validating the hypothesis with live test runs._

## Why this exists

`thinkific-uploader/` drives the Thinkific admin **UI** with Playwright because Thinkific's public
API is read-only for authoring. This session exposed the two recurring taxes of that approach:

- **Locator drift** — 3 selectors broke in a single upload (publish menu, unarchive flow, community
  image "Save") and had to be rediscovered by hand.
- **Auth fragility** — the login is behind Cloudflare Turnstile; a manually-authed persistent
  profile is the workaround, but its `cf_clearance`/session **expires within hours**.

The question we tested: can the **Claude Chrome extension** (agentic) and/or a **browser MCP**
replace or augment this?

## Test runs (validated this session)

| Test | Result |
|---|---|
| `chromium.connectOverCDP` → Chrome 149 | ✅ connected + drove the page in **<7 s**. Driving Chrome deterministically is a solved, fast problem. |
| `@playwright/mcp` / `chrome-devtools-mcp` exist & installable | ✅ `0.0.77` / `1.4.0` on npm; Chrome 149 present. |
| Naive **headless** CDP launch on the saved profile → `/manage/courses` | ❌ redirected to **`/users/sign_in`** — Cloudflare flagged it. |
| **Headed** CDP launch + `--disable-blink-features=AutomationControlled` | ❌ still `sign_in`. |
| Proven `launchPersistentContext` (channel:chrome + anti-automation) | ❌ **also** `sign_in` — i.e. the saved session had **expired** since the morning's upload. |
| Claude-in-Chrome via `/chrome` | ❌ **no browser MCP/tools attached** to the CLI session (verified via `claude mcp list` + tool search). Pairing not connecting yet. |

### The headline finding
**The bottleneck was never the driver — it's auth.** CDP/Playwright drive Chrome trivially. What
breaks us is Cloudflare + a session that expires in hours. So the migration's real prize is
*"stop re-fighting auth,"* not *"a smarter clicker."*

## Target architecture — two layers

| Layer | Job | Tool | Why |
|---|---|---|---|
| **Explore / self-heal** | find a drifted selector, one-off tasks, "what changed in the admin UI" | **Claude-in-Chrome extension** | Drives *your real, already-logged-in* Chrome → **no Cloudflare/auth dance**; adapts to UI changes. Agentic = perfect for discovery. |
| **Deterministic batch** | the repeatable 1.4 GB upload: create → upload → rename → publish → verify | **keep the Playwright code** (`src/*.mjs`) | Free, headless, resumable (`progress.json`), version-controlled, identical every run. Agentic can't give you that (re-reasons each run, costs tokens, not cron/headless-friendly). |

The extension is **above** Playwright, not instead of it.

## Why NOT rewrite the batch into an MCP
- The page object (`thinkific.mjs`) is ~600 lines of hard-won selectors + the Filestack file-dialog
  trick + API-polling for upload completion. It **works**. Porting it to `chrome-devtools-mcp` tool
  calls is high-risk, ~0-ROI churn.
- A browser MCP launching its *own* Chrome hits the **same Cloudflare wall** we just proved (naive
  launch → `sign_in`). The MCP only helps if it **attaches to your real, authed Chrome** — which is
  exactly what the extension already does, better.

## Migration steps (phased, low-risk first)

- **Phase 0 — connect the extension.** Get `/chrome` actually exposing tools (see Blocker). Until
  then, nothing below is testable.
- **Phase 1 — adopt the extension as the self-heal/explore layer.** Replace the throwaway
  `probe.mjs` scripts: when a locator breaks, point Claude-in-Chrome at the live page to find the new
  selector, then patch `thinkific.mjs`. Immediate value, zero risk to the batch. _This kills the
  locator-drift tax._
- **Phase 2 — kill the auth tax.** Either (a) drive uploads through the extension's real-session
  Chrome for the click-steps, or (b) add a **session-freshness guard** to the Playwright flow
  (detect `sign_in` → prompt for a quick re-auth) instead of failing mid-run. _This kills the
  session-expiry tax._
- **Phase 3 — keep deterministic code for the batch.** No rewrite. Optionally evaluate
  `chrome-devtools-mcp` **only** if it can CDP-attach to the everyday Chrome (reuse real session);
  otherwise it's not worth it.
- **Phase 4 — standardize + document.** Two-layer model in the README; a "selector drifted → self-
  heal with the extension → patch + resume" runbook; note in `[[project-thinkific-uploader]]`.

## Recommendation (opinionated)
1. **Keep Playwright for the batch.** It's the correct deterministic tool; migrating it away is a
   loss.
2. **Use Claude-in-Chrome for exploration, self-healing, and auth-free one-offs** — that's precisely
   where our pain is (drift + session expiry) and precisely its strength.
3. Highest-value single change: the **self-heal loop** (extension finds new selector → patch script
   → resume). It dissolves both taxes we hit today.

## Blocker to clear first
`/chrome` ran but no browser server/tools attached to this CLI session. To unblock, check:
- Extension installed **and signed into the same Claude account**, Chrome/Edge open.
- Re-run `/chrome` (or relaunch `claude --chrome`); confirm a connect/pairing prompt in the browser.
- Plan/version gating (it's beta) and CLI version.
- Then `claude mcp list` should show a chrome/browser entry and tool search should surface
  `navigate`/`click`/`read`-style tools.
