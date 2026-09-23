# Lyzr University — Portal & Initiative

A plain description of **what Lyzr University is** — both the *initiative* (the programme and the
effort behind it) and the *portal* (the platform learners actually use). For positioning, messaging,
and social-planning material see `README.md`; for the catalogue model and rationale see
`content-strategy.md`; for paste-ready copy see `planning/lyzr-university-copy.md`.

> Canonical name: **Lyzr University** (formerly "Lyzr Academy"). Delivered 100% on **Thinkific**.

---

## The initiative

**Lyzr University is the education and enablement arm of Lyzr** — the company building agentic AI
infrastructure. Its job is to turn "using Lyzr" and, more broadly, "building AI agents" from
something people piece together on their own into a **learnable, structured, certifiable craft**.

**Why it exists.** Agent-building is a new discipline with no coherent learning path. Today people
assemble understanding from blog posts, Discord threads, scattered docs, and half-finished
tutorials. Lyzr University replaces that with a deliberate path from "I know what an agent is" to
"I can ship one to production and debug it when it breaks" — taught through the Lyzr platform, but
teaching the craft, not just the tool.

**What it sets out to do:**
- Give every kind of builder a clear way in — developer, power user, or business user — and a way to
  go deeper as their needs grow.
- Teach the capabilities that production agents actually depend on (memory, RAG, tools,
  orchestration, voice, responsible AI, evaluation, deployment) as tool-agnostic craft.
- Help business functions understand where agentic AI fits in their domain.
- Make capability **provable** through stacking certifications, so a credential states exactly what
  its holder can build.

**Where it sits in the Lyzr ecosystem.** It's the learning layer over Lyzr's products (ADK, Agent
Studio, Architect). It supports adoption and developer relations, and it feeds the top of the
credential ladder: the founder-tier **"Lyzr Agentpreneur"** credential is earned through the separate
Agentpreneur programme, stacking above the University ladder.

**Who builds it.** Courses are authored and taught by the people closest to the material —
**product leads** own the product Tracks, **module specialists** own the craft Modules, and
**use-case SMEs** own the domain Functions. Production and scheduling are coordinated through a shared
Google Drive hub (recording tracker, content backlog, master tracker); local files in this repo are
the source of truth for course content and the upload bundle.

**How it rolls out (phase-wise, not date-bound).** The catalogue is published in phases as content is
recorded — the ADK Track is live first; Studio and Architect Tracks, the craft Modules, and the
domain Functions follow as they're produced. Course status is always described as **live** or
**coming soon**, never with a fixed launch date.

---

## The portal

**The portal is the Lyzr University site, hosted on Thinkific** — the learning-management platform
that runs the catalog, enrollments, course delivery, certifications, payments, and student
management. Thinkific was chosen deliberately so the team can focus on *content* rather than building
and maintaining a custom LMS; there is no custom app.

**What a learner does on the portal:**
1. **Browse the catalog**, organized into the three collections — Tracks (learn a product),
   Modules (master a craft), Functions (apply AI in a domain).
2. **Enroll** in a course (self-paced, on-demand).
3. **Learn** through video lessons paired with companion notes, working through hands-on projects.
4. **Earn certifications** that stack as they complete Tracks, Modules, and Functions.

**How the catalog is organized in the portal.** The three collections and their tags (product,
craft module, industry function) are surfaced through Thinkific **Categories**, so a learner can
find courses by product, by capability, or by their function. Structured Learning Paths are deferred
until the catalogue matures; for now courses are browsed and stacked individually.

**Course format.** Each course is a set of lessons; one media file becomes one lesson. Live courses
pair a **video** lesson with a **companion notes PDF**. Courses that aren't recorded yet ship as
**"coming soon"** shells with short branded placeholder slide decks, so the catalog looks intentional
end-to-end rather than showing empty pages.

**Certifications.** Credentials are a **stacking ladder** — product proficiency (a Track) →
Specialist (a Module, product-neutral) → Domain (a Function) → Expert (a defined set of these) →
**Lyzr Agentpreneur** (founder tier). Each badge stays on the learner's profile and names exactly
what was mastered.

**What's live today.** Three ADK Track courses are published — *Foundations*, *Multimodal*, and
*Knowledge & Memory* (~15 lessons). The remainder of the 34-course catalog (17 Tracks · 11 Modules ·
6 Functions) is in production.

---

## At a glance

| | |
|---|---|
| **What** | Lyzr's education & enablement programme — agent-building as a learnable craft |
| **Portal** | Thinkific-hosted; self-paced video courses + companion notes; certifications |
| **Catalog** | 34 courses across 3 collections — Tracks · Modules · Functions |
| **Live now** | 3 ADK Track courses (~15 lessons); rest coming soon |
| **Credentials** | stacking ladder → product proficiency · Specialist · Domain · Expert · Lyzr Agentpreneur |
| **Built by** | product leads (Tracks), module specialists (Modules), use-case SMEs (Functions) |

> Internal note: the browsable catalog in `catalog-demo/` is a **local preview** of the catalogue,
> not the live portal — the learner-facing portal is the Thinkific site.
