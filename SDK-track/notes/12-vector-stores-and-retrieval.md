# Vector stores and retrieval

*Lesson 12 · Module 3 — Knowledge & Memory*

## What you'll learn

- The two control points that decide what your agent retrieves: the **vector store** (set at KB creation) and the **retrieval strategy** (set at query time)
- How to use `kb.query()` as a raw retrieval API to debug exactly what the agent sees — chunks plus scores, no agent in the loop
- The four retrieval strategies (`basic`, `mmr`, `hyde`, `time_aware`) and when each one wins
- How to tune retrieval **per call** with `with_config()` without mutating the knowledge base

## Key concepts

**Stay on the default vector store until you have a reason not to.** A knowledge base defaults to **Qdrant** under the hood; the SDK also supports Weaviate, pgvector, Milvus, and Neptune, set with `vector_store=` at creation. The picking rule is short — keep Qdrant unless your team already runs a different vector DB in production. Don't introduce new infrastructure you don't need.

**`kb.query()` is your retrieval debugger.** When an agent gives a weird answer, the first question is "what did it actually retrieve?" `kb.query()` answers that directly: pass a question, get back ranked chunks with similarity scores and no agent in the loop. The score column is the signal — if your top result is below ~0.3–0.4, retrieval is uncertain and the agent's answer probably is too.

**Four retrieval strategies, picked by the shape of your queries.** `basic` is straight vector similarity — fast, predictable, the right default. `mmr` (maximal marginal relevance) adds a diversity penalty so you don't get five near-identical chunks. `hyde` (hypothetical document embeddings) has the model imagine an ideal answer, embed *that*, and search against it — better recall when questions are vague or phrased very differently from the source. `time_aware` weights recency on top of similarity, tunable via `time_decay_factor`, for version docs where you want the latest.

**The picking rule.** Default to `basic`. Switch to `mmr` if you're getting redundant chunks, `hyde` if queries are vague and recall is weak, `time_aware` when recency matters. On a small KB the differences are subtle; on a real corpus with near-duplicate chunks, MMR is the difference between five copies of one fact and five different angles.

**Tune retrieval per call, not per knowledge base.** `kb.with_config()` returns a wrapped knowledge base with per-call settings that pass through to `agent.run()` and **mutate nothing**. Same KB, three knobs tuned for one specific call — pull more chunks, use MMR for diversity, drop low-confidence matches with a score threshold — while the KB itself stays untouched for the next call that wants different settings. That's the level of control you want past the prototype stage.

## Code shown in this lesson

```python
# Vector store is chosen at KB creation. Default is Qdrant — keep it unless you
# already run another vector DB in production.
kb = studio.create_knowledge_base(name="veristack-docs")
# kb = studio.create_knowledge_base(name="veristack-docs", vector_store="weaviate")
# also: "pgvector", "milvus", "neptune"

# Seed several short docs (SSO, rate limits, data export, audit logs, RBAC) so
# retrieval actually has to choose between topics.
kb.add_text("VeriStack data export: admins can export workspace data from ...")
```

```python
# kb.query — raw retrieval, no agent. Returns ranked chunks + scores for debugging.
results = kb.query(
    "How do I export my data?",
    top_k=3,
    retrieval_type="basic",   # default
    score_threshold=0.0,      # default
)
for chunk in results:
    print(round(chunk.score, 2), chunk.text[:60])
# 0.47  data export ...   ← the doc we asked about
# 0.31  audit logs ...    ← plausibly related
# 0.12  sso ...           ← low confidence, basically noise
```

```python
# Switch strategy at query time.
results = kb.query("How do exports work?", top_k=3, retrieval_type="mmr")
# Recency-weighted variant:
# kb.query("...", top_k=3, retrieval_type="time_aware", time_decay_factor=0.3)
```

```python
# Tune retrieval per call without mutating the KB.
tuned = kb.with_config(top_k=5, retrieval_type="mmr", score_threshold=0.3)
response = agent.run("What roles can I assign?", knowledge_bases=[tuned])
print(response.response)   # answer sourced from the RBAC chunk, MMR-tuned for this call
```

## Try this

