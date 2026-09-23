> ⚠️ **ARCHIVED / SUPERSEDED (2026-05-28).** This April 2026 spec locks the *old* content model
> — Developer/Business tracks, horizontals vs verticals, flavored horizontals. That model is
> retired. The canonical strategy is now `../content-strategy.md` (Product × Module × Use-Case),
> with the categorization plan at `~/.claude/plans/yes-lets-go-mellow-dongarra.md`. Kept for history only.

# Lyzr Academy — Content Architecture Design

**Date:** 2026-04-07
**Status:** Draft (pending user review)
**Owner:** Harshit Choudhary
**Related:** `lyzr-university/content-strategy.md` (public-facing explainer), future sessions B/C/D/E

---

## Context

Lyzr Academy is Lyzr's education programme — a structured learning path from "I know what an agent is" to "I can build and ship production agents." It launches Day 30 (2026-05-07) with Agents 101 and builds toward a stable content engine by Day 90 (2026-07-06).

The original content strategy doc (`content-strategy.md`) introduced four concepts — horizontals, verticals, tracks, and stacking certs — but hand-waved over three critical design tensions:

1. How much content is actually shared between the Developer and Business tracks vs genuinely track-specific? Are they two courses or one course with two lab paths?
2. How do we draw the line between a horizontal and a vertical when they cover the same topics?
3. Do flavored horizontals (Agents for FinServ, etc.) make sense as full courses, or do they create content sprawl and a double-enrollment problem?

This spec resolves those tensions and locks the content architecture. It establishes the rules every downstream decision (syllabus, cert design, production pipeline) must follow.

## Design goals

Optimizing for four things, in priority order:

1. **Scalability to 15+ courses in Year 1** without content sprawl or credential redundancy
2. **Credential clarity** — every cert tells employers exactly what the holder can do
3. **Production efficiency** — minimize redundant work across tracks, topics, and industries
4. **Learner honesty** — every minute of video earns its place; no padding, no bait-and-switch between course tiers

## Non-goals

- "Covering everything about agents" — this is an opinionated curriculum, not an encyclopedia
- Serving every possible learner background — we optimize for two clear audiences (engineers and business operators) and don't try to please everyone
- Pre-building tooling or automation for Year 2+ features — the demo-example library is an architectural principle, not a Year 1 deliverable

## Architecture: two course shapes

The catalog contains exactly two course shapes. No third category, no exceptions.

### Horizontal

**Definition:** A foundational course covering the full agent lifecycle end-to-end. Teaches the happy path for every major component — what agents are, instructions, memory, tools, knowledge bases, deployment, basic monitoring.

**Agents 101 is the only horizontal in Year 1.** It's generic, cross-industry, cross-function.

| Attribute | Value |
|---|---|
| **Length** | 10–15 hours of content |
| **Learner outcome** | Can ship a simple production agent — real use cases, known patterns, happy paths. Will break on edge cases and weird data. |
| **Credential** | Foundation cert — "Lyzr Certified Builder" |
| **Depth per component** | One layer deep per topic. Enough to ship, not enough to master. |

### Vertical

**Definition:** A focused deep-dive on a single component or concern. Teaches the sad paths, edge cases, failure modes, scale considerations, and deeper design principles for one specific thing.

**~14 verticals in Year 1**, covering components like Memory, Knowledge Base / RAG, Instructions, Tools, Multi-Agent Orchestration, Evaluation, Observability, Cost & Performance, Security, etc. The exact list and ordering is for session D (first vertical roadmap).

| Attribute | Value |
|---|---|
| **Length** | 3–5 hours of content |
| **Learner outcome** | Production-grade mastery in one component. Can unblock a team on that topic. |
| **Credential** | Specialist cert per vertical — e.g. "Memory Specialist," "RAG Specialist" |
| **Depth per component** | Five layers deep on the one thing it covers. |

### The line between horizontal and vertical

This is the most load-bearing architectural principle in the spec. Without a clear rule, verticals drift into redundancy with the horizontal and the whole catalog loses credibility.

**Rule:** for every component covered in Agents 101, the Agents 101 framework doc (a Month 1 deliverable) must explicitly list what's covered in 101 vs what's deferred to the vertical. No ambiguity, no "we'll figure it out later."

**Example (Memory):**

