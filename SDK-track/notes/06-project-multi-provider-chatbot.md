# Project — Multi-provider chatbot

*Lesson 06 · Module 1 Capstone — Foundations*

## What you'll learn

- How to compose two agents into a small system: a classifier that routes, a responder that answers
- Why splitting routing and answering into two agents beats one agent doing both
- How structured outputs (video 05), provider swapping (video 03), and streaming (video 04) compose into a real pipeline
- The "plan, then fan out" architectural pattern you'll reuse across every project from here on

## Key concepts

**Two agents, one chat loop.** First agent is the *classifier* — structured output. It looks at the message and returns a typed routing decision: what kind of request is this, which provider should handle it. Second agent is the *responder* — provider swapping + streaming. It gets instantiated fresh with whichever provider the classifier picked, and streams the answer back.

**Why two agents instead of one?** Routing is a different job than answering. Classification needs a predictable typed output — perfect fit for `response_model`. Answering needs a conversational stream — perfect fit for `stream=True`. One agent trying to do both would be worse at both.

**Reach for small specialized agents.** It's a pattern you'll come back to. Each agent has one job. You can swap the classifier for a smarter version without touching the responder. You can add new providers to the routing table without changing the loop. You can repoint the classifier at a different decision schema — say, routing between tools instead of providers — and the same architecture holds.

**Responder is a function, not a persistent agent.** The provider changes per turn, so we spin up a fresh agent every call. `create_agent` is just a config call — cheap, stateless.

**The hard-coded routing table is the demo, not the design.** You tune it for your own use case. The point is that one decision (classifier) is type-shaped and reproducible, and the other (responder) is free-form and creative — and the architecture separates them cleanly.

## Code shown in this lesson

```python
from pydantic import BaseModel, Field
from typing import Literal

# Classifier — structured output (video 05)
class RoutingDecision(BaseModel):
    intent: Literal["creative", "factual", "urgent", "speed"]
    provider: Literal["claude-sonnet", "gpt-4o", "gpt-4o-mini", "grok-llama-3.3-70b"]
    reason: str = Field(description="One sentence.")

classifier = studio.create_agent(
    name="router",
    provider="gpt-4o-mini",  # fast and cheap for routing
    role="request classifier",
    goal="pick the right model for each user message",
    instructions=(
        "Creative → claude-sonnet. Factual → gpt-4o. "
        "Urgent → claude-sonnet (apologetic). Speed → grok."
    ),
    response_model=RoutingDecision,
)
```

```python
# Responder — fresh agent per turn, with the picked provider, streamed
def stream_answer(provider: str, message: str):
    responder = studio.create_agent(
        name="responder",
        provider=provider,
        role="helpful assistant",
        goal="answer the user clearly",
        instructions="Be direct. No preamble.",
    )
    for chunk in responder.run(message, stream=True):
        if chunk.done:
            break
        print(chunk.content, end="", flush=True)
```

```python
# Main loop — classify, route, stream
def chat(message: str):
    decision = classifier.run(message)              # typed RoutingDecision
    print(f"→ routing to {decision.provider} ({decision.reason})")
    stream_answer(decision.provider, message)
```

## Try this

1. Add a fifth intent — `"analytical"` — to the `RoutingDecision` model, mapped to `gpt-4o-mini` in the classifier's instructions. Feed it three analytical questions ("Summarize this CSV", "What's the trend?") and prove the classifier picks the right provider.
2. Replace the hard-coded routing table with a per-user preference dict (`{"creative": "claude-sonnet", "factual": "gpt-4o", "default": "gpt-4o"}`). Make the classifier honor those preferences in its instructions. Two users, same prompt, different providers — the architecture should hold.

## Transcript

Today's the first capstone. I'm not introducing anything new — we're just going to build a thing. The last three videos were pointing at two agents and a chat loop, and by the end of this video you've got a working chatbot that you can extend however you want.

Same setup as the rest of the series. Install. Load the API key. Spin up Studio.

Here's the shape. User types something. First agent is the classifier — structured output from video five. It looks at the message and returns a typed decision: what kind of request is this, and which provider should handle it? Second agent is the responder — provider swapping from video three, streaming from video four. It gets instantiated fresh with whichever provider the classifier picked, and streams the answer back.

Why two agents? Because routing is a different job than answering. Classification needs a predictable typed output — perfect fit for `response_model`. Answering needs a conversational stream — perfect fit for `stream=True`. One agent trying to do both would be worse at both. This is a pattern you reach for a lot once you're building real systems — small specialized agents beat one big one.

Classifier first. Pydantic model for the decision shape. Four intents, four providers, one-to-one today for clarity, but you can make this many-to-many later. The `reason` field is there so we can see what the classifier was thinking. Pydantic field description steers the model to keep it to one sentence. Instructions are the routing table in plain English — I'm hard-coding my opinion about which provider fits which intent. You tune this for your own use case. Creative intent → Claude. One-sentence reason. Exactly the shape we designed.

Responder is a function, not a persistent agent, because the provider changes per turn. We spin up a fresh agent every time. Cheap. Stateless. `create_agent` is just a config call. Same streaming loop from video four — `stream=True`, iterate, break before printing on `done`, print `chunk.content` otherwise. That break-before-print is the one to remember — the final chunk carries the full accumulated text, so printing it duplicates the whole answer. The only new thing here is the `provider` parameter — that's what makes the function a router target.

We can run it standalone. Now let's plug it into the classifier. The loop is short: classify, route, stream. Three lines of real work. Classifier runs first, returns a typed routing decision. I print the routing line so we can see the system's reasoning — you'd hide this in production, but for a demo it's the interesting part. Then `stream_answer` runs the responder with the picked provider.

Three different intents, three different providers, all handled by the same two-agent system. Kyoto request went creative — Claude. Merge-sort question went factual — GPT-4o. Urgent apology went to Claude, and Grok for speed. No branching logic in my code. The classifier decided all of it.

And look at the answer shapes. Kyoto came back as a full structured itinerary — days, headings, tips. Merge-sort came back as just the formula. The apology came back as a single sentence. Same instruction in the responder — "be direct, no preamble." Three different providers and each one trimmed itself to fit the question.

Quick framework to take with you. This is a two-agent system. Call it classify-and-answer if you want a label. Classifier is typed, synchronous, fast — uses `response_model`. It makes one decision and hands off. Responder is free-form, streamed, provider-flexible — uses `stream=True` and whatever provider the classifier picked. The separation is the point. Each agent has one job. You can swap the classifier for a smarter version without touching the responder. You can add new providers to the routing table without changing the loop. You can point the classifier at a different decision schema — say, routing between tools instead of providers — and the same architecture holds. Three features — structured outputs, provider swap, streaming — doing one job each.

That's the capstone. Build on this. Add a memory layer and turn it into a real multi-turn chat. Swap the hard-coded routing table for user-specific preferences. Add a fallback provider for when the first one fails. The architecture holds up under all of it.

Next block is multimodal — image generation and file inputs.

I'm Felipe with Lyzr. Until next time.
