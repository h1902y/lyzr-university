# Studio Track — Lyzr University

The product-facing track for **Lyzr Agent Studio** (the AI Studio at `studio.lyzr.ai`). Organized around the **agent lifecycle** a builder lives — **Build → Govern → Test → Deploy → Monitor** — across 6 phases + a Foundations journey course (14 courses / 71 lessons total). Shipped on **Thinkific**.

This folder holds the **course source** (raw transcript JSON, flattened transcripts, authored notes + renderer), mirroring `SDK-track/`. Plan of record: `../planning/studio-track-plan.md`.

## Layout

```
Studio-track/
├── README.md                    (this file)
├── transcripts/
│   └── NN-<slug>.txt            Plain-text transcript per lesson
├── notes/
│   └── NN-<slug>.md             Authored lesson notes (+ _render_pdfs.py, Studio-branded)
└── raw/
    └── NN-<slug>.json           Descript transcript JSON (segments + word-level timings)
```

Transcripts are word-level segments joined with spaces — readable but not punctuated. **ASR mangles names**: "Lyzr" → *Lizra / Lizer / Laser / Leiser / Lyserv*, and "Felipe" → *Filippo / Philippe*. Fix before any learner-facing use (the flatten script only catches the "Lizza" variant — review by hand). The `## Transcript` section of each notes file is kept as source-of-truth but is **excluded from the rendered PDF**.

## Course 1 — Studio: The Agent Lifecycle (Foundations)

*The whole agent lifecycle on one agent — a Northwind customer-support agent carried from a blank page to live and monitored.* 7 lessons · ~56 min · instructor Felipe. Upload folder: `../thinkific-upload/1 - Tracks/Studio/06 Studio The Agent Lifecycle (Coming Soon)/`.

