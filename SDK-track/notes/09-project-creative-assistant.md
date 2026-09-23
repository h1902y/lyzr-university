# Project — Creative assistant

*Lesson 09 · Module 2 Capstone — Multimodal*

## What you'll learn

- How to compose three specialized agents into a "plan, then fan out" pipeline
- Why a typed `creative_brief` is the right interface between the planner and the producers
- When to use the flagship model vs a cheap orchestrator inside the same system
- How to write image prompts that don't get sabotaged by the renderer adding logos or UI
- The architectural template you'll keep reusing: small typed specialized agents beat one big one

## Key concepts

**The pipeline.** User gives a one-line product description. The **brief agent** (structured output, video 05) returns a typed `CreativeBrief` — name, headline, key benefits, visual concept. The **image agent** (image generation, video 07) reads the visual concept and renders a hero PNG. The **doc agent** (file generation, video 08) reads the name, headline, and benefits and renders a marketing PDF. Three agents, one orchestrator, two artifacts.

**Plan, then fan out.** The planning step makes the brief. The fan-out runs the image and the doc against the *same* plan. Each agent has one job. This is the architectural template — same shape as the classify-then-answer pattern in video 06.

**Use the flagship model where the thinking happens.** Brief agent gets the heavy lifter (GPT-5.2) because it's doing real creative reasoning. Image agent gets GPT-5 Mini because its only job is to pass the visual concept to the renderer. Doc agent gets the flagship again because writing copy is its actual job. Match the orchestrator to the work.

**Field descriptions steer the model.** In the brief's `visual_concept`, the description specifies "no screenshots, no UI, no laptop screens" — because image models will sneak a logo or a label into any software-product render if given room. The image agent then reads this description, writes its prompt to match, and the wrapper repeats the rules at prompt level for belt-and-suspenders.

**Types travel between agents, English crosses the model boundary.** The brief is typed for the planning step. The doc agent flattens the brief back into natural language before handing it to the model. The structured brief is for *you*; the model reads English.

## Code shown in this lesson

```python
from pydantic import BaseModel, Field

class CreativeBrief(BaseModel):
    product_name: str
    headline: str
    key_benefits: list[str] = Field(description="3 short benefit statements.")
    visual_concept: str = Field(description=(
        "A photo brief — subject, lighting, composition, style. "
        "No screenshots, no UI, no laptop screens. "
        "If software, describe a metaphor or scene that evokes the product."
    ))

brief_agent = studio.create_agent(
    name="brief-agent",
    provider="gpt-5.2",                        # flagship — real creative thinking
    role="senior creative director",
    goal="distill a product description into a shippable brief",
    instructions="Tight, vivid, no fluff.",
    response_model=CreativeBrief,
)
```

```python
from lyzr.image_models import GeminiImage

image_agent = studio.create_agent(
    name="image-agent",
    provider="gpt-5-mini",                     # cheap orchestrator
    image_model=GeminiImage.gemini_pro,        # Nano Banana Pro
    role="image prompt renderer",
    goal="render the brief's visual concept",
    instructions="Pass the visual concept verbatim. No logos. No text in image.",
)

doc_agent = studio.create_agent(
    name="doc-agent",
    provider="gpt-5.2",                        # flagship — copy is the job
    role="marketing copy writer",
    goal="produce a one-page marketing PDF",
    instructions="Match the headline tone. Use the benefits as a bulleted block.",
    file_output=True,
)
```

```python
def creative_assistant(product_description: str):
    # Plan
    brief = brief_agent.run(product_description)
    print(f"BRIEF: {brief.product_name} — {brief.headline}")

    # Fan out — image
    image_prompt = (
        f"{brief.visual_concept}. "
        "High quality, no text, no logos, no UI."
    )
    image_response = image_agent.run(image_prompt)
    image_path = image_response.files[0].download(safe_file_name(brief.product_name + ".png"))

    # Fan out — doc
    doc_prompt = f"""
        Write a one-page marketing PDF for:
        Product: {brief.product_name}
        Headline: {brief.headline}
        Benefits: {', '.join(brief.key_benefits)}
        Format as a PDF.
    """
    doc_response = doc_agent.run(doc_prompt)
    doc_path = doc_response.files[0].download(safe_file_name(brief.product_name + ".pdf"))

    return image_path, doc_path
```

## Try this

1. Add a fourth agent — `social_post_agent` — that takes the brief and writes a LinkedIn caption (text-only, no `file_output`, no `image_model`). Wire it into the orchestrator after the doc agent. Now one product description fans out to three artifacts.
2. Cache the brief from one run, then call the image agent three times in a row with different image models (DALL-E 3, Gemini Pro image, GPT-Image-1). One plan, three renders. Compare the aesthetic register — which model honored the `visual_concept` most literally?

