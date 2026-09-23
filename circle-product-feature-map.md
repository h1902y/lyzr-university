# Circle.so — Exhaustive Product Feature Map (hands-on, Lyzr `academy.lyzr.ai`)

**Captured:** 2026-06-29, live admin walkthrough as an admin + Admin API v1 probe.
**Plan tier (confirmed):** **Professional** — the admin shows "Try the Business plan free for 30 days" and
Community AI says *"Your current plan doesn't support Community AI. Upgrade to Business."* Several
higher-tier features below are therefore gated/unavailable on Lyzr's current plan.
**Release note:** the community is on **"Circle Eclipse"** (banner: *Circle AI, Discover, Studios*) — a 2026
release that post-dates most public reviews.

---

## 0. Live numbers (Lyzr's community, for context)
- **Audience:** 7,727 people · **3,224 members** · 7,221 contacts (email list) · 3,315 invited · 3 admins · 8 moderators.
- **Engagement:** Total members 3,229 · Active 30d **199 (6% MAU)** · Daily active 18. (Low active-rate on a large base.)
- **Courses (5 live, as Spaces):** Lyzr Primer (4,721 members) · Developer's Course (4,598) · Gen AI Stack for Enterprise Leaders (4,568) · Agent Architect (3,215) · Recorded Sessions July (1,671). ~30 sections, ~77 lessons.
- **Media storage:** 21.8 GB of **200 GB** used (Video originals 8.16GB, encodings 13.08GB). Overage = 50GB add-on @ $10/mo.

---

## 1. Community structure & spaces
- **Space types** (create flow → "Choose space type"): **Posts · Events · Chat · Course · Members · Images**.
- Spaces live in **Space Groups** (e.g. "Lyzr Community", "Expert Sessions", "Lyzr Learn"). Visibility per space: Open / Private / Secret (the create-course flow defaults a course to **draft, hidden from members**).
- **Feed** (toggle-able), per-space post/topic settings, member directory.

## 2. Courses / LMS (the core question)
- **Course = a Space** (`space_type: course`). Delivery models: **Self-paced · Structured (drip by enrollment date) · Scheduled (fixed dates)**.
- **Builder tabs:** Lessons · Customize · Paywalls · Mobile lock screen · Members · Options · Workflows. **No "Certificates" tab.**
- **Lesson editor:** **Featured media** (drag/upload or embed Vimeo/YouTube/Wistia/Typeform; or record a clip) **+ rich-text body** (slash-command block editor → `body_html`) **+ Files tab** (attachments). Per-lesson: Enable featured media, Enable comments, **Enforce video completion** (≥90% watch), Auto-advance after video, Default tab (Comments/Curriculum/Files), Draft/Published.
- **Sections** group lessons; add **Lesson** or **Quiz** under a section.
- **Course Options:** Lesson-order enforcement · notify admins on lesson comments · hide member count · SEO (slug, meta, OG). **No certificate / completion-certificate setting anywhere.**
- **Course dashboard analytics:** Waitlist + **Average completion rate** (exists in UI even though the API hides it).

## 3. Quizzes / assessments
- Added at section level (Lesson **or** Quiz). Quiz settings: **Set a passing grade (e.g. 70%)**, **Enforce passing grade to proceed** (gate), **Hide answers on result page**, comments.
- **Question types: Single answer · Multiple answer** only (auto-graded). Each question can attach **video/image media**. **No** open-ended/essay, **no file-upload**, no randomization.
- **No rubrics, no graded assignments, no SCORM.**

## 4. Certificates — ❌ none native (the original blocker, re-confirmed on-screen)
- No "Certificates" tab in the course builder; no certificate toggle in course Options; **zero certificate endpoints** in the Admin API.
- Workaround path lives in **Workflows**: a "Member completed course" trigger → **Send webhook** action → Zapier → Accredible (or Canva). The community already has a (disabled) template workflow *"Congratulate members when they complete a course."* The **webhook action is gated to Circle Plus**.

## 5. Gamification (Circle's genuine strength)
- **Points → Levels** (9 levels, doubling thresholds: 10/20/40/80/160/320/640/1280) + **Leaderboard** (7-day / 30-day / all-time). Members earn points for lesson completion, posting, events, etc. Custom badges + achievement-triggered workflows.

## 6. Analytics (`/settings/analytics`)
- Sub-sections: **Overview · Members · Website · Spaces · Posts & comments · Messages · Devices · Events · Payments · Courses**. **CSV export** available.
- Overview KPIs: total/active/inactive members, MAU, daily-active, invitations pending, **Activity scores**.
- **Course-completion analytics exist in-UI + CSV export — but NOT via REST API** (the gap that breaks a Pulse-style poll).

