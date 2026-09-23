# Equip — model, tool, knowledge

*Lesson 03 · Foundations · The Agent Lifecycle*

## What you'll learn

- Pick the agent's model in Studio and understand when a fast, low-cost default is the right call versus when to swap up for more reasoning.
- Create a Knowledge Base, upload your own support docs, and ground the agent so it answers from your content instead of inventing facts.
- Attach a web-search tool so the agent can reach beyond its docs for the rare question they don't cover.
- Confirm memory is on so the agent holds context across a conversation and the customer never repeats themselves.

## Key concepts

**The model is the agent's brain, and you can swap it without rebuilding anything.** It's the engine that does the reasoning, and Studio offers a range across providers. A fast, low-cost default is exactly right for a high-volume support agent; if you later need more reasoning power, you change the model in one place and everything else stays intact.

**Grounding is the fix for confident hallucination.** Ask a plain model about Northwind's warranty and it will give a specific, authoritative answer that is completely made up — the fastest way to lose a customer's trust. Attaching a Knowledge Base of your own documents forces the agent to answer from your content, so every claim traces back to a real policy.

**Knowledge is what the agent knows; tools are what it can do.** A Knowledge Base grounds the agent in your docs. A web-search tool gives it a way to act when a question falls outside those docs — it sits in the background and the agent decides when to reach for it, instead of guessing.

**Memory turns a series of messages into a real conversation.** It's on by default, and it lets the agent remember what was said earlier so a customer never has to repeat themselves. Without it, every message starts from a blank state.

**Equipped is not the same as safe to ship.** With a model, grounded knowledge, a tool, and memory, the agent is genuinely useful — but useful and safe to ship are two different bars. Guardrails come next.

## In Studio

1. Open the support agent you built in the last lesson. Find the model selector — it shows the default, a fast, low-cost model from a major provider. Keep it for now; note that this is where you'd swap to a stronger model later without touching anything else.
2. Click **Add Knowledge Base**. Name the new base `Northwind Help Docs`.
3. Upload your actual support documentation into it — the returns, warranty, and shipping policy files. Studio ingests the documents and attaches the Knowledge Base to the agent.
4. Verify grounding: ask *"What is the warranty policy for laptops at Northwind?"* The answer (one-year limited manufacturer warranty, covers defects in materials and workmanship, excludes accidental and liquid damage) should come straight from your docs, with an offer to share the extended-warranty policy.
5. Attach a **web-search tool** so the agent can look beyond the docs for questions they don't cover. It runs in the background; the agent decides when to use it.
6. Confirm **memory** is enabled — it's on by default, so the agent carries context across the conversation.

## Try this

1. Build a tiny Knowledge Base with a single fact only your docs would know — *"Northwind laptops carry a one-year limited warranty."* Ask the agent the warranty question once *before* attaching it and once *after*. Watch it go from a confident guess to a grounded, doc-backed answer.
2. Ask the agent something your docs clearly *don't* cover (for example, a competitor's current pricing). Notice whether it reaches for the web-search tool instead of inventing an answer.
3. Have a short multi-turn chat — mention a detail in one message, then refer back to it (*"and what about that order?"*) a message later. Confirm memory is doing its job and the agent doesn't ask you to repeat yourself.

## Transcript

In the last video, we created our support agent. It can hold a conversation, but right now it's running on the model's general knowledge. It doesn't know a single thing about Northwind. So in this video, we're going to equip it. We'll give it a brain, our own knowledge, a tool, and memory. First, the model. This is the agent's brain, the engine that does the reasoning. Laser gives you a whole range to choose from across different providers. I'm keeping the default here, OpenAI's GPT 5.4 Mini. It's fast and inexpensive, which is exactly what you want for a high-volume support agent. And you're not locked in. If you ever need more reasoning power, you swap the model right here without rebuilding anything else. Now the most important step: knowledge. Here's the problem we're solving. If I ask a plain model about Northwind's warranty, it will give me a confident, specific answer. It will be completely made up. That is the fastest way to lose a customer's trust. The fix is to ground the agent in our own documents. I'll click Add Knowledge Base, create one called Northwind Help Docs, and upload our actual support documentation: returns, warranty, and shipping policies. Laser ingests that, and now it's attached to the agent. Let's prove it works. I'll ask, what is the warranty policy for laptops at Northwind? And look at the answer. Northwind laptops include a one-year limited manufacturer warranty covering defects in materials, workmanship, and it does not cover accidental damage, liquid damage, et cetera. It even offers to share the extended warranty policy. Every bit of that came straight from our docs, not from the model's imagination. That is the difference grounding makes. Next, a tool. Knowledge is what the agent knows. Tools are what it can do. I'm attaching a web search tool. Our docs cover the vast majority of questions, but every so often, a customer asks something that falls outside them. With search attached, the agent can look beyond the docs when it genuinely needs to, instead of guessing. It sits in the background, and the agent decides when to reach for it. And finally, memory, which is already on by default. This is what lets the agent remember the conversation, so a customer never has to repeat themselves. It's the difference between a real conversation and starting a blank state every single message. So now we have a real agent, a brain or knowledge, a tool for the edge cases, and memory. It's genuinely useful. But useful and safe to ship are not the same thing. In the next video, we add guardrails. I'm Felipe with Lieser. See you there
