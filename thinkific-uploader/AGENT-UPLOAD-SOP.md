# Agent SOP — push a Lyzr University course to Thinkific (browser-use / Claude-in-Chrome)

A natural-language, **intent-based** procedure for an agentic browser (Claude-in-Chrome, computer-use)
to publish one course bundle to the Thinkific admin, riding the human's already-logged-in session.

**Why intent-based, not selectors:** selectors drift (3 broke in one run on 2026-06-30); intents
("open the course's action menu, choose Publish") survive UI changes. Correctness is **not** assumed
from the clicks — it's confirmed by the deterministic API verifier in Step 7.

> **Inputs** (from the offline pipeline — produced before any browser work):
> - Bundle folder: `thinkific-upload/1 - Tracks/<Product>/<NN Course>/` with paired `NNa <Title>.mp4`
>   + `NNb <Title> Notes.pdf`.
> - Metadata: the course's `catalog-demo/catalog-data.json` entry (name, subtitle, description,
>   `status`, `collection`).
> - Card image: `catalog-demo/banner/exports/<slug>-card-760x420.png`.
> - Account: `university.lyzr.ai/manage` (you are already logged in — do not attempt login; if you
>   land on a sign-in or Cloudflare page, **stop and ask the human** to clear it).

## Guardrails (this is a live production LMS)
- **Read before you write.** Confirm the course doesn't already exist (search `/manage/courses`)
  before creating — avoid duplicates.
- **One course at a time.** Finish + verify before starting the next.
- **Stop-and-ask** on: any login/Cloudflare/2FA wall, a destructive prompt (delete/archive you didn't
  intend), or if a step's outcome looks wrong. Never guess on irreversible actions.
- **Don't touch** other courses, the `TEMPLATE`, or anything outside the target course.

## Steps (each ends in a CHECK the agent must confirm)

1. **Find or create the course.**
   - Search `/manage/courses` for the exact name. If it exists → open it (adopt it; do not duplicate).
   - Else create it by **duplicating the `TEMPLATE` course** (inherits pricing/collection/card/landing
     design). `TEMPLATE` is normally **archived** → if it's not in the active list, open the
     **Archived** tab, **Unarchive** it (confirm the modal), then duplicate from the active list.
     The new course appears as `Copy of TEMPLATE`.
   - **CHECK:** you are on a single course editor whose name you control.

2. **Set details.** Name, subtitle, description from the catalog entry. Upload the **card image**
   (Filestack picker → choose file → the crop dialog's commit button may be **"Save"**, not "Upload").
   - **CHECK:** name + card visible on the course.

3. **Add the lessons.** Open the curriculum, bulk-upload the bundle folder's files. Each file becomes
   one lesson; the `NNa…mp4` / `NNb… Notes.pdf` naming makes the video sort directly above its notes.
   Videos transcode for minutes — **wait for the count to reach the expected total** (it can sit at 0
   then jump). Don't close the tab mid-upload.
   - **CHECK:** lesson count = (videos + notes) expected; video sits above its notes for each pair.

4. **Rename lessons** to clean titles (strip the `NNa/NNb` prefix; notes = "<Title> Notes").
   - **CHECK:** titles read cleanly, order preserved.

5. **Pricing + collection.** Free; assign the catalog `collection` (Track/Module/Function) if not
   inherited from TEMPLATE.
   - **CHECK:** price = Free; collection set.

6. **Publish** (only if catalog `status: live`). Course editor → **Action Menu** → **"Publish now"**
   → confirm the **"Publish"** modal. (A published course's menu then shows "Unpublish".)
   - **CHECK:** menu shows "Currently published".

7. **Verify deterministically (the real definition of done).** Hand back to code:
   ```
   python3 ../../.agents/skills/descript-to-thinkific/scripts/thinkific_verify.py "<NN Course folder>"
   ```
   PASS = counts, pairing, order, names, status all match the manifest. **The task is not done until
   this passes.** If it flags a gap, fix that specific item in the UI and re-verify.

8. **Report the paths you used** (which menu, which button labels) so the deterministic
   `src/thinkific.mjs` page object can be refreshed — keeps the cheap headless/cron path current.

## Known gotchas (expect these; they're why selectors drift)
- `TEMPLATE` is intentionally **archived** between uses → unarchive before duplicating, re-archive
  after if you want the active list tidy.
- Filestack image crop commit is **"Save"** for some surfaces, "Upload" for others — read the dialog.
- Community products live under `/manage/communities/<id>/settings` ("Community image" → first
  "Upload"), **not** under courses, and aren't in the public API — verify those visually.
- The public API is **read-only for authoring** — it can verify (Step 7) but cannot create/fix.

## Where this fits
Offline pipeline (deterministic) → **this SOP (agentic browser push)** → API verify (deterministic).
The agent absorbs auth + UI drift; the verifier guarantees the outcome. See
`BROWSER-AUTOMATION-MIGRATION.md` for the rationale and the test runs that motivated it.
