# University Pulse

Weekly Lyzr University analytics digest → Slack. Reads Thinkific enrollments, computes the learner
funnel + content pipeline week-over-week, and posts to a Slack channel via an Incoming Webhook.
Runs autonomously in **GitHub Actions** (no local machine needed).

## Metrics

The digest is organized into four labelled sections, each carrying week-over-week (WoW) change:

- **📈 Growth:** unique learners and total enrollments, each rendered as `value (+Δ, ▲N%)`.
- **🎯 Engagement:** "≥1 lesson" (did `%>0`) as a share of enrolled, plus active-this-week. The ≥1-lesson rate carries the WoW growth of the engaged count.
- **🏅 Certifications:** total completions (the cert proxy) with WoW % and cert rate (completed ÷ enrolled), then a by-collection split (ADK · Studio · Legacy) with absolute weekly deltas.
- **📚 Content pipeline:** live course + lesson counts, and "+courses / +lessons shipped this week".

Below the sections, a **per-course table**: live-since (age), enrolled (+new), ≥1-lesson, completed with its weekly cert delta (`Done(+Δ)`), completion rate, active 7d. The 6 live courses are listed; everything else rolls into a "Legacy & retired" line.

**Certificates = completions.** The Thinkific API exposes no certificate-issuance data, so completion is the proxy (a footnote in the digest says as much). **WoW % is hidden when the prior week's base is < 5**, to avoid noisy percentages off a tiny base — the absolute delta still shows.

## The "week" window

Everything "this week" is measured **since the last snapshot** (snapshot-to-snapshot), not a fixed
calendar week — so mid-week uploads and any missed run both behave correctly. The first run is a
**baseline** (existing courses are the starting line, not "shipped this week"). The job runs **Monday
13:00 IST**, after the Monday-morning course-upload slot, so same-week uploads are captured.

## Run

```bash
node pulse.mjs --dry-run       # compute + print, no Slack, no snapshot write
node pulse.mjs --channel-test  # post once to the webhook, no snapshot write
node pulse.mjs                 # post + write snapshot (CI commits it back)
```

## Config & secrets

- `config.json` — live course IDs/names/collection + per-course launch dates (`liveSince`). New courses
  auto-derive "live since" from when they first appear in a snapshot.
- Secrets (GitHub Actions): `THINKIFIC_TOKEN` (OAuth Bearer, read), `SLACK_WEBHOOK_URL` (Incoming Webhook).
  Locally, `THINKIFIC_TOKEN` falls back to `TOKEN=` in `../.env`.
- `snapshots/` — one JSON per week, committed by CI = durable WoW + content-pipeline state.
