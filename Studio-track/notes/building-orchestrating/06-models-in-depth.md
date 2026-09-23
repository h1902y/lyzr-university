# Models in depth

*Lesson 01 · Equip & Connect — Studio: Tools, Models & MCP*

## What you'll learn

- Choose the right model for an agent based on four parameters: speed, cost, context window, and reasoning capability.
- Navigate the Compare Models dashboard to evaluate and sort different hosted or custom model offerings.
- Set up a fallback model chain under Connections to ensure service continuity in case of primary provider outages.
- Fine-tune reasoning effort settings (low, medium, high) on reasoning-heavy models to balance output quality against latency and cost.

## Key concepts

**The model is the agent's brain and your primary reasoning lever.** Every decision an agent makes, from tool-selection to natural language formatting, depends on the underlying LLM. Choosing the right model dictates the response latency, cost, and overall intelligence of the system.

**Compare Models is your evaluation center for speed, cost, context, and reasoning.** Instead of guessing or hardcoding, Studio provides a side-by-side dashboard where you can filter by provider (OpenAI, AWS Bedrock, etc.) and sort based on what your application prioritizes.

**Most agent builds fall into three model profiles: fast, high-reasoning, or balanced.** Fast models are best for real-time customer chats where low latency is critical; high-reasoning models excel at complex background tasks where a slow but deep response is acceptable; balanced models serve as the standard middle ground.

**Never ship to production without setting up a model fallback chain.** Models and provider endpoints experience outages. Configuring a chain under Connections ensures that if your primary model fails, the next swappable brain takes over automatically, preventing agent downtime.

**Reasoning effort settings let you tune the trade-off between thought depth and cost.** For reasoning models, Studio exposes low, medium, and high settings. Low is fast and economical, while High tells the model to think harder before responding, which is ideal for complex, multi-variable logic.

## In Studio

Studio feature: **Compare Models** and **Connections → Models**. Here's how to configure and optimize your agent's reasoning engine:

1. Open your agent in **Agent Studio** and locate the **Model** selector dropdown under the agent's primary configuration block.
2. Click **Compare Models** on the left navigation panel. Inspect the comparison table containing speed, cost, context, and reasoning metrics.
3. Filter by provider or sort by speed/cost to find the model that fits your performance and budget target.
4. Go to the **Connections** tab, select **Models**, and click **Configure Fallback Chain**. Add one or two backup models in order of priority.
5. In the agent's advanced parameters, toggle **Reasoning Effort** (Low, Medium, High) to dial in the reasoning level for reasoning-capable models.
6. Click **Save** to lock in your swappable brain and fallback setup.

## Try this

1. Open **Compare Models** and sort by speed. Identify the fastest model on the list. Then, sort by cost and find the cheapest model.
2. Go to **Connections → Models** and configure a fallback chain with at least two backup models.
3. Switch your agent's brain from a fast model to a high-reasoning model and verify that the instructions, knowledge, and tools remain unchanged.

## Transcript

Welcome to Agent Essentials. This track is about the handful of choices that quietly decide whether your agent is good: the model, its memory, and its knowledge. We're starting with the model because it's the agent's brain. Get it right and everything downstream gets easier. Here's our agent, and this, the model, is the engine doing the reasoning. It's the single biggest lever you have over how the agent behaves, how fast it responds, and what it costs you. Lyzr gives you a wide range to choose from, hosted for you across all the major providers, and if you'd rather run on your own provider account, you can bring that too. You can see the providers right here, OpenAI's models, Amazon Bedrocks, and several more. That's a lot of options, which is great, but it raises the obvious question: How do you pick? You don't have to guess. This is Compare Models, and it lays every option out side by side. There are four things worth looking at: speed, how fast it answers; cost, how much each call burns; context, how much it can read at once; and reasoning, how hard it can think. I can filter down to a single provider, like just OpenAI, or look across all of them, and I can sort by what I actually care about. Here's the way I think about it. Most choices fall into three buckets: fast models, when your agent is talking to a customer in real time, and a snappy reply matters most; high-reasoning models, when the task is high value and runs in the background, where you'd happily wait a few seconds for a better answer; and balanced models in the middle, which honestly covers most of what you build. Sort by speed, and the fast ones rise to the top. Sort by cost, and you can find the cheapest model that still does the job. You're matching the model to the work. And here's the part I really like. You're not locked in. Changing the model is one click. I'll switch this from one model to another, and nothing else about my agent changes. Same instructions, same knowledge, same tools. The brain is swappable, so you can always start simple and upgrade later. One thing worth setting before you ship anything for real: fallbacks. Models have bad days. Providers have outages. Under Connections, Models, you can configure a fallback chain. If your primary model fails, the next one in line picks up automatically, so your agent keeps answering instead of going dark. Set it once and stop worrying about it. Last, the fine-tuning. I'll enable the advanced parameters, and because I've put this agent on a reasoning model, I get a reasoning effort setting: low, medium, or high. Low is faster and cheaper. High thinks harder, which costs you a little more time and money, but gets you a more careful answer on tough problems. Match it to how hard the work actually is. I'll save, and that's our model dialed in. So that's the model. Start with a sensible default. Use compare models to match the model to the job. Lean fast for live conversations, and high reasoning for the heavy stuff. Set a fallback before you ship, and remember, you can always swap. Next up in Agent Essentials: Memory, what your agent remembers and how. I'm Felipe. See you there.
