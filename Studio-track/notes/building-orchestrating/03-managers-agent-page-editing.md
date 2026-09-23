# Managers, part 2 — editing from the agent page

*Lesson 03 · Design & Create*

## What you'll learn

- See why a manager is "just an agent" — and edit it from the ordinary agent page, not only the canvas
- Add a new specialist to a live manager's team and tell the manager when to use it
- Prove a newly added specialist is wired in by reading the manager's event trail
- Choose between the Orchestrate canvas and the agent page for growing a team

## Key concepts

**A manager isn't a special, separate thing — it's an agent with a team.** Because it's an agent, you can open it, edit it, and grow its team right from the regular agent page, with the same Build, Playground, and Deploy tabs as any other agent. The canvas is one way in; the agent page is another.

**You grow the team from the Build tab's managed-agents section.** Open the manager — the Northwind support agent — and scroll to its managed-agents section on Build. The order-lookup and returns agents you wired on the canvas show up right here; it's the same team, just viewed from the agent's own page.

**Adding a specialist is: pick the agent, tell the manager when to use it, save.** Click **Agent**, choose the Northwind billing agent, and give it a short usage note — "billing and duplicate-charge questions." That note is how the manager knows when to route to it. Hit **Update** to save, and the team is now three.

**Prove the wiring with a Playground question and the event trail.** Ask something only the new specialist can handle — "I think I was charged twice for order 5832" — and you'll get a billing-aware reply (flag to payments, refund in 5–7 business days, no stored card numbers). Open the **events** in the activity panel and you'll see the manager calling the billing agent: proof it's really the new specialist doing the work.

**Because a manager is an agent, it deploys and ships like everything else.** No separate orchestration runtime to manage — grow the team whenever you need, and the manager keeps the same deploy story as any single agent.

## In Studio

Studio feature: **Agent page → Build tab → managed-agents section** (editing a manager outside the canvas).

1. From the **registry**, open your manager — the **Northwind support agent**. It opens like any agent, with **Build**, **Playground**, and **Deploy** tabs.
2. On the **Build** tab, scroll down to the **managed-agents** section. You'll see the team set up earlier: the order-lookup agent and the returns agent.
3. Click **Agent** and pick the **Northwind billing agent** to add a new specialist.
4. Give it a short **usage note** — *when to use it*: "billing and duplicate-charge questions" — and save.
5. Click **Update** to save the manager. The team is now three.
6. In the **Playground**, test the new specialist: *"I think I was charged twice for order 5832."* Confirm the billing-aware reply.
7. Open the **events** in the activity panel and find the manager **calling the billing agent** — proof the new specialist is wired in.

## Try this

1. Open an existing manager from the registry (not the canvas) and find its managed-agents section on the Build tab. Confirm the team matches what you wired on the canvas.
2. Add one new specialist from the agent page, write a one-line usage note that clearly scopes *when* it should be called, and Update.
3. Ask a Playground question that only the new agent can answer, then open the event trail and confirm the manager actually routed to it. *If it didn't, sharpen the usage note* and try again.

## Transcript

In the last video, we built our concierge manager on the Orchestrate canvas. But here's something worth knowing: a manager is really just an agent, so you can open it, edit it, and grow its team right from the regular agent page. Let me show you by adding a new specialist to the team. I'll open our manager, the Northwind support agent, from the registry. It opens just like any agent with its Build, Playground, and Deploy tabs. On the Build tab, I scroll down to the managed-agents section. There's the team we set up earlier: an order-lookup agent and a returns agent. This is the same team from the canvas, just shown here in the agent's own page. Now I'll add a new specialist. I click Agent and pick our Northwind billing agent. I can give it a quick note on when to use it — billing and duplicate-charge questions — and save. And that's it. The team is now three. I'll hit Update to save the manager. Let's prove the new specialist is wired in. In the Playground, I'll ask: "I think I was charged twice for order 5832." And here's the reply. It apologizes, saying it will flag the order to the payments team, and explains that if it's a duplicate charge, the extra amount comes back to the original payment method within five to seven business days. It even notes we don't store full card numbers. And here's the proof it's really the new agent doing the work. Over on the activity panel, I'll open the events, and there it is — the manager calling the billing agent, the specialist I added a minute ago. So a manager isn't a special separate thing. It's an agent with a team. You can build it on the canvas or edit it right here. Grow the team whenever you need, and because it's an agent, it deploys and ships like everything else. Next up, the other style of orchestration: SuperFlow, for when the steps are fixed. I'm Felipe with Lyzr. I'll see you there.
