# Document parsing & ingestion

*Lesson 03 · Knowledge & RAG*

## What you'll learn

- Trace what happens to a document the moment you add it to a knowledge base — read, extract, chunk, embed
- Judge why clean source documents matter more than clever prompting for answer quality
- Use the score threshold under Configure to dial retrieval between broad context and high-confidence precision
- Read a retrieval result's confidence scores and predict which chunks a threshold will keep or filter
- Keep a knowledge base fresh by pushing updates through its API instead of re-uploading by hand

## Key concepts

**Ingestion is four steps that run the moment you add a document: Lyzr reads it, pulls the text out, splits it into chunks, and turns every chunk into an embedding.** An embedding is a numerical fingerprint the agent can search against, so retrieval is really a search over those fingerprints. None of this is visible at query time, but it quietly decides how good every answer will be.

**Garbage in, garbage out — the quality of your source documents matters more than almost anything else.** A clean document ingests beautifully; a messy scanned PDF is harder to parse, and if the extracted text comes out garbled, no amount of clever prompting will save the answers. Fixing the source is the highest-leverage thing you can do before you touch any other setting.

**The score threshold is the one retrieval knob worth knowing — it sets the minimum confidence a chunk needs to come back.** A raw query returns several matches with different confidence scores; sometimes you don't want every loosely related chunk, only the strong ones. Set the threshold to 0.8 and only matches above eighty percent confidence are returned — the weaker ones get filtered out before they ever reach the agent.

**The threshold is a deliberate trade between context and precision, not a fixed best value.** Lower it when you want the agent to see more surrounding context; raise it when you only want high-confidence answers. This single setting does much of the work in tuning answer quality, so reach for it first when retrieval feels too noisy or too thin.

**Every knowledge base has an API, so you don't have to babysit it — you can keep it fresh from your own systems automatically.** The classic example is a support team: each time a ticket is resolved, you push that resolution into the knowledge base through the API, and the next customer with the same problem gets the answer instantly. The knowledge base stays current without anyone uploading a thing.

## In Studio

Primary surface: **Knowledge → Knowledge Base** (the base you built in the previous lesson, with its documents already added).

1. Open the **Knowledge Base** you built earlier — the documents you added (product guide, support docs) are already ingested: read, chunked, and embedded.
2. Run a raw retrieval to see scores: search `warranty`. You get three matches — the product guide at about 83%, the support docs at 79%, and another chunk at 71% — each with its own confidence score.
3. Open **Configure** and set the **score threshold** to `0.8` — meaning only matches above eighty percent confidence are returned.
4. Hit **Save**, then run the same `warranty` query again. Now you get exactly one result, the product guide at 83%; the 79% and 71% matches were filtered out because they didn't clear the bar.
5. Adjust the threshold to taste: lower it to let the agent see more context, raise it to keep only high-confidence matches.
6. To keep the base fresh, use the knowledge base **API** — the config and the inference endpoint shown let your own systems push new content (for example, a resolved support ticket) straight in, no manual upload required.

## Try this

1. Add one clean document and one messy scanned PDF to a knowledge base, then run the same query against each. Compare the retrieved chunks and notice how parse quality shows up directly in the text that comes back.
2. Run a broad query with no threshold and note the confidence scores of every match. Then set the score threshold to `0.8` under Configure, Save, and re-run the *same* query — confirm which matches survive and which get filtered.
3. Sweep the threshold deliberately: try a low value and a high value on one query, and write one sentence on the trade you observed between getting more context and getting only high-confidence answers.

## Transcript

When you drop a document into a knowledge base, a lot happens before your agent can use it, and the quality of that process quietly decides how good your answers are. So let's look at what ingestion actually does, the one knob that matters most, and how to keep your knowledge from going stale. Here's the knowledge base we built. When I added these documents, Lyzr didn't just store them. It read each one, pulled the text out of it, split it into chunks, and turned every chunk into an embedding, a numerical fingerprint it can search against. That's ingestion. And here's the thing to internalize: garbage in, garbage out. A clean document ingests beautifully. A messy scanned PDF is harder to parse, and if the text comes out garbled, no clever prompting will save your answers. So the quality of your source documents matters more than almost anything else. Now, the one knob worth knowing. Let me run a query first so you can see the raw retrieval. I'll search warranty, and I get three matches: the top one from our product guide at about eighty-three percent, then our support docs at seventy-nine, and another chunk at seventy-one. Three results with different confidence scores. Sometimes you don't want every loosely related chunk. You only want the strong matches. That's the score threshold. Under Configure, I'll set it to zero point eight, which means only matches above eighty percent confidence come back. Then I'll hit Save Same query again, and now I get exactly one result, the product guide at 83%. The 79 and 71% matches got filtered out because they didn't clear the bar I set. That's the trade. Lower the threshold when you want the agent to see more context. Raise it when you only want high confidence answers. This one setting does a lot of the work in tuning answer quality One last piece, and it's what keeps your agent from going stale. Every knowledge base has an API, so you don't have to babysit it. You can update it from your own systems automatically. My favorite example is a support team. Every time a ticket gets resolved, you push that resolution into the knowledge base through this API. The next customer with the same problem gets the answer instantly because your agent just learned it here's the config, and here's the inference endpoint you'd call. Your knowledge base stays current without anyone uploading a thing. So that's ingestion and retrieval. Get clean documents in, use the score threshold to dial in precision, and use the API to keep it fresh. Next, we look at connecting external data sources. I am Felipe Wollizer. I'll see you there
