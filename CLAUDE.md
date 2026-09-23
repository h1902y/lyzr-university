# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in `lyzr-university/`.

## What this is

The Lyzr University programme — **content + planning only, no app**. The LMS is **Thinkific** (handles courses, cohorts, certs, payments, student management). The decision to use Thinkific was deliberate — do **not** suggest building a custom LMS, custom auth, or a Next.js app for Lyzr University unless the user explicitly asks.

**Canonical name: "Lyzr University"** (renamed 2026-05-28). "Lyzr Academy" is the **former** name — use **Lyzr University** in all new copy and learner-facing surfaces; don't introduce "Academy" into anything new. The on-disk folder was renamed to `lyzr-university/` on 2026-06-03. Note that the Google Drive root folder still carries the old name until renamed; its ID/URL is unaffected by the rename.

## Strategy of record

`content-strategy.md` is canonical. Read it before making structural suggestions. Key shape (recategorized 2026-05-28 — **the old "Developer / Business track" model is retired**):

- Courses are categorized on **three Thinkific Category axes**: **Product** (Architect / Studio / ADK — the product *is* the audience, replacing Dev/Business tracks), **Module** (12 topics: Getting Started, Agents, Models, Memory, Knowledge & RAG, Tools & Integrations, Orchestration, Voice, Responsible AI, Evaluation, Deployment, Administration), and **Use-Case Vertical** (6 domain-strategy courses: HR, Marketing, Sales, Procurement, VC, AI Strategy — product-agnostic, *not* product courses).
- Each product has a **Foundations** entry course + **Module** depth courses. Multi-assign Categories; **Learning Paths deferred.**
- **Stacking certs**: Foundation (product Foundations) → Specialist (per Module, product-neutral) → Expert. Path certs deferred with Learning Paths; "Lyzr Agentpreneur" founder cert tops the ladder.
- Industry flavoring of product courses = demo-example library (later phase), distinct from the Use-Case Vertical strategy courses.
- Full grid + course→category mapping: `~/.claude/plans/yes-lets-go-mellow-dongarra.md` and [[project-lyzr-academy-catalogue]] memory.

## In scope right now

Only one course is in production: **Lyzr for Developers** (aka **SDK Track**) — teaches the Lyzr Agent Development Kit (ADK) Python module. **19 lessons / 4 modules**:

1. Foundations (01–06) — lesson 06 is *Project: Multi-provider chatbot*
2. Multimodal (07–09) — lesson 09 is *Project: Creative assistant*
3. Knowledge & Memory (10–15) — lesson 15 is *Project: Document Q&A bot*
4. Tools & Workflows (16–19) — four how-to lessons: Why tools matter, Writing local tools, Agent context, Multi-step workflows (no project capstone)

Lessons `06 / 09 / 15` are **project capstones** (longer build-alongs), not standard lessons; Module 4 has none. Thinkific lesson titles use the canonical prefix `SDK Track: NN - <title>`. Order is sequential — later lessons assume earlier ones.

> **Module 4 finalized at 4 lessons (2026-06-01).** The earlier curriculum's "Backend integrations" and the "Project: Workflow agent" capstone were never recorded and were dropped (the series runs v16→v19); lesson 18 is **Agent context**, not the earlier-planned "Context variables". The ADK product ships as **4 complete courses**; `04 ADK Tools and Workflows` is no longer partial.

## Folder map

