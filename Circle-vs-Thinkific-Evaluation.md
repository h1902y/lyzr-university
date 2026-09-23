# Circle.so vs Thinkific — End-to-End Platform Evaluation for Lyzr University

**Date:** 2026-06-29 · **Prepared for:** Lyzr University (internal) · `#lyzr-academy-pipeline`
**Scope:** Can Circle.so replace Thinkific as the LMS for Lyzr University?
**Evidence base:** (1) two web-research sweeps, (2) a live read-only **Admin API v1 probe** of Lyzr's Circle, (3) a full **hands-on admin walkthrough** of `academy.lyzr.ai` as an admin, incl. **a dummy course built end-to-end**.
**Status:** Complete. This is the single consolidated report; the companion `circle-course-automation-recipe.md` retains the engineering-level Playwright selectors.

---

## ✅ Decision (2026-06-29): Continue on Thinkific

After this evaluation, the call is to **stay on Thinkific** — Lyzr University does **not** migrate to Circle at this time. Rationale:
- **The original deal-breaker stands:** Circle has no native, branded, **stacking** certificates — and the stacking-cert ladder is core to the University's value proposition.
- **Analytics is a regression:** no API completion pull; the University Pulse can't be reproduced without a paid webhook/Data API path.
- **The workarounds cost money:** the Accredible cert chain, advanced workflows, Headless API, and managed migration all require upgrading from Lyzr's current **Professional** tier to Business/Plus.
- **The "audience already on Circle" upside is real but qualified** — a large but mostly-inactive list (~6% MAU), so a migration wouldn't auto-activate it.

