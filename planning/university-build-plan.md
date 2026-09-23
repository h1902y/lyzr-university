# Lyzr University — Build Plan (LangChain-Academy parity)

> Companion to [`langchain-academy-audit.md`](./langchain-academy-audit.md). Grounded 2026-07-08 against our live Thinkific admin + plan.

## Decisions locked
- **Theme engine → Option A: customize the Vogue Site Builder** (not a Classic-theme migration). Brand via theme settings + custom CSS/JS injected through **Settings → Code & Analytics → Site footer code**.
- **No plan upgrade** — our **Grow** plan covers the entire replication.
- **Model (LOCKED 2026-07-08):** **ALL courses free** — the academy is an adoption / lead-gen engine, not a revenue product (LangChain's playbook). No paid tier.

## Grounding (verified in-admin this session)
| Capability | Status on our plan (Grow) |
|---|---|
| Editable HTML/CSS | ✅ (Start-tier feature; we're above it) |
| API access | ✅ (read + collections write) |
| Communities (3) | ✅ (Lyzr Community exists) |
| Remove Thinkific branding | ✅ |
| Native analytics + Code&Analytics injection | ✅ (Site-footer + Signup-tracking snippets) |
| Custom domain | ✅ `university.lyzr.ai` |
| Theme engine | **Vogue Site Builder** (new, section-based) — `/manage/themes` 404s = not Classic |
| Native HubSpot/Salesforce, SSO, Learning Paths | ❌ Plus-only — **but not needed** (LangChain injects HubSpot via code, uses collections not paths, no SSO) |

## Phases

**Phase 0 — Decide & confirm**
- ✅ Model decided: **all courses free**.
- Confirm **certificates** in course completion settings (for stacking certs).
- Spot-check the Vogue custom-CSS surface (how far Option A goes) + capture the live LangChain player UX (enroll in one free course).

**Phase 1 — Look & IA**
- Brand Vogue: logo/colors/fonts (theme settings) + custom CSS via Code & Analytics.
- Homepage mirroring LangChain: **Hero+video → Category cards → Featured → Product-CTA → Community → footer** (extend the "Start here" fork already shipped).
- IA: journey cue + **`Track: Title`** naming convention; keep our 3 collections, make the journey legible. (Collection ops via API; course renames via admin/Playwright — API is read-only for course authoring.)
- Nav cross-links: **Docs · architect.new (AI Studio) · Community**.

**Phase 2 — Course template**
- Standardize: **Module 0** (overview + setup text&video + transcripts) → concept modules → **project capstone**; per-module **Resources**; a **Transcripts** lesson.
- Video: evaluate **YouTube-embedded lessons** (free + SEO + marketing) vs our MP4 pipeline for public courses.
- Enable **completion certificates**.

**Phase 3 — Funnel & analytics**
- Inject via Code & Analytics: **GA4 + GTM + Meta/LinkedIn pixel + HubSpot** (Site-footer) + **Signup-tracking** conversion events + consent banner.
- Free Foundations = lead magnets; signup = conversion → HubSpot.
- **CTA every course → architect.new + Circle** (community/events).

**Phase 4 — Growth (later)**
- Retargeting / ABM once volume justifies.

## Immediate next actions
1. **Me:** finish the 2 grounding spot-checks (Vogue custom-CSS surface + live player UX) → fold into Phase 1/2 specs.
2. **Me:** draft the Phase-1 homepage section layout + brand CSS for Vogue.
3. **You:** brand inputs (logo variants, color hex, fonts) + the analytics IDs (GA4, GTM, pixels, HubSpot portal) for Phase 3.
4. **You:** confirm free-vs-paid model.
