# Structured Outputs

*Lesson 05 · Module 1 — Foundations*

## What you'll learn

- Why prompt-the-model-for-JSON is a fragile pattern and what breaks it
- How `response_model` with a Pydantic class replaces parsing entirely
- That `agent.run()` returns the typed instance directly when `response_model` is set
- How Pydantic `Field` descriptions steer the model's output (not just document the schema)
- When structured outputs become a force multiplier (nested schemas)

## Key concepts

**The wrong way:** ask the model for JSON in the prompt, then parse the string on the other side. The model will wrap it in a markdown code fence, skip the preamble unpredictably, or just return malformed JSON on the fourth case you didn't think of. You end up writing a parser with three fallbacks and it still breaks. That's not the model's fault — you didn't tell it the shape, you hoped.

**The right way:** define a Pydantic model and pass it to `create_agent` as `response_model`. `agent.run()` returns an instance of that model directly. No `.response` to unwrap, no parsing, no JSON-cleanup helpers. Your IDE knows the fields, types are enforced, and Pydantic raises before bad data reaches your code.

**`Field` descriptions are not decoration.** The SDK passes them to the model as part of the schema, which means they actually steer the output. If you want a field a certain way, put the instruction in `Field(description=...)`, not in the prompt.

**The real payoff is nested schemas.** A list of issue models, a float with a 0-to-1 constraint, a boolean, descriptions everywhere — the agent returns the whole thing typed, ready to drop into a database, a dashboard, or a follow-up agent.

**One mental shift.** Your prompt stops carrying schema instructions. Your code stops carrying parsers. The SDK handles both ends. Once you use this you stop writing parsing code forever.

## Code shown in this lesson

```python
# The wrong way — ask for JSON in the prompt
prompt = "Return a JSON object with sentiment and confidence for: " + review
response = agent.run(prompt)
data = json.loads(response.response)  # breaks on code fences, preambles, drift
```

```python
# The right way — define a Pydantic model
from pydantic import BaseModel, Field
from typing import Literal

class ReviewAnalysis(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    confidence: float = Field(ge=0, le=1)
    summary: str = Field(description="One-sentence issue summary, no padding.")

agent = studio.create_agent(
    name="review-analyzer",
    provider="gpt-4o",
    role="customer feedback analyst",
    goal="classify and summarise customer reviews",
    instructions="Be objective.",
    response_model=ReviewAnalysis,
)

analysis = agent.run(review)
print(analysis.sentiment, analysis.confidence, analysis.summary)
```

```python
# Nested schemas — where structured outputs really pay off
class Issue(BaseModel):
    category: Literal["billing", "quality", "shipping", "support"]
    description: str = Field(description="One-sentence issue summary.")

class RichAnalysis(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    confidence: float = Field(ge=0, le=1)
    issues: list[Issue]
    would_recommend: bool
```

## Try this

1. Extend the `ReviewAnalysis` model with a new field — `topics: list[str] = Field(description="3-5 short tags that capture what the review is about.")`. Re-run on a longer review and inspect the tags. Note whether the field description actually steered the model toward short tags or whether it ignored your guidance.
2. Constrain `confidence` to `Field(ge=0.5, le=1.0)`. Feed in a genuinely ambiguous review (mixed sentiment, contradictions). Observe what the model returns — does it clip its confidence, or refuse, or do something else?

## Transcript

Today we're getting structured data out of an agent — not a string you have to parse, not JSON you have to hope is valid. A Pydantic model — validated, typed, ready to use. One parameter on `create_agent` and the shape of the return value changes completely.

Same setup as always. Install Lyzr, load the key, spin up Studio. I've pinned the review we're going to analyze to a `review` variable so we can feed the exact same input to every agent in this video.

Before we do this the right way, let me show you the wrong way — because this is what most people reach for first. Ask the model for JSON in the prompt. "Return a JSON object with sentiment and confidence." Then parse the string on the other side.

Look at that. The model wrapped it in a markdown code fence — triple backticks, `json` tag, then the object inside. Technically correct JSON, completely impossible to `json.loads` without stripping those fences first. And *this* time it skipped the "here's your JSON" preamble — but run it again or run it on a different provider and you'll get one. There's no contract. There's no guarantee. This is the reality — you end up writing a parser with three fallbacks and it still breaks on the fourth case you didn't think of. That's not the model's fault. You didn't tell it the shape — you just hoped.

Here's the fix. Define a Pydantic model for the shape you want. Pass it to `create_agent` as `response_model`. That's it. Three fields. `sentiment` is an enum — one of three strings. `confidence` is a float. `summary` is a string. Standard Pydantic.

Notice something. `agent.run()` didn't return an `AgentResponse` object. It returned a `ReviewAnalysis` instance directly. No `.response` to unwrap. I can pull `.sentiment` and `.confidence` off it like any Pydantic object — and they're typed. My IDE knows `sentiment` is one of those three strings. If the model ever tries to return something that doesn't fit the schema, Pydantic raises before the bad data reaches my code. That's the whole feature.

Your prompt stops carrying schema instructions. Your code stops carrying parsers. The SDK handles both ends.

The simple case is cheap. But the real payoff is when the schema gets real. Nested `Issue` model. A list of them. A float with a 0-to-1 constraint. A boolean. And `Field` descriptions everywhere. Those descriptions are not decorators — the SDK passes them to the model as part of the schema, which means they steer the output. If you want a field a certain way, put it in a description, not in the prompt.

Same input, richer output. Three issues this time — shipping, quality, support. Each one categorized. Each one with a one-line description pulled from the review. `would_recommend` flagged `false`. All typed. Ready to drop into a database, a dashboard, or a follow-up agent — whatever's next in your pipeline.

And notice the field descriptions are earning their keep. I told the description field it should be a one-sentence issue summary, and the model honored that. No padding. Just the substance.

That's structured outputs. One parameter, one Pydantic class, a typed object on the other side. This is one of those features where once you use it, you stop writing parsing code forever.

Next video is the first capstone. We take everything from the last three — multi-provider swapping, streaming, structured outputs — and build a small chatbot that uses all three.

I'm Felipe with Lyzr. Until next time.
