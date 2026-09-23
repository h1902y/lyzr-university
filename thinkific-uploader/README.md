# thinkific-uploader

Full-automation **publish** step for Lyzr University courses. Reads the same artifacts the rest of
the pipeline already produces — `thinkific-upload/` (named media) + `catalog-demo/catalog-data.json`
(metadata) + `catalog-demo/banner/exports/` (card images) — and drives the Thinkific admin **Course
Builder** with Playwright to: create the course → fill subtitle/description → upload the card image
→ add video + PDF lessons in order → set price (Free) → assign collection → publish.

It exists because **Thinkific's public API is read-only for authoring** (verified 2026-06-17: every
`POST/PUT/DELETE` on courses/chapters/lessons returns `404 no Route matched`). The admin UI is the
only programmatic path, so we drive it.

## The one honest caveat
The bot targets the admin **UI**, so its locators can drift between Thinkific releases. They're
written as **best-effort semantic locators** (role/label/text) that often work as-is — but the first
real run is a short **selector-tuning pass**: when a step misses, the tool screenshots the page and
prints the failing `step:`, so you (or Claude, from the screenshot) fix that one locator in
`src/thinkific.mjs` (look for `// CAPTURE:`) and re-run — it resumes where it left off. `npm run
codegen` opens Playwright's recorder against the live admin to grab exact locators.

## Setup (once)
```bash
cd lyzr-university/thinkific-uploader
npm install
npx playwright install chromium
npm run auth        # opens Chrome; log in by hand (Cloudflare + 2FA). Session is saved, never your password.
```

## Run
```bash
npm run plan                    # dry run — full plan, no browser. ALWAYS look at this first.
ONLY="Design" npm run upload    # upload just the Design & Create course
npm run upload                  # upload every bundle course not already done
PUBLISH=true npm run upload     # also flip live courses to Published (default leaves them draft)
```
- **Idempotent**: every finished lesson is recorded in `progress.json`; re-run to resume (after a
  crash, a fixed locator, or added content). Finished lessons are skipped.
- **Existing courses**: if a course with the same name already exists, it opens it instead of making
  a duplicate (so it won't recreate the cleanup mess).
- **Headed by default** so you can watch and clear any Cloudflare re-challenge mid-run.

## After uploading — verify
```bash
python3 ../../.agents/skills/descript-to-thinkific/scripts/thinkific_verify.py
```
Confirms the live course matches the bundle (count, pairing, order, status) — closes the loop.

## What it sets, per course (from catalog-data.json)
| Field | Source |
|---|---|
| name, subtitle, description | catalog course entry |
| card image (thumbnail) | `banner/exports/<course>-card-760x420.png` |
| price = Free | default (all Lyzr University courses) |
| collection | catalog `collection` (Tracks/Modules/Functions) — best-effort; assign by hand if it misses |
| publish vs draft | catalog `status` (`live` → publish, only with `PUBLISH=true`) |
| chapters → lessons | bundle folder: `NNa <Title>.mp4` (video) + `NNb <Title> Notes.pdf` (PDF), in order |

## Files
- `src/config.mjs` — paths + env (defaults to `lyzr` subdomain, `../thinkific-upload`, `../catalog-demo`).
- `src/bundle.mjs` — bundle → course/chapter/lesson tree (skips placeholder-only coming-soon folders).
- `src/catalog.mjs` — match each course to its catalog metadata + card image.
- `src/thinkific.mjs` — the admin page object (**the file you tune** when a locator misses).
- `src/upload.mjs` — orchestrator (dry-run, resume, screenshots on failure).
- `src/auth.mjs` — one-time manual login into the persistent profile.
- `src/codegen.mjs` — Playwright recorder against the live admin, for capturing exact locators.

State (`.browser-profile/`, `auth.json`, `progress.json`, `screenshots/`, `.env`, `node_modules/`)
is gitignored — including the profile, which holds your session.
