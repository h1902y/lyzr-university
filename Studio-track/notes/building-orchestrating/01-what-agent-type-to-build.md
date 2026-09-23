# What agent type should I build?

*Lesson 01 · Design & Create*

## What you'll learn

- Apply one guiding principle — choose the simplest architecture that reliably solves the problem — to every build decision
- Tell apart the four shapes a Lyzr solution can take: a single agent, a manager, a SuperFlow, and a voice agent
- Recognise the signal that you've outgrown a single agent and which way to step up
- Map a real use case (support, onboarding, invoice processing) to the right architecture before you build anything

## Key concepts

**Picking the agent type is the most important decision you'll make — so start from one principle: the simplest architecture that reliably solves your problem.** You only reach for something more elaborate when a single agent stops being reliable. Everything below is just a way to recognise *when* that moment has arrived and *which* direction to go.

**A single agent is always where you start, and often where you stop.** When one agent can handle the whole task on its own, that's the right call — we built single agents in the last course. The real question is never "should I use more agents?" but "has this one agent stopped being reliable?" If it hasn't, you're done.

**Step up to a manager when the work is conversational, ambiguous, and non-deterministic.** A manager fits when the problem needs reasoning, planning, and delegating tasks on the fly — an AI consultant, a research assistant, a support system that thinks through a few possibilities before it answers. Behind the scenes several specialists collaborate; to the user it stays one smooth conversation.

**Reach for a SuperFlow when the process is deterministic and you want it to run the same way every time.** Instead of letting agents decide what happens next, you define the sequence explicitly. It's ideal for one-shot business processes where the steps are known in advance — employee onboarding, payment processing, patient intake, resume screening, document approval. SuperFlow trades dynamic reasoning for predictability and process control.

**Voice isn't a different brain — it's a different way in.** The intelligence underneath can still be a single agent, a manager, or a SuperFlow; voice just lets people talk to it instead of type. Choose it when speaking is the natural interaction: customer support, healthcare intake, appointment scheduling, field operations, sales and contact centres.

## In Studio

Studio feature: **Create Agent** — the type picker (Agent · Voice Agent · SuperFlow · Proxy Agent), plus **Orchestrate** for managers.

This lesson is the decision, not a build — but here's where each choice lives so the framework maps onto real screens:

1. **Create Agent → Agent** — a single agent doing one focused job. Your default; start here.
2. **Orchestrate → Manager** — you don't create a "manager" from the picker; you build a team and connect a lead agent to its specialists (next lesson). The connection is what makes it a manager.
3. **Create Agent → SuperFlow** — the visual builder for deterministic, multi-step flows (lessons 04–05).
4. **Create Agent → Voice Agent** — a voice front door over any of the above.

The decision in one line: **single** agent when one can solve it alone; **manager** when it needs reasoning, collaboration, or handling ambiguity; **SuperFlow** when the process is fixed and predictable; **voice** when people mostly interact by speaking.

## Try this

1. Write down a problem you actually want to solve, then argue *for a single agent first* — list what it would need to do. Only if you can name a specific reason it would be unreliable should you step up.
2. For that same problem, decide: is the work open-ended and conversational (→ manager) or a fixed sequence of known steps (→ SuperFlow)? Justify the pick in one sentence.
3. Take three everyday processes — onboarding a hire, answering a support ticket, screening a stack of resumes — and tag each as single / manager / SuperFlow / voice. Notice how the *shape of the work*, not its difficulty, drives the choice.

## Transcript

Lyzr gives you a few different agent types, and picking the right one is the most important decision you'll make. So let's walk through them and more importantly, when to use each. We already covered single agents in the last course. A single agent is the right call when one agent can handle the whole task on its own, and that's always where you start. The real question is when to move beyond a single agent and which way to go. And there is one guiding principle behind all of this. Choose the simplest architecture that can reliably solve your problem. You only reach for more when a single agent stops being reliable. The first step up is the manager agent. You reach for it when the problem is complex enough that one agent can't reliably handle it, and when the work is conversational and non-deterministic. That means ambiguity, reasoning, planning, decision-making, delegating tasks on the fly. Think of an AI consultant, a research assistant, or a customer support system that has to think through a few possibilities before it answers. Behind the scenes, several specialized agents collaborate, but to the user, it's one smooth conversation. The other direction is SuperFlow, and it's almost the opposite. SuperFlow is for deterministic automation. Instead of letting agents decide what happens next, you define the workflow explicitly. It's ideal for one-shot business processes where the sequence is known in advance: employee onboarding, payment processing, patient intake, or resume screening, document processing, and approval workflows. Anywhere you want the system to behave the same way every time with no surprises. SuperFlow gives you that predictability through structured orchestration. Then there's voice. Voice agents aren't really a different brain, they're a different way in. The intelligence underneath can still be a single agent, a manager, or SuperFlow. Voice just lets people talk to it instead of type. You use it when speaking is the natural interaction: customer support, healthcare intake, appointment scheduling, field operations, sales and contact centres. So here's how to choose. A single agent when one agent can solve the problem on its own, a manager agent when it needs reasoning, collaboration, planning, or handling ambiguity, a SuperFlow when the process is deterministic and follows a defined sequence of steps, and voice when the main way people interact is by speaking. Start simple and move up only when you have to. Step up to a manager when you need intelligence and collaboration, and reach for SuperFlow when predictability and process control matter more than dynamic reasoning. Over the next few videos, we'll build each of these for real, starting with the manager agent. I'm Felipe with Lyzr. Let's get into it.
