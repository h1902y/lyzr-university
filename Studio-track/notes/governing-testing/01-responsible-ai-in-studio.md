# Responsible AI in Studio

*Lesson 01 · Govern — Studio: Responsible AI & Guardrails*

## What you'll learn

- Build and understand the risks of a naive agent with zero grounding context.
- Implement fact-grounding and self-reflection features using the Hallucination Manager.
- Interpret reflection reports and groundedness evaluations in the playground activity panel.
- Understand the trade-offs in response latency when enabling real-time self-checking.
- Design reusable security and safety policies at the platform level (responsible AI) and subscribe agents to them.

## Key concepts

**A naive model will hallucinate plausible but incorrect answers with high confidence.** LLMs are next-token autocompleters; they do not know what facts they lack, resulting in fabricated business metrics or commitments if not grounded.

**The Hallucination Manager provides a localized safety layer for individual agents.** By combining Groundedness (pinning the model to facts you declare) and Reflection (forcing the model to evaluate and rewrite drafts before output), you eliminate fabricated responses.

**Self-reflection creates a latency trade-off that is essential for production security.** Checking draft responses requires additional background cycles. While this adds seconds to response time, it is vital for customer-facing applications.

**Responsible AI policies act as shared compliance infrastructure.** Security rules (PII masking, toxic blocking, prompt-injection defense) are defined at the platform level. Agents subscribe to them, centralizing compliance management.

## In Studio

Studio features: **Hallucination Manager** (within Agent Settings) & **Build → Responsible AI** (for platform-wide policies).

1. Navigate to the agent registry and edit an agent's details.
2. Under **Features**, locate the **Hallucination Manager** section.
3. Toggle on **Groundedness** and enter key business facts (e.g., return rules, support boundaries).
4. Toggle on **Reflection** to enable the self-checking critique loop.
5. Save the agent, open the Playground, ask a previously hallucinated question, and trace the reflection report in the activity logs.
6. To build org-wide rules: Go to **Build → Responsible AI**, click **New Policy**, and select safety modules (PII masking, toxicity detectors, SQL validators, or external engines like AWS Bedrock / Google Model Armor).
7. Go back to your agent, open the **Responsible AI** feature, and subscribe the agent to your newly created policy.

## Try this

1. Build a simple naive agent and ask a question it cannot know. Observe its confident hallucination.
2. Toggle on the Hallucination Manager, supply one ground truth fact, repeat the query, and inspect the reflection traces in the playground.

## Transcript

Ask an agent a question it doesn't know the answer to, and it will not say, "I don't know." It will probably make something up with confidence. In this video, I build an agent that invents a store policy on camera, and then I fix it with two features, guardrail policies and the hallucination manager. This is the govern stage of the agent life cycle. First, the trap. I'm building the most naive agent possible, a role, a goal, and a one-line instruction that boils down to sound confident. No knowledge base, no facts, nothing. Studio even gives it a friendly name for me. This is how a lot of first agents actually get built, and it works right up until someone asks a question the model can't know Yes, we do price match qualifying items with other retailers, and our return window is 30 days. Sounds great, completely made up. Northwind has no price match program, and that return window is a guess that happens to land close to the real policy, which almost makes it worse because nothing about this answer looks wrong. The model isn't lying, it's autocompleting. It has no idea what Northwind's policies are, so it generates something plausible in a demo, that's funny. In production, that's a pricing commitment your company now has to honor. The fix lives in the agent's features in a group called the hallucination manager. Three modules. Reflection makes the agent check its own answer before sending it. Groundedness pins the agent to facts you declare. An LLM as judge brings in a second model to grade every response. I'll use the first two. Groundedness takes a list of facts in plain English. I'll give it two. We don't price match, and here's the real return policy. Reflection I just switched on. I update, back to the playground, same question Same model, same prompt, and this time no price matching. That's my facts, almost word for word, because there is now a layer that evaluates the draft answer against them and rewrites it if it drifts. You can see the machinery in the activity panel, a reflection report, a groundedness evaluation, and a rewrite event. One honest trade-off, this answer took noticeably longer because the agent is doing real checking work now. For a customer-facing agent, that trade-off is almost always worth it. Hallucinations are one failure mode. The responsible AI page handles the rest as policies you define once and attach to any agent. A policy is a bunch of guardrail modules. Most run right here pII masking, secret detection, banned topics, toxicity, prompt injection detection, Even validators that check output is legal SQL or a valid API spec. And if your company already standardized on an enterprise guardrail stack, there are managed modules for AWS Bedrock Guardrails and Google Model Armor. I'll keep it simple. One module on save, and then in the agent, I attach the policy under the responsible AI feature. That's the whole pattern. The policy is governance infrastructure. The agent just subscribes to it. Build it once, attach it to 50 agents, and if legal ever changes a rule, you add it just one place. So that's Govern in practice. Facts and reflection at the agent level, policies at the platform level. Think about which failure would actually hurt your business, a made-up answer or a leaked email address, and turn on the modules that block it. Next video, we stress test this agent with the simulation engine. I'm Philippe Voelyser. I'll see you there.
