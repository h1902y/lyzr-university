# Lyzr University — Content Strategy

## TL;DR

Lyzr University teaches agent building as a craft, using Lyzr as the throughline. The catalogue is **three independent collections** — every course belongs to exactly one:

| Collection | Teaches | Identity | Cert |
|---|---|---|---|
| **Tracks** | how to build in a product, hands-on | product-specific (ADK · Studio · Architect) | product proficiency (e.g. *Lyzr ADK Developer*) |
| **Modules** | a capability as a craft, tool-agnostic | product-neutral (Memory, RAG, Tools, …) | *"X Specialist"* |
| **Functions** | applying AI in a domain | product-neutral (HR, Sales, …) | domain credential |

**The one-liner: Tracks teach a tool · Modules teach a craft · Functions teach a domain.**

A learner can enter from any collection: learn a product end-to-end (Track), master a capability across tools (Module), or learn to apply AI in their function (Function). Certs stack as they go.

> Full course list + rollout live in `~/.claude/plans/yes-lets-go-mellow-dongarra.md` and the [[project-lyzr-university-catalogue]] memory. The browsable catalog + thumbnail generator are in `lyzr-university/catalog-demo/`.

---

## Why it exists

Agent building is a new discipline with no coherent learning path. Today people stitch knowledge from blog posts, Discord threads, half-finished tutorials, and scattered docs. Lyzr University replaces that with a structured path from "I know what an agent is" to "I can ship one to production and debug it when it breaks" — taught through the Lyzr platform but teaching the craft, not just the tool.

---

## Collection 1 — Tracks: learn a product, hands-on

Product-specific paths. This is where the recorded, hands-on content lives, grouped by product.

| Product | Who it's for | Build surface |
|---|---|---|
| **ADK** | developers, engineers | build agents in Python (code) |
| **Studio** | power users, ops teams, PMs | configure agents visually (low-code) |
| **Architect** | business users, non-technical builders | describe an app in plain English (no code) |

A Track course carries exactly one product. Tracks own the "how do I do this *in this tool*" knowledge — the SDK series for ADK; the **agent-lifecycle phases** (Build → Govern → Test → Deploy → Monitor, rebalanced into 6 phases + a Foundations journey course) for Studio; Fundamentals for Architect. **Cert:** completing a Track signals product proficiency.

---

## Collection 2 — Modules: master a craft, tool-agnostic

The capability layer — the "teach the craft, not the tool" courses. Each Module teaches a capability *independent of any product*: what it is, when to use it, the tradeoffs, the failure modes.

`Agents` · `Models` · `Memory` · `Knowledge & RAG` · `Tools & Integrations` · `Orchestration` · `Voice` · `Responsible AI` · `Evaluation` · `Multimodal` · `Deployment`

Modules are **product-neutral** — there is one "Memory" course (the craft), not an ADK version and a Studio version. Owned by module specialists. **Cert:** *"X Specialist"* (e.g. Memory Specialist), product-neutral.

> A topic can legitimately appear in more than one collection — e.g. Memory shows up in the ADK Track (in code), the Studio Track (in the UI), and as a product-neutral Module (the craft). Three lenses on the same capability, by design.

---

## Collection 3 — Functions: apply AI in a domain

Domain-strategy courses for a business function — the landscape, the build-vs-buy/ROI framework, the top agentic use cases, how to prioritize, and skills/readiness.

`HR` · `Marketing` · `Sales` · `Procurement` · `Venture Capital` · `AI Strategy`

Functions are **product-neutral** — they teach how to *think about AI* in a function, not how to operate a product. Owned by use-case SMEs. **Cert:** a per-function domain credential.

---

## Why three collections (not one tagged set)

The earlier model tagged every course on a flat Product × Module × Use-Case scheme, which made a clean ADK progression and a sprawling Studio set look like peers and buried the craft/domain expertise inside product tracks. Splitting into three collections gives each its own clear job and entry point, lets capabilities be taught as a tool-agnostic craft (Modules) distinct from product mechanics (Tracks), and keeps domain strategy (Functions) where business leaders can find it.

---

## Certification: a stacking series

| Tier | Earned by | Signals |
|---|---|---|
| **Product proficiency** | completing a Track | can build in that product |
| **Specialist** | completing a Module | tool-agnostic depth in one capability |
| **Domain** | completing a Function | can lead AI adoption in that function |
| **Expert** | a defined set of the above | breadth + proven depth |

**Design principles:**
- **Stacking, not replacing** — each cert stays on the profile forever.
- **Specialist certs are product-neutral** — "Memory Specialist" is the capability, earned from the Module.
- **A "Lyzr Certified" badge is never generic** — it always says exactly what the holder mastered.
- **Path/Expert rules + Thinkific Learning Paths are deferred** until the catalogue matures.
- **Founder tier:** above the ladder sits **"Lyzr Agentpreneur"**, issued via the Agentpreneur programme (see [[project-agentpreneur-cohort-2]]).

---

## Industry flavoring (inside Track courses)

Industry/function flavor *inside a Track course* is an examples concern, not a course concern — the demo scenario changes, the teaching doesn't. A later **demo-example library** lets any Track course pull industry-specific demos on demand; new industries are added by contributing demos, not new courses. This is distinct from **Functions**, which are standalone domain-*strategy* courses.

---

## Summary

| Collection | Teaches | Product-specific? |
|---|---|---|
| **Tracks** | a tool, hands-on | yes (ADK / Studio / Architect) |
| **Modules** | a craft, tool-agnostic | no |
| **Functions** | a domain | no |

Tracks meet you at your tool. Modules make you good at the craft. Functions point it at your work. Certs prove what you can actually build.
