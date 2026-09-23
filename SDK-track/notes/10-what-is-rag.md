# What is RAG?

*Lesson 10 · Module 3 — Knowledge & Memory*

## What you'll learn

- The failure mode RAG is designed to fix: confident hallucinations on private/internal data
- The three-step RAG flow in Lyzr: create a knowledge base, add a doc, pass it to `agent.run()`
- Why the knowledge base is attached at runtime, not at agent creation
- When to use RAG and — equally important — when to skip it

## Key concepts

**The failure mode without RAG.** Ask a model about your private B2B SaaS company and it will pattern-match from generic setup docs and ship a confident guess. Even if you instruct the agent to "only answer from documentation provided," without that documentation it will either refuse (good) or hallucinate (bad). The instruction *forces* the gap to be visible.

**Three-step RAG in Lyzr.**
1. Create a knowledge base — defaults handle the rest (vector store: Qdrant; embedding: OpenAI `text-embedding-3-large`; persisted to your Lyzr account).
2. Add a document — `add_text`, `add_pdf`, `add_docx`, or `add_website`.
3. Pass it to `agent.run(knowledge_bases=kb)` at call time.

**The knowledge base is attached at runtime.** Same agent can answer with different knowledge bases on different calls. Useful when you've got a routing layer in front (think back to lesson 06).

**The model still adds value on top of retrieval.** Retrieval gives the agent grounded facts. The LLM shapes them — numbered walkthroughs, separated sections, structured walkthrough. Don't think of RAG as "the LLM goes away" — think of it as "the LLM stops guessing about facts it doesn't know."

**When to use RAG.** Your data is private or internal. The data changes over time. The data is recent enough to be past the model's training cutoff. You need source attribution. The corpus is too large to dump into the prompt.

**When to skip RAG.** Data fits in the prompt window (modern flagship models take hundreds of thousands to millions of tokens — if your knowledge base is one PDF, just paste it in). Data lives in a structured database — SQL or an API call beats vector search on structured data, so use a tool, not a knowledge base. The model already knows the territory well — adding RAG would slow you down and add nothing.

**The honest version.** RAG is the right tool when your data is external, dynamic, or large. Otherwise reach for prompt context, a tool call, or a system prompt. Don't add infrastructure you don't need.

## Code shown in this lesson

```python
agent = studio.create_agent(
    name="veristack-support",
    provider="gpt-4o",
    role="VeriStack customer support agent",
    goal="answer admin questions accurately from documentation only",
    instructions=(
        "Only answer from documentation provided in context. "
        "If the answer isn't in the docs, reply: "
        "'I don't have that information in the documentation I can see.'"
    ),
)

# Without RAG — the agent refuses cleanly (or would hallucinate without strict instructions)
agent.run("Our VeriStack workspace needs SSO with Okta. What are the steps?")
```

```python
# Step 1 — create a knowledge base
kb = studio.create_knowledge_base(name="veristack-admin-docs")

# Step 2 — add a document
kb.add_text("""
    VeriStack SSO with Okta — admin steps...
    [...documentation snippet here...]
""")

# Step 3 — pass to agent.run
response = agent.run(
    "Our VeriStack workspace needs SSO with Okta. What are the steps?",
    knowledge_bases=[kb],
)
print(response.response)
```

## Try this

1. Build a knowledge base with one fake fact — *"VeriStack supports SSO with Okta via SAML 2.0."* Query the same agent twice — once *without* the knowledge base attached, once *with*. Verify it refuses cleanly without it and quotes the fact verbatim with it.
2. Attach the *same* knowledge base to two agents — one with `role="customer support agent"`, one with `role="senior platform engineer"`. Same question, same knowledge base, two different `role`s. Note how the role shapes the *form* of the answer even when the facts are identical.

## Transcript

Today we add RAG to an agent. Three lines of new code, and the agent stops guessing about your documents and starts quoting them. We'll do the before, the after, and then talk about when this is the right tool and when it isn't.

Same setup as the rest of the series. Pin the SDK, load the API key, spin up Studio.

Single cell. Customer support role for a fictional B2B SaaS platform called VeriStack. I made the name up, so the model has zero training data on it — which means we get a clean view of what the agent does without context. The question is right there at the top of the cell: "Our VeriStack workspace needs SSO with Okta. What are the steps?"

Critical bit in the instructions — I'm telling the agent to only answer from documentation provided in context, and to refuse with a fixed phrase otherwise. Without this, the model will pattern-match from some generic setup docs and ship a confident guess. That's the failure mode this video is trying to surface. Strict instructions force the gap to be visible.

There it is. The refusal phrase, word for word from the instructions. Clean, predictable — exactly what you want from an enterprise support bot when the source isn't reachable. Better than a confident hallucination every day. But this isn't useful to the customer yet. That's where RAG comes in.

Now the fix. Three steps: create a knowledge base, add a document to it, pass it to `agent.run`. That's the whole RAG flow.

Step one — create the knowledge base. Defaults handle the rest. Vector store is Qdrant. Embedding model is OpenAI's `text-embedding-3-large`. And the knowledge base lives in your Lyzr account, so it persists across runs. We'll go deeper on those choices in video twelve.

Step two — add the doc. I'm using `add_text` here so we don't need a file on disk. The SDK also has `add_pdf`, `add_docx`, and `add_website` — those are in video eleven. Behind the scenes, the SDK chunked that text, embedded each chunk into a vector, and stored everything in Qdrant — none of which we wrote any code for. That's the value.

Step three — pass the knowledge base into `agent.run` with `knowledge_bases=[kb]`. Same agent, same question variable from the previous cell. The only thing that changes is the knowledge base attachment.

One important detail. The knowledge base is attached at runtime, not at agent creation. This means the same agent can answer with different knowledge bases on different calls. Useful when you've got a routing layer in front of it.

Look at that. Same agent, same question, same model. Only the knowledge base attachment changed. The agent pulled the admin settings path straight out of the doc. It named the specific Okta fields — Single Sign-On URL and Audience URI. All of that came from the snippet we ingested a few seconds ago. None of that was present in its training data.

One more thing worth noticing. The agent didn't just retrieve. It structured the retrieved facts into a numbered walkthrough — broke the steps out by location, separated the VeriStack side from the Okta side. That's the LLM still adding value on top of RAG. The retrieval gives it grounded facts; the model gives it shape.

Quick guide so you don't reach for this when something simpler works. Use RAG when the data is private or internal; the data changes over time; the data is past the model's training cutoff; you need source attribution; or the corpus is too large to dump into the prompt.

And skip RAG when the data fits in the prompt window. Modern flagship models take hundreds of thousands of tokens — if not millions. If your knowledge base is one PDF, just paste it in. RAG is overhead for that case. Skip it also when the data lives in a structured database. SQL or an API call beats vector search on structured data every time. Use a tool, not a knowledge base. Also skip it when the model already knows the territory well. Asking GPT-5.2 about JavaScript features doesn't need a knowledge base. Adding one would slow you down and add nothing.

The honest version: RAG is the right tool when your data is external, dynamic, or large. Otherwise reach for prompt context, a tool call, or a system prompt. Don't add infrastructure you don't need.

That's RAG end-to-end. Three lines of new code — create a knowledge base, add a doc, pass it to `agent.run`. Next video, we go deeper on ingestion — PDFs, Word docs, websites, and the parser options that change how each one gets indexed. After that, vector stores and retrieval strategies. By video fifteen, we're building a full document Q&A bot.

I'm Felipe with Lyzr. Until next time.
