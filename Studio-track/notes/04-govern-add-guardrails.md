# Govern — add guardrails

*Lesson 04 · Foundations · The Agent Lifecycle*

## What you'll learn

- Create a Responsible AI policy in Studio and turn on the personally identifiable information (PII) guardrail
- Choose between *block* and *redact* for each data type, and pick the right one for a support agent
- Attach the policy to your agent so it runs automatically on every message, in and out
- Prove the guardrail works by sending sensitive data and watching it get masked before the model sees it

## Key concepts

**A guardrail is enforcement, not a request.** In the build lesson you *instructed* the agent never to repeat personal data — that's a request the model may or may not honor. A guardrail under Responsible AI is a rule that runs automatically on every message, completely separate from whatever the model decides. You want both: the instruction guides, the guardrail enforces.

**Guardrails run on the way in and the way out.** They sit between the customer and the model, screening each message before it reaches the model and before the reply goes back. That's why redacted PII never reaches the model in the first place — the agent literally cannot read a card number back to a customer because it never received it.

**Redact keeps the conversation useful; block stops it.** For each kind of sensitive data you choose *block* (stop the message entirely) or *redact* (mask just the sensitive part and let the conversation continue). For a support agent you want *redact* — you still need to help the customer, you just never want to see or store their private data.

**One policy covers far more than PII.** The same Responsible AI policy library includes prompt-injection protection, toxicity, banned topics, and more. You switch on the protections that match your risk and leave the rest off — governance is opt-in, per agent.

## In Studio

1. Open **Responsible AI** and create a new policy. Name it `Northwind PII masking`.
2. Inside the policy, browse the guardrail library and find **Personally Identifiable Information**. Switch it on.
3. For each sensitive data type, choose how to handle it — **Block** or **Redact**. Set **credit card numbers**, **email addresses**, and **phone numbers** to **Redact**.
4. **Save** the policy.
5. Open your support agent. Under **Features**, open **Responsible AI** and pick **Northwind PII masking**, then **Save** to attach it.
6. Test it: send a message the way a customer would — include an email address and a full card number, e.g. *"I was charged twice. Help."* Confirm the reply says it can't see the email or card details, yet still routes the duplicate-charge issue to the payments team.

## Try this

1. Build a policy with the PII guardrail and set email to *Redact*. Send a message containing your email, then change that one setting to *Block* and send the same message. Note the difference: redact still answers, block stops the message cold.
2. In the guardrail library, switch on **toxicity** or **banned topics** alongside PII in the same policy. Re-attach and send a message that trips it — see one policy enforce multiple protections at once.
3. Send a phone number *without* attaching the policy first, then attach it and resend. Confirm the agent could read the number back before, and can't after — that's the guardrail, not the instruction, doing the work.

## Transcript

Our support agent is sharp and grounded in our docs. But before it ever talks to a real customer, we have to deal with a real risk. Customers will hand it sensitive information, their email, their phone number, sometimes a full card number. We do not want any of that reaching the model or sitting in our logs. So in this video, we add a guardrail Leiser live under responsible AI. Think of them as rules that run automatically on every message, on the way in and on the way out, completely separate from whatever the model decides to do. Remember in the build video, we told the agent never to review personal data? That was an instruction, a request. A guardrail is an enforcement. You want both. I'll create a new policy and call it Northwind PII masking. Inside the policy, there's a whole library of guardrails. The one we want is personally identifiable information. I'll switch it on Now I choose how to handle each kind of sensitive data, and I have two options: block, which stops the message entirely, or redact, which masks just the sensitive part and lets the conversation keep going. For a support agent, I want redact. We still want to help the customer. We just never want to actually see or store their private data. So I'll set credit card numbers, email addresses, and phone numbers to redacted, and save Then I attach the policy to our agent. Under Features, I open Responsible AI, pick Northwind PII masking, and save Now let's prove it. I'll send a message the way a customer actually would. I'll include my email address, my full card number, and say, "I was charged twice. Help." And watch the reply. The agent says it can't see or repeat my email or card details. This is the guardrail doing its job. It redacted the email and the card before the model ever saw them, so the agent literally cannot read them back to me. And notice it still helps. It tells the customer that duplicate charges go to the payments team and offers to help with their order instead. Safe and still useful. And this is just one guardrail. The same policy covers prompting action, toxicity, banned topics, and more. You turn on the protections that match your risk. Our agent is now governed. Next, we put it through a proper test across real scenarios. I'm Felipe with Lyzr. See you there.
