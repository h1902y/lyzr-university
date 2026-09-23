# Lyzr University — Track structure

> Decided 2026-07-08 via `/ce-brainstorm`. Feeds [`phase1-homepage-spec.md`](./phase1-homepage-spec.md) and [`university-build-plan.md`](./university-build-plan.md).

## The three tracks

| Track | Audience | How you build | Origin |
|---|---|---|---|
| **Foundations** | Everyone (product-agnostic) | The shared on-ramp — "what is an AI agent", core concepts, agent literacy | the "legacy" track, **repositioned** |
| **Studio** | Business users | Visually, in Lyzr's AI Studio | Studio |
| **ADK** | Developers | In code, with the Agent Development Kit | ADK |

**The story:** *Start with **Foundations** → then choose how you build — **Studio** (visually) or **ADK** (in code).*

## Decisions
- The **"legacy" track is repositioned as Foundations** — the audience-neutral concept on-ramp everyone takes *before* forking to Studio or ADK. It is **not** a dumping ground for old content.
- **Name = "Foundations"** (parallels LangChain Academy's "Foundation" collection).
- **Clash fix:** plain "Foundations" collides with per-track entry courses → **rename `ADK: Foundations` → `ADK: Getting Started`** (Studio's entry "The Agent Lifecycle" is already clash-free). One-time rename via admin.
- Naming convention stays **`Track: Title`** (`Foundations: …` · `Studio: …` · `ADK: …`).

## Content mapping — audited 2026-07-08 (via API)
The 4 legacy courses are **one content library repackaged for 3 audiences** (shared lessons: Welcome to Lyzr, Enterprise Architecture, Studio Walkthrough, Use-Case Framework, Industry deep-dives, ROI).
- **`[Legacy] Lyzr Agent Building`** (course 3447255 · product **3788224** · 24 lessons) → **SEED FOR FOUNDATIONS** ✅ — the product-agnostic arc: Welcome → Core Concepts (LLM·Tools·Context, Tool Calling, Agentic RAG, Orchestration) → Use-Case Framework → Industry deep-dives → Blueprints → ROI.
- `[Legacy] Engineering for Developers` (3447258 · 29) → concepts overlap Foundations, code superseded by **ADK** → **retire / cherry-pick**.
- `[Legacy] Value Enablement for Business Users` (3447264 · 20) → base + **sales-enablement** (customer conversations, objection handling — internal/partner training, *not* learner content) → **retire**.
- `AI Agent Management on Lyzr Certification` (3407697 · 10, thin/HTML) → old generic cert-prep → **retire**.

## Status (2026-07-08)
- ✅ **Foundations collection created + seeded** — id **1456222** (`foundations`), holds **Lyzr Agent Building** (26 learners). Layout: All Tracks · Studio · ADK · Legacy · **Foundations**.
- ✅ **`AI Agent Management Cert`** (0 learners) — already archived; no action.
- ✅ **Kept live** the 2 legacy duplicates (Engineering-for-Devs, Value-Enablement — 14 learners each) per decision; retire once enrollments wind down. Just don't feature them.
- ✅ **Homepage (Site Builder, published):** **Community section live** ("Learn with the Lyzr community" → Lyzr Community); **Foundations card auto-appears** in "Start here" (smart All-categories section + the new collection). **Product-CTA → architect.new is NOT a section** — Vogue CTA buttons link *internally only*; the product cross-link lives in the **footer** (Studio · Architect · Docs).
- 🔄 **Homepage refinements:** (a) **Legacy card removed** (collection `1447148` deleted via API; the 2 duplicate courses stay live, just ungrouped) → cards now **All Tracks · Studio · ADK · Foundations**. The 4th, **All Tracks**, is Thinkific's built-in default (slug `products`) — the smart section *always* renders it; true "exactly 3" needs the **custom-code storefront** (see Direction) or deleting the default (risky — backs the `/collections` catalog). (b) **Foundations cover generated** → `catalog-demo/banner/exports/cat-foundations-track-760x420.png` (book-open · "START HERE" · Founda*tions*); **pending manual upload** to the category image (extension can't drive the OS file picker). (c) optional: "Build in AI Studio" external link in the header nav.

## Direction (2026-07-08) — full theme-code build (corrected)
**Correction:** the earlier "no code editing on Vogue" read was **wrong** (misled by the deprecated `/manage/themes` 404, and by Vogue's Site-Builder section list having no raw-HTML block). The Vogue theme has a **full code editor** at `/manage/custom_site_themes/<id>/edit`, reached via **Channels → Website → Theme Library → ⋮ → Edit code**. It exposes the theme source: **Layouts · Sections (+ "Add New Section") · Site Pages · Snippets · Styles · Assets · manifest.json** = full **Liquid + SCSS + JS** control. This unlocks the ② **full custom-coded storefront** (curated 3 cards, external CTAs, page templates) the *right* way — clean Liquid, not fragile injection.
**Existing sections** (Liquid, editable): `banner · banner_community · call_to_action · call_to_action_community · call_to_action_course · collections · community_overview · checkout_* · bonus · checklist …`
**Safe workflow (live = 199 learners):** work on a **duplicate** — **`Vogue (Copy 1)` = theme `649350`**; the live **`Vogue` = theme `639418`** stays published & untouched. Edit copy → **Preview** → **Publish** only on approval.
**Next:** map the copy (home Site Page + `collections`/categories + `call_to_action` sections + Styles) → land the curated **3-card "Choose your track"** section as the first win → build out to LangChain parity.
- ✅ **Renamed** `ADK: Foundations` → **`ADK: Getting Started`** (clash cleared; verified via API).

## Storefront presentation
- Homepage **"Start here — choose your track"**: **3 cards — Foundations · Studio · ADK** (swap the current "All Courses" card for **Foundations**), plus a journey subhead: *"Start with Foundations, then pick how you build — visually in Studio, or in code with the ADK."*
- **Collections:** create 3 Thinkific collections (Foundations / Studio / ADK) for browsability — matches LangChain's collection-per-journey.

## Architect → folded into Studio (decided)
`Architect` **folds into Studio** — architect.new *is* Lyzr's AI Studio, so they're the same surface. Drop the separate Architect track; `Architect: Fundamentals` becomes Studio content (or retires). Result: a clean **3-track model — Foundations / Studio / ADK**.

## Implementation (ties to Phase 1)
1. Homepage: add **Foundations** track card (+ journey subhead); do the paused **Product CTA → architect.new** and **Community** sections at the same time.
2. **Rename** `ADK: Foundations` → `ADK: Getting Started` (+ any other clash).
3. Create the **Foundations** collection; map/seed courses.
4. **Content audit** of the 3 legacy courses.
