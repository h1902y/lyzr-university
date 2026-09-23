# Thinkific control via Claude Code — build plan (parked 2026-06-15)

> Goal: drive Thinkific end-to-end from Claude Code sessions, using the `cli-printing-press` tool (installed; turns an API spec or captured traffic into a Go CLI + MCP bundle). Parked mid-exploration — this doc is the resume point.

## The decision (2026-06-15)

Build in **two layers**, and **start with the content layer** (course/chapter/lesson creation + video upload), deferring the ops layer. This deliberately tackles the powerful-but-fragile frontier first.

| Layer | Covers | Source | Maintenance |
|---|---|---|---|
| **Content** (do first) | create course / chapter / lesson, **upload video** | Thinkific's **internal, undocumented API** — captured by sniffing the admin UI | **Higher** — fragile |
| **Ops** (deferred) | enrollments, users, coupons, promotions, groups, orders, reporting | Thinkific **public Admin API** (official OpenAPI) | Near-zero — stable |

## Why two sources (the ceiling)

Thinkific's **public** Admin API is GET-only for courses/chapters/contents — **no content authoring, no video upload, on any plan.** The admin **web app** does it via internal HTTP endpoints not in the public spec. `cli-printing-press` breaks that ceiling by **sniffing the admin UI's traffic** and generating a CLI that replays those internal calls.

## How to execute the content CLI (resume here)

**Capture route = HAR (chosen).** Agent-driven browsers (agent-browser, browser-use, the chrome-devtools MCP) all launch *isolated* Chrome profiles where you're **not logged into Thinkific** — so they don't work for this. The one true "real-browser" agent option is the **Claude for Chrome** extension (not connected in this session; would need separate install). HAR sidesteps all of it: you use your own logged-in Chrome.

Steps:
1. In your normal logged-in Chrome admin, open DevTools → **Network**; tick **Preserve log** + **Disable cache**; clear the log.
2. Walk the full flow slowly: create a test course (`_sniff-test delete-me`) → add chapter → add lesson → **upload a small .mp4, let it fully finish** → save.
3. Right-click → **Save all as HAR with content** → save the `.har`.
4. Re-invoke the `printing-press` skill (or run directly):
   ```
   cli-printing-press browser-sniff --har <capture.har> --name thinkific-content \
     --output <run>/research/thinkific-content-spec.yaml \
     --analysis-output <run>/discovery/traffic-analysis.json
   cli-printing-press generate --spec <that-spec> --spec-source browser-sniffed \
     --traffic-analysis <run>/discovery/traffic-analysis.json --force --lenient --validate
   ```
5. Inspect the discovered upload handshake; **video upload likely needs hand-coding** (signed-URL → PUT bytes to storage → notify Thinkific → attach to lesson; often chunked/resumable).

## Caveats to go in eyes-open (the real ongoing cost)

- **Re-capture cycle (reactive, not scheduled):** internal endpoints aren't contractual. When Thinkific ships a UI/backend change, the affected command breaks → re-capture that flow's HAR + regenerate. Unpredictable timing.
- **Auth refresh (recurring):** the HAR captures a *session cookie* that expires (and gets stripped from the CLI as a secret). Internal endpoints are **cookie/session auth, not a stable API key**, so the CLI needs a fresh-session step periodically (see the `press-auth` companion pattern). This is the main day-to-day friction.
- **Runs against the live site:** the capture creates real content on university.lyzr.ai — use a throwaway course, delete after.
- Video upload is the part most likely to be partial after generation.

## The deferred ops layer (stable, low-maintenance — pick up anytime)

Already scaffolded in a printing-press run on **2026-06-15** from the official spec:
- Run state: `~/printing-press/.runstate/lyzr-402bfbd1/runs/20260615-153007-thinkific1/`
  - `thinkific-admin-api-v1.yaml` (official OpenAPI, ~40 ops), research brief, absorb manifest, `research.json`.
- Auth: `THINKIFIC_API_KEY` + `THINKIFIC_SUBDOMAIN` (headers `X-Auth-API-Key` / `X-Auth-Subdomain`); **needs the Grow plan** (≥$199/mo) for API access; 120 req/min limit.
- Planned commands: all ~40 endpoints auto-generated + 5 transcendence commands that map to the GTM engine — `enrollments bulk` (Ring-1 auto-enroll), `report completion` (weekly-metrics), `since`, `stale`, `cert-ready` (cert-share loop). See [[project-lyzr-university-gtm]].
- To build it: `cli-printing-press generate --spec <that yaml> ...` — it's a clean, stable build whenever you want the ops/automation surface.

## Prereqs checklist before resuming the content CLI
- [ ] A throwaway test course is OK to create on university.lyzr.ai
- [ ] A small sample `.mp4` to upload during capture
- [ ] (For the ops layer instead) Grow plan active + API key generated
