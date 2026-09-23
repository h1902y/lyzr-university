# Lyzr University — Thinkific homepage arrangement (first-timer sequencing)

**Goal:** a first-time visitor to university.lyzr.ai immediately sees what to take first, second, third —
each product's Foundations first, then in order — with no clutter (TEMPLATE, scaffolds, legacy) in the way.

**Approach (decided 2026-06-17):** achieve sequencing through the **simple admin pages** (Re-order +
Categories + Archive) plus a **single Banner/hero edit** — NOT the fragile Site Builder featured-rows, NOT
native Learning Paths (deferred), NOT step-numbers in card art. Source of truth for names/order:
`catalog-demo/catalog-data.json` + `content-strategy.md`.

> Thinkific has **no write API** for catalog structure — everything here is the admin UI. Storefront pages
> are **CDN-cached** (~minutes): after a change, the logged-out site can lag before it reflects.

---

## The 6 live curriculum courses, in learning order

| # | Course | Thinkific ID | Track | catalog slug |
|---|--------|-------------|-------|--------------|
| 1 | ADK: Foundations | 3443593 | ADK | track-adk-foundations |
| 2 | ADK: Multimodal | 3443592 | ADK | track-adk-multimodal |
| 3 | ADK: Knowledge & Memory | 3443591 | ADK | track-adk-knowledge-memory |
| 4 | ADK: Tools & Workflows | 3445031 | ADK | track-adk-tools-workflows |
| 5 | Studio: The Agent Lifecycle | 3451858 | Studio | track-studio-foundations |
| 6 | Studio: Design & Create | 3458141 | Studio | track-studio-choosing-building |

(+ **Lyzr Community** — keep, place last.)

---

## Status of each phase

### ✅ A — Declutter (DONE, automated)
Archived so only the 6 + Community remain in the active catalog (`/manage/courses` shows "6 of 6").
Archived: **TEMPLATE** (3458123), **[Legacy] Agent Building/Engineering/Value Enablement**
(3447255/3447258/3447264), **Lyzr for Developers — the SDK Track** (3429997, old umbrella), **AI Agent
Management on Lyzr Certification** (3407697, old umbrella), **Building Production-Ready AI Agents** (3427138),
**2× "New course"** (3428061/3427128).
Script: `thinkific-uploader/src/arrange-archive.mjs`. To restore any: `/manage/courses/archived` → Actions → Restore.
> **Finding: archiving alone does NOT remove a *published* course from the storefront.** The 3 legacy
> courses stayed on `/collections` after archiving. Fix = set **Settings → Hidden course = true** on each
> (script: `arrange-hide-legacy.mjs`). After that the public `/collections` shows exactly the 6 (verified).
> "Hidden course" keeps them reachable by direct link for any existing enrollments. The umbrella/scaffold
> products were drafts (never published) so archiving was enough for them.

### ✅ C(tagging) — Studio Track category (DONE, automated)
"Studio Track" category had **0 products**; added both Studio courses. Public
`university.lyzr.ai/collections/track-studio` now lists them.
Script: `thinkific-uploader/src/arrange-tag-studio.mjs` (category id 1445649).
ADK Track (id per admin) already has its 4 courses → `…/collections/track-adk` is correct & ordered.

### ⏳ B — Order the 6 courses (MANUAL — 1 min)
The reorder list is a custom drag-sortable (not reliably scriptable). Do it by hand:
1. Go to **`/manage/courses/list`** (Courses → Re-order). Mode dropdown = **"Manually Ordered"**.
2. Drag (left grip handle ⠿) the rows so the **top 6** read, in order:
   **ADK: Foundations → ADK: Multimodal → ADK: Knowledge & Memory → ADK: Tools & Workflows →
   Studio: The Agent Lifecycle → Studio: Design & Create**, then **Lyzr Community**.
   (Archived rows may still appear in this list — leave them below; they're off the storefront.)
3. Order saves on drop. This sets the order on the homepage "Courses" section and the All-Courses page.

### ⏳ C(order) — Category order (MANUAL — 30 sec)
On **`/manage/collections`**, drag the **Track** categories so order is **ADK Track → Studio Track →
Architect Track** (ADK leads — it's the only complete track). Leave the 12 Modules + 6 Functions below as
the signposted (empty) collections for when those courses ship.

### ⏳ D — "Start here" hero (MANUAL — Site Builder, ~5 min)
Edit the **existing Banner** on the Home page into a start-here hero (the builder is fragile; do this by hand):
1. **Design → Website → Home page** (opens Site Builder, theme "Vogue"), or directly the
   `/manage/site_builder/…/home/…` URL.
2. Select the **Banner** section (top of the preview) → its settings open on the left.
3. **Heading:** `New to building AI agents? Start here.`
   **Subtext:** `Learn Lyzr hands-on — pick your starting point below.`
4. **Two buttons (CTAs):**
   - Primary: **`Start with ADK Foundations`** → link to the ADK Foundations course
     (`/courses/...` or `/collections/track-adk`).
   - Secondary: **`Build in Lyzr Studio`** → Studio: The Agent Lifecycle (or `/collections/track-studio`).
5. **Save** (top-right). Verify logged-out.
   *Optional:* below the hero, the existing "Courses" section already lists products in the Phase-B order;
   leave as-is (don't try to build per-track featured rows — the Category collection pages serve that).

---

## The 3-collection front door (native, already wired)

Each Thinkific Category has its own ordered page — these ARE the per-collection rows:
- **Tracks:** `…/collections/track-adk` (4, ordered ✓) · `…/collections/track-studio` (2 ✓) · `…/collections/track-architect` (0, coming soon)
- **Modules (12)** and **Functions (6):** categories exist with 0 products → stand as "coming soon"
  signposts until those courses are built. No placeholder courses needed.

## Maintenance rule
When a new course goes live: (1) publish it; (2) **tag it into its Track category** (`/manage/collections`
→ Edit category → add product → Update); (3) **insert it at the right position** in `/manage/courses/list`
(Manually Ordered). Keep this table and `catalog-data.json` in sync.

## Verification
- Logged-out `university.lyzr.ai/collections` shows only the 6 (+ Community), ADK Foundations first; no
  TEMPLATE / New course / legacy / umbrellas.
- `…/collections/track-adk` = 4 ADK in order; `…/collections/track-studio` = 2 Studio.
- Homepage Banner = start-here hero; both CTAs land on the right Foundations course.
