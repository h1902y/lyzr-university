# LangChain Academy — Deep Audit & Lyzr University Replication Blueprint

> **Goal:** rebuild Lyzr University to match LangChain Academy's experience (our chosen "gold standard").
> **Method:** authenticated browse of `academy.langchain.com` (Harshit's work Google profile) on 2026-07-08 — screenshots, downloaded page sources, JS config extraction, and full network-request capture.
> **Raw evidence:** `scratchpad/lc-audit/{home,collections,course_lc_python}.html` + network/JS captures in the session log.

---

## 1. TL;DR — what makes it "gold standard"

1. **Thinkific (Classic) + a heavily customized theme + custom domain** — looks nothing like stock Thinkific.
2. **Ruthlessly simple IA:** 3 *journey* collections — **Foundation · Quickstart · Project** — and every course is named `Collection: Title`.
3. **100% free courses = a lead-generation funnel**, not a revenue product. Every surface pushes to the product (**LangSmith**) and the **community** (meetups).
4. **Serious demand-gen instrumentation:** Segment CDP → Mixpanel + 2×GA4 + HubSpot, plus a full ad-retargeting + ABM stack.
5. **One repeatable course template:** a **"Module 0" onboarding** module + concept→project modules; lessons mix **video (YouTube) + text + resources + transcripts + surveys**.

The lesson for us: **the academy is a marketing engine with courses attached**, built on cheap primitives (Thinkific + YouTube), wrapped in a strong brand theme, and wired to a real growth stack.

---

## 2. Platform & tech stack

| Layer | LangChain Academy | Notes for us |
|---|---|---|
| **LMS** | **Thinkific Classic** (jQuery 3.5.1, `toga` design system, `application-themes-v2`) | Same platform we're on ✓ |
| **Theme** | **Custom site theme** — account `967498`, theme `446829` (`cdn-themes.thinkific.com/967498/446829/…`), base "Light – rounded corners" | We're on a lightly-customized Vogue; they've gone full custom |
| **Domain** | `academy.langchain.com`, behind **Cloudflare** | We have `university.lyzr.ai` ✓ |
| **Fonts** | Inter + Roboto (Google) + brand fonts (Aeonik Mono, TWK Lausanne) | Wire Lyzr brand fonts |
| **Video host** | **YouTube (embedded)** — lessons *and* marketing hero videos | We host MP4s on Thinkific; YouTube = free + doubles as marketing/SEO |
| **Consent** | **CookieYes** (`d2e859934c…`) | GDPR banner |
| **Forms** | Google **reCAPTCHA** | signup/lead forms |
| **CDN / utils** | jsDelivr, cdnjs (Font Awesome), Finsweet attributes | — |

**Analytics / CDP (the growth brain):**

| Tool | ID / detail | Purpose |
|---|---|---|
| **Segment** | writeKey `u3F8DDyFgfalTmTmazQmUhET8TEe2unb` | CDP hub — fans out to everything below |
| **Google Tag Manager** | `GTM-W8T257GK` | tag orchestration |
| **GA4 ×2** | `G-47WX3HKKY2`, `G-2S3P88WQL8` | web + product analytics (dual property) |
| **Mixpanel** | `mixpanelPerson` | behavioral/product analytics |
| **HubSpot** | portal `242623570` (hs-scripts, hs-analytics, hs-banner, web-interactives) | CRM + chat/banners — the lead lands here |
| **reo.dev** | `334496741e114fd` | dev-audience intent/identity |

**Ads & ABM (retarget everyone):** Google Ads/DoubleClick · Meta Pixel `4383348228602695` · LinkedIn Insight `5973154` · Twitter/X `uwt` · Reddit Pixel `a2_iu5i0mdlzisy` · **Influ2** (account-based ads) · **OpenAI ads SDK** (`oaiq`).

---

## 3. Information architecture

**Top nav (custom):** `Academy Home · Docs · Community · LangSmith · All Courses · My Account · My Dashboard · Sign Out`
→ deliberately cross-links **out to the product (LangSmith) and docs and community** — the academy is a hub, not an island.

**Collections (= Thinkific categories) — only 3, on a *journey* axis:**

| Collection | Slug | Meaning |
|---|---|---|
| **Foundation** | `/collections/foundation` | Learn a capability end-to-end |
| **Quickstart** | `/collections/quickstart` | Fast, task-focused (often no-code) |
| **Project** | `/collections/project` | Build a real thing |
| *(All Products)* | `/collections/products` | Thinkific default |

**Naming convention:** every course title is **`Collection: Title`** — e.g. *Foundation: Introduction to LangChain – Python*, *Quickstart: LangSmith Fleet*, *Project: Deep Agents*. The collection is literally the prefix, so the journey stage is legible everywhere (cards, tabs, search).

**Catalog page (`/collections`, "All Courses"):** filter tabs (`All · Foundation · Project · Quickstart`) + **search box** + a paginated card grid (3 pages). Each card = dark node-diagram thumbnail + "Course" badge + `Collection: Title` + one-line description.

---

## 4. Catalog (8 courses, all FREE)

| Course | Collection | Topic |
|---|---|---|
| Introduction to LangChain – Python | Foundation | LangChain SDK + LangSmith observability |
| Introduction to LangSmith Deployment | Foundation | Deploy/manage agents |
| Introduction to Deep Agents | Foundation | Long-running agents (Deep Agents harness) |
| Building Reliable Agents | Foundation | first run → production via LangSmith |
| Monitoring Production Agents | Foundation | cost/trace/quality/latency |
| LangSmith Essentials | Quickstart | platform essentials |
| LangSmith Fleet | Quickstart | **no-code** agents |
| Agent Builder | Quickstart | build agents |
| Deep Agents | Project | build-a-thing capstone |

Topics map 1:1 to **products** (LangChain, LangGraph, LangSmith, Deep Agents, Fleet) — courses exist to drive product adoption.

---

## 5. Homepage / storefront layout

Top → bottom: **Hero** (wordmark + "Level up with LangChain Academy" + a **YouTube "Getting Started" video**) → **Course Categories** (3 cards: Quickstart / Foundation / Project, each with LangGraph-style node art) → **Featured Courses** (3 cards + "See all courses") → **Product CTA** ("Ready to start shipping reliable agents?" → LangSmith) → **Community** ("Learn with the community" → meetups) → **corporate footer** (Products / Resources / Company + status + legal).

---

## 6. Course-page template (repeatable)

1. **Hero:** `Collection: Title` + description + **YouTube marketing video** + **"Enroll for free"** button.
2. **Curriculum accordion** (modules, collapsible).
3. **"About this course":** `Free · N lessons · X hours of video content`.
4. **Product CTA** (→ LangSmith) → **Community/meetups block** → footer.
5. SEO `<title>` differs from display title (e.g. display *"Foundation: Introduction to LangChain – Python"* / SEO *"Introduction to LangChain: Build AI Agents with Python"*).

---

## 7. Course structure & learning UX

Example — *Introduction to LangChain – Python* (**Free · 30 lessons · 1.5h video**):

- **Module 0 — "Welcome to the course!"** *(the onboarding module)*: Course Overview · Getting Set Up **(Text)** · Getting Set Up **(Video)** · Module 0 Resources · **Course Transcripts**
- **Module 1: Create Agent** — Module Introduction · Module Resources · *Lesson 1: Foundational Models · L2: Tools · L3: Short-Term Memory · L4: Multimodal Messages* · **L5: Personal Chef (Project)**
- **Module 2: Advanced Agent** · **Module 3: Production-Ready Agent**

**Patterns to steal:**
- A dedicated **Module 0** for orientation + environment setup (in **both** text and video) + a **Course Transcripts** page.
- Each content module = **Introduction → Resources → numbered Lessons → a Project capstone** (concept→practice→project — same rhythm we already use in the ADK/SDK track).
- **Lesson types in play:** Video (YouTube-embedded), Text, Resources (downloadable code/links), Transcripts, Survey.
- **Player:** Thinkific's standard course player (left sidebar of modules/lessons + progress; main pane video/text; mark-complete; prev/next). *(Not screenshotted — Harshit isn't enrolled in any course; I can capture it by enrolling in a free course on request.)*
- **Certificates:** not surfaced on course pages — consistent with a free/lead-gen model (completion certs appear to be off or de-emphasized).

