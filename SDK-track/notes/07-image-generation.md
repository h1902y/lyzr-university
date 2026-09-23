# Image generation

*Lesson 07 · Module 2 — Multimodal*

## What you'll learn

- How `image_model` flips a normal agent into one that returns image artifacts
- Why the `provider` (text LLM) and the `image_model` are separate roles
- How to retrieve and save generated files from the response
- How to swap the image model on an existing agent at runtime
- The aesthetic difference between DALL-E 3 (illustrative) and Gemini Pro image (literal/photographic)

## Key concepts

**Same agent shape, different artifact.** Add `image_model=DALLE.dalle_3` to `create_agent` and the same `agent.run()` call you've used in every video so far comes back with a file instead of text.

**Two LLMs, two roles.** The `provider` parameter is the LLM that orchestrates the request — it takes the user's words and shapes them into something the image model wants. The `image_model` does the actual rendering. You can pair a cheap orchestrator (GPT-mini) with an expensive renderer, or vice versa.

**Available image models.** DALL-E 3, DALL-E 2, GPT-Image-1, GPT-Image-1.5, Gemini Pro image, Gemini Flash image — among others.

**Artifact retrieval is uniform.** `response.has_files` tells you whether the run produced files. `response.files` is the list. Each artifact has `format_type` (image / document / audio), `name`, and `download(path)`.

**Swap the renderer at runtime with `agent.set_image_model()`** — no need to create a new agent. Useful for A/B-ing aesthetics on the same prompt.

**Aesthetic tradeoffs.** DALL-E 3 leans illustrative — it embellishes, paints stylized continents on a "map," reaches for cinematic lighting. Gemini Pro image leans literal — given the same "stay literal" instruction, it produced a real cartographic map with readable place names. Neither is right; reach for DALL-E when you want art direction baked in, reach for Gemini when you want a near-photographic translation of words.

## Code shown in this lesson

```python
from lyzr.image_models import DALLE

agent = studio.create_agent(
    name="image-generator",
    provider="gpt-5-mini",                  # orchestrator
    image_model=DALLE.dalle_3,              # renderer
    role="creative image generator",
    goal="produce visually striking images from short prompts",
    instructions="Stay literal to the prompt.",
)

response = agent.run("A weathered brass compass over a paper map, warm dramatic lighting.")

if response.has_files:
    for artifact in response.files:
        if artifact.format_type == "image":
            path = safe_file_name(artifact.name)   # helper from setup
            artifact.download(path)
            display.Image(path)
```

```python
# Same agent, swap to Gemini at runtime
from lyzr.image_models import GeminiImage

agent.set_image_model(GeminiImage.gemini_pro)     # gemini-3-pro-image-preview
response = agent.run("A weathered brass compass over a paper map, warm dramatic lighting.")
```

## Try this

1. Take a single prompt — *"A weathered brass compass over a paper map, warm dramatic lighting"* — and generate it twice on DALL-E 3 and twice on Gemini Pro image. Open the four images side-by-side and write two sentences describing the aesthetic split.
2. Within a single agent, use `agent.set_image_model()` to swap renderers between two consecutive calls of `agent.run()` — same prompt both times, different renderer. Save both images. Verify you didn't have to recreate the agent.

## Transcript

Today the agent stops returning text and starts returning images. One extra parameter on `create_agent` — `image_model` — and the same `agent.run()` call we've been using comes back with a file. Different artifact, same shape.

Same setup as the rest of the series. Install pinned to `0.1.9`. Load the API key. Spin up Studio.

Here's the change. Two new lines. Import `DALLE` from `lyzr.image_models`. Add `image_model=DALLE.dalle_3` to `create_agent`. Everything else is the same agent shape you already know.

One thing to call out — the `provider` here is the LLM that orchestrates the request, not the image model. GPT-5 Mini does the lightweight job of taking the user's words and shaping them into something the image model wants. The actual rendering is `image_model`'s job. So you can pair a cheap orchestrator with an expensive renderer or vice versa, depending on where you want quality to live.

Available image models currently include DALL-E 3, DALL-E 2, GPT-Image-1, GPT-Image-1.5, Gemini Pro, Gemini Flash.

Now we run it. Same `agent.run()` you've used in every video so far. The difference is the response. `response.has_files` tells you whether the run produced artifacts, and `response.files` is the list. Each artifact has a `format_type` — image, document, audio — a `name`, and a `download(path)` method that drops it on the disk. The `safe_file_name` helper from the setup cell builds a clean safe path, and I do `display.Image()` to render the file inline.

Image saved, displays inline. That is a nice render. Weathered brass compass, dead center, paper map underneath, warm dramatic lighting. But notice something — I told the agent "stay literal" and it embellished anyway. The map under the compass isn't a real cartographic map — it's painted, stylized, decorative continents. The whole composition is illustrative, almost cinematic. DALL-E 3 leans toward art when given any room to do so. The instruction is there, but it doesn't always stick.

One more thing worth showing. You don't need a new agent to switch image models. There's `agent.set_image_model()` on the existing agent. Same agent, different renderer. Same prompt, same orchestrator, different render. Gemini Pro — under the hood is `gemini-3-pro-image-preview`, Google's newest image model. DALL-E 3 is OpenAI. Two different training regimes, two different aesthetics, same prompt — completely different image.

Where DALL-E gave us an illustration, Gemini gave us a photograph. Look at the map underneath — that's a real cartographic print. You can read "North America," "Gulf of Mexico," city names. And the compass has actual cardinal letters — northeast, southwest. Lighting is even and daylight-flat, much closer to the actual top-down. And the "stay literal" instruction landed this time. Gemini went with the most literal interpretation possible: a real compass on a real map, photographed from above. Different training, different aesthetic. Neither is right or wrong. They're useful for different jobs.

Reach for DALL-E when you want art direction baked in. Reach for Gemini when you want the model to translate words to image without adding a layer of style on top.

Quick guide so you don't have to memorize the catalog. DALL-E 3 is the default reach — reliable composition, predictable behavior, well-understood by the prompting community. Start here.

One parameter, one method, one new artifact type. `image_model` flips the agent into image mode. `set_image_model` swaps the renderer at runtime. And `response.files` is how you get the bytes out.

Okay. Next video — we look at file generation. The same artifact pattern but for PDFs, spreadsheets, and documents. Then we put it all together in the second capstone.

I'm Felipe with Lyzr. Until next time.
