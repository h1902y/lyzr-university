# 🏛️ Lyzr Agent Studio: Operations, Governance & FinOps

> **Course Title:** `Lyzr Agent Studio: Operations, Governance & FinOps` (or `Studio Operations Trio`)  
> **LMS Category / Track:** `1 - Tracks / Studio`  
> **Thinkific Categories to Tag:** `Track` · `Studio` · `Voice` · `Administration` · `Responsible AI` · `Deployment`  
> **Thinkific Course ID:** Draft (New Studio Course)  
> **Curriculum Structure:** **3 Chapters** · **3 Lessons** (1 Video MP4 + 1 Formatted Plain Text Block per lesson)  
> **Total Video Runtime:** **11 minutes 46 seconds** (707s across 3 core operational masterclasses)  
> **Target Audience:** Enterprise Solutions Architects, AI Engineers, Team Leads, and Platform Administrators  
> **Default Status:** `Draft` (Publish upon video and text block verification)  

---

## 📋 High-Level Master Syllabus Table

| # | Chapter | Lesson Title | Duration | Descript Source | Video Filename |
|---|---|---|---|---|---|
| **01** | Chapter 01: Voice Agents & Telephony Integration | Voice Agents End-to-End | 4m 37s | [Descript: Voice Agents](https://share.descript.com/view/ROHvTW1ydE2) | `01a Voice Agents End-to-End.mp4` |
| **02** | Chapter 02: Team Administration & Access Governance | Teams & Access | 3m 00s | [Descript: Teams & Access](https://share.descript.com/view/fPcphjLKUE2) | `02a Teams and Access.mp4` |
| **03** | Chapter 03: Production FinOps & Cost Optimization | FinOps | 4m 09s | [Descript: FinOps](https://share.descript.com/view/cx6t3YALzxG) | `03a FinOps.mp4` |

---

## 🛠️ Step-by-Step Thinkific Course Creation Guide

> [!TIP]
> **Thinkific Builder Instructions:**
> 1. Create **3 Chapters** in Thinkific corresponding to the 3 Chapters below.
> 2. For each lesson, copy the **Lesson Title** and attach/upload the corresponding video (`NNa <Title>.mp4`).
> 3. In the lesson body, paste the formatted text block below into Thinkific's **Text Block**.
> *(Text is formatted cleanly with plain-text bullet points and headers without raw markdown syntax to prevent rendering glitches in Thinkific).*

================================================================================
### 📂 Chapter 01: Voice Agents & Telephony Integration
**Chapter Name to Copy:** `📂 Chapter 01: Voice Agents & Telephony Integration`
================================================================================

#### 📖 Lesson 01: Voice Agents End-to-End
- **Lesson Title to Copy:** `📖 Lesson 01: Voice Agents End-to-End`
- **Video Filename:** `01a Voice Agents End-to-End.mp4`
- **Duration:** 4m 37s (277 seconds)
- **Descript Source:** [https://share.descript.com/view/ROHvTW1ydE2](https://share.descript.com/view/ROHvTW1ydE2)
- **Suggested Handout:** `01b Voice Agents End-to-End Notes.pdf`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Understand the architecture and capabilities of Lyzr Studio Voice Agents.
• Contrast Realtime voice models with modular Pipeline engines (STT, LLM, TTS).
• Test conversational speech, interruption handling, and speech parameter extraction in Playground.
• Deploy voice agents to live telephony carriers (Twilio) and inspect turn-by-turn call logs.

OVERVIEW
Every agent built so far lives in a chat box, but a massive share of real-world enterprise conversations happen on the phone—customer support lines, appointment scheduling, and automated outbound follow-ups. In this masterclass, we give a Lyzr Agent Studio agent a voice and a phone number, test it in the interactive Playground, wire it to an enterprise carrier, and inspect live call analytics.

STEP-BY-STEP WALKTHROUGH
1. Navigate to Create Agent and select Voice Agent. Configure Role, Goal, and Instructions identically to standard Studio agents.
2. Choose First Speaker: Select AI to deliver an immediate opening greeting on inbound customer support calls.
3. Select the Voice Engine: Choose Realtime for lowest latency and unified speech processing, or Pipeline to independently configure Speech-to-Text, LLM models, and multi-provider TTS voice libraries.
4. Toggle Call Settings: Enable audio recording for compliance transcripts and turn on active background noise cancellation.
5. Attach Agent Resources: Equip the voice agent with relevant Knowledge Bases, external tools, manager delegations, and human escalation rules.
6. Test in Voice Playground: Click Start Voice Call to verify speech recognition, automatic field extraction (e.g. order numbers), and natural interruption handling.
7. Connect Telephony: Integrate Twilio using your Account SID and encrypted Auth Token under Telephony Integrations.
8. Bind Phone Numbers: Map carrier phone numbers to your voice agent for inbound call answering and automated outbound outreach.
9. Audit Call Transcripts: Inspect session history to review turn-by-turn timestamps, transition latencies, and disconnect reasons.

KEY TAKEAWAYS
• Voice agents use the same instruction, knowledge, and tool architecture as chat agents—zero separate platform learning required.
• Realtime delivers speed; Pipeline delivers granular provider and voice customization.
• Automatic interruption handling and complete turn-by-turn transcript logs make voice deployment secure and auditable.
```

---

================================================================================
### 📂 Chapter 02: Team Administration & Access Governance
**Chapter Name to Copy:** `📂 Chapter 02: Team Administration & Access Governance`
================================================================================

#### 📖 Lesson 02: Teams & Access
- **Lesson Title to Copy:** `📖 Lesson 02: Teams & Access`
- **Video Filename:** `02a Teams and Access.mp4`
- **Duration:** 3m 00s (180 seconds)
- **Descript Source:** [https://share.descript.com/view/fPcphjLKUE2](https://share.descript.com/view/fPcphjLKUE2)
- **Suggested Handout:** `02b Teams and Access Notes.pdf`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Understand the 3 fundamental organizational roles: Owner, Admin, and Member.
• Manage team rosters, invite members in batches, and review permission matrix safeguards.
• Scale resource access and knowledge base sharing using Organizational Groups.
• Audit enterprise actions and track security events using comprehensive Audit Logs.

OVERVIEW
Building alone in your Studio lasts about a week before colleagues need to edit agents, teams need access to shared knowledge bases, and security teams require full auditability. This lesson covers how Lyzr Agent Studio scales across an enterprise team with robust role-based access control, grouped sharing, and immutable audit logs.

STEP-BY-STEP WALKTHROUGH
1. Access Manage Organization from your user avatar menu to review organization plan status, credit balance, and member counts.
2. Understand Role Boundaries: Owner (single account holder managing billing and admin removal), Admin (team management, reports, and audit logs), and Member (active builders).
3. Review Team Analytics: View aggregated credits, runs, and token consumption per team member over customizable timeframes, and export data directly to CSV.
4. Batch Invite Members: Select Member or Admin, paste comma-separated email addresses, and inspect the live permissions matrix preview before dispatching invites.
5. Configure Resource Groups: Create functional groups (e.g. Support, Finance) to share collections of agents and knowledge bases automatically with current and future team members.
6. Inspect Audit Logs: Filter security and operational events by date range, user, action, resource type, and success outcome to resolve compliance and change-management questions instantly.

KEY TAKEAWAYS
• Establish clear role definitions on paper before issuing invitations (one Owner, several Admins, mostly Members).
• Organizational Groups eliminate repetitive manual resource sharing as teams grow.
• Audit Logs transform security investigations into instant, filterable queries.
```

---

================================================================================
### 📂 Chapter 03: Production FinOps & Cost Optimization
**Chapter Name to Copy:** `📂 Chapter 03: Production FinOps & Cost Optimization`
================================================================================

#### 📖 Lesson 03: FinOps
- **Lesson Title to Copy:** `📖 Lesson 03: FinOps`
- **Video Filename:** `03a FinOps.mp4`
- **Duration:** 4m 09s (249 seconds)
- **Descript Source:** [https://share.descript.com/view/cx6t3YALzxG](https://share.descript.com/view/cx6t3YALzxG)
- **Suggested Handout:** `03b FinOps Notes.pdf`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Understand Lyzr's Agent Processing Credit (APC) consumption model and billing cycles.
• Track credit and token expenditure per member, agent, and billing cycle with CSV exports.
• Enforce Rate Limits (the ceiling) on organizations, sub-organizations, agents, and users.
• Deploy LLM Routing (the thermostat) across 4 query complexity tiers to maximize cost efficiency.

OVERVIEW
The question that kills more enterprise AI initiatives than any bug is: What is this going to cost us next month? This masterclass covers the operational side of AI FinOps—where credits show up, who is consuming them, and how to utilize rate limit ceilings and multi-tier LLM routing thermostats to maintain predictable, cost-effective agent deployments.

STEP-BY-STEP WALKTHROUGH
1. Review Credit Structure: Understand monthly plan allocations (resetting on cycle dates) versus non-expiring top-up credits.
2. Audit Spend by Person: Navigate to Team to inspect credit, run, and token consumption per person, and export reports for finance teams.
3. Track Historical Usage: Analyze billing cycle trends and daily consumption charts via the Usage dashboard.
4. Implement Rate Limits (The Ceiling): Set hard credit and token caps per hour, day, or month across organizations, sub-orgs, individual agents, or users to prevent runaway loops.
5. Use Zero Caps for Instant Pausing: Apply a zero-credit limit to temporarily disable agent execution without deleting configurations.
6. Configure LLM Routing (The Thermostat): Assign cost-appropriate models across 4 complexity tiers (Simple, Medium, Complex, Reasoning) to automate cost-efficient inference.
7. Configure Fallback Models: Equip agents with secondary provider fallback models in agent settings to eliminate retries and downtime during vendor outages.
8. Analyze Traces & Observability: Trace cost spikes to specific agents, executions, and spans using monitoring dashboards.

KEY TAKEAWAYS
• APC pricing delivers transparent forecasting: Runs multiplied by Agent Tier.
• Rate limits provide bulletproof ceilings against infinite loops and testing spikes.
• LLM routing is the single largest operational cost-saver, matching query complexity directly to model price tiers.
```

---
