# File generation

*Lesson 08 · Module 2 — Multimodal*

*Curriculum note: this lesson was originally listed as "File inputs" but covers file **generation** (PDFs, CSVs, DOCX). Treat "File generation" as canonical.*

## What you'll learn

- How `file_output=True` switches an agent from text/image to document mode
- Why the file *format* is a property of the prompt, not the agent
- How the same artifact retrieval pattern from image generation reuses for documents
- Where document generation is most reliable — and where the model is most likely to drift

## Key concepts

**Same agent, different artifact.** Add `file_output=True` to `create_agent` and the same `agent.run()` returns a document. PDF, CSV, DOCX, XLSX — whatever you ask for in the prompt.

**Format lives in the prompt, not the agent.** The agent doesn't know what format it's producing until you tell it in the message. "Format as a CSV" → CSV. "Format as a PDF" → PDF. Same agent can generate one of each across two calls without recreating it.

**Artifact retrieval is identical to image generation.** `response.has_files` to check, iterate `response.files`, call `artifact.download(path)` to write to disk. Each artifact has `format_type` so you can branch on document vs image vs audio.

**Tabular formats are most reliable.** Five columns and five rows? The model has very little room to drift. The schema is rigid; cells get populated cleanly. PDFs give the model more room to embellish — it will invent metrics, headings, "outlook" sections you didn't ask for. Useful when you want a polished one-pager, dangerous when you need accuracy.

**Numbers are AI-generated.** If you ask for "revenue highlights," the dollar figures will be plausible but invented. Don't ship them as truth.

## Code shown in this lesson

```python
# Agent in document mode
agent = studio.create_agent(
    name="document-generator",
    provider="gpt-4o",
    role="business writer",
    goal="produce structured business documents",
    instructions="Be concise and well-formatted.",
    file_output=True,
)
```

```python
# PDF — format clause is in the prompt
response = agent.run("""
    Write a Q3 sales QBR with revenue highlights, top three wins, and one risk.
    Format as a PDF.
""")

for artifact in response.files:
    artifact.download(safe_file_name(artifact.name))
```

```python
# CSV — same agent, different format clause
response = agent.run("""
    Generate five rows of project status data with columns:
    project, owner, status, priority, due_date.
    Format as a CSV.
""")
```

## Try this

1. Same agent, same prompt content — *"five rows of project status data with columns: project, owner, status, priority, due_date"* — but ask once for CSV and once for DOCX. Compare. Note where the model embellishes more (you should see CSV stay rigid and DOCX add formatting flourish).
2. Ask the doc agent for a 2-page PDF report on a topic you actually know well (your last sprint, your favourite product). Read the output critically — circle every metric the model invented vs every fact that was grounded.

## Transcript

Last video the agent returned an image. Today it returns a document. Same `agent.run()` call. Same response shape. Just a different artifact type — PDF, CSV, DOCX, whatever you ask for.

First, run a PDF report. I'm asking for something with structure — headings, a few paragraphs, a numbered section. Format clause is "as a PDF" at the end of the prompt.

Same artifact retrieval pattern as video seven. `response.has_files` to check, `response.files` to iterate, `artifact.download(path)` to write to disk. The artifact also has `format_type`, so you can tell document from image from audio if you've got an agent that produces multiple kinds.

PDF saved. Opens cleanly. And look what the model did with it. I asked for revenue highlights, top three wins, and one risk. It gave me all of that and elaborated past the brief. It invented a fictional company called "ApexFlow." Opened with an executive snapshot and layered in sales efficiency metrics — CAC payback, pipeline coverage, retention numbers. Three named wins with deal type, ARR, TCV, and a "why we won" rationale. Customers across financial services, healthcare, and manufacturing. The risk section came with mitigation actions, and it closes with a forward-looking outlook section.

The numbers are AI-generated in this case, so don't trust the dollars. But the *shape* — this could pass for a real internal sales QBR at any early-stage SaaS company. Headings hierarchy, bullets, the right metrics in the right places. One prompt, one parameter.

Now the same agent, different format. Prompt asks for tabular data and the format clause becomes "as a CSV." Same shape, different format. Five rows, five columns. Every cell populated. Status values cover the full spread — open, in-progress, resolved, on-hold, closed. Priority hits high, medium, low, critical.

Tabular data is where this is most reliable, because the schema is rigid. The model has fewer ways to drift when you've told it five columns and five rows. Two formats, same agent, same `file_output=True`.

The format is a property of the request, not a property of the agent. That means the same agent can generate a PDF on one call and an Excel file on the next without recreating it. One parameter, multiple formats. Same artifact retrieval pattern as the image generation video.

`file_output=True` flips the agent into document mode. The format clause in your prompt picks the type. And `response.files` is how you get the bytes out.

Next video is the second capstone — creative assistant. We take image generation from video seven, file generation from this one, and build an agent that produces a marketing one-pager — image, copy, PDF — all from a single prompt.

I'm Felipe with Lyzr. Until next time.