| # | Title | Studio feature | Descript | Transcript |
|---|---|---|---|---|
| 01 | Welcome to Agent Studio & the lifecycle | Home · Agent Registry | [view](https://share.descript.com/view/QSwoPpR6hKL) | [01-welcome-agent-studio-lifecycle.txt](transcripts/01-welcome-agent-studio-lifecycle.txt) |
| 02 | Build — choose a type & create an agent | Create Agent → Agent | [view](https://share.descript.com/view/r0i0W0qxzAh) | [02-build-choose-type-create-agent.txt](transcripts/02-build-choose-type-create-agent.txt) |
| 03 | Equip — model, tool, knowledge | Connections → Models, Tools · Knowledge → KB | [view](https://share.descript.com/view/GobPzBquAVF) | [03-equip-model-tool-knowledge.txt](transcripts/03-equip-model-tool-knowledge.txt) |
| 04 | Govern — add guardrails | Responsible AI · Guardrails | [view](https://share.descript.com/view/c1cv27a45SV) | [04-govern-add-guardrails.txt](transcripts/04-govern-add-guardrails.txt) |
| 05 | Test — run it in the Playground | Playground · Monitoring → Traces | [view](https://share.descript.com/view/lJdFYCeMQq9) | [05-test-simulation-engine.txt](transcripts/05-test-simulation-engine.txt) |
| 06 | Deploy — ship it | Deploy · Lyzr App Store | [view](https://share.descript.com/view/s9Pgt7FDngv) | [06-deploy-ship-it.txt](transcripts/06-deploy-ship-it.txt) |
| 07 | *Project:* one agent, full lifecycle | Monitoring → Traces (+ all above) | [view](https://share.descript.com/view/W02dpgBGWAM) | [07-project-one-agent-full-lifecycle.txt](transcripts/07-project-one-agent-full-lifecycle.txt) |

> **Lesson 05 — recording vs. syllabus.** The Foundations plan tags lesson 05 as the *Simulation Engine*; the recording actually demos the **Playground** (a fresh chat + reading the trace for one message). Notes/title use "run it in the Playground" to match what learners see. The dedicated Simulation Engine surface is covered later in the **Test & Simulate** course (Phase · Test & Improve).

## Course 2 — Studio: Design & Create

*Choose the right agent architecture, then build it — the agent-type decision framework, the Lyzr Manager (and growing its team), and SuperFlow for automation that's deterministic where you need guarantees and agentic where you need judgment.* 5 lessons · ~45 min · instructor Felipe. Upload folder: `../thinkific-upload/1 - Tracks/Studio/07 Studio Design and Create/`.

Source files for this course live in **per-course subdirs** (`raw/design-create/`, `transcripts/design-create/`, `notes/design-create/`) so lesson numbers are scoped per course and never collide with Foundations' `01`–`07`. The renderer's `COURSES` list (in `notes/_render_pdfs.py`) maps each course's notes dir → its chapter folder + phase eyebrow; render just this course with `python3 Studio-track/notes/_render_pdfs.py "07 Studio Design and Create"`.

| # | Title | Studio feature | Descript | Transcript |
|---|---|---|---|---|
| 01 | What agent type should I build? | Create Agent — agent-type framework | [view](https://share.descript.com/view/FOzm28nV9YM) | [01-what-agent-type-to-build.txt](transcripts/design-create/01-what-agent-type-to-build.txt) |
| 02 | Lyzr Manager | Orchestrate → Manager | [view](https://share.descript.com/view/JxjoIomKT1C) | [02-lyzr-manager.txt](transcripts/design-create/02-lyzr-manager.txt) |
| 03 | Managers, part 2 — editing from the agent page | Agent page → Managed Agents | [view](https://share.descript.com/view/HapNcaeURx7) | [03-managers-agent-page-editing.txt](transcripts/design-create/03-managers-agent-page-editing.txt) |
| 04 | SuperFlow: Invoice Reconciliation | Create Agent → SuperFlow | [view](https://share.descript.com/view/e9Ny8ysXwMc) | [04-superflow-invoice-reconciliation.txt](transcripts/design-create/04-superflow-invoice-reconciliation.txt) |
| 05 | SuperFlow: Loops | SuperFlow → loop node | [view](https://share.descript.com/view/cyOXlcLJI5R) | [05-superflow-loops.txt](transcripts/design-create/05-superflow-loops.txt) |

> **Recorded vs. original plan.** This course merges the plan's two Design & Create courses (`Choosing & Building Agents` + `Orchestration & Multi-Agent`) into one. Per Felipe's notes: SuperFlow split into a main walkthrough (Invoice Reconciliation) + a short **Loops** video; the "Project" slot became a **second Manager** video (agent-page editing); the standalone single-Agent video was dropped (covered in Foundations), so the course opens with the agent-type framework. The deferred topics (Proxy Agent, Code IDE, Workflow, idea→architecture) move to the coming-soon **Studio: Advanced Agent Patterns** (folder 08).
>
> **Descript title mismatch (noted, harmless).** Internal Descript titles don't match the team's V-labels — `HapNcaeURx7` is titled `design-v12` but is the agent-page editing lesson; `e9Ny8ysXwMc` is just `SuperFlow`. The team's per-link descriptions are authoritative and were verified against each transcript's content; local numbering (01–05) follows the course narrative.

## Course 3 — Studio: Knowledge & RAG

*Ground agents in your data — RAG in Studio, building and structuring a knowledge base, document parsing & ingestion, live Data Connectors, agent memory in depth, and a capstone document-Q&A agent that ties retrieval and memory together.* 6 lessons · ~48 min · instructor Felipe. First course of the **Ground in Knowledge** phase. Upload folder: `../thinkific-upload/1 - Tracks/Studio/11 Studio Knowledge and RAG/`.

Source files live in per-course subdirs (`raw/knowledge-rag/`, `transcripts/knowledge-rag/`, `notes/knowledge-rag/`). Render just this course with `python3 Studio-track/notes/_render_pdfs.py "11 Studio Knowledge and RAG"`.

| # | Title | Studio feature | Descript | Transcript |
|---|---|---|---|---|
| 01 | RAG in Studio | Knowledge → Knowledge Base · Traces | [view](https://share.descript.com/view/iLyDbKWJXxv) | [01-rag-in-studio.txt](transcripts/knowledge-rag/01-rag-in-studio.txt) |
| 02 | Build a Knowledge Base | Knowledge → Knowledge Base | [view](https://share.descript.com/view/u8SqXwIKzjT) | [02-build-a-knowledge-base.txt](transcripts/knowledge-rag/02-build-a-knowledge-base.txt) |
| 03 | Document parsing & ingestion | Knowledge → Knowledge Base | [view](https://share.descript.com/view/CGqBLgAbGUG) | [03-document-parsing-and-ingestion.txt](transcripts/knowledge-rag/03-document-parsing-and-ingestion.txt) |
| 04 | Data Connectors as live sources | Connections → Data Connectors | [view](https://share.descript.com/view/pUlHqpAkEuL) | [04-data-connectors-live-sources.txt](transcripts/knowledge-rag/04-data-connectors-live-sources.txt) |
| 05 | Agent memory in depth | Connections → Memory | [view](https://share.descript.com/view/zMdeiKC7LUO) | [05-agent-memory-in-depth.txt](transcripts/knowledge-rag/05-agent-memory-in-depth.txt) |
| 06 | *Project:* document Q&A agent with memory | Knowledge → Knowledge Base · Connections → Memory | [view](https://share.descript.com/view/bUGvjWAPxeK) | [06-project-document-qa-agent-with-memory.txt](transcripts/knowledge-rag/06-project-document-qa-agent-with-memory.txt) |

> **Descript titles don't follow the `vNN-slug` convention** for this batch — the share pages are titled `A1`/`A2`/`B1`–`B5`, so `fetch_descript.py`'s title parser can't name outputs (the script now falls back to explicit `--json`/`--mp4` paths). Lesson order follows the plan / the team's email labels, verified against each transcript. Note the team grouped these as "Agent Essentials" (Models in depth + Agent memory in depth) and "Ground in Knowledge" (the five KB lessons); per the plan, **"Agent memory in depth" belongs here (L05)** while **"Models in depth" is L01 of the separate _Tools, Models & MCP_ course** (folder 09, not yet built).

## Production pipeline

Same `descript-to-thinkific` flow as the SDK Track, but Studio is **no-code**, so notes use an **`## In Studio`** click-by-click walkthrough section in place of the SDK "Code shown in this lesson" section (renders as a plain section). Render with:

```
python3 Studio-track/notes/_render_pdfs.py
```

The renderer is Studio-branded (violet `#7A639D`, "Lyzr University", phase eyebrow — not "Module N"). It writes `NNb {Title} Notes.pdf` into the course folder above.

## Go-live checklist (after notes are authored)

1. Author the 7 notes (fill the `TODO`s; `## In Studio` from the video, `## Key concepts` lead-ins for sidebar takeaways).
2. `python3 Studio-track/notes/_render_pdfs.py` → 7 PDFs into the course folder.
3. Re-fetch the 7 MP4s (signed URLs are fresh per page-load) and place as `NNa {Title}.mp4`.
4. Rename folder `06 Studio The Agent Lifecycle (Coming Soon)` → drop the suffix; delete the 4 placeholder PDFs; update `CHAPTER_DIR` in the renderer.
5. Rebuild `thinkific-upload/manifest.csv`.
6. Flip this course's `status: coming-soon` → `live` in `catalog-demo/catalog-data.json`; update the Master Tracker.

## Status

**Course 1 — Foundations · The Agent Lifecycle**
- **Recorded / Transcribed / Notes / MP4s:** 7 / 7 — Felipe, delivered 2026-06-09 (contract + transcript-faithfulness + brand pass; PDFs rendered; 1.6 GB MP4s)
- **PACKAGED:** ✅ folder `06 Studio The Agent Lifecycle` holds 7 a/b MP4+PDF pairs; `manifest.csv` rebuilt; placeholders removed — **ready for the Thinkific Content Uploader.**
- **Remaining to fully go live:** flip this course `status: coming-soon → live` in `catalog-demo/catalog-data.json` (still reads coming-soon); update the Master Tracker. (Marketing-site / tracking only — not needed to upload to Thinkific.)

**Course 2 — Design & Create**
- **Recorded / Transcribed / Notes / MP4s:** 5 / 5 — Felipe, processed 2026-06-16 (V9–V13; ~1.55 GB MP4s)
- **PACKAGED + LIVE in catalog:** ✅ folder `07 Studio Design and Create` holds 5 a/b MP4+PDF pairs; `manifest.csv` rebuilt; `catalog-data.json` flipped to `status: live`. **Ready for the Thinkific Content Uploader.**
- Folder `08 Studio Advanced Agent Patterns (Coming Soon)` holds the deferred topics as a 4-lesson coming-soon shell.

**Course 3 — Knowledge & RAG**
- **Recorded / Transcribed / Notes / MP4s:** 6 / 6 — Felipe, processed 2026-06-30 (Descript `A1`/`B1`–`B5` batch; ~1.4 GB MP4s)
- **PACKAGED + LIVE in catalog:** ✅ folder `11 Studio Knowledge and RAG` holds 6 a/b MP4+PDF pairs; `manifest.csv` rebuilt; `catalog-data.json` flipped to `status: live`; card image `studio-knowledge-rag-card-760x420.png` generated. **Ready for the Thinkific Content Uploader.**
- The 7th recording from this batch — **"Models in depth"** — is **L01 of the separate _Tools, Models & MCP_ course** (folder 09) and is being held until the rest of that course is recorded.

**Remaining Studio courses:** 11 (Tools/Models/MCP → Reuse & Distribute) — not yet recorded.