| Agents 101 Memory module covers | Deferred to the Memory vertical |
|---|---|
| Short-term conversation memory | Episodic memory |
| Simple vector-store RAG with one embedding model | Entity memory |
| Basic retrieval (top-k) | Chunking strategies for different data types |
| How to wire memory into an agent end-to-end | Retrieval tuning and failure modes |
| | Evaluation harnesses |
| | Cost trade-offs at scale |
| | Cross-session memory |
| | Multi-agent shared memory |

**Informal test for the line:** a learner who completes Agents 101 and then takes the Memory vertical should say *"the vertical deepened what 101 started"* — not *"the vertical repeated what 101 covered"* and not *"the vertical was disconnected from 101."* Expect ~20% revisit-and-deepen material, ~80% net new.

## Architecture: tracks

Every course — horizontal and vertical — runs in two parallel tracks. Learners pick one at enrolment.

| | Developer Track | Business Track |
|---|---|---|
| **Tooling** | Lyzr ADK, API, CLI | Lyzr SaaS platform (no-code) |
| **Audience** | Engineers who prefer code | Ops, PMs, SMEs, analysts, non-coders |
| **Hands-on artifacts** | Python projects, code repos | Deployed SaaS agents, platform configurations |

### Track structure: merged modules

**Courses are not two parallel recordings.** Every module is internally structured as:

```
Module N
  ├── Concept video (shared)         — taught once, watched by both tracks
  └── Hands-on video (track-specific) — watched only by learners in that track
        ├── Dev hands-on   (Python / ADK / API / CLI)
        └── Business hands-on (Lyzr SaaS platform walkthrough)
```

**Production implications:**

- Shared concept videos are produced once and reused across both tracks
- Hands-on videos are produced twice (once per track)
- At Year 1 scale, this is **~1.4× single-track production cost**, vs ~2× for fully parallel tracks
- Year 1 savings: roughly 40 hours of polished video production — equivalent to ~10 additional verticals worth of capacity

**Learner experience:**

- Learner picks a track once, on enrolment
- They see all shared concept videos + their track's hands-on videos
- The LMS handles the "branch to your track" navigation
- Certs are **track-neutral** — "Memory Specialist" is the same credential whether you took the Dev or Business track

**Production rule:** before any module is recorded, the team decides which sections are shared vs track-specific. Unclear splits get rejected — if you can't cleanly separate the concept from the hands-on, the module's design isn't ready.

**Track parity rule:** Business-track hands-on must be as rigorous as Dev-track hands-on. The Business track is not a "lite" version. Learners should finish each module with equivalent capability to ship, using their respective tooling.

## Architecture: prerequisite model

**Agents 101 is strongly recommended before any vertical, but not gated.**

