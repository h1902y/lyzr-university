# SDK Track — Lyzr for Developers

The developer-facing course for Lyzr Academy / Lyzr University. Teaches the **Lyzr Agent Development Kit (ADK)**, the Python module for creating and managing agents on Lyzr. Shipped on **Thinkific**.

19 lessons, grouped into 4 modules. Modules 1–3 each end in a build-along project; Module 4 is four how-to lessons (16–19).

## Layout

```
SDK-track/
├── README.md                    (this file)
├── transcripts/
│   └── NN-<slug>.txt            Plain-text transcript per lesson
├── notes/
│   └── NN-<slug>.md             Authored lesson notes (+ _render_pdfs.py)
└── raw/
    └── NN-<slug>.json           Descript transcript JSON (segments + word-level timings)
```

Transcripts are word-level segments joined with spaces — readable but not punctuated. ASR rendered **Lyzr** as **"Lizza"** in places; run a find/replace before any learner-facing use.

## Lesson index

### Module 1 — Foundations

| # | Title | Descript | Transcript |
|---|---|---|---|
| 01 | What is a Lyzr Agent | [view](https://share.descript.com/view/l0epSX3Joov) | [01-what-is-a-lyzr-agent.txt](transcripts/01-what-is-a-lyzr-agent.txt) |
| 02 | Your first Agent | [view](https://share.descript.com/view/yfYCe1knewa) | [02-your-first-agent.txt](transcripts/02-your-first-agent.txt) |
| 03 | Swapping LLM Providers | [view](https://share.descript.com/view/hxtkvfWflEe) | [03-swapping-llm-providers.txt](transcripts/03-swapping-llm-providers.txt) |
| 04 | Streaming Responses | [view](https://share.descript.com/view/eIDkrH3oXLJ) | [04-streaming-responses.txt](transcripts/04-streaming-responses.txt) |
| 05 | Structured Outputs | [view](https://share.descript.com/view/4xzQOA2jpvz) | [05-structured-outputs.txt](transcripts/05-structured-outputs.txt) |
| 06 | *Project:* Multi-provider chatbot | [view](https://share.descript.com/view/QahGYAZPvu7) | [06-project-multi-provider-chatbot.txt](transcripts/06-project-multi-provider-chatbot.txt) |

### Module 2 — Multimodal

| # | Title | Descript | Transcript |
|---|---|---|---|
| 07 | Image generation | [view](https://share.descript.com/view/ZbJKEPBji0H) | [07-image-generation.txt](transcripts/07-image-generation.txt) |
| 08 | File generation | [view](https://share.descript.com/view/G3LX75UbRQP) | [08-file-generation.txt](transcripts/08-file-generation.txt) |
| 09 | *Project:* Creative assistant | [view](https://share.descript.com/view/6fGAFVIZbaz) | [09-project-creative-assistant.txt](transcripts/09-project-creative-assistant.txt) |

> **Lesson 08 — renamed 2026-05-18.** The curriculum entry was originally "File inputs"; it has been renamed to **File generation** to match the recording (the agent returns a document — file output, not consuming one). The file-inputs use case is covered later in the RAG / document-ingestion lessons (10–12).

### Module 3 — Knowledge & Memory

| # | Title | Descript | Transcript |
|---|---|---|---|
| 10 | What is RAG? | [view](https://share.descript.com/view/YjB4kflZeOi) | [10-what-is-rag.txt](transcripts/10-what-is-rag.txt) |
| 11 | Document ingestion | [view](https://share.descript.com/view/lbzhEJ1MPYD) | [11-document-ingestion.txt](transcripts/11-document-ingestion.txt) |
| 12 | Vector stores and retrieval | [view](https://share.descript.com/view/kT2yIEf5llZ) | [12-vector-stores-and-retrieval.txt](transcripts/12-vector-stores-and-retrieval.txt) |
| 13 | Agent memory basics | [view](https://share.descript.com/view/soJ5OJwX7Nk) | [13-agent-memory-basics.txt](transcripts/13-agent-memory-basics.txt) |
| 14 | Conversation memory | [view](https://share.descript.com/view/n6bwiP6ooLy) | [14-conversation-memory.txt](transcripts/14-conversation-memory.txt) |
| 15 | *Project:* Document Q&A bot | [view](https://share.descript.com/view/3ryANcnn2MN) | [15-document-qa-bot.txt](transcripts/15-document-qa-bot.txt) |

### Module 4 — Tools & Workflows

| # | Title | Descript | Transcript |
|---|---|---|---|
| 16 | Why tools matter | [view](https://share.descript.com/view/8KgUjKNXNwX) | [16-why-tools-matter.txt](transcripts/16-why-tools-matter.txt) |
| 17 | Writing local tools | [view](https://share.descript.com/view/ZYHNqFDjBJY) | [17-writing-local-tools.txt](transcripts/17-writing-local-tools.txt) |
| 18 | Agent context | [view](https://share.descript.com/view/dfJuVXwrXqd) | [18-agent-context.txt](transcripts/18-agent-context.txt) |
| 19 | Multi-step workflows | [view](https://share.descript.com/view/zBBNFo83hvv) | [19-multi-step-workflows.txt](transcripts/19-multi-step-workflows.txt) |

> **Module 4 finalized at 4 lessons (2026-06-01).** The earlier curriculum's "Backend integrations" and the "*Project:* Workflow agent" capstone were never recorded and have been dropped — the recorded series runs v16→v19. Lesson 18 is **Agent context** (standing-knowledge context objects), not the earlier-planned "Context variables" (the recording explicitly disclaims per-message variable templating). The SDK Track is now **19 lessons**; the ADK product ships as **4 complete courses**.

## Status

- **Recorded:** 19 / 19 — all four modules complete (Module 4 finalized at 4 lessons: 16–19)
- **Transcribed:** 19 / 19 of recorded
- **Remaining:** none — SDK Track fully recorded
