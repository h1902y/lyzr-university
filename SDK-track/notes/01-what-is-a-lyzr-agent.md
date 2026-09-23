# What is a Lyzr Agent

*Lesson 01 · Module 1 — Foundations*

## What you'll learn

- What a Lyzr Agent actually is in concrete terms
- How to install the Lyzr ADK and configure a single API key for the whole SDK
- The five parameters that define a basic agent
- How `agent.run()` returns text from a model
- Where every other capability (streaming, structured outputs, memory, tools, knowledge bases) plugs into this same shape

## Key concepts

**One API key, not one per provider.** Lyzr handles provider credentials server-side. You sign in at `studio.lyzr.ai`, copy your API key from the account page, and put it in a `.env` next to your notebook. The SDK reads `LYZR_API_KEY` automatically — no OpenAI key, no Anthropic key, no per-vendor secret to wrangle.

**Studio is the entry point.** Two lines of setup: `from lyzr import Studio` and `studio = Studio()`. That's how you create agents, knowledge bases, and everything else the SDK exposes.

**Five parameters define a basic agent.** `name` (a label so you can find it later), `provider` (the LLM — e.g. `gpt-4o`), `role` (what the agent *is*), `goal` (what it's *trying to do*), and `instructions` (how it should respond). Memory, tools, knowledge bases, structured outputs — they all hang off the same `create_agent` signature, layered on top.

**An agent is three things.** An LLM, a set of instructions that shape how it responds, and a run loop (`agent.run()`) that ties them together. That's the whole mental model. Everything else in this course is a way to feed more context in, get more structured data out, or let the agent take action.

**No ceremony.** If you're coming from other agent frameworks, you might expect more scaffolding. There isn't any here, and that's the point.

## Code shown in this lesson

```bash
pip install lyzr-adk==0.1.9
```

```python
from lyzr import Studio
studio = Studio()
```

```python
agent = studio.create_agent(
    name="my-assistant",
    provider="gpt-4o",
    role="A helpful assistant",
    goal="Answer the user's questions accurately",
    instructions="Be concise.",
)

response = agent.run("What is an agent?")
print(response.response)
```

## Try this

1. Re-run the agent in cell 4 with `provider="claude-sonnet"` instead of `"gpt-4o"`. Same question, same instructions. Compare the two answers side-by-side. What changed — the substance, the voice, both?
2. Change the instructions from `"Be concise."` to `"Answer in exactly three sentences."` Re-run. Verify the constraint held; if it didn't, note which sentence the model added or dropped.

## Transcript

Today we're building your first agent with the Lyzr SDK. By the end of this video you'll have a working agent running locally, and you'll understand what *agent* actually means in this stack. Let's jump in.

First thing — install the SDK. The package is `lyzr-adk`. Note the `-adk` on the end. I'm pinning to `0.1.9` so that everything in these videos works exactly the same for you.

You need one API key for the whole SDK, not one per provider. Lyzr handles the provider credentials server-side, so you don't need an OpenAI key, an Anthropic key — one Lyzr key covers everything. Sign in at `studio.lyzr.ai`, go to your account page, copy the API key. I've got mine in a `.env` file next to the notebook — that keeps the key out of the code. The SDK reads `LYZR_API_KEY` automatically, so all I need to do is load the file.

Here's cell three. Two lines. Import `Studio` from `lyzr` and initialize it. Studio is the entry point for the whole SDK. It reads your API key from the environment, and it's how you create agents, knowledge bases, everything else we're going to cover.

Cell four is the agent itself. Five parameters: a `name` so you can find it later; a `provider` — I'm using GPT-4o; a `role` that describes what the agent *is*; a `goal` that describes what it's *trying to do*; and `instructions` that shape how it responds. That's the whole surface for a basic agent. Everything else we'll cover — memory, tools, knowledge bases, structured outputs — hangs off the same call.

Cell five runs the agent. `agent.run()` takes a message, sends it to the model, returns a response object. The text is on `response.response`. There it is — a clean three-sentence answer: definition, how it works, examples — image recognition, recommendation systems, autonomous vehicles. Honestly, the instruction says "be concise" and this leans more textbook than concise. It's a solid answer, but on the longer side. That's exactly the kind of behavior we'll tune in the next video when we open up `create_agent`.

So what is an agent, really? An agent is three things: an LLM (that's the provider line — GPT-4o in our case), a set of instructions that shape how it responds (role, goal, instructions), and a run loop (`agent.run()` is the call that ties it all together). That's it. Everything in this course builds on those three. Streaming is a different way to get the response back. Structured outputs constrain what comes out. Memory gives the agent context across calls. Tools let it do things beyond text. Knowledge bases let it read your documents. All of it hangs off the same `create_agent` and `agent.run()` shape you just wrote.

If you've used other agent frameworks, you might be expecting more ceremony. There isn't any, and that's the point.

Next up, we open up the hood on `create_agent` — every parameter, what it does, when to reach for it. If you want to get ahead, change the provider in cell four to `claude-sonnet` or `gemini` and see what happens. We'll cover provider swapping in more depth soon.

I'm Felipe with Lyzr. Until next time.