## 7. Monetization
- **Paywalls** (`/settings/paywalls`): Stripe-based. Sub-areas: Paywalls · **Coupons · Subscription groups · Subscriptions · Transactions · Taxes · Export logs**. Gate community / course / spaces; share checkout links. (Lyzr courses are free → Stripe not connected.)
- **Affiliates** (`/settings/affiliates_settings`): built-in affiliate program — Affiliates · Commissions · Settings (commission rates, tracking script), Stripe payouts.

## 8. Marketing / Email Hub (`/settings/emails`)
- **Broadcasts** (email editor, import contacts), **Forms** (sign-up/lead capture), audience + Settings. They've sent broadcasts incl. "Cohort 2", "Primer_course_certif…".

## 9. Automation — Workflows (`/settings/workflows`)
- **Automations · Bulk actions · Scheduled.** Triggers incl. member completed course / quiz passed-failed-submitted / joined / posted / tag added. Actions incl. email/DM, add/remove space, add tag, push, **send webhook** (Plus). Plan-gated limits (advanced workflows = Business+).

## 10. AI / "Circle Eclipse" (new — gated on current plan)
- **Community AI** (`/settings/community_ai`) — content brainstorm/repurpose, event transcription, member insights. **Gated to Business+** (not active on Lyzr's plan).
- **AI Agents** (`/settings/ai-agents`) — **Knowledge** (Community / Custom knowledge bases, filter by space group) + **Agents** (build custom community AI agents). Lyzr has a default **"Lyzr Academy agent"** (Active: Off, 0 conversations). "New agent" / "Edit agent".
- **Discover** + **Studios** — surfaced in the Eclipse banner (Discover = cross-community discovery at discover.circle.so); not deep-dived.

## 11. Audience / member management (`/audience/manage`)
- **Manage audience · Access groups · Connections · Segments · Bulk logs · Invite links · Onboarding · Tags · Profile fields · Gamification · Activity logs.**
- Per-member: role, email-marketing opt-in, **Activity score**, invitation status. Bulk actions, save segments.

## 12. Content / Files (`/settings/files`)
- **Media** (All/Videos/Recordings/Audio/Images/Files — 200GB) · **Posts · Pages** (CMS-style custom pages) · **Spaces · Topics · Moderation · Live · Bulk logs.**

## 13. Site / branding (`/settings/home`)
- **Navigation · SEO · Redirects · Defaults** (enable Feed, default landing space for new/existing members) **· Code snippets** (custom JS/HTML injection — viable host for an Accredible cert widget or external analytics).

## 14. Platform / general settings
- **General** (community name "Lyzr Academy", language, **Community ID 225567**, visibility) · **Custom domain** (academy.lyzr.ai) · **Mobile app** (members use Circle's iOS/Android app; white-label branded app = Plus tier; reorder home tabs) · **Weekly digest** · **Embed** (embed community in your site) · **Single sign-on** (OAuth SSO; surfaces the **Headless API**, Business+) · **Connect** (member directory + networking, not API) · **Legal.**

## 15. Plans & pricing (live, `/settings/plans`)
- **Professional** — current (entry: courses, quizzes, gamification).
- **Business — $219/mo monthly ($199/mo annual)** — Community AI, advanced workflows, **Admin + Headless API**, branded emails, integrations.
- **Plus — from $649/mo** — full feature access, highest limits, optional **branded mobile apps**.
- (No separate public "Enterprise" tier surfaced in-app, unlike some third-party write-ups.)

---

## What this changes vs the desk-research report
- **Tier corrected:** Lyzr is on **Professional**, NOT Business+ (earlier inferred from the working API token). Many migration-relevant features (Community AI, advanced workflows, Headless API, webhook action for the cert workaround) require **upgrading to Business or Plus**.
- **Pricing corrected:** Business **$219/mo** (not $199), Plus **from $649/mo** (not "custom"); no public Enterprise tier in-app.
- **Quiz media:** questions DO support video/image (research said "no media-based") — but still MCQ-only, no rubrics/essays.
- **Completion analytics:** confirmed they exist **in-UI + CSV**, just not via REST API.
- **Audience reality:** the builders the team wants are already here — **3,224 members / 7,221 contacts** vs the Thinkific University's 88 learners — but engagement is thin (6% MAU).
