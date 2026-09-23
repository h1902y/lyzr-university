# Agent memory basics

*Lesson 13 · Module 3 — Knowledge & Memory*

## What you'll learn

- Why agents are **stateless by default** — and what that looks like in practice
- The two lines that turn memory on: a `memory=N` rolling window and a `session_id` on every `agent.run()`
- The three kinds of memory in Lyzr (conversation, Cognis, external providers) and which to reach for
- The single most common "why isn't memory working?" bug

## Key concepts

**Agents are stateless by default.** Run two queries through the same agent and the second has no idea what happened in the first. Ask "we're a data infra team of 8 engineers" then "how many seats should we buy?" and you get a generic playbook covering every team size, because the team size from turn one didn't carry into turn two. That's what stateless looks like.

**Two changes turn on memory: a window and a session.** Set `memory=10` on `create_agent` for a rolling window of the last ten messages, and pass the same `session_id` to every `agent.run()`. Same string on both turns means the SDK threads them together; a different string means a different conversation with fresh context. With both in place, "how many seats?" becomes "for a data infra team of eight engineers, six seats default..." — same agent shape, two new lines of code.

**The most common memory bug: a missing `session_id`.** If you forget it, the SDK auto-generates a fresh one per call. Memory is technically "on," but every call lands in a new session, so nothing connects. If an agent seems to have amnesia, check the `session_id` first — before anything else.

**Conversation memory covers ~80% of cases.** A rolling window of the last N messages, scoped by `session_id`, living in the agent and expiring with the conversation. Reach for it whenever the agent needs to remember what the user said a couple of turns ago — chatbots, support flows, anything multi-turn.

**Cognis is persistent, searchable, cross-session memory.** A separate client that stores conversations long-term, scoped by owner / agent / session, and lets you search them by *meaning* later. Different session, different day, and the agent can still recall what the user told it months ago — the piece conversation memory structurally can't do. The scoping IDs keep one tenant's memory separate from another's.

**External providers are for teams already invested in one.** Mem0, AWS AgentCore, and Supermemory onboard as Studio credentials and attach to an agent's memory config. Same shape as creating any other credential. Don't introduce a new memory backend you don't need — reach for these only when your team already runs one in production.

## Code shown in this lesson

```python
# Stateless by default — turn 2 can't see turn 1.
agent = studio.create_agent(
    name="onboarding-advisor", provider="gpt-4o",
    role="rollout advisor",
    goal="recommend seat counts and onboarding plans",
    instructions="Give specific, sized recommendations.",
)
agent.run("We're a data infra team of 8 engineers.")
agent.run("How many seats should we buy?")   # generic — no memory of the team size
```

```python
# Two changes: a rolling window + a session id threaded through every turn.
agent = studio.create_agent(..., memory=10)   # last 10 messages

sid = "acme-data-infra"
agent.run("We're a data infra team of 8 engineers.", session_id=sid)
agent.run("How many seats should we buy?", session_id=sid)
# → "For a data infra team of 8 engineers: 6 seats default, 8 if everyone logs in, 4 minimal."
```

```python
# Cognis — persistent semantic memory across sessions (a separate client).
cognis.add(messages, owner_id="acme", agent_id="onboarding-advisor", session_id="s1")

# Later, a different session / different wording still finds it by meaning:
hits = cognis.search("compliance evidence", owner_id="acme", agent_id="onboarding-advisor")
print(hits[0].score, hits[0].text)   # 1.0  "...needs SOC 2 evidence quarterly, we use Vanta..."
```

```python
# External providers (Mem0, AWS AgentCore, Supermemory) — onboard as a Studio credential.
cred = studio.create_memory_credential(provider="mem0", config={...})
agent = studio.create_agent(..., memory_config=cred)
```

## Try this

1. Build an agent with **no** `memory` and **no** `session_id`. Run a two-turn exchange where turn two depends on turn one. Then add `memory=10` and a shared `session_id` and rerun — diff the two answers.
2. Reproduce the classic bug: keep `memory=10` but *omit* `session_id`. Confirm the agent still has amnesia, then fix it by threading one `session_id`.
3. With Cognis, store a fact in session A, then search for it from session B using *different wording*. Confirm it comes back ranked by meaning, not exact match.

## Transcript

Agents are stateless by default. Run two queries through the same agent, the second one has no idea what happened in the first. Today we add memory — three kinds of it, depending on what you actually need to remember and for how long. We'll run two of them live, the simple in-session case and persistent semantic memory, and walk through the third. Same setup as the rest of the series.

Quick demo to make stateless concrete. Agent has no memory parameter, no session ID. Two turns. First one establishes context, second one needs that context. Watch what happens. The agent has no idea I told it I have eight engineers, so it gave me a generic playbook covering every team size from eight to sixty-plus, with rules of thumb for each bracket and then four clarifying questions at the bottom. Useful content, but it's working blind. The team size from turn one didn't carry into turn two. That's what stateless looks like in practice.

Two changes. `memory=10` on `create_agent` — that's a rolling window of the last ten messages. And every `agent.run` gets a session ID. Same string on both turns means the SDK threads them together; different string means different conversation, fresh context. Completely different answer: "for a data infra team of eight engineers" — both the team size and the data infrastructure context from turn one are right there. Specific recommendation: six seats default, eight if everyone logs in, four for a minimal subset. Same agent shape as before, two new lines of code. The agent went from "here's a playbook for every possible team size" to "here's the answer for your team."

One gotcha worth stating out loud. If you forget session ID, the SDK auto-generates one per call. Memory is on, but every call lands in a fresh session, so nothing connects. This is the most common "why isn't memory working" bug. Check the session ID first.

What we just used is one of many memory systems in Lyzr. They solve different problems. One: conversation memory — what we just did, a rolling window of the last N messages scoped by session ID. Lives in the agent, expires with the conversation. Reach for this when the agent needs to remember what the user said two turns ago. That's the 80% case: chatbots, support flows, anything multi-turn. Two: Cognis — persistent semantic memory, a separate client. Stores conversations long-term, scoped by owner and agent and session, and you can search them by meaning later. Different sessions, different days — the agent can still recall what the user told it months ago. Let's run it. Score 1.0, perfect match, and the original message comes back: "our compliance team needs SOC 2 evidence quarterly, and we use Vanta for evidence collection." Different session, different question wording, Cognis still pulls the SOC 2 mention back. That's the cross-session piece conversation memory can't do. Owner ID, agent ID, and session ID give you the scoping to keep one tenant's memory separate from another's.

Now the third memory kind: external memory providers — Mem0, AWS AgentCore, Supermemory. Onboarded as Studio credentials with `create_memory_credential` and attached to an agent's memory config. We're not running this one; the surface is the same shape as creating any other credential. Reach for these when your team already has a memory backend in production. Don't introduce a new memory system you don't need.

Short version: default to conversation memory — `memory=N` and session ID — that covers most agents. Switch to Cognis when you need facts to persist across sessions. Reach for external providers only when your team is already invested in one. Whichever you pick, the most common bug is forgetting to thread the session ID. If your agent seems to have amnesia, check the session ID first. Next video, we go deeper on conversation memory specifically — the patterns you'll actually use in production. I'm Felipe with Lyzr. Until next time.