---

## 8. The real "gold" — the demand-gen funnel

```
Visitor → free course (SEO'd, YouTube video) → Thinkific signup (lead) → HubSpot CRM
        → every page CTAs to LangSmith (product) + Community (meetups/events)
        → Segment CDP unifies identity → Mixpanel/GA4 for behavior
        → retarget across FB / LinkedIn / Reddit / X / Google + Influ2 ABM
```

The courses are the **top of a product-led-growth funnel.** Free removes friction; the signup is the conversion; the content nurtures toward LangSmith; the ad stack re-engages non-converters. This is the part most "academies" miss — LangChain treats it as **growth infrastructure.**

---

## 9. Gap analysis — Lyzr University today vs LangChain Academy

| Dimension | LangChain Academy | Lyzr University today | Action |
|---|---|---|---|
| Platform | Thinkific Classic | Thinkific (Vogue) ✓ | — |
| Theme | Fully custom brand theme | Lightly-customized default | **Invest in a custom theme** |
| IA | 3 journey collections + `Collection: Title` naming | 3 collections (Tracks/Modules/Functions) — a *taxonomy* axis | Add a clear **journey/level cue** + naming convention |
| Pricing | 100% free (lead-gen) | mixed / undecided | **Decide: free TOFU vs paid**; wire to architect.new/Studio |
| Onboarding | **Module 0** (overview + setup text+video + transcripts) | ad-hoc per course | **Adopt a "Start here / Module 0" per course** |
| Video | YouTube (free + SEO + marketing) | Thinkific-hosted MP4s | Consider **YouTube hosting** (cost + reach) |
| Analytics | Segment CDP + GA4×2 + Mixpanel + HubSpot | none wired | **Add GA4 + a pixel + HubSpot/CRM at minimum** |
| Funnel/CTAs | every page → product + community | weak | **CTA to architect.new + Circle community on every course** |
| Retargeting/ABM | full stack + Influ2 | none | Optional Phase-later |
| Cross-links | Docs / product / community in nav | thin | Add **Docs · Studio · Community** to nav |
| Transcripts | per-course "Course Transcripts" page | we author lesson notes/PDFs ✓ | Publish transcripts as a lesson too |

