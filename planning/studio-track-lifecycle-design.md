# Studio Track — Agent-Lifecycle design (decision record)

**Date:** 2026-06-02 · **Status:** approved, implemented in `catalog-data.json` + bundle + tracker.

## Problem
The Studio Track was organized by feature clusters (101/201/401 spine + 9 deep-dives). It didn't answer the questions a builder actually asks — *"what agent type do I pick? then what?"* — and the framing didn't match how agents are actually shipped.

## Decision
Re-cast the Studio Track around the **agent lifecycle**: **Build → Govern → Test → Deploy → Monitor** (Govern deliberately before Test/Deploy — set guardrails before shipping).

Because a literal 5-stage split is lopsided (Build = ~22 of ~40 screens; Test/Deploy/Monitor tiny), the lifecycle is **rebalanced into 6 phases** of ~9–13 lessons, with a **Foundations journey course** on top.

- **Foundations — The Agent Lifecycle** (7): one agent, all the way through the loop. Answers the builder's questions end to end.
- **Phase 1 · Design & Create** (11): Choosing & Building Agents · Orchestration & Multi-Agent
- **Phase 2 · Equip & Connect** (10): Tools, Models & MCP · Voice Agents
- **Phase 3 · Ground in Knowledge** (11): Knowledge & RAG · Knowledge Graph & Semantic Model
- **Phase 4 · Govern** (10): Responsible AI & Guardrails · Policies, Access & Org Governance
- **Phase 5 · Test & Improve** (9): Test & Simulate · Evaluate & Improve
- **Phase 6 · Deploy & Operate** (13): Deploy & Scale · Monitor & Observe · Reuse & Distribute

**14 courses · 71 lessons.**

## Principles
- **Levels retired** — no 101/201/401; the lifecycle phase is the only top axis (`level` field carries the phase).
- **Lesson-level coverage** — every lesson is tagged with the **Studio feature/tab** it teaches (`feature` field in the syllabus). 41/41 nav screens appear as a primary feature; zero orphans. This is the verifiable coverage contract.
- **Every lesson has a description** (`summary` field).
- **Capstone projects kept** — each depth course ends in a build-along; Foundations ends in a full-lifecycle project.
- **Build is genuinely the biggest part of the lifecycle**, so it spans 3 balanced phases (Create · Equip · Ground) rather than one jumbo course.

## How it maps to the user's 5 steps
Build → Phases 1–3 · Govern → Phase 4 · Test → Phase 5 · Deploy + Monitor → Phase 6 (with reuse/distribution folded in).

## Artifacts
- `catalog-demo/catalog-data.json` — 14 Studio courses, syllabus lessons = `{n, title, feature, summary}`.
- `planning/studio-track-plan.md` — full course/lesson tables + coverage matrix.
- `planning/studio-track-production-plan.md` — objectives, minutes, pipeline, week schedule.
- `planning/master-tracker.xlsx` — single-tab Studio lesson tracker (71 rows).
- `planning/master-tracker-replacement.md` — same as a paste-ready markdown table.
- `thinkific-upload/` — folders 06–19 (Studio), downstream renumbered.

## Supersedes
The 101/201/401 spine + deep-dive model (the earlier `studio-track-plan.md` revision). The feature map (`studio-feature-map.md`) is unchanged — still the surface of record.
