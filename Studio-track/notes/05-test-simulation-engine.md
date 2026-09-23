# Test — run it in the Playground

*Lesson 05 · Foundations · The Agent Lifecycle*

## What you'll learn

- Run your agent in the Playground and confirm it answers in-scope questions straight from your knowledge base
- Probe the harder case — an out-of-scope question — and verify the agent admits the gap and escalates instead of guessing
- Open the trace for any reply to see the exact knowledge-base search and why the agent answered the way it did
- Use the test → adjust → re-test loop to decide when an agent is actually ready to ship

## Key concepts

**Testing means checking behaviour, not just that the agent runs.** "Does it execute" is a low bar. The real questions are sharper: does it know what it should, does it admit what it doesn't, and can you see why it answered the way it did. The Playground is where you put those questions to the agent before a customer does.

**A trustworthy agent admits what it doesn't know.** Asked about a price-match policy that lives nowhere in the Northwind help docs, our agent says it's not sure, notes the docs don't cover it, and offers to escalate to a human. A weaker setup would have invented a confident answer — and a confident wrong answer is the most expensive kind.

**The trace turns "I hope it works" into "I can verify it works."** Open the trace on any reply and you see the agent's actual steps: here, it searched the knowledge base for `Do you price match Best Buy?`, got nothing back on price matching, and escalated rather than guessing. You're not trusting the reply — you're reading the reasoning behind it.

**Testing is a loop, and it tells you when to ship.** If an answer comes back wrong, the fix is one of three knobs: the instructions, the knowledge, or the model. Adjust, re-run the scenario, repeat. When the agent passes the scenarios that matter to you, it's ready — and deploying is the next lesson.

## In Studio

1. From the agent's page, open the **Playground** and start a fresh chat.
2. Test an in-scope question first — type *"What's the return window for an unopened laptop?"* The reply comes straight from the Northwind help docs: returnable within 30 days of delivery for a full refund.
3. Now test the harder case — an out-of-scope question the docs don't cover: *"Do you price match Best Buy?"* Read the reply: the agent says it's not sure, notes the docs don't mention a price-match policy, and offers to escalate to a human agent.
4. Open the **trace** for that last message (Monitoring → Traces). Inspect the steps: the agent searched the knowledge base with the query `Do you price match Best Buy?`, the docs returned nothing on price matching, so it escalated instead of guessing.
5. If any answer comes back wrong, adjust the **instructions**, the **knowledge base**, or the **model**, then re-run the same scenario. Repeat until the scenarios that matter to you all pass.

## Try this

1. Open the Playground and ask one question you *know* is answered in your docs and one you *know* isn't. Confirm the first quotes the source and the second admits the gap and escalates — *don't accept a confident answer to the out-of-scope question.*
2. Open the trace on the out-of-scope reply and find the knowledge-base search step. Read the query the agent sent and the (empty) result — that empty result is *why* it escalated.
3. Deliberately break it: temporarily remove the relevant doc from the knowledge base, re-ask the in-scope question, and watch the agent move from a grounded answer to an honest "I don't know." Then restore the doc and confirm the grounded answer returns.

## Transcript

We've built our agent, equipped it, and locked it down with a guardrail. Before we put it in front of real customers, we test it. Not just does it run, but does it behave the way we need it to? That's what the playground is for I'll open the playground and start a fresh chat. A couple of things I want to confirm: does it know what it should? Does it admit what it doesn't? And can I see why it answered the way it did? First, something it should know. What's the return window for an unopened laptop? And there it is. Unopened laptops can be returned within 30 days of delivery for a full refund. That came straight from our help docs, exactly what we want Now the more important test. What happens when I ask something that isn't in our docs? Do you price match Best Buy? Watch the reply. It says it's not sure, that our help docs don't mention a price match policy, and it offers to escalate to a human agent. This is the behavior that builds trust. A weaker setup would have invented a confident answer. Ours admits what it doesn't know and routes the customer to a person And I can see exactly why. I'll open the trace for that last message. Here's the agent searching our knowledge base with the query, "Do you price match Best Buy?" The docs come back with nothing on price matching, so instead of guessing, it escalated. That's the difference between an agent you hope works and one you can actually verify. If an answer ever comes back wrong, this is your loop. Adjust the instructions, the knowledge, or the model, and test again. When it passes the scenarios that matter to you, it's ready to ship, and shipping is exactly what's next. I'm Philippe with Leizer. See you there
