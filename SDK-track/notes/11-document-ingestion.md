# Document ingestion

*Lesson 11 · Module 3 — Knowledge & Memory*

## What you'll learn

- How to ingest real files (PDF, DOCX, websites) into a knowledge base — not hard-coded strings
- The two chunking parameters worth knowing about: `chunk_size` and `chunk_overlap`, and sensible defaults
- The three PDF parsers Lyzr offers (`llmsherpa`, `pymupdf`, `laserparse`) and when to reach for each
- How the same retrieve-then-shape pattern from lesson 10 holds when the documents get real

## Key concepts

**Same shape as lesson 10, different doc.** Create a knowledge base. `add_pdf` the file. Run the query. The agent quotes from the file.

**Two chunking parameters worth knowing.** `chunk_size` — how much text goes into each searchable chunk, measured in tokens. Default 1024. Bigger chunks → more context per retrieval, lower precision. Smaller chunks → more precise retrieval, more chunks to score. `chunk_overlap` — how much consecutive chunks share. Default 128. Some overlap is good — it stops you from cutting an important sentence in half across two chunks. **Don't tune these unless you have a reason.**

**Three PDF parsers, three different jobs.**
- `llmsherpa` (default) — layout-aware. Reads the visual structure of the PDF; preserves headings, tables, bullet hierarchies. **Best for structured docs:** whitepapers, manuals, reports.
- `pymupdf` — fast, text-only. No layout awareness, minimal overhead. **Reach for this** when you've got clean text-heavy docs (legal contracts, plain prose) and don't need visual structure.
- `laserparse` — multimodal. Uses DocLin plus a vision model under the hood. **For visually complex documents** — technical drawings, slide decks, anything where images and charts carry information that text alone can't capture. Slower and more expensive, but it sees what others can't.

**Picking rule.** Layout-aware default for most things. Switch to PyMuPDF for speed on plain text. Reach for laserparse when the visuals matter.

**The retrieval pattern is unchanged from lesson 10.** Same strict-refusal instructions. Same `knowledge_bases=[kb]` at runtime. The model adds shape (numbered steps, formatted lists, footnotes) on top of grounded retrieved facts.

## Code shown in this lesson

```python
# Setup includes fpdf2 to generate a sample PDF for the demo;
# in production you'd skip this and point at a real file.

kb = studio.create_knowledge_base(name="veristack-handbook")

# Default parser (llmsherpa), default chunking
kb.add_pdf("veristack_admin_handbook.pdf")

agent = studio.create_agent(
    name="veristack-support",
    provider="gpt-4o",
    role="VeriStack customer support agent",
    goal="answer admin questions from documentation only",
    instructions="Only answer from documentation. Refuse if not in docs.",
)

response = agent.run(
    "How do I export workspace data?",
    knowledge_bases=[kb],
)
print(response.response)
```

```python
# Picking a parser explicitly
kb.add_pdf("structured_whitepaper.pdf", data_parser="llmsherpa")   # default — layout-aware
kb.add_pdf("legal_contract.pdf",        data_parser="pymupdf")     # fast, text-only
kb.add_pdf("technical_drawings.pdf",    data_parser="laserparse")  # multimodal vision
```

```python
# Tuning chunk parameters (don't unless you have a reason)
kb.add_pdf("large_report.pdf", chunk_size=1024, chunk_overlap=128)
```

## Try this

1. Ingest the same PDF three times into three separate knowledge bases — `chunk_size=512`, `1024`, and `2048`. Ask the same question against each. Note where retrieval precision changes and where it doesn't.
2. Pick a visually-rich PDF you have (a slide deck, a product spec with diagrams). Ingest it three times with `data_parser="llmsherpa"`, `"pymupdf"`, and `"laserparse"`. Ask *"what's on page 5?"* against each. Compare how well each parser captured the visual content.

## Transcript

Last video we ingested a hard-coded string. Today we move to real files — PDFs, Word docs, websites — what you'd actually have in production. Plus the chunking parameters you need to tune, and three different PDF parsers depending on what you're feeding in.

Same setup, one small addition. `fpdf2` lets us generate a sample PDF for this demo so the notebook is self-contained. In production you'd skip this and point at a PDF you already have.

Quick scaffolding cell — we're generating a fake VeriStack admin handbook (that's our made-up company) with four sections: SSO, API rate limits, data export, and role-based access control. Multi-section content is what makes chunking meaningful. Treat this cell as setup.

Now the real work. Same shape as last video — create a knowledge base, add a doc, run a query. The difference is the doc.

Two parameters worth knowing about. `chunk_size` — how much text goes into each searchable chunk, measured in tokens, defaulting to 1024. Bigger chunks mean more context per retrieval but lower precision. Smaller chunks mean more precise retrieval but more chunks to score. 1024 is a sensible default for most documents. `chunk_overlap` — how much consecutive chunks share, defaulting to 128. Some overlap is good. It stops you from cutting an important sentence in half across two chunks. Don't tune these unless you have a reason.

Same agent shape as video ten. Same strict refusal-by-default instructions — the agent only answers from documentation it can see. Different question this time — hitting the data export section of the handbook.

There it is. The agent quoted the admin settings → Data Export path word for word from the handbook. Walked through the four-item zip archive — contacts JSON, records, member metadata, attachments, and schema manifest — and pulled the specifics. Even caught the audit logs. All sourced from one chunk of the handbook we ingested ten seconds ago. Same pattern as last video: retrieval gives the agent grounded facts, the model gives them shape. Numbered steps, formatted lists, the audit-log footnote — that structure came from the LLM, not from the source.

Quick aside on parsers. `add_pdf` takes a `data_parser` argument with three options. Default is `llmsherpa` — layout-aware. It reads the visual structure of the PDF, preserves headings and tables and bullet hierarchies. Best for structured docs — whitepapers, manuals, reports. Second option is `pymupdf` — fast, text-only. No layout awareness, but minimal overhead. Reach for this when you've got clean text-heavy documents — legal contracts, plain prose — and you don't need the visual structure. Third is `laserparse` — multimodal. Uses DocLin plus a vision model under the hood. This is the one for visually complex documents — technical drawings, slide decks, anything where the images and charts carry information that text alone can't capture. Slower, more expensive, but it sees what others can't.

The picking rule is simple. Layout-aware default for most things. Switch to PyMuPDF when you want speed on plain text. And reach for laserparse when the visuals matter.

That's ingestion. `add_pdf` with the two chunking parameters and three parser options to pick depending on what you're feeding in.

Next video — vector stores and retrieval strategies. How to control what actually comes back when you query.

I'm Felipe with Lyzr. Until next time.
