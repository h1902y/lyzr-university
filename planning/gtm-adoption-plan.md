# Lyzr University — GTM & Adoption Engine

> **Strategy of record for distribution.** `content-strategy.md` owns *what we teach*; this doc owns *how people find it, finish it, and bring the next learner*. Drafted 2026-06-11. Phase-wise by design — no calendar commitments; a phase ends when its exit criteria are met.

---

## 1 · The engine in one picture

Every surface feeds one loop; every phase lights the loop in a new, larger audience ring.

```
            ┌────────────── THE LOOP ──────────────┐
            │                                      │
        discover ──→ enroll ──→ complete ──→ certify
            ▲                                      │
            └────────────── share ←────────────────┘

   Ring 1 · Captive      Agentpreneur cohort · partners · support
   Ring 2 · Customers    in-product · lifecycle email · official channels
   Ring 3 · Open market  cert-share loop · project gallery · landing page
```

**Why rings, not a launch?** A launch is a spike; an engine is a loop that compounds. Ring 1 needs nobody's permission and proves the loop works on people we already reach. Ring 2 takes that proof to the product and marketing teams as evidence, not a pitch. Ring 3 is where the loop pays for itself — every certificate shared on LinkedIn is a discovery surface we didn't build.

**Where it stands today (baseline, 2026-06-11):** 4 ADK courses live on university.lyzr.ai, Studio Foundations packaged and ready to upload, 12 of 26 Agentpreneur members enrolled — all of it driven by manual 1:1 outreach. That is the gap this engine closes: adoption currently scales with founder hours, not with surfaces.

---

## 2 · The loop — stages and metrics

