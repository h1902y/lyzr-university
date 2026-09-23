# Streaming Responses

*Lesson 04 · Module 1 — Foundations*

## What you'll learn

- How `stream=True` flips `agent.run()` from a single response into an iterator of chunks
- The standard four-line loop to print streamed tokens as they arrive
- Why you skip the final `done` chunk (and what would happen if you didn't)
- Which fields on a chunk you actually use, and which to know exist
- One silent fallback to watch for when a Responsible AI policy is attached

## Key concepts

**`stream=True` changes the return type.** Without it, `agent.run()` returns a response object. With it, you get an iterator. Each pass of the loop is one chunk arriving from the model.

**The standard streaming loop is four lines.** Loop the iterator. First thing in the body: check `chunk.done` and break. Otherwise print `chunk.content` with `end=""` and `flush=True` so Python doesn't buffer — the whole point is to see the text as it arrives.

**Why break *before* printing on the done chunk.** The final chunk in this SDK carries the full accumulated text in `.content`, not just the last token. Print it and you get your whole answer twice. Every prior chunk already emitted its piece, so skipping the done chunk is the right move.

**The fields that matter.** `chunk.content` (the new tokens for this chunk) and `chunk.done` (terminal marker) handle 90% of streaming code. `chunk.structured_data` is populated on the done chunk when a `response_model` is set (next video). `chunk.artifact_files` shows up when the agent generates files (image generation video).

**Streaming silently turns off when you attach a Responsible AI policy.** Guardrails for PII, toxicity, prompt injection — any of that — and the SDK falls back to non-streaming so the guardrail can scan the full response before any of it reaches the user. Correct behavior for safety; streaming half an answer past a policy check defeats the purpose. But it's *silent*. Your loop still runs, your code still works, you just get one big chunk at the end. If you're building something user-facing with guardrails, plan for it — show a spinner on policy-enabled agents, or render the final chunk as if it were streamed.

## Code shown in this lesson

```python
# Standard non-streaming call (baseline)
response = agent.run("Write a short paragraph about why streams feel fast.")
print(response.response)
```

```python
# Streaming — same agent, one extra keyword
for chunk in agent.run("Write a short paragraph about why streams feel fast.", stream=True):
    if chunk.done:
        break
    print(chunk.content, end="", flush=True)
```

```python
# Inspecting every field on every chunk (debug helper)
for chunk in agent.run("Count to three.", stream=True):
    print({
        "content":         chunk.content,
        "delta":           chunk.delta,
        "done":            chunk.done,
        "structured_data": getattr(chunk, "structured_data", None),
        "artifact_files":  getattr(chunk, "artifact_files", None),
    })
```

## Try this

1. Wrap the streaming loop with `time.time()` markers — one before the first chunk arrives, one at the `done` chunk. Run the same prompt non-streaming. Compare *time-to-first-token* vs *total time*. You'll feel the UX difference even when total time is identical.
2. Inside the loop, print `chunk.delta` alongside `chunk.content` for every chunk. Watch how the two fields differ (or don't) across the full response. Then attach a Responsible AI policy to the agent and run it again — note what happens to the chunk stream.

## Transcript

Today we're turning on streaming. One parameter on `agent.run` — `stream=True`. Instead of waiting for the full answer, you get tokens as the model produces them. The UX feels completely different, and the code change is about four lines.

Usual setup — same `.env` and same Studio init you've seen in the first three videos. If you've been following along, skip ahead.

Baseline first. Standard agent, standard call. Prompt: "Write a short paragraph about why streams feel fast even when total time is the same." Couple of seconds of silence, then the whole paragraph lands. That pause is the problem streaming solves. The model is generating tokens the whole time — we're just not showing them until it's done.

Here's the change. Same agent. `agent.run()` with one extra keyword — `stream=True`. That flips the return type. Instead of a response object, you get an iterator. Each pass of the loop is one chunk.

Four lines. Loop. First thing in the body, check `chunk.done` and break. If it's the last chunk, then print `chunk.content` with `end=""` and `flush=True` — so Python doesn't buffer, because the whole point is to see the text arrive.

Why break before the print? The final chunk in this SDK carries the full accumulated text in `.content`, not just the last token. If you print it, you get your whole answer twice. We've already emitted every token via the chunks that came before. So skipping the done chunk is the right move.

There it is. Same agent, same prompt, same total time roughly — but the words arrive as they're generated. For anything user-facing — a chat UI, a writing tool, a code assistant — this is the difference between "is it working" and "it's working."

Quick look at what's actually on each chunk, so you're not guessing. I'm running a tiny prompt — "Count to three" — and dumping the fields on every chunk until the loop naturally exits on `done`.

One thing to notice — look at chunks zero through five. `content` and `delta` are identical in each one. Both give you the new text for this chunk, just a token or two. That's why our simple print loop works. Each chunk is the next piece, and `end=""` glues them together. You get the running output for free.

Two more fields worth knowing about but not using today. `structured_data` is populated on the done chunk if you set a `response_model` — that's the next video. `artifact_files` shows up when the agent generates files, which we'll hit when we get to image generation. For most streaming code, `chunk.content` and `chunk.done` are all you need.

One gotcha you need to know before you ship this. When you attach a Responsible AI policy to an agent — guardrails for PII, toxicity, prompt injection, any of that — streaming turns off silently. Your code still runs, the loop still works, you just get one big chunk at the end instead of tokens arriving live. The SDK falls back to non-streaming so the guardrail can scan the full response before any of it reaches the user. That's the right behavior for safety. Streaming half an answer past a policy check defeats the point. But it's silent. No warning. And it will make your streaming UI look broken the moment someone attaches a policy.

If you're building something user-facing with guardrails, plan for it. Show a spinner on policy-enabled agents, or render the final chunk as if it were streamed. We'll cover RAI policies in future videos.

That's streaming. One flag. One iterator. `chunk.content` and `chunk.done` for the 90% case.

Next up — structured outputs. Instead of free-form text, you hand the agent a Pydantic model and get back a typed object.

I'm Felipe with Lyzr. Until next time.
