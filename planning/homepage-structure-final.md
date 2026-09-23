# Lyzr University — Homepage structure (FINAL)

> Decided via `/ce-brainstorm` 2026-07-08. Supersedes the section map in `phase1-homepage-spec.md`.
> Build target: the Thinkific **Vogue** theme, edited in `lyzr-university/thinkific-theme/` → zip → import → preview `?ctid=<id>` → publish. Live sandbox theme so far: **649416**.

## Header / nav — cross-link *out* (LangChain's hub move)
`Lyzr University` (wordmark) · **All Courses** · **Docs ↗** · **Community** · **AI Studio ↗** · `[Sign in · Get started]`

## Body — section order (top → bottom)
| # | Section | Contents | Status |
|---|---|---|---|
| 1 | **Hero** | Wordmark + value prop + primary **Choose your track** + secondary **Browse all courses** (no video) | refine |
| 2 | **Choose your track** | 3 audience-led dark cards (Foundations · For Business Teams · For Developers) | ✅ shipped |
| 3 | **Featured courses** | 3 curated entry courses + **Browse all →** | new |
| 4 | **Product CTA** | *"Ready to build? Open Lyzr's AI Studio."* → architect.new | new |
| 5 | **Community** | "Learn with the Lyzr community" → on-site community | ✅ shipped |
| 6 | **Footer** | 3 columns + social + legal | rebuild |

**Featured 3 (one per track):** Lyzr Agent Building · Studio: The Agent Lifecycle · ADK: Getting Started.

## Footer
- **Product** — AI Studio (`architect.new`) · ADK · Pricing (`lyzr.ai/pricing`)
- **Learn** — All Courses · Foundations · Docs (`docs.lyzr.ai`) · Community
- **Company** — About (`lyzr.ai`) · Blog (`lyzr.ai/blog`) · Contact (`lyzr.ai/book-demo`)
- **Social** — LinkedIn · YouTube (`youtube.com/@LyzrAI`) · X · Instagram
- **Legal** — © Lyzr · Privacy · Terms

## Copy (locked)
- **Hero value prop:** "Learn to build production-grade AI agents — visually in Lyzr's AI Studio, or in code with the ADK."
- **Product CTA:** "Ready to build? Open Lyzr's AI Studio." → `https://architect.new`
- Terminology: **"Lyzr's AI Studio"**, never "no-code". All courses free.

## Build split — theme-code (ships in zip) vs Site-Builder (after import)
- **Theme code / zip:** footer (full rebuild) · hero styling · track cards (done) · featured-grid styling · a **Product-CTA section type** that allows the external architect.new link.
- **Site Builder (user, post-import):** add the **Product-CTA instance** to the home page · set the hero **CTA button** text/link · fix the "Start here" **subheading** (drop "SDK" → the new naming) · point the Featured section at the 3 courses.
  *(Which section instances appear on a page + their text are Site-Builder data, not in the theme zip.)*
