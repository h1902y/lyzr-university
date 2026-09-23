# Why tools matter

*Lesson 16 · Module 4 — Tools & Workflows*

## What you'll learn

- Why an agent is a **text model** that, by default, can't query your database, hit an API, or check live state
- How `agent.add_tool()` hands the agent a plain Python function and lets it decide when to call it
- How the **docstring becomes the description** and **type hints become the schema** — no decorators, no special class
- The picking rule for tools vs. RAG vs. prompt context

## Key concepts

**An agent is a text model — it can reason, but it can't *do*.** Ask about a specific product SKU and a tool-less agent will admit it can't see real-time inventory and offer to interpret a snapshot if you paste one. Honest, but the customer still has no answer. The agent can reason about the question and tell you which fields to pull; it just can't go look at the data itself. That's the gap tools close.

**A tool is just a Python function.** No decorators, no special class — anything callable. The **docstring** becomes the description the model reads to decide *when* to call it; the **type hints** become the schema that tells it *what* to pass. The SDK handles the call-and-return loop. In a real system the function hits a database or an API; for a demo a hard-coded dict has the same shape from the agent's perspective.

**`agent.add_tool()` wires it up in one line.** Register the function, rerun the same question, and the agent reads the docstring, recognizes the tool fits, parses the argument out of your prompt (e.g. the SKU `GH-2400`), calls the function, gets the result, and reformats it into a clean answer. Docstring tells the model what the tool does; type hints tell it what to pass; the SDK handles the call.

**Tools, RAG, and prompt context solve different problems.** **Tools** are for *actions and real-time state* — anything the agent needs to do or look up that isn't in its training data and isn't a static document: inventory lookups, DB queries, API calls, sending email, calculations on live data. If the answer changes after training, you need a tool. **RAG** is for *static knowledge* you control — docs, policies, manuals, read once per query (videos 10–15). **Prompt context** is for *small, stable* info — the user's name, the date, system rules — a few hundred tokens that don't justify infrastructure.

**The picking rule is short.** Tools when the answer requires *doing* something. RAG when the answer is a *document* you control. Prompt when it's a *sentence or two* of context. Most production agents use all three.

## Code shown in this lesson

```python
# One install tweak for notebooks: the [jupyter] extra pulls in nest_asyncio so tool
# calls work inside a notebook event loop.
# pip install "lyzr-adk[jupyter]"
```

```python
# Tool-less agent — honest, but stuck.
agent = studio.create_agent(
    name="support", provider="gpt-4o",
    role="customer support agent",
    goal="answer product and inventory questions",
)
agent.run("Is SKU GH-2400 in stock?")
# → "I can't see real-time inventory, but if you paste a snapshot I can interpret it."
```

```python
# A tool is just a Python function. Docstring = description, type hints = schema.
def check_inventory(sku: str) -> str:
    """Look up live inventory status for a product SKU."""
    # Real system: hit a database or API. Demo: a hard-coded dict, same shape.
    inventory = {"GH-2400": "in stock, 47 units, DC East"}
    return inventory.get(sku, "SKU not found")
```

```python
# Hand the function to the agent, rerun the same question.
agent.add_tool(check_inventory)
agent.run("Is SKU GH-2400 in stock?")
# → "In stock — 47 units (DC East)."  The agent parsed GH-2400, called the tool, reformatted.
```

## Try this

1. Run the question once *before* `add_tool` and once *after*. Diff the answers — the before is an honest dodge, the after is a real answer.
2. Change `check_inventory`'s docstring to be vague ("does stuff with a sku") and see whether the agent still reliably picks it. Restore a crisp docstring and watch reliability return — proof the docstring is the interface.
3. Add a second tool (e.g. `get_price(sku: str) -> float`) and ask a question that needs both. Watch the agent chain the calls and combine the results.

## Transcript

Agents are text models. By default, they can't query your database, hit an API, or check the current state of anything. Today we close that gap. The SDK lets you hand the agent a Python function — anything that's callable — and the agent figures out when to call it. We'll do the before, after, and look at when this is the right reach versus RAG or just stuffing context into the prompt. Same setup as the rest of the series with one tweak: the install line uses `lyzr-adk[jupyter]`, which pulls in nest_asyncio so that tool calls work inside a notebook event loop.

We have a real business question. A customer is asking about a specific product SKU. The agent has no tools, no knowledge base, no way to check the actual inventory system. Watch what happens. The agent admitted it can't see real-time inventory and offered to interpret a snapshot if I paste one. Honest, but the customer still doesn't have an answer. The agent is a text model — it can reason about the question, ask the right follow-ups, even tell me which fields to pull. But it can't go look at the data itself. That's the gap.

A tool is a Python function. That's it. No decorators, no special class. The docstring becomes the description the model reads. The type hints become the schema. The SDK does the rest. In a real system this hits a database or an API; for the demo it's a hard-coded dict, same shape from the agent's perspective. The function takes a SKU and returns a string with the inventory status. The model reads the docstring to know when to call it, reads the type hint to know what argument to pass, and the SDK handles the call-and-return loop.

One line to wire it up — `agent.add_tool(check_inventory)` — then rerun the same question. Same agent, same question. The answer: in stock, forty-seven units, DC East. The agent read the docstring on check_inventory and recognized it was the right tool for the question. It also parsed GH-2400 out of my prompt, called the function, and got the result back. And reformatted it as clean bullets. That's the loop: docstring tells the model what the tool does, type hints tell it what to pass, the SDK handles the call.

Quick rundown so you know when to reach for this versus the other patterns we've covered. Tools are for actions and real-time state — anything the agent needs to do or look up that isn't already in its training data and isn't in a static document: inventory lookups, database queries, API calls, sending emails, running calculations on live data. If the answer changes after the agent was trained, you need a tool. RAG is for static knowledge — documentation, policies, manuals, things that don't change minute to minute and that the agent reads once per query; we cover this in videos ten through fifteen. Prompt context is for small, stable info you can just paste in: the user's name, the current date if you really want it pinned, system rules, anything that fits in a few hundred tokens and doesn't justify infrastructure. The picking rule is short: tools when the answer requires doing something, RAG when the answer is a document you control, prompt when it's a sentence or two of context. Most production agents use all three.

That's the fundamentals: a tool is a Python function, the agent reads the docstring, calls it when it makes sense, uses the result. Next video, we go deeper on writing local tools — the patterns that hold up in production, the edge cases, and the structured output patterns for richer return types. I'm Felipe with Lyzr. Until next time.
