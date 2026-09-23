# Agent context

*Lesson 18 · Module 4 — Tools & Workflows*

## What you'll learn

- What a **context** is: named standing knowledge the agent carries on *every* call
- How to attach contexts at create time with `contexts=[...]`, and add or remove them **between calls**
- Why context lives in the **system prompt** — no retrieval step, unlike RAG
- The picking rule that separates **context vs. RAG vs. memory** so you stop confusing them

## Key concepts

**Context is named background the agent always carries.** Company information, support hours, the current quarter, your brand voice — small, stable facts the agent should simply *know*. A context is a named string (`create_context(name, value)`) that lives in the system prompt, so the agent has it on every single call without looking anything up. No knowledge base, no documents, no retrieval.

**Attach it at create time with `contexts=[...]`.** Pass a list of context objects into `create_agent` and they're baked into the system prompt from the first run. Ask for the support hours and the answer comes straight from the context — there's no retrieval step to wait on, because the fact was already in front of the model.

**Contexts are dynamic between calls — add and remove on the fly.** Say maintenance gets scheduled. `agent.add_context(maintenance)` folds it in mid-session and the agent uses it on the next run — no recreate, same agent. When the window's over, `agent.remove_context(maintenance)` takes it back out. You're changing the agent's standing knowledge between calls, not rebuilding it.

**Dynamic between calls is not per-message templating.** This is the trap. There's no per-user variable substitution *inside* a single `agent.run` — context changes apply to subsequent calls, not to one message mid-flight. If you need per-user values, give each user their own context object, or just put the value in the message itself.

**Context vs. RAG vs. memory — the three get confused, so here's the rule.** **Context** is small, stable knowledge that's always in the system prompt and applies to every call — company facts, brand voice, a maintenance notice; the agent never goes looking for it. **RAG** is a document corpus the agent *retrieves* from per query; large and searchable, only the relevant chunks reach any one answer (lessons 10–13). **Memory** is the conversation itself — what the user said earlier in the session (lessons 13–14). If it's small, stable, and always-known → context. A big pile of documents you search → RAG. The back-and-forth of the conversation → memory. Most real agents use all three.

## Code shown in this lesson

```python
from lyzr import Studio

studio = Studio(api_key="...")

# Two contexts — each is a named string.
company = studio.create_context(
    name="company_information",
    value="Acme Corp — industrial IoT sensors. Founded 2019. Current quarter: Q2.",
)
support = studio.create_context(
    name="support_information",
    value="Support hours: 9am–6pm ET, Mon–Fri. Status page: status.acme.com.",
)
```

```python
# Attach both at create time via the contexts parameter — no KB, no documents,
# no tools. Pure standing knowledge, baked into the system prompt.
agent = studio.create_agent(
    name="support", provider="gpt-4o",
    role="customer support agent",
    goal="answer customer questions",
    contexts=[company, support],
)

# Answered straight from the support context — hours and status page, no retrieval.
agent.run("What are your support hours?")
```

```python
# The dynamic part — change standing knowledge between calls.
maintenance = studio.create_context(
    name="maintenance",
    value="Scheduled maintenance Sat 2am–4am ET; the dashboard may be briefly unavailable.",
)

agent.add_context(maintenance)      # folded in mid-session — same agent, no recreate
agent.run("Any planned downtime this weekend?")

agent.remove_context(maintenance)   # take it back out once maintenance is over
```

## Try this

1. Ask the agent a question answerable from a context (support hours), then a question that *isn't* covered. Notice it answers the first with no retrieval and is honest about the second — context is knowledge, not a search index.
2. Add the `maintenance` context, ask about downtime, then remove it and ask again. Confirm the agent's standing knowledge changed between calls without recreating the agent.
3. Try to make a context behave per-user by templating a name into one `run`. Watch it *not* work the way per-message substitution would — then fix it properly by giving the value in the message. This is the distinction worth feeling firsthand.

## Transcript

We've given agents documents to retrieve and conversations to remember. Today, standing knowledge: context. A context object is a named piece of background the agent always carries — company information, support hours, the current quarter, or your brand voice. It lives in the system prompt, so the agent knows it on every single call without retrieving anything.

Same setup as the rest of the series. Two contexts, each a named string: company information and support information. Both are attached at create time via the `contexts` parameter — no knowledge base, no documents, no tools. This is pure standing knowledge baked into the system prompt. Ask for the support hours and the answer comes straight from the support context, hours and status page — no retrieval step, no documents.

Here's the dynamic part. You can add, remove, and update contexts over the agent's life, between calls. Say maintenance gets scheduled — add a context for it. The agent folds the maintenance context right in mid-session: same agent, no recreate. We just changed its standing knowledge between calls. When maintenance is over, `agent.remove_context(...)` takes it back out.

One thing to be clear about: this is dynamic between calls, not per message. There's no per-user variable templating inside a single `agent.run`. If you need per-user values, give each user their own context object, or put the value in the message itself.

Quick mental model, because these three get confused. Context is standing knowledge that's always in the system prompt — small, stable, applies to every call: company facts, brand voice, the current quarter, a maintenance notice. The agent never has to go look for it. RAG is a document corpus the agent retrieves from per query — large, searchable, only the relevant chunks make it into any one answer; that's lessons ten through thirteen. Memory is the conversation itself, what the user said earlier in the session; that's lessons thirteen and fourteen. The picking rule: if it's small, stable, and the agent should always know it, that's context. If it's a big pile of documents you search, that's RAG. If it's the back-and-forth of the conversation, that's memory. Most real agents use all three.

That's context: named background knowledge in the system prompt, attached at create time or added between calls, separate from your documents and your conversation history. Next video, multi-step workflows — managing agents and scheduling work. I'm Felipe with Lyzr. Until next time.
