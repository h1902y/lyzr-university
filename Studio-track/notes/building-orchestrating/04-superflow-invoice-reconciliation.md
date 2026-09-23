# SuperFlow: Invoice Reconciliation

*Lesson 04 · Design & Create*

## What you'll learn

- Read a real SuperFlow end to end — trigger, document parsing, extraction, a branch, a human approval, and two exits
- Mix deterministic logic and agentic judgment on one canvas, sometimes in the very same node
- Pause a run durably for human approval — for minutes, hours, or days — at no cost
- Replay and resume runs from history without re-running steps that already completed

## Key concepts

**SuperFlow is Lyzr's visual builder for systems of agents — deterministic where you need guarantees, agentic where you need judgment.** Hand work to a manager and you get intelligence but lose control over *when* things happen; wire a rigid static workflow and you get control but hit a ceiling fast. SuperFlow refuses that trade-off: you choose, node by node, which cells are guaranteed and which are judged.

**Every SuperFlow starts with a trigger, and one trigger can start three ways.** The invoice flow's trigger accepts **file uploads**; the same trigger also exposes a **webhook URL with a secret** so another system can fire it programmatically, and a **cron schedule** to run it on a timetable. One node, three ways to start.

**Document AI nodes turn a raw file into structured fields.** **Parse document** takes whatever the trigger received — PDF, Word doc, image, same node — and extracts its text. **Extract fields** then runs an extraction model against that text using a schema you define; here it returns an invoice ID and a total amount as structured fields you can reference downstream.

**The same node can be deterministic or AI-judged — that's the core idea.** **Match SOR** is an `if` node checking whether the extracted invoice ID equals an ID in your system of record: match routes one way, no-match the other. But the same `if` has an **AI mode** — for a fuzzy condition like "does this invoice look unusual," you write it in plain language and let an LLM evaluate it. Some cells you want guaranteed; some you want judged.

**A `wait for approval` node pauses the run durably — and the pause is free.** On the no-match branch, an **approval-summarizer agent** writes a short paragraph for the human, who then sees a form with that summary and a field to paste a corrected invoice. The run holds there for minutes, hours, or days at no cost; approve and it resumes, reject and it ends with an error.

**Replayable history is what makes it production-grade, not a toy canvas.** Every run is saved; you can open history, replay any execution on the canvas, and rerun from a specific node. Steps that already completed don't run again — so a mid-flow retry won't double-charge anyone, approvals can wait days, and schedules survive restarts.

## In Studio

Studio feature: **Create Agent → SuperFlow** (the visual flow builder, document-AI nodes, `if` node, wait-for-approval, HTTP request nodes).

Walking the **invoice reconciliation** flow node by node:

1. **Trigger** — accepts a file upload (an invoice). Also offers a webhook URL + secret and a weekday cron, if another system or a schedule should start it.
2. **Parse document** — a document-AI node; extracts text from the uploaded PDF / Word / image.
3. **Extract fields** — runs an extraction model with your schema; pulls the **invoice ID** and **total amount** as structured fields.
4. **Match SOR** — an `if` node comparing the extracted ID against your system of record. *(In production this would be an HTTP request to your database just before the `if`; the demo hard-codes one ID to keep the flow in focus.)*
5. **Match → S3.** On a match, an **HTTP request** node posts the original file straight to S3 — no human in the loop.
6. **No match → approval summarizer.** An agent (built earlier in the agents tab) reads the extracted data and writes a short summary for the approver.
7. **Wait for approval** — the run pauses. The approver sees the summary plus a field to paste the corrected invoice's URL. Durable pause; approve to continue, reject to end with an error.
8. **Recovery → S3.** On approval, an HTTP request posts the **corrected** file to S3.
9. **Run it with a non-matching invoice** and watch each node light up; the false branch summarizes, pauses (blue = waiting), then resumes on approval and posts the corrected file. Open **history** to replay or rerun from any node.

## Try this