## Transcript

One sentence in, two artifacts out. Hero image and a marketing PDF, both built by three agents working in sequence. That's a creative assistant, and today we're going to build it.

This is the second SDK capstone. Three agents, one orchestrator, no new APIs. Everything we use today comes from videos five, seven, and eight — structured outputs, image generation, and file generation. Today we wire them together into something that ships.

Same setup as the rest of the series — install, load the API key, spin up Studio.

Here's the shape. User gives us a one-line product description. First agent is the **brief agent** — structured output from video five. It returns a typed creative brief: name, headline, key benefits, visual concept. That brief feeds the next two agents. Second agent is the **image agent** from video seven. It reads the `visual_concept` of the brief and generates a hero PNG. Third agent is the **doc agent** from video eight. It reads the rest of the brief — name, headline, benefits — and generates a marketing PDF with copy. Three specialized agents, one orchestrator, two artifacts.

Call this pattern "plan, then fan out." The planning step makes the brief. The fan-out runs image and doc against the same plan. Each agent has one job.

Brief agent first. Pydantic model defines the shape of the brief. Four fields. The `visual_concept` description does most of the heavy lifting here. Field descriptions are passed to the model as part of the schema, which means the brief agent reads this and writes its `visual_concept` to match. Specifically: no screenshots, no UI, no laptop screens for software products. Image models will fail at those every time. Instead, the agent has to describe a metaphor or scene that evokes the product. Flagship model — GPT-5.2. The brief agent does real creative thinking, so it gets the heavy lifter. `response_model` is set to `CreativeBrief`, which means `agent.run()` returns the typed instance directly. No `.response` to unwrap.

There's the brief. All four fields filled — product name, headline, three benefits, and a visual concept that reads like an actual photo brief. Subject, lighting, composition, style. Exactly the shape we asked for in the field description. Structured outputs doing the job.

Image agent next. Same pattern as video seven — `image_model` parameter. We're using Gemini's latest "Nano Banana" model this time — Gemini Pro under the hood is `gemini-3-pro-image-preview`, branded as Nano Banana Pro, Google's flagship image renderer. Notice the provider shift — brief agent got GPT-5.2 because it's doing creative reasoning; image agent gets GPT-5 Mini because its only job is to pass the visual concept to the renderer. Match the orchestrator to the work.

The wrapper repeats the "no text, no UI" rules at the prompt level, because image models will sneak a logo or a label if you give them any room.

The doc agent. `file_output=True`. Same pattern as video eight. Flagship again, because writing copy is the agent's actual job. The function flattens the brief back into natural language and hands it to the doc agent. The structured brief is for the planning step; the doc agent reads English. That's a useful pattern — types travel between agents, English crosses the model boundary.

Now orchestrator. Takes one product description, returns two artifact paths. Three steps — brief, image, doc. Each prints what it's doing so we can see the pipeline run. In production you'd hide the chatter; for a demo it's the interesting part.

Two complete runs, four artifacts. Garden hose first. The image agent took the visual concept off the brief and rendered the spray attachment as a product shot. The PDF picked up the headline and the benefits and laid them out as a clean one-pager.

Chili crisp next. Completely different aesthetic, same pipeline. Food photography on the image side, copy ties back to the ingredient list on the doc side. Two products, two visual treatments, same pipeline. The brief agent read "garden tool" and "craft chili crisp" and translated each into a different photographic register. That's the lesson — small specialized agents fed the right structured plan produce work that's actually shippable.

Brief agent is the planner — typed output, one decision, hands a structured brief to the rest of the system. That's video five's `response_model` doing the heavy lifting. Image agent and doc agent are the producers — each reads a different field of the brief (`visual_concept` for image, name and copy for doc) and emits a different artifact. That's video seven's `image_model` and video eight's `file_output` running in sequence. The whole thing is one function — plan, then fan out.

You can extend this pattern in obvious ways. Add an audio-track agent. Add a social-post agent. Add a translation step. The brief stays the source of truth. Every producer downstream stays specialized.

This is also the architectural template for video six's classify-then-answer. Different problem, same shape. Small typed specialized agents beat one big one.

That's the second capstone. Build on this. Cache the brief if you're producing multiple variants. Add a critic agent that reviews the brief before it fans out. Pipe the artifacts into a Slack post or a Notion page. The architecture holds.

Next block — knowledge and memory. We start with what RAG is and why every serious agent reaches for it.

I'm Felipe with Lyzr. Until next time.
