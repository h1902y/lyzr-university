# Build — choose a type & create an agent

*Lesson 02 · Foundations · The Agent Lifecycle*

## What you'll learn

- Create a working agent in Studio from three plain-English fields — role, goal, and instructions
- Choose the right agent type for a single-focus job versus a coordinator, a workflow, or a voice line
- Write a role, a goal, and instructions that actually steer behaviour, using the new-hire briefing pattern
- Recognise which behaviour rules are real controls and which are still just promises waiting on a guardrail

## Key concepts

**An agent in Studio is three plain-English fields, not a codebase.** You describe the job in a role, define success in a goal, and set the standing rules in instructions. The visual builder turns that brief into a running agent — no schema, no boilerplate, and (here) without writing a line of code.

**Brief an agent the way you'd onboard a new hire.** The role is its job title (`customer support agent`). The goal is what success looks like — answer questions about orders, returns, warranties, and shipping from the help docs, and escalate what it can't resolve. The instructions are the standing rules: be friendly and concise, answer from the knowledge base, admit when it doesn't know, and offer to escalate. Same mental model as a person joining your team.

**Pick the simplest agent type that fits the job.** Studio offers several types — `Agent` for a single focused job, a manager type to coordinate several agents, `Superflow` for multi-step workflows, and `Voice` for phone and IVR. Our support bot does one focused job, so the plain `Agent` type is the right call. Don't reach for a coordinator or a workflow when one agent will do.

**An instruction is only a promise until a guardrail enforces it.** One of our rules — never handle a customer's personal data — is a behaviour we *state* in the instructions, but the model can still slip. Stating it sets intent; it isn't a hard control yet. A couple of lessons from now we enforce it for real with a guardrail (lesson 04).

**Creating the agent already makes it live.** When Felipe clicks Create, the agent doesn't just save to a list — it's immediately reachable behind an API. There's no separate deploy step. We unpack what "live" means in the deploy lesson (lesson 06). Right now the agent only knows what the model already knows — nothing about Northwind yet; the next lesson equips it.

## In Studio

Studio feature: **Create Agent → Agent**.

1. From the Studio home screen, click **Create Agent**.
2. Studio asks what kind of agent you want. Choose the **Agent** type — a single agent doing one focused job (the other types are the manager/coordinator type, **Superflow** for multi-step workflows, and **Voice** for phone and IVR).
3. Fill in the **Role** — its job title: `customer support agent`.
4. Fill in the **Goal** — what success looks like: answer customer questions about orders, returns, warranties, and shipping using the help docs, and escalate anything it can't resolve.
5. Fill in the **Instructions** — the standing rules: be friendly and concise, answer from the knowledge base, admit when it doesn't know and offer to escalate, and never handle a customer's personal data.
6. Give the agent a **Name**: `Northwind Support Agent`.
7. Click **Create**. The agent is built and is already live behind an API.

## Try this

1. Create your own single-focus `Agent` for a domain you know — a returns assistant, an onboarding helper, whatever. Fill only the role, goal, and instructions, name it, and click Create. *Resist adding anything else* — you'll equip it next lesson.
2. Rewrite your goal so it names the *exact* topics the agent should cover and says what to do with anything outside them (e.g. "escalate"). Notice how a sharp goal does more steering than a vague one.
3. In your instructions, add one rule that's really a *promise* — something like "never share another customer's data." Note it down: in lesson 04 you'll turn that promise into an enforced guardrail.

## Transcript

In the last video, we toured Studio. Now we build. We're going to create our customer support agent from scratch, and the whole thing comes down to three plain English fields, no code at all I'll click Create Agent. Lizer asks what kind I want. There is voice, Superflow, and a few others, but ours is a single agent doing one focused job, so I'll pick Agent Now I brief it the same way you'd onboard a new hire. First, the role. This is its job title, customer support agent Then the goal, what success looks like. Answer customer questions about orders, returns, warranties, and shipping using our help docs and escalate anything it can resolve And then the instructions, the standing rules for how it behaves. I'm telling it to be friendly and concise, to answer from our knowledge base, to admit when it doesn't know, and offer to escalate, and never to review a customer's personal data. That last rule is a promise, and in a couple of videos, we'll actually enforce it with a guardrail I'll give it a name, Northwind Support Agent, then click Create. And there it is. Notice it didn't just save, it's already live. We'll come back to what that means in the deploy video. That's a working agent built from three fields and no code. But right now it only knows what the model already knows. Nothing about Northwind. In the next video, we equip it with our knowledge, a tool, and memory. I'm Felipe with Lieser. See you there