Each vertical begins with a **topic-specific primer** (15–20 minutes, counted as part of the vertical's runtime) that:

- Orients learners to where this topic fits in the overall agent architecture
- Recaps what Agents 101 covered on this topic (briefly, 5–10 min)
- Sets up what the vertical is about to add on top

**Example — Memory vertical primer:**

> "Here's where memory fits in an agent's architecture. In Agents 101 we covered short-term conversation memory and basic RAG. In this vertical we're going deeper into long-term and episodic memory, chunking strategies for different data types, retrieval failure modes, and memory at scale. If you've done 101, skip ahead to Module 1. If not, watch this primer first."

**Design alternatives considered and rejected:**

| Alternative | Why rejected |
|---|---|
| **Strict prerequisite gate** (must finish 101 before any vertical) | Paternalistic. Blocks experienced learners arriving from elsewhere. Hurts the "verticals are for depth, regardless of where you learned the basics" positioning. |
| **No primer at all** | Learners who skip 101 land cold in a deep-dive. Drop-off risk. |
| **Shared generic primer video reused across verticals** | Boring, repetitive for anyone taking multiple verticals. Doesn't orient learners to the specific vertical's topic. |

**Production cost:** ~4–5 hours of primer content across 14 verticals (~20 min × 14). Acceptable — roughly one vertical's worth of runtime total, amortized across the whole catalog.

## Architecture: industry / function flavoring

**Principle:** specialization by industry or function is not a course-level concern. The concepts, patterns, and architecture of agent building are universal. What changes for FinServ vs Healthcare vs HR vs Marketing is the **specific scenario used in the hands-on examples** — not the teaching itself.

**Year 2+ implementation model (architectural principle, not Year 1 deliverable):**

- Build a **demo-example library** tagged by industry and function
- Any course — Agents 101 or any vertical — can draw demo examples from this library
- Learners can filter courses by demo flavor ("show me Memory with FinServ demos")
- New industries/functions are added by contributing new demo examples, not by producing new courses

**Year 1 scope:**

- No flavored content of any kind
- No demo-example library build
- All demos are generic or drawn from common cross-industry use cases (customer support bot, docs Q&A, sales assistant, etc.)
- The demo-example library is captured in this spec as an architectural principle and explicitly deferred to Year 2

**Design alternatives considered and rejected:**

| Alternative | Why rejected |
|---|---|
| **Full flavored horizontal courses** (10-12h "Agents for FinServ" as a standalone course) | Creates double-enrollment problem (learner takes 101 + FinServ = redundant content). Content math doesn't support it — industry-specific content is ~3-5h, not 10-12h. Credential story gets muddy (is "FinServ Foundation" different from "Foundation"?). |
| **Flavored verticals** (e.g. "Agents for FinServ" as a 4h vertical) | Cleaner than full horizontals but still creates a "flavored" content track separate from generic verticals. Not as clean as "flavoring is a demo concern." |
| **Ship 1-2 flavored horizontals in Year 1 as a test** | Creates design debt — once shipped, they're load-bearing. Better to defer entirely and let the demo-library principle prove itself. |

**Why the demo-library principle is better:**

- No double-enrollment problem
- No content sprawl (new flavor = new demo examples, not new courses)
- Clean credential story
- Scales linearly with industries/functions, not exponentially with topics × flavors
- Matches the actual content math (industry-specific content is demo-sized, not course-sized)

## Year 1 concrete scope

| | Count | Runtime | Production load (at 1.4×) | Credential |
|---|---|---|---|---|
| **Agents 101** (horizontal) | 1 | 10-15h | ~18h equivalent | Foundation — "Lyzr Certified Builder" |
| **Verticals** | ~14 | 3-5h each (~56h total) | ~78h equivalent | Specialist per vertical |
| **Primer content** (inside verticals) | ~14 × 15-20 min | ~4-5h | ~5h | (included in vertical) |
| **Total** | **15 courses** | **~68h learner runtime** | **~100h production equivalent** | **1 Foundation cert + ~14 Specialist certs** |

Production estimate uses the target 1.4× merged-track ratio. Budget up to ~107h (1.5× ratio) as a safety margin per the open risks section below.

**Specific vertical list and ordering is for session D.** The architecture supports any ordering.

## Sequencing constraints

Architecture-level constraints on when things ship. Detailed scheduling is for session E.

- **Agents 101 must launch complete at Day 30.** Merged-module structure means the concept and hands-on videos for all modules ship together — you can't half-ship the horizontal with "Dev track today, Business track next week."
- **Verticals ship independently as they're ready.** Each is self-contained (modulo the primer bridge to 101), so the first verticals can begin shipping anytime after Day 30.
- **No vertical depends on another vertical as a prerequisite.** Each stands alone with its primer. This keeps the production order flexible.

## Production rules (derived from architecture)

These are hard constraints the architecture imposes on downstream sessions. Violating any of them breaks the architecture.

1. **The horizontal/vertical line must be written down before Agents 101 is recorded.** For every component 101 touches, the framework doc lists what's covered and what's deferred. Without this, verticals drift into redundancy and there's no way to scope them later.
2. **The track split in each module must be decided at script time, not recording time.** Before Felipe walks on camera, the module's script specifies which sections are shared concept (taught once) and which are track-specific (taught twice). Unclear splits get sent back to scripting.
3. **Every vertical's primer is topic-specific, not generic.** Primers are produced per-vertical as part of that vertical's production. Cost: ~20 min per vertical, budgeted into the 3-5h vertical runtime.
4. **Business-track hands-on must be rigorous, not a lite version.** Any module that feels watered down on the Business side gets sent back. Credential parity is non-negotiable.

## Success criteria

How we know this architecture is working, once content starts shipping:

- **Line-drawing test:** a learner who completes Agents 101 + any vertical should say *"the vertical deepened what 101 started"* — not *"the vertical repeated what 101 covered"* and not *"the vertical was disconnected from 101."*
- **Credential clarity test:** an employer reading a learner's credentials should know exactly what that learner can and cannot do from the cert labels alone — without reading course descriptions.
- **Production efficiency test:** the 1.4× track production ratio actually holds once courses start shipping. If it drifts toward 1.8× or 2.0×, the merged-module discipline is breaking down.
- **Track parity test:** Business-track learners rate their course at parity with Dev-track learners — *not* as "the lite version." Merged modules only work if the hands-on sides are equally rigorous.
- **Primer effectiveness test:** learners who skipped Agents 101 and started with a vertical complete Module 1 of that vertical at similar rates to learners who did 101 first. If drop-off is materially worse for skippers, the primer is too short and needs rework.

## Open architectural risks

Three things that could break this architecture as it meets reality:

1. **The 1.4× merged-track ratio might not hold.** If in practice the concept sections end up shorter than the hands-on sections, savings shrink. **Mitigation:** budget for 1.5× and treat anything lower as upside.
2. **Topic-specific primers might be too short to actually orient skippers.** If 15-20 min isn't enough for a learner who never touched 101 to understand a deep-dive vertical, we'll see drop-off. **Mitigation:** measure Module 1 completion rates on verticals, split by "completed 101" vs "skipped 101." Iterate primer length if skippers drop off disproportionately.
3. **The horizontal/vertical line might get blurred over time.** As Felipe records 101 and feels tempted to "cover memory properly while I'm here," the vertical loses its reason to exist. **Mitigation:** treat the framework doc as a contract; anything scripted outside the horizontal's scope gets cut back at script review.

## Deferred to other sessions

This spec intentionally stops at the content architecture level. The following are handed off:

| Deferred to | What's decided there |
|---|---|
| **LMS selection** (Month 1 decision) | Assessment mechanics, module structure inside the LMS, navigation pattern for the track split, payment integration, badge issuance |
| **Session B — Agents 101 syllabus** | Exact module breakdown for 101, learning outcomes per module, what's covered and what's deferred to which vertical, module-level run time, hands-on labs |
| **Session C — Certification series** | Cert tier logic (Foundation → Specialist → Expert stacking rules), exam format per tier, badge taxonomy, Credly integration details, stacking rules for Expert tier |
| **Session D — Vertical roadmap** | Which 14 verticals ship, in what order, with what rough scope each, dependencies on the 101 line-drawing decision |
| **Session E — Production lifecycle** | How a course actually goes from outline → script → record → edit → publish → feedback; cadence; team handoffs; feedback loops |
| **Year 2+** | Demo-example library build, additional horizontals if needed, flavored demo rollout |

## Decision log

For future reference, the architectural decisions made in this brainstorming session and the rationale for each:

| # | Decision | Rationale |
|---|---|---|
| 1 | Year 1 scale = ~15 courses (1 horizontal + ~14 verticals) | User-stated expectation ("ambitious" scale); balances ambition and feasibility with a 2-person core team + hires |
| 2 | Horizontal teaches "simple production," not "demo" or "production-grade" | Middle-path ambition gives every course (horizontal and vertical) a clear reason to exist. Verticals add real value without making the horizontal feel like a trailer. |
| 3 | Agents 101 = 10-15h, verticals = 3-5h each | Horizontal-heavier model. Maps to how mature learning platforms (AWS, Coursera) handle foundation + specialty. Front-loads production cost on the course every learner touches. |
| 4 | Recommended (not strict) prerequisite, with 15-20 min topic-specific primer in each vertical | Respects experienced learners. Primers are short enough not to waste vertical runtime, specific enough to genuinely orient skippers. |
| 5 | Merged-module track structure (1 shared concept + 1 per-track hands-on per module) | ~40 hrs of Year 1 production saved vs fully parallel tracks. Equivalent to 10+ additional verticals worth of capacity. |
| 6 | No flavored courses in Year 1. Industry/function flavoring is a demo-example concern, not a course concern. | Avoids double-enrollment, content sprawl, and credential confusion. Matches the actual content math. |

## Companion deliverables

This spec should be read alongside:

- **`lyzr-university/content-strategy.md`** — public-facing explainer of the architecture (to be revised to match this spec)
- **Agents 101 framework doc** (Month 1, not yet written) — the contract that locks what Agents 101 covers and what's deferred, per the line-drawing rule above