The full evaluation below is retained as the decision record. **Revisit if:** Circle ships native *stacking* certificates **and** a completion-data API, or if strategy shifts decisively to community-led learning (where Circle's community + gamification edge would outweigh the cert gap).

**Follow-on (2026-06-29):** rather than keep Circle in parallel, the direction is now to **sunset Circle entirely** and consolidate to **Thinkific (LMS) + Discord (community)** — see **`circle-sunset-plan.md`**. The audience CSV export has been triggered to preserve the 7.2k-contact list before any decommission.

---

## 1. Evaluation detail — recommendation as assessed

> **Conditional — lean toward consolidating Lyzr University onto Circle as a community-first re-platform, but
> NOT as a free like-for-like replacement of Thinkific.** Circle is where Lyzr's audience already is, and its
> community-integrated learning is a genuine strategic upgrade. But the original blocker — native, branded,
> **stacking** certificates — is *still unsolved*, analytics-by-API is a *regression*, and the features needed
> to work around both sit on **paid upper tiers Lyzr isn't on yet**. A move is justifiable only if you accept
> three concrete pieces of work and a plan upgrade. If branded stacking certs are non-negotiable and the
> Accredible workaround proves inadequate, **stay on Thinkific.**

**TL;DR**
1. **The audience is already on Circle, at scale** — 3,224 members / 7,221 contacts / 5 live courses (1.6k–4.7k members each) vs the Thinkific University's **88 learners**. (But engagement is thin: ~6% MAU.)
2. **No native certificates** — confirmed three ways (API has zero cert endpoints; no Certificates tab/Option in the live builder; multiple dated 2026 reviews). No branding, no per-course control, **no cert-stacking** — and stacking is Lyzr's whole model (Foundation→Specialist→Expert→Agentpreneur). Only an Accredible-via-Zapier bolt-on.
3. **Analytics-by-API is a step back** — Thinkific exposes an enrollment/completion pull the University Pulse relies on; Circle exposes none. Completion data is reachable only by **webhook push (Circle Plus)** or the **Data API warehouse stream (Plus Platform)**.
4. **Authoring automation is parity-at-best** — both need Playwright for a real course build; Circle's v1 API can POST HTML-body lessons (a modest edge) and its media uploader is a real file input.
5. **You're on the Professional tier** — Community AI, advanced Workflows, the Headless API, the **webhook for the cert workaround**, and Circle's managed migration **all require upgrading** to Business ($219/mo) or Plus (from $649/mo).

### The strategic fork (the real question)
| If Lyzr University is primarily… | …the right platform is | because |
|---|---|---|
| **A credentialing engine** (the stacking-cert ladder *is* the product) | **Thinkific** (± Accredible) | Circle can't issue branded/stacking certs natively |
| **A community-led learning loop** (builders learn where they already are) | **Circle** | Courses are Spaces, lesson-completion earns points, 4.7k builders already here |

The audience-fit question pushes toward #2; the cert ladder pushes toward #1. The recommendation above is the synthesis: go community-first on Circle **only if you explicitly fund the cert workaround + analytics rebuild + plan upgrade.**

---

## 2. Context & mandate
In the Jun 23 weekly, the team raised whether Circle/Thinkific is the right platform and whether the builders Lyzr wants (enterprise devs, partners) are even in the community. Thinkific was chosen in **April 2026** because Circle's LMS lacked **certifications**; Lyzr is on a **rolling monthly Thinkific plan** (low switching cost). The mandate was to map Circle's LMS vs Thinkific. Circle has since relaunched its developer platform and shipped native quizzes + the **"Circle Eclipse"** AI release, so every original blocker was re-verified against the current product.

---

## 3. Lyzr's current Circle footprint (live, 2026-06-29)
- **Plan tier:** **Professional** (admin offers a Business trial; Community AI is gated off). Community ID **225567**.
- **Audience:** 7,727 people · **3,224 members** · 7,221 contacts (email list) · 3,315 invited · 3 admins · 8 moderators.
- **Engagement:** Active 30d **199 (6% MAU)** · Daily active 18. Large base, thin activity.
- **5 live courses (each a Space):**

  | Course | Members (enrollment proxy) | Sections |
  |---|--:|--:|
  | Lyzr Primer Course | 4,721 | 8 |
  | Developer's Course | 4,598 | 4 |
  | Gen AI Stack for Enterprise Leaders | 4,568 | 10 |
  | Agent Architect Course | 3,215 | 3 |
  | Recorded Sessions (July Cohort) | 1,671 | 5 |

  ~30 sections, ~77 lessons total. **Media storage:** 21.8 GB of 200 GB (overage = 50 GB add-on @ $10/mo).
- **Implication:** this isn't "switch tools" — Lyzr already *runs* on Circle at far larger scale than the Thinkific University (88 learners). The gap is the credential + analytics layer, not the audience.

---

## 4. The five must-have criteria — verdicts & evidence

**① Certifications & stacking certs — ❌ HARD GAP (decisive).**
No native certificate engine in 2026. Verified on-screen: no "Certificates" tab in the course builder, no certificate toggle in course Options; verified in API: zero certificate endpoints; verified in research: dated reviews + Circle's own migration drops certificates. Workaround = **Workflows → "Member completed course" → Send webhook → Zapier → Accredible** (or Canva). A disabled template *"Congratulate members when they complete a course"* already exists. **The webhook action is gated to Circle Plus.** No native cert-stacking. *Mitigant:* Lyzr's stacking ladder is partly aspirational (Thinkific Learning Paths/Expert rules are deferred; Thinkific's API can't expose cert issuance either — Pulse already uses a completion-as-cert proxy), so the gap is "branded cert generation," solvable via Accredible — but it adds a third-party dependency for Lyzr's core differentiator.

**② Rubrics / graded assessments — ❌ but low real weight.**
Native quizzes confirmed live: **Single/Multiple-answer**, auto-graded, **passing-grade gate (e.g. 70%)**, **enforce-to-proceed**, **hide-answers**, optional video/image per question. **No** rubrics, graded assignments, essays, file-upload, or SCORM. Note: rubrics are **not a live Lyzr University LMS dependency** (they're an Agentpreneur judging concept), and Thinkific lacks rubrics too — so this "blocker" is weaker than the April recollection implies.

**③ Analytics + API — 🟡 / ❌ REGRESSION (second real problem).**
Course-completion analytics **exist in-UI + CSV export** (course dashboard "Average completion rate" + Analytics → Courses). But the **Admin API (v1 and v2) exposes no enrollment/completion/progress/certificate endpoints** (spec-verified + live-probe-confirmed: every such endpoint 404s). The University Pulse polls Thinkific's REST API weekly — **that pattern can't be reproduced on Circle.** Substitutes: **webhook push** on course completion (Circle Plus) or the **Data API** event stream into a warehouse (Plus Platform + a data engineer). Either way Pulse needs a **poll→push re-architecture**, and historical completion data does **not** migrate (clean-slate baseline).

**④ Community + audience fit — ✅ STRENGTH.**
Courses are Spaces inside the community; lesson completion earns **gamification points** (9 levels, doubling thresholds, 7d/30d/all-time leaderboard); the right builders are already here (§3). This is the inverse of Thinkific (weak community) and the strongest argument *for* Circle.

**⑤ Course-creation automation — 🟡 PARITY, not an upgrade.**
Admin API **v2 is GET-only** for courses/sections/lessons (open "Create Course in V2" feature request). Legacy **v1 can POST lessons** (HTML `body_html`) — a small edge over Thinkific (whose API authors nothing) — but no native media param and v1 is **frozen**. Full authoring still needs **Playwright**, like today's `thinkific-uploader`. **Live win:** the featured-media uploader is a real `<input type="file">`, so Playwright `setInputFiles()` works (no drag-drop). The `descript-to-thinkific` renderer would need a Circle variant emitting an HTML lesson body + featured-media video instead of the video+PDF pair.

---

## 5. Circle vs Thinkific — feature matrix
Legend: ✅ native/strong · 🟡 partial/workaround · ❌ absent.

| Capability | Thinkific | Circle (2026) | Notes |
|---|:--:|:--:|---|
| Branded completion certificates | ✅ | ❌ | Circle: Accredible-via-Zapier only; webhook needs Plus |
| Cert *stacking* ladder | 🟡 | ❌ | No native cert to stack |
| Quizzes (auto-graded) | ✅ | ✅ | Circle: single/multi, 70% gate, media per question |
| Graded assignments / file submission | 🟡 | ❌ | |
| Evaluation rubrics | ❌ | ❌ | Neither |
| Course / section / lesson structure | ✅ | ✅ | Circle: course = a Space |
| Lesson content types | ✅ (1 file/lesson) | ✅ (HTML body + featured media + ≤15 files) | Different shape |
| Drip / scheduled / self-paced | ✅ | ✅ | Self-paced / Structured / Scheduled |
| In-course sequencing & gates | ✅ | ✅ | lesson-order lock, 90%-watch, quiz-pass |
| Cross-course prerequisites | 🟡 | ❌ | Circle: feature request only |
| Per-learner progress / gradebook | ✅ | 🟡 | Circle: "no gradebook", shallow progress |
| Analytics export (CSV) | ✅ | ✅ | Circle: 10 analytics sub-sections |
| Analytics via API (poll) | ✅ | ❌ | **Regression** |
| Completion via push (webhook) | 🟡 | ✅ (Plus) | "Member completed course" trigger |
| API course authoring | ❌ | 🟡 (v1 HTML lessons) | Both need Playwright for full build |
| Community-integrated learning | 🟡 | ✅ | Circle's core strength |
| Gamification (points for completion) | ❌ | ✅ | levels, badges, leaderboard |
| Payments / paywall | ✅ | ✅ (Stripe) | LU courses are free |
| Affiliate program | 🟡 | ✅ | built-in, Stripe payouts |
| Email marketing / broadcasts | 🟡 | ✅ | Email Hub (broadcasts, forms) |
| AI (content/agents) | ❌ | ✅ (Eclipse, Business+) | Community AI + AI Agents |
| Native branded mobile app | ❌ | 🟡 (Plus only) | |

---

## 6. Exhaustive Circle product feature map (live admin)
*Full detail in `circle-product-feature-map.md`; summarized here for completeness.*

- **Spaces:** 6 types — Posts · Events · Chat · **Course** · Members · Images; grouped in Space Groups; visibility Open/Private/Secret (courses default to draft/hidden).
- **Courses/LMS:** 3 delivery models; builder tabs = Lessons · Customize · Paywalls · Mobile lock screen · Members · Options · Workflows (**no Certificates tab**); lesson = featured media (Vimeo/YouTube/Wistia/embed/record) + slash-command HTML body + Files; per-lesson gates (90% watch, auto-advance); course Options = lesson-order enforcement, comment notifications, hide member count, SEO.
- **Quizzes:** single/multiple answer, pass-grade gate, enforce-to-proceed, hide answers, media per question.
- **Gamification:** points → 9 levels (doubling) + leaderboard (7d/30d/all-time); custom badges; achievement workflows.
- **Analytics:** Overview · Members · Website · Spaces · Posts · Messages · Devices · Events · Payments · **Courses** + CSV export.
- **Monetization:** Paywalls (Stripe; coupons, subscription groups, transactions, taxes) + built-in **Affiliates** (commissions, tracking, Stripe payouts).
- **Marketing/Email Hub:** Broadcasts · Forms · audience.
- **Workflows:** Automations · Bulk actions · Scheduled; triggers (course completed, quiz passed/failed, joined, tag) → actions (email/DM, tag, push, **webhook [Plus]**).
- **AI / Circle Eclipse:** **Community AI** (Business+, gated off) · **AI Agents** (Knowledge bases + custom agents; Lyzr has a default "Lyzr Academy agent", off) · Discover · Studios.
- **Audience:** Manage · Access groups · Connections · Segments · Invite links · Onboarding · Tags · Profile fields · Gamification · Activity logs.
- **Content/Files:** Media (200 GB) · Posts · **Pages** (CMS) · Spaces · Topics · Moderation · Live.
- **Site:** Navigation · SEO · Redirects · Defaults · **Code snippets** (custom JS — viable Accredible-widget host).
- **Platform:** General · Custom domain · Mobile app (Circle app; white-label = Plus) · Weekly digest · Embed · **SSO (OAuth) + Headless API** · Connect (member directory) · Legal.

---

## 7. API & data model (live probe)
- **Auth:** `CIRCLE_TOKEN` (in `lyzr-university/.env`) works on **Admin API v1**, header `Authorization: Token <token>`, admin scope.
- **Model:** a **course = a Space** (`space_type:"course"`); there is no `/courses` endpoint.
- **Readable:** `community_members`, `spaces`, `space_groups`, `course_sections`, `course_lessons` (HTML `body_html`; the `course_section_id` filter is ignored — filter by `section_id` client-side), `space_members?space_id=` (enrollment proxy, has `count`).
- **Absent (v1 & v2):** course/lesson completions, progress, certificates, gamification — all 404.
- **v2** (`api-headless.circle.so/api/admin/v2`) is GET-only for courses; needs a Business-tier token. **Headless/Data API** = embedding + warehouse ETL (Plus Platform). Rate limit ~2,000 req / 5 min.

---

## 8. Course-creation automation — feasibility & recipe
**Hybrid strategy:** course shell + sections = **Playwright**; HTML-body lessons = optionally **v1 API POST**; native media = Playwright `setInputFiles` on the real file input; read/verify = Admin API v1. Login is **email-OTP** → a headless run needs a persisted authenticated storage state (don't script OTP). Full deterministic selectors/steps + URL patterns are in **`circle-course-automation-recipe.md`** (create-space → choose type "Course" → delivery model → draft course → Edit lessons → + Add section → + Add new Lesson/Quiz → lesson editor `setInputFiles` + body + Save). Verdict: **automatable to parity with the Thinkific uploader** — not a reason to switch *for* automation.

---

## 9. Pricing & plan reality (live)
| Tier | Price | Unlocks (relevant) |
|---|---|---|
| **Professional** *(current)* | entry | Courses, quizzes, gamification |
| **Business** | **$219/mo** ($199 annual) | Community AI, advanced Workflows, **webhook action**, **Admin + Headless API**, branded emails, managed migration |
| **Plus** | **from $649/mo** | full features, highest limits, **branded mobile apps**, Data API (Plus Platform) |

**Cost reality:** Lyzr already pays for Circle, so consolidating could remove the separate Thinkific spend — **but** the cert workaround (webhook) and a webhook-based Pulse both need **Business or Plus**, and the Data API path needs **Plus Platform**. Budget a tier upgrade, not a free migration.

---

## 10. Migration plan + effort/cost
Circle offers a **free, managed Thinkific→Circle migration** (eligibility Business-annual / Plus; ~2–4 weeks; one course at a time, run both in parallel). It migrates course structure, sections, lessons + content, files, video/audio/embeds — and **drops quizzes, assignments, certificates, completion history, and learner progress.**

- **Phase 1 — Decide & de-risk (no migration):** stand up Accredible-via-Zapier on the "Member completed course" workflow for **one** course (requires the Plus webhook) and validate branding/"stacking" — **this is the go/no-go gate**; finish the few uncaptured UI checks (§12).
- **Phase 2 — Pilot one course:** migrate e.g. ADK Foundations via managed migration; rebuild its quiz; run Circle + Thinkific in parallel; validate the learner + gamification experience.
- **Phase 3 — Rebuild automation:** re-architect University Pulse from Thinkific REST poll → Circle **webhook push** (or Data API); re-point the Playwright uploader at Circle; add a Circle renderer to `descript-to-thinkific`.
- **Phase 4 — Cut over the catalogue:** migrate remaining live courses + map the 3-collection taxonomy (Tracks/Modules/Functions → Spaces/Space Groups); retire Thinkific once parity holds.

---

## 11. Risks & open questions
- **Lock-in inversion:** moving credentialing onto an Accredible+Zapier chain adds a third-party dependency for Lyzr's differentiator.
- **Analytics continuity:** completion history doesn't migrate — Pulse trends reset.
- **Plan-cost step-up:** the features needed for a real migration sit on Business/Plus.
- **Engagement:** ~6% MAU on a 3.2k base — re-platforming won't fix activation by itself.
- **Single-instructor bandwidth:** rebuilding quizzes + re-pointing two automations is real engineering.
- **Unverified (research flags):** exact v1 lesson-create params; Data API event catalogue; whether v1 can create a course shell.

---

## 12. Coverage note (what was not deep-dived)
For full honesty: the live walkthrough covered course creation (incl. a dummy build), quizzes, course Options/Workflows, and every Settings section. **Not** deep-dived: the new **Discover** & **Studios** Eclipse surfaces, the member-facing **course player** experience, course **Customize / Mobile-lock-screen** tabs, and Events. None are expected to change the recommendation, but they can be captured on request.

---

## 13. Sources & method
- **Live API probe** (read-only, 2026-06-29): Circle Admin API v1 with `CIRCLE_TOKEN`.
- **Live admin walkthrough** (2026-06-29): `academy.lyzr.ai` as admin; dummy course built end-to-end (GIF: `circle-dummy-course-build.gif`).
- **Research:** Circle help center, circle.so/pricing & /gamification, api.circle.so (admin/headless/data + usage-and-limits), v2 OpenAPI spec, circle.so/migration, LinoDash (2026-05-16), group.app, SellCoursesOnline, SchoolMaker (2026).
- **Companion docs:** `circle-product-feature-map.md` (feature catalog) · `circle-course-automation-recipe.md` (Playwright recipe).

*Confidence: high on API facts (spec- + probe-verified) and the certificate gap (multiple dated sources + zero API surface + on-screen confirmation); medium on v1 lesson-create mechanics, Data API event coverage, and the uncaptured UI surfaces in §12.*