---

## 10. Replication blueprint (phased)

**Phase 1 — Look & IA**
- Build/commission a **custom Thinkific theme** in Lyzr brand (matching LC's polish).
- Restructure the storefront homepage to mirror LC: Hero+video → Category cards → Featured → Product CTA → Community → footer. *(We already shipped a "Start here" fork — extend it.)*
- Introduce a **journey cue** (e.g. Foundations / Deep-dive / Project) and a **`Track: Title`** naming convention.
- Cross-link nav to **Docs · AI Studio (architect.new) · Community**.

**Phase 2 — Course template**
- Standardize every course on **Module 0 (overview + setup text+video + transcripts) → concept modules → project capstone**.
- Add per-module **Resources** pages (code/links) + a **Transcripts** lesson.
- Evaluate **YouTube hosting** for lessons (free + marketing/SEO), keep MP4 pipeline as fallback.

**Phase 3 — Funnel & analytics**
- Free "Foundations" courses as **top-of-funnel lead magnets**; signup = the conversion.
- Wire **GA4 + Meta/LinkedIn pixel + HubSpot** (or Segment if we want the CDP), CookieYes for consent.
- Every course page CTAs to **architect.new** (product) + **Circle** (community/events).

**Phase 4 — Growth (optional)**
- Retargeting + ABM (LinkedIn/Meta/Influ2-style) once volume justifies it.

---

*Prepared from a live authenticated audit; extend by enrolling in a free LangChain course to capture the in-player UX and any completion/cert flow.*