1. Trace a flow you care about as a SuperFlow on paper: name the trigger, the parse/extract steps, the one `if` that branches it, and the two terminal exits. Mark which single node would need a human approval.
2. For your branching `if`, decide whether it should be **deterministic** (an exact match) or **AI-judged** (a fuzzy "does this look off?"). Write the condition both ways and notice which one your case actually needs.
3. Add a **wait-for-approval** step in your design and write the summary an agent should hand the approver. *Keep it to what they need to decide* — what it is, the amount, and what's worth flagging.

## Transcript

Real agentic work is almost never one agent answering one prompt. It's several steps. A branch where the path depends on what came back. A point where a human has to sign off. Today, you usually pick a side. You hand it to a manager agent. You get intelligence, but you lose control over what happens when. Or you wire it as a static workflow. You get control, but you hit a ceiling fast. SuperFlow is Lyzr's new visual builder for systems of agents. Deterministic where you need guarantees, agentic where you need judgment. Let me show you a workflow I built to make this concrete. This workflow is called invoice reconciliation. The story is simple. An invoice comes in, we parse it, we pull out the invoice ID and the total amount. We check the ID against our system of record. If it matches, the file goes straight to S3. If it doesn't, the workflow pauses. An agent writes a summary for the human approver. The approver either uploads a corrected invoice, and the corrected version goes to S3, or rejects, and the run stops with an error. Let me walk the nodes. Every SuperFlow starts with a trigger. This one accepts file uploads, which is what makes sense for an invoice flow. The same trigger has a webhook URL with a secret if I want another system to fire it programmatically, and a cron schedule if I want to run it every weekday at nine. One node, three ways to start. Parse document is one of Lyzr's document AI nodes. It takes whatever the trigger received and extracts the text: PDFs, Word docs, images, same node. Extract fields runs an extraction model against that parsed text using a schema I defined. I'm asking for two things: an invoice ID and a total amount. The model returns them as structured fields I can reference downstream. Match SOR is an if node. This is where deterministic logic lives. I'm checking whether the extracted invoice ID equals an ID from my system of record. Match route one way. No match, route the other. What's interesting about this node is that the same if has an AI mode. If my condition were fuzzy, like does this invoice look unusual, I'd write it in plain language and let an LLM evaluate it. Some cells you want guaranteed, some you want judged, and it's the same node. One honest note: in production, the SOR check would be an HTTP request to my database before this if. Here I've hard-coded one ID to keep the demo focused on the flow. If the IDs don't match, the failed invoice goes to an AI agent. This is the approval summarizer, an agent I built earlier in the agents tab. It reads the extracted data and writes a short paragraph for the human approver — what the invoice is, the amount, and what's worth flagging. Then we hit wait for approval. The run pauses here. The approver sees a form with the agent summary at the top and a field below where they paste the URL of the corrected invoice. The pause is durable. Minutes, hours, days, SuperFlow holds the run at no cost. If they approve, we continue. If they reject, the run ends with an error. The terminal nodes are HTTP requests to S3, one on each branch. Each sends the right file, the original on the matched path, the corrected file on the recovery path. Let me run this with an invoice that won't match. The trigger receives the file. Parse document extracts the text. Extract fields pulls the ID and the amount. Match SOR runs the comparison. The IDs don't line up, so it routes to the false output. The approval summarizer reads the fields and writes its summary. The workflow pauses here. Blue means we're waiting. There's the agent summary, and below it, the field where the approver pastes the corrected invoice. I'll paste in the corrected invoice ID and approve. The run resumes. The corrected file gets posted to S3. Done. If the IDs had matched in the first place, this would have gone straight to S3 with no human in the loop. Same canvas, both paths. Every run is saved. I can open history, replay any execution on the canvas, and rerun from a specific node if I just want to retry a tail. Steps that already completed don't run again, so if I retry mid-flow, I don't double-charge anyone. Approvals can wait days at no cost. Schedules survive restarts. This is the part that makes it production grade instead of a toy canvas. So that's SuperFlow. Deterministic where you need guarantees. Agentic where you need judgment. One canvas, and it survives failure. I'm Felipe with Lyzr. Until next time.
