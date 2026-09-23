# Swapping LLM Providers

*Lesson 03 · Module 1 — Foundations*

## What you'll learn

- How a single string change moves an agent between providers
- Short-form vs explicit `provider/model` notation, and when to reach for each
- Which providers Lyzr supports out of the box
- The behavioural differences across OpenAI, Anthropic, Google, and Grok on the same prompt
- A practical default for picking a model when you start a new project

## Key concepts

**One string changes the brain.** The `provider` parameter on `create_agent` takes a model name. Lyzr routes the call to the right place. Same agent, different brain.

**Two notations.** Short form is just the model name — `gpt-4o`, `claude-sonnet`, `gemini-2.5-pro`. Lyzr auto-detects which provider it belongs to. Explicit form is `provider/model` — `openai/gpt-4o`, `anthropic/claude-sonnet`. Start short; fall back to explicit only when an auto-detect error tells you to.

**Providers supported out of the box:** OpenAI, Anthropic, Google, Grok, Perplexity, AWS Bedrock.

**Models converge on canonical answers.** Four out of five providers in the side-by-side landed on "abstraction" as the most elegent idea in programming. That's the real lesson — for definition-shaped questions, the model choice barely matters. Provider comparisons earn their keep on **open-ended work** — creative angles, taste-dependent tasks. Not on questions with a single textbook answer.

**Practical defaults.** For most apps, start with the latest GPT or Claude Sonnet — broad capability, reliable, what most apps ship with. For high-volume work where each call doesn't need to be brilliant, drop to the latest GPT-mini, Claude Haiku, or Gemini Flash. For research and citations, Perplexity models are tuned for grounded answers with sources — different job. For most prototypes, the model choice matters less than the prompt; get the agent working on the default first, then try swapping providers.

## Code shown in this lesson

```python
# Short form — Lyzr auto-detects the provider
agent = studio.create_agent(provider="gpt-4o", ...)
agent = studio.create_agent(provider="claude-sonnet-4.5", ...)
agent = studio.create_agent(provider="gemini-2.5-pro", ...)

# Explicit form — provider/model
agent = studio.create_agent(provider="openai/gpt-4o", ...)
agent = studio.create_agent(provider="anthropic/claude-sonnet", ...)
```

```python
# Same role, goal, instructions across four providers
prompt = "What's the most elegant idea in programming? Answer in two sentences."

for provider in ["gpt-4o", "claude-sonnet-4.5", "gemini-2.5-pro", "grok-llama-3.3-70b"]:
    agent = studio.create_agent(
        name=f"compare-{provider}",
        provider=provider,
        role="programming philosopher",
        goal="answer concisely",
        instructions="Two sentences max.",
    )
    print(provider, "→", agent.run(prompt).response)
```

## Try this

1. Run the same prompt — *"What's the most elegant idea in programming? Answer in two sentences."* — across five providers (GPT-4o, Claude Sonnet, Gemini Pro, Grok-Llama, and one Perplexity model). Document which providers converged on the same idea and which one disagreed.
2. Pick one provider you'd default to for *factual* queries and one for *creative* queries. Write two sentences explaining your reasoning. Keep it for reference the next time you start a project.

## Transcript

One string changes your entire backend. The `provider` parameter on `create_agent` takes the name of a model, and that's it. Lyzr routes the call to the right place. Same agent, different brain. Today we swap through four providers on the same prompt and watch the answers change.

Usual setup. If you've watched the first two videos, this is familiar.

Two formats work. Short form — just the model name. `gpt-4o`, `claude-sonnet`, et cetera. Lyzr figures out which provider it belongs to and routes the call. Or explicit form — `provider/model`. `openai/gpt-4o`, et cetera. Short form is what I use day to day. It's cleaner. And if Lyzr can't auto-detect for some reason, the error message tells you to use the explicit form. So start short, fall back explicit only when you need to.

Multiple providers work out of the box — OpenAI, Anthropic, Google, Grok, Perplexity, AWS Bedrock. We're going to run four of them today.

Starting with OpenAI, GPT-4o. Same role, goal, instructions you've seen in the last two videos. Prompt: in two sentences, what's the most elegant idea in programming? *Abstraction.* Classic textbook answer. Measured, explanatory — "enables developers to build upon existing functionality." That's the baseline. OpenAI register. Safe, complete, not electric.

Swap one string. Claude Sonnet 4.5. Everything else identical. Also abstraction — but feel the voice shift. It's shorter, drier on the details. Claude reached for a turn of phrase where OpenAI reached for a definition. Same idea, different instincts.

Let's go with Google Gemini 2.5 Pro. Abstraction again. Gemini leans more formal — "enormously complex systems, understandable parts" — cleaner clauses, a little more academic. Three models, same answer.

And Grok. I'm using Llama 3.3 70-billion-parameter — the same open-weight model most places run, but served fast. Here's the outlier — Llama didn't say abstraction, it went with recursion. Only disagreement across the four. Smaller open-weight models aren't pulling from the exact same associations as the frontier closed models, and on open-ended prompts like this one you feel it. Also: speed. Grok serves that noticeably faster than the others, which is the thing Grok is actually selling.

Quick note before the rundown. Four of these five landed on abstraction. That's the real headline. Models converge on canonical safe answers. Provider comparisons earn their keep on open-ended work — creative angles, taste tasks, anything with room for taste — not on definition-shaped questions. Keep that in mind when you do your own side-by-sides.

You don't need to memorize the catalog. Here's how I think about picking. Default: the latest GPT or Claude Sonnet — broad capability, reliable, what most apps ship with. Fast and cheap: the latest GPT Mini, Claude Haiku, the latest Gemini Flash — when you're doing high volume and each call doesn't need to be brilliant. Research and citations: Perplexity models are tuned for grounded answers with sources. It's a different job.

The honest version: for most prototypes, the model choice matters less than the prompt. Get your agent working on the latest GPT or Claude Sonnet, then try swapping providers. Once you know what good looks like, that's when the comparison is useful.

One string changes the brain. Start with a default. Swap when you have a reason.

Okay. Next up, streaming responses — the same agent, but getting the text back token by token instead of all at once.

Until next time.
