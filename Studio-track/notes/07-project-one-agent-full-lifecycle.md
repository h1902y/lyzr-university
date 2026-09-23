# Project — one agent, full lifecycle

*Lesson 07 · Foundations · The Agent Lifecycle*

## What you'll learn

- Trace one agent's full lifecycle — build, equip, govern, test, deploy, monitor — in a single pass through the Studio UI
- Open a production trace and read the whole story of one conversation: the question, the steps, the knowledge pulled, the model, the latency, and the cost
- Recognise the signal that a trace gives you, and know which lever to pull — instructions, knowledge, or guardrails — when something looks off
- Use monitoring to *know* your agent is behaving in production instead of hoping it is

## Key concepts

**The whole lifecycle lives in one place, on one agent.** Build (role, goal, instructions), equip (tools and a Northwind knowledge base), govern (a Responsible AI guardrail that redacts personal data before the model sees it), test, deploy — every stage you've learned is visible on the same agent record in Studio. You don't assemble five tools; you walk one page top to bottom.

**Monitoring is the stage that closes the loop.** Building, governing, and testing all happen before customers arrive. Traces are how you watch the agent once it's live — every conversation it has leaves a trace, so production stops being a black box.

**A single trace tells the whole story of one interaction.** Open the most recent trace and you see the question that came in, the steps the agent took, the knowledge it pulled, the model it used, how long it took, and what it cost. That's the difference between knowing your agent behaves and hoping it does.

**A trace that looks off is a signal, not a verdict.** When something in the trace looks wrong, that's your cue to go back one stage — adjust the instructions, the knowledge base, or the guardrails — and improve the agent. Monitoring feeds straight back into build; the lifecycle is a loop, not a line.

## In Studio

1. Open the support agent's record and read it top to bottom: its **identity** (role, goal, instructions), what it's **equipped** with (the tools it can call and the Northwind help-docs knowledge base), and how it's **governed** (the Responsible AI guardrail that redacts personal data before the model sees it).
2. Jump into the **Playground** and ask one of the suggested questions — confirm the answer comes back grounded in the docs, exactly as intended.
3. Note the agent's status: it's already **deployed and published**, live and ready for customers — no extra step needed.
4. Go to **Monitoring → Traces** — the one stage not yet explored — to see every conversation the agent has logged.
5. Open the **most recent trace** and walk through it: the incoming question, the steps the agent took, the knowledge it pulled, the model it used, the latency, and the cost.
6. Read it as a health check. When a trace looks off, treat it as the signal to go back and adjust the **instructions**, the **knowledge**, or the **guardrails**.

## Try this

1. Open your own support agent and walk its record *top to bottom* — name its role, goal, instructions, attached tools, knowledge base, and guardrail out loud. If you can't point to all six on one page, you've found the gap to fill.
2. Ask your agent two questions in the **Playground** — one answerable from the docs, one clearly outside them. Then open both **traces** and compare: which one pulled knowledge, how long each took, and what each cost.
3. Find a trace where the answer wasn't quite right. Decide *which single lever* — instructions, knowledge, or guardrail — you'd change first, make that one change, and re-run the same question to confirm the trace looks better.

## Transcript

over the last six videos, we built a customer support agent and took it all the way to live. In this final video, we will review the whole journey in one pass, and then close the loop by reading the agent's traces to see exactly what it does in production. This is the project. By the end, you'll have touched every stage yourself. Here's the agent we built. Let's walk it top to bottom. This is its identity: the role, the goal, and the instructions that tell it how to behave. Here's what we equipped it with: the tools it can call and the knowledge base, our Northwind help docs, that grounds its answers in our real policies. And here's how we governed it, the responsible AI guardrail that redacts a customer's personal data before the model ever sees it. Build, equip, govern, all in one place. Now let's test it. I'll jump into the playground and ask one of the suggested questions And there's the answer, grounded in our docs exactly like we want And it's already deployed and published, live and ready for customers Now the one stage we haven't really gone deep into yet, this is where the life cycle closes. Every conversation the agent has leaves a trace. I'll open the most recent one and walk through it. You can see the whole story of that single interaction, the question that came in, the steps the agent took, the knowledge it pulled, the model it used, how long it took, and what it cost. This is how you know your agent is behaving out in the real world instead of just hoping it is. And when something looks off in here, that's your signal to go back, adjust the instructions, the knowledge, or the guardrails, and improve it. And that's the full life cycle. One agent built, equipped, governed, tested, deployed, and monitored entirely in Laser Studio. You've now seen every stage, and you've got everything you need to go build one of your own. I'm Felipe with Lizer. Thanks for watching
