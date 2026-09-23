# Conversation memory

*Lesson 14 · Module 3 — Knowledge & Memory*

## What you'll learn

- How to wrap `agent.run()` in a small **chat helper** so you can hold a real multi-turn conversation
- How a rolling `memory=20` window behaves across several exchanges
- The production pattern for keeping different users' conversations separate: **one `session_id` per user**

## Key concepts

**A chat helper turns one-off calls into a conversation.** Instead of scattering `agent.run()` calls, write a small function that prints both sides of the exchange and threads the *same* `session_id` through every call. `memory=20` gives a rolling window of the last twenty messages — enough for a real back-and-forth — and the helper just takes a message and a session ID and lets the agent thread them together.

**Memory does the work across turns.** Turn one asks for an onboarding checklist. Turn two adds "remote, from London" and the agent adjusts — UK shipping, remote-first, MDM, time-zone and support coverage. Turn three just says "do all of this" and the agent threads a full timeline against everything from the previous two turns. No re-stating context; the window carries it.

**One agent, one `session_id` per user, is the multi-tenant pattern.** The same agent serves many users — you keep them separate by giving each user their own `session_id`. Ask the same identifying question in Sarah's session and Marcus's session and each answer stays scoped to that user; neither leaks into the other. This is the shape for any multi-user or multi-tenant chatbot: shared agent, per-user session.

## Code shown in this lesson

```python
# A rolling window big enough for a real exchange.
agent = studio.create_agent(
    name="onboarding-helper", provider="gpt-4o",
    role="employee onboarding assistant",
    goal="build and adjust onboarding checklists across a conversation",
    memory=20,   # last 20 messages
)

# Chat helper: threads one session_id through every turn and prints both sides.
def chat(message, session_id):
    print(f"you> {message}")
    resp = agent.run(message, session_id=session_id)
    print(f"agent> {resp.response}\n")
    return resp
```

```python
# Three exchanges in one session — memory threads the context.
sid = "user-alex"
chat("Draft an onboarding checklist for a new hire.", sid)
chat("They're remote, based in London.", sid)        # agent adjusts: UK shipping, MDM, time zones
chat("Great, now give me the full timeline for all of this.", sid)  # threads turns 1 + 2
```

```python
# Multi-tenant isolation: same agent, one session_id per user.
chat("Remind me who I am and what my team does.", "user-sarah")   # knows Sarah / design system
chat("Remind me who I am and what my team does.", "user-marcus")  # knows Marcus / platform
# Neither session leaks into the other.
```

## Try this

1. Write the `chat()` helper and run a 3-turn conversation where each turn depends on the last. Drop `memory` to `2` and rerun the same script — watch the agent lose the early context once it falls out of the window.
2. Run the same identifying question under two different `session_id`s in the same process. Confirm zero cross-talk — that's your multi-tenant isolation proof.
3. Reuse one `session_id` across what should be two *different* users and watch their context bleed together — the bug the per-user-session pattern prevents.

## Transcript

Last video we proved memory works in two turns. Today we wire it into something usable: a chat helper for multi-turn flows, and the pattern for keeping different users' conversations separate on the same agent. Same setup as the rest of the series.

First, a small chat helper so we can have an actual conversation instead of one-off `agent.run` calls. The function prints both sides of the exchange and threads the same session ID through every call. `memory=20` is a rolling window of the last twenty messages — enough for a real exchange. Pass a message and a session ID, and the agent threads them together. Three exchanges. Turn one: onboarding checklist. Turn two: I add "remote, from London" and the agent adjusts — UK shipping, remote-first, MDM, time zone, support coverage. Turn three: I just say "all of this," and the agent threads a full timeline against everything from the previous two turns. Memory doing the work.

Same agent, two users, two session IDs. Same identifying question to both. Sarah's session knows about Sarah and the design system team. Marcus's session knows about Marcus and platform. Neither one leaks into the other. This is the pattern for any multi-tenant or multi-user chatbot: one agent, one session ID per user.

That's conversation memory in production shape: a chat helper that threads session ID for multi-turn flows, and one session ID per user for clean multi-tenant isolation. Next video is the second Knowledge & Memory capstone — a document Q&A bot that pulls everything from this block together: knowledge base ingestion, retrieval tuning, conversation memory, all in one app. I'm Felipe with Lyzr. Until next time.