1. Build a KB with five short docs on different topics. Run the *same* query through `kb.query()` with `retrieval_type="basic"` and then `"mmr"`. Compare the third result — watch MMR trade a little similarity for diversity.
2. Find a query where your top score sits below 0.3. Now rephrase the question to match the source wording and watch the score climb — then try `hyde` on the *original* vague phrasing and see if recall recovers without the rewrite.
3. Wrap the KB with `with_config(score_threshold=0.4)` and ask something your corpus doesn't cover. Confirm the agent gets *nothing* back rather than low-confidence noise.

## Transcript

Last video we filled a knowledge base. Today we tune what comes back when you query it. Two control points: the vector store you pick at creation and the retrieval strategy you pick at query time — plus the API you'll reach for when you need to debug what your agent is actually seeing. Same setup. We'll boot a fresh knowledge base this time, multiple short docs, so retrieval has something to choose between. Five short VeriStack docs (that's our made-up company for the tutorial), each on a different topic: SSO, rate limits, data export, and audit logs. Different topics mean retrieval has to actually pick the right one. With a single doc, the retrieval story is a little bit boring.

Quick aside on the vector store. The knowledge base defaults to Qdrant under the hood. The SDK also supports Weaviate, pgvector, Milvus, and Neptune — set `vector_store` to Weaviate and so on at creation time. The picking rule is short: stay on Qdrant unless your team already has a different vector DB in production. Don't introduce new infrastructure unless you really need it.

When you're debugging what your agent is seeing, don't just look at the agent's answer — look at what got retrieved. `kb.query` is the raw retrieval API. Pass a question, get back ranked chunks with scores, no agent in the loop. Three things on the call: the query string, `top_k` for how many chunks to return. By default `retrieval_type` is basic and `score_threshold` is zero. Those are next. Three results: top one is data export at 0.47, exactly the doc we're asking about. Second is audit logs at 0.31, which makes sense — anything mentioning data overlaps a bit. Third is SSO at 0.12, low confidence, basically noise. The score column is the most useful debugging signal here. If your top result is below 0.3 or 0.4, your retrieval is uncertain, and your agent's answer is probably uncertain too. This API is what you reach for when an agent gives you a weird answer and the first question is: what did it actually retrieve?

Four strategies on retrieval type — pick one based on the shape of your queries. Basic is the default: straight vector similarity, fast, predictable, the right starting point. Use it until you have a reason not to. MMR is maximal marginal relevance: vector similarity plus a diversity penalty, so you don't get five chunks that all say nearly the same thing. Reach for this when your knowledge base has redundant docs and the agent keeps getting near-duplicate context. HyDE is hypothetical document embeddings: the model first imagines what an ideal answer would look like, embeds that, and searches against it. Better recall when the user's question is vague or short ("how do exports work?") and the relevant chunk is phrased very differently from the question. time_aware weights recency on top of similarity — useful when your knowledge base has version docs and you want the latest. Adds a `time_decay_factor` parameter you can tune. Picking rule: default is basic. Switch to MMR if you're getting redundant chunks. Switch to HyDE if your queries are vague and recall is weak. Switch to time_aware when recency matters.

Same query, different ranking. Top two are unchanged — data export and audit logs are both genuinely related, so MMR keeps them. But the third slot changed. Basic gave us SSO at 0.12. MMR pulled in rate limits at 0.07 — lower score because MMR docks similarity to favor diversity. On a small knowledge base like this, that's all the diversity it can find. On a real corpus where you have multiple near-duplicate chunks of the same doc, MMR is the difference between five copies of the same fact and five different angles.

Last piece. When you wire the knowledge base into an agent, you don't have to bake retrieval settings into the knowledge base itself. `kb.with_config` returns a wrapped knowledge base with per-call settings, passes through to `agent.run`, and mutates nothing. Same knowledge base, three knobs tuned for this specific call: pull more chunks, use MMR for diversity, drop low-confidence matches with the score threshold. The agent gets exactly what you want it to see, and the knowledge base itself stays unmodified for the next call that might want different settings. Clean answer — the agent listed the four built-in roles (owner, admin, member, guest) and called out custom roles as enterprise only. All sourced from the RBAC chunk, retrieved with the per-call MMR tuning we just set up. That's the level of control you want once you're past the prototype stage.

That's retrieval: `kb.query` to debug what's coming back, four strategies to pick from, and `with_config` to tune per call without mutating the knowledge base. Next block, we move to memory — how agents remember what happened across turns. I'm Felipe with Lyzr. Until next time.
