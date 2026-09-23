# SuperFlow: Loops

*Lesson 05 · Design & Create*

## What you'll learn

- Handle a whole batch in one SuperFlow run instead of rebuilding the same steps per item
- Start from a template (the Batch Sentiment Analyzer) rather than wiring a loop from scratch
- Use the loop node's two outputs — `loop` and `done` — for the right job
- Generalise one loop to resumes, support tickets, or spreadsheet rows without changing its shape

## Key concepts

**A lot of real work isn't one item — it's a whole batch, and you don't want to rebuild the steps for each one.** A stack of reviews, a folder of resumes, a list of orders: the answer is a loop. It's the one piece of SuperFlow the invoice lesson didn't cover, and it's what turns a single-run flow into a batch processor.

**Starting from a template beats building from scratch.** Begin a new SuperFlow, name it (here, *Northwind Review Sentiment*), and load the **Batch Sentiment Analyzer** template. It comes as a ready-made loop you can build on: a trigger, a code step that splits incoming text into a list (one item per line), the loop, an LLM classify step, and an output.

**A loop runs its inner steps once per item — that's the whole point.** Whatever list comes in, the loop sends each item through the steps inside it one at a time. Five reviews in means the classify step runs five times, independently, without you duplicating a single node.

**The loop node has two outputs, and the difference matters.** The **`loop`** output runs the inner steps once for every item on the list. The **`done`** output fires only once the loop has finished, and it carries the *full set* of results out the other side — so downstream steps see the complete batch as a single bundle, not a trickle of individual items.

**One loop generalises to any batch of the same shape.** Five customer reviews classified positive / negative / neutral with confidence scores is just one example — swap the reviews for resumes, support tickets, or rows in a spreadsheet and the same flow works unchanged. The loop is about the *shape* of the work, not the specific content.

## In Studio

Studio feature: **Create Agent → SuperFlow → loop node** (plus the template gallery).

1. Start a **new SuperFlow** and name it — *Northwind Review Sentiment*.
2. Instead of building from scratch, **start from a template**: the **Batch Sentiment Analyzer**. It loads a ready-made loop.
3. Read the shape: a **trigger** → a **code step** that splits incoming text into a list (one item per line) → the **loop** → an **LLM classify** step → an **output**.
4. Note the loop's two outputs: **`loop`** (runs the inner steps once per item) and **`done`** (fires once at the end, carrying the full result set).
5. **Run it** — paste five customer reviews, one per line, and hit **Run**. Watch each step light up as the loop sends the reviews through the classify step one at a time.
6. Read the result: five reviews in, five classifications out (positive / negative / neutral), each with a confidence score; the **`done`** branch hands back the whole set in a single bundle.
7. Generalise: swap the reviews for resumes, support tickets, or spreadsheet rows — the same loop handles them the same way.

## Try this

1. Load the **Batch Sentiment Analyzer** template, paste in five short reviews (one per line), and run it. Confirm you get one classification per line, each with a confidence score.
2. Trace the loop's two outputs: follow what leaves the **`loop`** output versus what leaves the **`done`** output. Write one sentence on why a final report step should hang off `done`, not `loop`.
3. Repurpose the flow for a different batch — paste a handful of support tickets or resume blurbs instead of reviews, and adjust the classify step's prompt. *Notice you changed the content, not the loop.*

## Transcript

In the last video, we built a SuperFlow that ran once, start to finish. But a lot of real work isn't one item. It's a whole batch: a stack of reviews, a folder of resumes, or a list of orders. And you don't want to rebuild the same steps for each one. You want a loop. That's the one piece of SuperFlow we didn't cover last time. So let me show you. I'll start a new SuperFlow, call it Northwind Review Sentiment, and instead of building from scratch, I'll start from a template, the Batch Sentiment Analyzer. It loads a ready-made loop I can build on. Here's the shape: a trigger to kick it off, a code step that splits whatever text comes in into a list, one item per line. Then the important one, the loop. Then an LLM step that classifies and an output. The loop has two outputs worth pointing at. One is loop, which runs the steps inside it once for every item on the list. The other is done, which only fires once the loop has finished, and it carries the full set of results out the other side. Let me run it. I'll paste in five customer reviews, one per line, and hit Run. Watch each step light up. The loop takes the five reviews and sends them through the classify step one at a time. And here's the result. Five reviews in, five classifications out. Arrived early. Works perfectly. Positive. Support never answered my refund email. Negative. Decent monitor, but the stand feels cheap. Neutral. Fast shipping. Very happy. Positive. Charger stopped working after a week. Negative. Each one with a confidence score. One flow, the whole batch handled, and a done branch hands back the complete set in a single bundle. That's loop. The same steps run over every item in a batch on their own. Swap those reviews for resumes, support tickets, or rows in a spreadsheet, and it works exactly the same way. And that wraps the Design and Create course. You've got single agents, managers, and SuperFlows, plus the judgment to pick between them. I'm Felipe with Lyzr.
