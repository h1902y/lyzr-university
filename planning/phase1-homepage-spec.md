# Phase 1 Spec — Homepage + Brand (Lyzr University → LangChain parity)

> Review-ready spec. Grounded in [`university-build-plan.md`](./university-build-plan.md) (Option A: customize Vogue), the LangChain audit, our brand guide (`agentpreneur/lyzr-brand.md`), and our live catalogue.

## ✅ Current state (verified live 2026-07-08) — we're ~80% there
The homepage is **already branded + structured** from the earlier "Start here" work. Live section order:
`Header → Hero banner (branded) → "Start here — choose your track" (track cards w/ art) → "Tracks" (full course grid) → Video`.
So **brand foundation + hero + category cards + course grid + video are DONE.** The broad brand-CSS in §B below is **redundant — do NOT paste** (theme already uses Playfair / White Amber / Ferra).

**Real remaining gaps vs LangChain (the only Phase-1 work left):**
1. **Product CTA → architect.new** ("Ready to build? Open Lyzr AI Studio") — the funnel push (LangChain's LangSmith CTA).
2. **Community section** ("Learn with the Lyzr community").
3. *Optional:* move the Video into the hero (LangChain-style) instead of the page bottom.

## A. Homepage section map (Vogue Site Builder)

Mirrors LangChain's proven flow, mapped to *our* content. Order top → bottom:

| # | Section (LangChain equiv.) | Lyzr University content | Vogue section type |
|---|---|---|---|
| 1 | **Hero** (hero + video) | Lyzr University wordmark (light logo on White Amber) · headline *"Learn to build production-grade AI agents on Lyzr"* · subhead *"Self-paced courses for building visually in AI Studio or in code with the ADK — from your first agent to production."* · primary CTA **"Choose your track"** + secondary **"Browse all courses"** · a **YouTube intro video** on the right | Banner |
| 2 | **Course Categories** (3 cards) | **Choose your track** — cards: **Studio** ("Build agents visually in Lyzr's AI Studio" → start *Studio: The Agent Lifecycle*) · **ADK** ("Build agents in code with the Agent Development Kit" → start *ADK: Foundations*) · **Architect** (coming soon). *Extends the "Start here — choose your track" fork already live.* | All-categories smart section or custom cards |
| 3 | **Featured Courses** | 3 live entry courses: **Studio: The Agent Lifecycle** · **ADK: Foundations** · **Studio: Knowledge & RAG** + "See all courses" | Additional products (curated) |
| 4 | **Product CTA** (→ LangSmith) | *"Ready to build? Open Lyzr AI Studio."* → **architect.new** | Call to action |
| 5 | **Community** (→ meetups) | *"Learn with the Lyzr community."* → Lyzr Community | CTA / custom |
| 6 | **Footer** | **Products** (AI Studio · ADK · Architect) · **Resources** (Docs · Blog · University · Community · YouTube) · **Company** (About · Careers · Contact) | Footer |

*Terminology per brand feedback: Studio = "Lyzr's AI Studio" / "build visually" — never "no-code". Course art = light variant only.*

## B. Brand CSS (inject via Settings → Code & Analytics → *Site footer code*)

Starter override block — Lyzr tokens over Vogue defaults. **Selectors need tuning against Vogue's live class names when we apply** (I'll inspect the rendered DOM at apply-time); the tokens + intent are final.

```html
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Noto+Sans:wght@300;400;500;600;700&display=swap');
:root{
  --lyzr-ferra:#71514F; --lyzr-white-amber:#F3EFEA; --lyzr-cream:#E3D0C2;
  --lyzr-congo:#4A2F2D; --lyzr-black:#27272A; --white:#FFFFFF;
  --font-heading:'Playfair Display',Georgia,serif;
  --font-body:'Noto Sans','Inter',system-ui,sans-serif;
}
body{ background:var(--lyzr-white-amber); color:var(--lyzr-black); font-family:var(--font-body); }
h1,h2,h3,[class*="heading"]{ font-family:var(--font-heading); font-weight:600; color:var(--lyzr-black); }
a{ color:var(--lyzr-ferra); }
/* primary button */
[class*="btn"][class*="primary"], .button--primary{
  background:var(--lyzr-ferra)!important; color:var(--lyzr-white-amber)!important;
  border:none; border-radius:10px;
}
[class*="btn"][class*="primary"]:hover{ background:var(--lyzr-congo)!important; }
/* secondary button */
.button--secondary,[class*="btn"][class*="secondary"]{
  background:var(--lyzr-white-amber)!important; color:var(--lyzr-ferra)!important;
  border:1.5px solid var(--lyzr-ferra)!important; border-radius:10px;
}
/* cards + rules */
[class*="card"]{ background:var(--white); border:1px solid var(--lyzr-cream); border-radius:14px; }
hr,[class*="divider"]{ border-color:var(--lyzr-cream); }
/* alternating section wash */
section:nth-of-type(even){ background:var(--lyzr-cream); }
</style>
```

Feel: warm earth tones, matte, generous White-Amber breathing room, Playfair headlines, Ferra only on CTAs/accents (60-30-10). Optional: an *Elevate* layered corner element on the hero (Ferra tonal ramp, opacity-layered) per the brand guide.

## C. IA / naming

- **Keep `Track: Title`** naming (`ADK: …`, `Studio: …`, `Architect: …`) — product *is* the audience; it's our journey-legible convention (parallels LangChain's `Collection: Title`).
- **Journey cue = "Foundations first"** per track: the entry course is the start (ADK → *Foundations*; Studio → *The Agent Lifecycle*). Order Foundations-first (already done).
- **Collections:** we're down to one "Tracks" collection after the earlier cleanup. The **homepage track cards** carry the journey — keep collections minimal; no need to re-add category shelves.

## D. To go live (needs your OK — outward changes)
1. Apply the **brand CSS** to Code & Analytics (I'll tune selectors against Vogue live).
2. Build the **homepage sections** above in the Site Builder (I drive it; the one manual bit is any image upload).
3. Provide/confirm a **YouTube hero video** URL (or I use an existing Felipe intro).
4. Confirm the **track-card copy** above.
