# Your first Agent

*Lesson 02 · Module 1 — Foundations*

## What you'll learn

- The role each of the five `create_agent` parameters plays
- The mental shortcut: role is identity, goal is direction, instructions are behavior
- How `temperature` actually changes model behavior (and when it doesn't)
- What fields live on the response object beyond `.response`
- Which response field matters for memory work later in the course

## Key concepts

**Pick descriptive names.** `my-assistant` is fine for a demo. For real work, `support-triage-bot` is what shows up in Studio and in your logs. The name is for *you*, not the user.

**Role vs goal vs instructions.** Role is one sentence describing what the agent *is* — `customer support agent`, `senior python engineer`, `travel concierge`. Role sets voice. Goal is what it's trying to *achieve* — `help customers resolve issues`, `review code for correctness and style`. Goal orients every response. Instructions are the specific behavior rules — `be empathetic, concise, and solution-oriented`. Instructions tune tone and behavior. **If your agent isn't behaving how you'd like, 90% of the time it's one of these three fields.**

**Temperature is the one optional knob worth knowing.** Range 0 to 2, default 0.7. Low temperature plays it safe — predictable, repetitive, close to the model's single most likely answer. High temperature takes more risks — creative, varied, sometimes weirder. **Caveat:** temperature only moves behavior when there are lots of good answers to pick from. Ask for the definition of recursion and the model lands in the same sentence regardless. Ask for a metaphor for recursion and you see the spread.

**Temperature in practice.** Drop it below 0.7 for factual, consistent answers. Raise it above 0.7 for creative work — brainstorming, naming, copywriting. Crank it too high and you get nonsense. Don't touch it unless you have a reason.

**The response object is more than text.** `response.response` is the answer. `response.session_id` is the conversation thread this response belongs to — it matters when we get to memory. `message_id` and `metadata` come back as `None` for now; they populate in specific cases covered later.

## Code shown in this lesson

```python
agent = studio.create_agent(
    name="support-triage-bot",
    provider="gpt-4o",
    role="customer support agent",
    goal="help customers resolve issues",
    instructions="Be empathetic, concise, and solution-oriented.",
)
```

```python
# Optional knob: temperature
agent = studio.create_agent(
    name="creative-writer",
    provider="gpt-4o",
    role="creative writing partner",
    goal="generate vivid metaphors",
    instructions="Be imaginative.",
    temperature=1.5,
)
```

```python
response = agent.run("Give me a metaphor for recursion.")
print(response.response)
print(response.session_id)  # save this for memory work later
```

## Try this

1. Build a code-reviewer agent. `role="senior python engineer"`, `goal="review code for correctness and style"`, `instructions="Always explain your reasoning before giving code."` Feed it a five-line Python function with a deliberate off-by-one bug and see whether the agent catches it.
2. Run the recursion-metaphor prompt three times at `temperature=0` and three times at `temperature=1.8`. Note which temperature produced repetition and which produced range. Then try `temperature=1.0` and see where it lands.

## Transcript

Last video we shipped a working agent in about ten lines. Today we open it up. Five parameters shape every Lyzr agent you will ever build. We'll walk through each one, then I'll show you one optional knob that changes the agent's behavior in a way you can actually see.

Quick setup. Install the SDK pinned to `0.1.9`. Load the API key from the `.env` file. Initialize Studio. Same as last video. If you've done video one, you can skip to the next section.

Here's a standard agent — five parameters.

First, a `name` — a label for this agent. It's how you find it later in Studio, and it's what shows up in logs. Pick something descriptive. `my-assistant` is fine for a demo. `support-triage-bot` is better for real work.

Second, a `provider` — the LLM you want the agent to use. GPT-4o, Claude Sonnet 4.5, Gemini 2.5, et cetera. We'll swap these in the next video. For now we're sticking to GPT-4o.

Third, a `role` — one sentence describing what the agent *is*, not what it does. *What it is.* Customer support agent. Senior python engineer. Travel concierge. The one word matters because it sets the voice.

Followed by `goal` — what the agent is trying to achieve. Help customers resolve issues. Review code for correctness and style. Plan trips that fit the user's budget. The goal orients every response.

Finally, `instructions` — the specific behavior rules. Be empathetic, concise, and solution-oriented. Always explain your reasoning before giving code. Never recommend restaurants without checking availability. This is where you tune tone and behavior.

Role is identity. Goal is direction. Instructions are behavior. If your agent is not behaving how you'd like it to, 90% of the time it's one of these three fields.

`agent.run()` takes a message and returns a response object. The text is on `.response`. We saw this last video. Let's run it with a question where I can show you something interesting. Clean one-sentence textbook definition — "a function calls itself to solve smaller instances of the same problem." That's our baseline.

Now I want to show you one optional parameter, because it changes behavior in a way you can feel. **Temperature.** Zero to two. Default is 0.7. Low temperature — the model plays it safe. Predictable, repetitive, close to its most likely response. High temperature — it takes more risks, more creative, more varied, sometimes weirder.

One note on the demo: temperature only moves behavior when there are lots of good answers to pick from. Ask for a definition of recursion, and the model's going to land in the same sentence no matter what. So I'm switching the prompt to something more open-ended — a metaphor for recursion. Same agent otherwise. What happens at zero, then at 1.5?

"Mirrors. Two mirrors facing each other, each reflection holding a smaller version of itself." That's the model's single most likely metaphor for recursion at zero. Run it ten times, you'll get the same sentence almost word for word.

Now let's turn it up. Temperature 1.5. Same prompt. "Russian nesting dolls." Different metaphor entirely. And notice it added a little more — "until reaching the tiniest one that can't be opened. That's the base case." Dressed up. At 1.5 the model isn't picking the top answer anymore — it's sampling from a wider slice of the distribution. Ask again, you might get a tree, a fractal, something even weirder. Crank it higher and eventually you get nonsense.

That's the trade. Higher temperature is great for brainstorming, naming things, creative writing — anything where you want range. Bad for anything that needs to be consistent and accurate. Default of 0.7 is a good middle ground. Drop it for factual, consistent answers. Raise it for creative work. And don't touch it unless you have a reason.

One more thing. The response object isn't just text. Let me show you what else is on it. `text` (which `.response` gives you) is the answer itself. `session_id` is set — that's the conversation thread this response belongs to, and it will matter when we get to memory in a few videos. `message_id` and `metadata` came back as `None` — they'll populate in specific cases that we're going to cover later. For now, `.response` is the one you use 90% of the time. The session ID is the other one worth remembering. The rest is there when you need it.

That's the anatomy. Five required parameters — name, provider, role, goal, instructions. One optional knob that matters — temperature. And a response object with more on it than just text.

The following videos in this series will add more parameters to `create_agent` — memory, tools, knowledge bases, structured outputs, guardrails. They all hang off the same signature you just walked through. Next up, we swap the provider. Same agent, different brain.

I'm Felipe with Lyzr. Until next time.