One owner-metric per stage. All four map onto the existing snapshot ritual (`planning/weekly-metrics/` — template metrics #1–#6); nothing new to build, only a source split to add.

| Stage | What it means | Owner metric | Pulled from |
|---|---|---|---|
| **Discover** | Someone lands on a course page | New enrollments **by source** | Template #2 + UTM split (§7) |
| **Enroll** | They actually start | First-lesson engagement (inverse of "not-engaged enrollments") | Template optional metric |
| **Complete / Certify** | They finish and earn the credential | Completion rate · certificates issued | Template #4 · #6 |
| **Share** | The credential travels | Cert/project shares sighted on LinkedIn | Manual count (no API — same constraint as SOCIAL.md) |

**Why one metric per stage:** more than one and nobody knows which number is the job. The stage metric is the tiebreaker when prioritizing surface work inside a phase.

---

## 3 · Ring 1 — Captive (Phase 1)

Audiences we already control. **Zero external buy-in needed; every item here is self-serve.** Exit criteria: all four surfaces live + the loop measured end-to-end at least once on real learners.

| Surface | The move | Why it works |
|---|---|---|
| **Agentpreneur journey** | Make University lessons a required artifact in the 30-day member dashboard journey (specific lessons per sprint, not "go browse") | Closes the 12/26 gap structurally — enrollment becomes a journey step, not a favor. The cohort is also the loop's test lab: 26 known learners to measure discover→share on. |
| **Partner certification requirement** | Bake "N certified builders per partner" into partner tier criteria; put the relevant courses in the partner onboarding kit (portal already maps assets per phase) | Creates *obligated* enrollments, not hoped-for ones — partners push their own teams through because their tier depends on it. The only Ring-1 surface that scales headcount we don't employ. |
| **Support macros** | Canned support replies answer with the *specific lesson* for the screen in question — the Studio Track's 41/41 screen→lesson map is the enabling asset | Reaches users at the exact moment of confusion, and gives the support team a ticket-deflection win to champion — which is the evidence Ring 2's product ask leans on. |
| **Own LinkedIn (per `SOCIAL.md`)** | University milestones are standing P1 material (Mon slot); course frameworks/checklists are P2 save-bait; Studio Foundations going live is the first post | Already-committed cadence; University just supplies the ammunition. No new channel to run. |

---

## 4 · Ring 2 — Customer base (Phase 2)

The Lyzr customer base, reached through surfaces owned by the product and marketing teams. **Needs two buy-ins (§6).** Entry criteria: Ring 1 live and producing the numbers the asks cite. Exit criteria: in-product links live + lifecycle email running + University in the site nav.

**In-product (product-team surfaces) — the strongest structural channel in the whole engine:**

- **Contextual "learn this screen" links** — every Agent Studio screen deep-links to its lesson. The 41/41 mapping already exists in `planning/studio-track-plan.md`; this is a content lookup table for the product team, not a content project. Reaches users *inside the moment of need*, which no campaign can do.
- **Onboarding checklist item** — "Watch the Foundations course (7 lessons, ~56 min)" as a step in Studio's new-user onboarding. New users are the highest-intent learners we will ever have.
- **Docs cross-links** — each docs page links to its corresponding course. Cheap, and docs are where stuck users already go.

**Lifecycle email (marketing-team surface):**

- **Footers everywhere** — University link in the standing footer of sign-up, welcome, and other key transactional emails. Low CTR individually; the point is ambient presence.
- **One dedicated onboarding email** — "your learning path: from blank page to a deployed agent" shortly after sign-up. A real email beats ten footers; the footer is the reminder, this is the pitch.
- **Behavior-triggered sends** — first agent created → "go deeper" course email; gone quiet → re-engagement via a course rather than a feature pitch. Triggered email converts on intent, calendar email converts on luck.

**Marketing site + official channels (marketing-team surfaces):**

- **Nav + footer links** — University as a standing item on lyzr.ai (nav under Resources, plus footer). Permanent discovery, zero maintenance.
- **Recurring newsletter section** — "New in Lyzr University" as a standing slot, not a one-off announcement. 14 Studio courses are coming; every one gets distribution automatically instead of re-pitching each time.
- **Leader-amplified launch post** — packaged as a mini comms kit: 2–3 pre-written post variants + course banner images (already generated in `catalog-demo/banner/exports/`) so leaders post in one click. Ask for *original posts*, not reshares — originals reach far more. Ignition moment: Studio Foundations going live (§8).

---

## 5 · Ring 3 — Open market (Phase 3)

Learners with no prior Lyzr relationship. Entry criteria: completion volume from Rings 1–2 (the loop has nothing to share until people finish courses). This ring is mostly *unlocking compounding*, not adding channels:

- **Cert-share loop** — Thinkific completion certificates, branded (light variant, per `agentpreneur/lyzr-brand.md`), with a share-to-LinkedIn prompt at the moment of completion. Every graduate becomes a discovery surface. This is the only channel in the engine that grows with output rather than effort.
- **Learner project gallery** — capstone projects (every Track course ends in one) published as a public gallery; "look what I built" travels further than "I took a course," and gives the cert-share post something concrete to point at.
- **University landing page live** — the destination for all the shared links; copy already drafted in `landing/academy.md` (needs an Academy→University pass before shipping).

**Explicitly deferred:** paid acquisition, SEO content, YouTube clips. Decided out of scope 2026-06-11 — the captive and customer rings are nowhere near saturated, and open-web channels have real direct cost and ongoing upkeep. Revisit only if Ring 3's organic loop plateaus.

---

## 6 · Buy-in asks

Two asks, framed as "here's what we'd like to try, thoughts?" — both arrive carrying Ring-1 evidence, not projections.

**To the product team (Agent Studio):**
> We've mapped all 41 Studio screens to a free University lesson and support is already using the mapping to answer tickets. We'd love to surface it in-product — a "learn this screen" link per surface and a Foundations step in new-user onboarding. We have the full screen→lesson table ready; happy to start with just one or two screens to see if it moves anything. Thoughts?

**To the marketing team:**
> Lyzr University is live at university.lyzr.ai with five courses and learners from the Agentpreneur cohort and partner teams already going through it. Three things would help it reach the rest of our audience: a nav/footer link on the site, a recurring "new in University" slot in the newsletter, and — for the Studio course launch — a small comms kit we've prepared so leaders can post about it. Open to whatever subset makes sense. Thoughts?

**Why the humble shape:** these teams own their surfaces; the engine borrows them. Evidence-first, small-start, easy to say yes to a piece of.

---

## 7 · Instrumentation

- **UTM scheme** — every surface gets a distinct tag so the Discover metric splits by source. Convention: `utm_source` = surface (`studio-app` · `docs` · `lifecycle-email` · `newsletter` · `lyzr-site` · `linkedin` · `partner-portal` · `agentpreneur-app` · `support`), `utm_medium` = `referral`/`email`/`social`, `utm_campaign` = course slug for launch pushes. Links without tags are links we can't learn from.
- **Snapshot ritual** — the existing `planning/weekly-metrics/` template already covers metrics #1–#6; add a per-source enrollment split to the Read once UTMs flow. LinkedIn shares stay a manual count (no API).
- **Master Tracker** — course go-lives keep flowing through the existing tracker; this doc doesn't duplicate operational state.

---

## 8 · Phase-1 checklist (the concrete first moves)

The ignition moment is **Studio Foundations going live** — it's packaged and upload-ready, and it's the first course the whole customer base (not just developers) can take.

1. Upload Studio Foundations to Thinkific; flip `catalog-data.json` to `live`; update Master Tracker.
2. Add University lessons as required artifacts in the Agentpreneur 30-day journey (map specific lessons to sprints).
3. Draft the partner certification requirement and place courses in the partner onboarding kit (coordinate in `partners/` — partner tasks stay out of Linear).
4. Write the support macro set from the screen→lesson map; hand to the support team with the deflection pitch.
5. Publish the launch LinkedIn post (P1 slot per `SOCIAL.md`); prepare the leader comms kit alongside it so it's ready the moment marketing says yes.
6. Apply UTM tags to every link shipped in 1–5; confirm the source split shows up in the next metrics snapshot.
7. Send the two buy-in asks (§6) once 1–4 are live and the first numbers exist.

**Phase-1 exit:** all seven done + one full metrics snapshot showing the loop measured end-to-end. Then Ring 2 opens.