| Folder | Role |
|---|---|
| `content-strategy.md` | **Canonical** strategy of record (root). Read before structural suggestions. |
| `planning/` | Planning + ops docs: `content-backlog-tracker.md`, `video-recording-tracker.md`, `lyzr-university-copy.md` (about-us/marketing copy variants). |
| `catalog-demo/` | Runnable web demo (no build step): `course-catalog-demo.html` + `catalog-styles.css` + data JSONs + `thumbnail/` generator. Serve with `python3 -m http.server` from this folder. |
| `SDK-track/` | Course source: `transcripts/` (`NN-<slug>.txt`), `notes/` (authored `.md` + `_render_pdfs.py`), `raw/` (Descript JSON). Recordings on Descript (links in `SDK-track/README.md`). |
| `thinkific-upload/` | **Collection-organized** upload bundle: `1 - Tracks/<product>` · `2 - Modules` · `3 - Functions`, every course a numbered leaf folder (01–34). Each leaf = one Thinkific course — select all, drag into the Content Uploader. 3 live ADK courses (`01`–`03`); coming-soon courses hold 4 placeholder slide PDFs each; `04 …(Partial)` holds recorded lesson 16. `_UPLOAD-GUIDE.md` is the per-course checklist; `manifest.csv` indexes real lesson media only. See its `README.md`. |
| `landing/` | Landing-page copy (`academy.md`, `sdk-track.md`). |
| `landing-images/` | Visual assets + HTML mockups for landing pages. |
| `jds/` | Job descriptions (instructor, devrel content lead, AI-native video editor). |
| `archive/` | Superseded docs kept for history (e.g. the April 2026 content-architecture spec — old Dev/Business model). |

## Course production pipeline

Turning a Descript recording into a Thinkific upload is a repeatable, easy-to-get-subtly-wrong
workflow — it's codified in the **`descript-to-thinkific` skill** (`.agents/skills/descript-to-thinkific/`).
Use it whenever the user drops Descript share links or asks to add lessons / make lesson notes /
package for Thinkific. The pipeline: identify the lesson from the Descript page title → bring in the
transcript JSON + MP4 (account-side export — only the title is fetchable from the share page) →
flatten the transcript (fixes the "Lizza"→"Lyzr" ASR error) → author lesson-notes markdown to a
strict contract → render a branded PDF via headless Chrome (`SDK-track/notes/_render_pdfs.py`) →
drop `NNa <Title>.mp4` + `NNb <Title> Notes.pdf` into the chapter folder and rebuild `manifest.csv`.
The skill bundles the transcript-flatten and manifest scripts and documents the notes-markdown
contract and the 19-lesson → module → chapter map.

## Known content quirks

- **ASR renders "Lyzr" as "Lizza"** in transcripts. Find/replace before any learner-facing use (the `descript-to-thinkific` flatten script does this automatically).
- **Lesson 08 was renamed** (2026-05-18) from "File inputs" → **"File generation"** to match the recording; file-inputs use case is covered later in the RAG / document-ingestion lessons (10–12).
- **Lessons 01–11 are recorded** on Descript; **12–21 are not yet recorded** (verify against `SDK-track/README.md` before claiming current state).

## Coordination layer (Google Drive)

Drive is the **collaboration** layer; local files are the source of truth. Owner: `harshit.choudhary@lyzr.ai`. Root folder: `Lyzr Academy` (`1ehiIsik3QupHLAtnZDmuuPK3lYvOdo50`). Full ID map is in memory (`reference_lyzr_academy_drive.md`).

- **Master Tracker** sheet (`1fcyno0qMy7N7_pi2DddOqs8SxKdgp8aj-vXqKE5czo8`) is the primary source of truth for catalog + lesson + todo state (one tab, 3 stacked blocks). Update it when state changes.
- **Running Notes Doc** — append new decisions at the top with a date stamp; don't edit historical entries.
- Drive folder is **not** for MP4/PDF archival — uploads go straight from local `thinkific-upload/` to Thinkific.
- The standalone Lesson Tracker sheet was **archived 2026-05-13**; do not read/edit it or duplicate its rows into the Master Tracker.

## Work tracking

- **Operational tracking** (lesson recording/upload state, course catalog status, day-to-day todos) goes in the Drive Master Tracker.

## Brand

Per parent `CLAUDE.md`, `agentpreneur/lyzr-brand.md` is the canonical Lyzr brand guide and applies to all Lyzr University-facing surfaces (landing pages, Thinkific course art, slides).
