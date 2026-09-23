# Circle Sunset Plan — consolidate to Thinkific (LMS) + Discord (community)

**Date:** 2026-06-29 · **Status:** Proposal (exploration) · **Companion to:** `Circle-vs-Thinkific-Evaluation.md`

## Why
The platform evaluation concluded Lyzr University's credentialed catalogue stays on **Thinkific**. This plan
takes the next step: **sunset Circle entirely** and consolidate to two surfaces — **Thinkific for courses/LMS**
and **Discord for community**. This matches the model Agentpreneur already chose ("Thinkific-only, no Circle")
and the Lyzr **Discord** that DevRel already runs, removes a parallel platform + its direct cost, and ends the
split between a Thinkific University and a separate Circle community.

## The reframe (read this first)
You **cannot bulk-move members** between platforms — accounts don't port. A sunset is **(a) preserve the
audience list, (b) redirect course + community traffic, (c) decommission Circle** — *not* a member migration.
And Circle's engagement is ~**6% MAU**: the 3,224 "members" are largely a **dormant imported email list**
(Bulk Logs shows the audience was built by repeated CSV imports). So:
- Realistic outcome = keep the **active core (~200)** + whatever the email campaign re-converts. The dormant
  majority won't follow — but they're already dormant.
- Manage expectations: Discord will show your **true** active size, which is smaller than Circle's vanity count.

## What's on Circle → where it goes
| Circle asset | Destination | Mechanic |
|---|---|---|
| **5 courses** (~30 sections / ~77 lessons / 21.8 GB media): Lyzr Primer · Developer's · Agent Architect · Gen AI Stack (Enterprise Leaders) · Recorded Sessions (July) *(verify: "Lyzr Agent Studio 101" + "Handbooks" space types)* | **Thinkific** | re-upload via the existing `thinkific-uploader`; much source content already owned (Descript / local recordings) |
| **Community** (feed, spaces, posts, events) | **Discord** | new channels mirror Circle spaces; Circle events → Discord events/scheduled; no content port (start fresh) |
| **Gamification** (points / 9 levels / leaderboard) | **Discord bots** (MEE6, Lurkr, etc.) | re-create; resets |
| **Audience** (7,727 people / 7,221 contacts / 3,224 members) | **Both** | **Export CSV** (✅ available, triggered 2026-06-29 — emailed to admin) → import to Thinkific + email-invite to Discord |
| **Email Hub** (broadcasts, forms) | **Thinkific email / a dedicated ESP** | Circle's email goes away |
| **Paywalls / Affiliates** | — | unused (free courses, Stripe not connected) — nothing to migrate |

## Sequencing (phase-wise)
**Phase 1 — Preserve the assets (do first, before touching anything).**
- ✅ Export the full audience CSV (done — confirm the emailed file arrived; it carries name/email/opt-in/score/role/invitation-status for 7.7k people).
- Inventory + download Circle course media (200 GB library; cross-check against source content already held in Descript/local so you only re-pull what's Circle-only).
- Export any community content worth keeping (key posts/resources) — most is disposable.

**Phase 2 — Stand up the destinations.**
- **Discord:** build the channel structure to absorb the community (mirror the live Circle spaces — e.g. announcements, build-help, expert-sessions, per-course discussion); set moderation + a gamification bot; confirm DevRel owns it.
- **Thinkific:** confirm which courses land (see Decisions) and rebuild them via the uploader pipeline.

**Phase 3 — Announce + redirect.**
- Email the exported list: *"Lyzr Academy is moving — courses → university.lyzr.ai (Thinkific), community → Discord (invite link)."* Segment by active vs dormant; expect low dormant conversion.
- Put a banner on Circle pointing to both destinations.
- Set `academy.lyzr.ai` redirects (course URLs → Thinkific equivalents; community → Discord invite) so existing links don't die.

**Phase 4 — Grace period.**
- Run Circle (read-only / frozen) in parallel with the new homes so stragglers migrate. No new content on Circle.

**Phase 5 — Sunset.**
- Cancel the Circle subscription; repoint/retire the `academy.lyzr.ai` domain. Keep the exported CSV + content archive.

## Gains vs costs
- **Gain:** end the Circle subscription (direct cost saved); one LMS + one community; aligns with the existing Thinkific-only + Discord model; simpler stack.
- **Cost/loss:** integrated courses-in-community UX splits into two destinations; gamification continuity resets; content re-hosting effort for the kept courses; the membership headline number drops to its real (smaller) active size; redirect/SEO cleanup for `academy.lyzr.ai`.

## Risks
- **Asset loss if Phase 1 is skipped** — never decommission before the audience CSV + content are safely exported. (Mitigated: export already triggered.)
- **Live-cohort disruption** — if any cohort is currently *running* on Circle, freezing it mid-flight breaks the learner experience. Confirm before announcing.
- **Discord readiness** — if the Discord isn't structured/moderated to absorb the community, the move lands badly.
- **Attrition optics** — leadership should expect the active count to look small post-move (it always was).

## Open decisions (need Harshit)
1. **Which of the 5 courses migrate to Thinkific** — all, or only the evergreen ones (Primer, Developer's, Agent Architect) and retire the dated "Recorded Sessions (July)" / webinar content?
2. **Any live cohort currently on Circle** that a freeze would disrupt? (timing gate)
3. **Is the Lyzr Discord ready** to absorb the community, or does DevRel build out structure + bots first?
4. **Email/marketing home** — move broadcasts to Thinkific, or stand up a dedicated ESP for the 7.2k list?

## What this does NOT touch
This is about **where Lyzr University's catalogue + community live**, not the curriculum itself. The SDK/Studio
Track content and the cert ladder are unaffected — they already live on Thinkific. The Circle community's 5
courses are largely cohort/webinar recordings, a separate (and re-homeable) body of content.
