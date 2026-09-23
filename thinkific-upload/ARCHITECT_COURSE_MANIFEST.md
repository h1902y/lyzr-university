# 🏛️ Lyzr Architect: Complete Master Course Manifest

> **Course Title:** `Architect Fundamentals` (or `Lyzr Architect: From Prototype to Production`)  
> **LMS Category / Track:** `1 - Tracks / Architect`  
> **Thinkific Course ID:** `#3489969` (Draft)  
> **Descript Source Recording:** [AR 03 — Vendor Renewal Desk](https://share.descript.com/view/D3JR0UMPLL6)  
> **Total Lessons:** 10 Lessons across 4 Chapters  
> **Total Video Runtime:** 12 minutes 45 seconds (445.8 MB total payload)  
> **Media Directory on Disk:** `university/thinkific-upload/1 - Tracks/Architect/20 Architect Fundamentals/`  

---

## 📋 High-Level Syllabus & Video Assets

| # | Chapter | Lesson Title | Duration | Size | Video Filename |
|---|---|---|---|---|---|
| **01** | Chapter 01: Overview & The Three Acts | Welcome & The Three Acts Roadmap | 1m 27s | 34.1 MB | `01a Welcome & The Three Acts Roadmap.mp4` |
| **02** | Chapter 02: Act 1 — Feed It (Knowledge, Data & Artifacts) | Knowledge Bases & PDF Contract Ingestion | 1m 24s | 45.4 MB | `02a Knowledge Bases & PDF Contract Ingestion.mp4` |
| **03** | Chapter 02: Act 1 — Feed It (Knowledge, Data & Artifacts) | Workspace Database & Data Persistence | 0m 38s | 44.3 MB | `03a Workspace Database & Data Persistence.mp4` |
| **04** | Chapter 02: Act 1 — Feed It (Knowledge, Data & Artifacts) | Generating Application Artifacts & Documents | 0m 59s | 40.8 MB | `04a Generating Application Artifacts & Documents.mp4` |
| **05** | Chapter 03: Act 2 — Connect It (Tools, Integrations & MCP) | The Integrations Catalog & Gmail Actions | 2m 11s | 63.0 MB | `05a The Integrations Catalog & Gmail Actions.mp4` |
| **06** | Chapter 03: Act 2 — Connect It (Tools, Integrations & MCP) | The Human-in-the-Loop Approval Gate | 0m 17s | 28.7 MB | `06a The Human-in-the-Loop Approval Gate.mp4` |
| **07** | Chapter 03: Act 2 — Connect It (Tools, Integrations & MCP) | Beyond the Catalog - MCP Servers & Custom APIs | 1m 30s | 62.1 MB | `07a Beyond the Catalog - MCP Servers & Custom APIs.mp4` |
| **08** | Chapter 04: Act 3 — Ship It (Production, Sharing & Governance) | One-Click Cloud Deployment & Sharing Doors | 1m 53s | 50.6 MB | `08a One-Click Cloud Deployment & Sharing Doors.mp4` |
| **09** | Chapter 04: Act 3 — Ship It (Production, Sharing & Governance) | Eject to Code - GitHub Sync & Full-Stack Next.js | 0m 40s | 39.4 MB | `09a Eject to Code - GitHub Sync & Full-Stack Next.js.mp4` |
| **10** | Chapter 04: Act 3 — Ship It (Production, Sharing & Governance) | Enterprise Guardrails, Credit Habits & Wrap-up | 1m 46s | 44.3 MB | `10a Enterprise Guardrails, Credit Habits & Wrap-up.mp4` |

---

## 🛠️ Step-by-Step Thinkific Course Creation Guide

> [!TIP]
> **How to build each lesson in Thinkific:**
> 1. In Thinkific Course Builder, create the **Chapter** using the exact name below.
> 2. Add a new **Video Lesson** or **Multimedia Lesson**.
> 3. Upload the corresponding `.mp4` file from `university/thinkific-upload/1 - Tracks/Architect/20 Architect Fundamentals/`.
> 4. In the lesson text area, copy and paste the formatted text block directly (formatted for clean LMS rendering without raw markdown issues).


================================================================================
### 📂 Chapter 01: Overview & The Three Acts
**Chapter Name to Copy:** `📂 Chapter 01: Overview & The Three Acts`

================================================================================

#### 📖 Lesson 01: Welcome & The Three Acts Roadmap
- **Lesson Title to Copy:** `📖 Lesson 01: Welcome & The Three Acts Roadmap`
- **Video Filename:** `01a Welcome & The Three Acts Roadmap.mp4`
- **Duration & Size:** 1m 27s (86.8s) · 34.1 MB
- **Descript Cut Range:** `00:00.07 to 01:26.85`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Understand the shift from rapid local prototyping to team-ready production software.
• Master the overarching Three Acts framework: Feed It, Connect It, and Ship It.
• Explore how Lyzr Architect builds full-stack applications with real enterprise agents.

OVERVIEW
Moving an AI application from a prototype on your personal screen to a production tool for your organization requires three distinct phases: feeding it private company data and documents, connecting it to enterprise tools and external APIs, and deploying it with security, observability, and cost guardrails. In this orientation, we lay out the roadmap using a real-world Vendor Renewal Desk application.

STEP-BY-STEP WALKTHROUGH
1. Access the Vendor Renewal Desk workspace in Lyzr Architect.
2. Review the three-act roadmap: Feed It (Knowledge & Artifacts), Connect It (Integrations & MCP), and Ship It (Deploy & Code Export).
3. Identify the current limitations of basic prompt-only agents (working from static pasted clauses vs. dynamic live data).

KEY TAKEAWAYS
• Production applications must graduate beyond prompt-only demos into grounded, integrated workflows.
• The Three Acts (Feed, Connect, Ship) provide a predictable playbook for taking any Architect app live.
```

---


================================================================================
### 📂 Chapter 02: Act 1 — Feed It (Knowledge, Data & Artifacts)
**Chapter Name to Copy:** `📂 Chapter 02: Act 1 — Feed It (Knowledge, Data & Artifacts)`

================================================================================

#### 📖 Lesson 02: Knowledge Bases & PDF Contract Ingestion
- **Lesson Title to Copy:** `📖 Lesson 02: Knowledge Bases & PDF Contract Ingestion`
- **Video Filename:** `02a Knowledge Bases & PDF Contract Ingestion.mp4`
- **Duration & Size:** 1m 24s (84.3s) · 45.4 MB
- **Descript Cut Range:** `01:26.85 to 02:51.16`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Provision dedicated Knowledge Bases for agents via natural language prompt commands.
• Ingest multi-page PDF contracts containing complex terms, notice windows, and renewal clauses.
• Observe how agents quote verifiable document citations rather than hallucinating answers.

OVERVIEW
Enterprise agents must read authentic source material rather than rely on snippets pasted into prompt fields. In this lesson, we ask Architect in natural language to attach a Knowledge Base to our Cancellation Terms agent. We then upload three real-world vendor contracts as PDFs and inspect the agent's generated brief, confirming exact clause citations and auto-renew trap identification without configuring chunking or vector databases manually.

STEP-BY-STEP WALKTHROUGH
1. In the Architect build chat, enter the prompt: 'Give the cancellation terms agent a knowledge base of our contract PDFs. Let me attach PDFs to each vendor contract.'
2. Locate the newly generated 'Knowledge Bases Available' card in the left architectural pane.
3. Upload vendor contracts as multi-page PDFs directly to the vendor records.
4. Execute the agent and verify that the output analysis directly quotes clauses, termination penalties, and notice periods from the PDF.

KEY TAKEAWAYS
• Architect abstracts manual RAG setup—no manual vector databases, chunking parameters, or embedding model selection needed.
• Agents grounded in authentic PDFs produce verifiable, audit-proof contract briefs.
```

---

#### 📖 Lesson 03: Workspace Database & Data Persistence
- **Lesson Title to Copy:** `📖 Lesson 03: Workspace Database & Data Persistence`
- **Video Filename:** `03a Workspace Database & Data Persistence.mp4`
- **Duration & Size:** 0m 38s (38.1s) · 44.3 MB
- **Descript Cut Range:** `02:51.16 to 03:29.26`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Understand how Architect automatically provisions structured relational databases for your app.
• Inspect stored vendor profiles, contract terms, and historical agent outputs.
• Distinguish between unstructured knowledge (PDFs) and structured relational data (Postgres tables).

OVERVIEW
While Knowledge Bases handle unstructured documents, applications also require robust relational data persistence. Architect provisions and manages a structured database under the hood whenever you build an app. In this lesson, we inspect the Database tab to understand how vendor metadata, contract schemas, and agent executions are permanently recorded.

STEP-BY-STEP WALKTHROUGH
1. Navigate to the Database tab in the left-hand workspace navigation.
2. Inspect the automatically generated tables, schemas, and columns for vendor records.
3. Review how agent execution results are written back to relational records for auditability.

KEY TAKEAWAYS
• Architect applications are backed by real, persistent relational databases, not ephemeral session state.
• Unstructured document retrieval (RAG) and structured relational querying seamlessly coexist.
```

---

#### 📖 Lesson 04: Generating Application Artifacts & Documents
- **Lesson Title to Copy:** `📖 Lesson 04: Generating Application Artifacts & Documents`
- **Video Filename:** `04a Generating Application Artifacts & Documents.mp4`
- **Duration & Size:** 0m 59s (59.1s) · 40.8 MB
- **Descript Cut Range:** `03:29.26 to 04:28.30`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Direct Architect to produce formatted downstream business documents as Artifacts.
• Explore the four primary artifact types: feature specs, slide decks, research briefs, and Word/HTML files.
• Export generated artifacts for stakeholder review and executive sign-off.

OVERVIEW
Feeding an application documents is only half the equation—enterprise workflows require the application to produce polished, shareable documents in return. Architect introduces Artifacts, allowing agents to generate executive slide decks, comprehensive feature specifications, research summaries, and formatted Word/HTML documents directly from workspace context.

STEP-BY-STEP WALKTHROUGH
1. Prompt Architect to compile an executive renewal brief or technical specification.
2. Switch to the Artifacts tab adjacent to Database in the workspace navigation.
3. Review the generated artifact structure: overview, agent breakdown, database schema, and operational risks.
4. Export the artifact as a formatted PDF, DOCX, or presentation slide deck.

KEY TAKEAWAYS
• Artifacts turn raw agent reasoning into professional, shareable deliverables for non-technical stakeholders.
• Architect natively generates specs, decks, research briefs, and formatted documents.
```

---


================================================================================
### 📂 Chapter 03: Act 2 — Connect It (Tools, Integrations & MCP)
**Chapter Name to Copy:** `📂 Chapter 03: Act 2 — Connect It (Tools, Integrations & MCP)`

================================================================================

#### 📖 Lesson 05: The Integrations Catalog & Gmail Actions
- **Lesson Title to Copy:** `📖 Lesson 05: The Integrations Catalog & Gmail Actions`
- **Video Filename:** `05a The Integrations Catalog & Gmail Actions.mp4`
- **Duration & Size:** 2m 11s (131.5s) · 63.0 MB
- **Descript Cut Range:** `04:28.30 to 06:39.77`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Browse and utilize Architect's pre-built enterprise integrations catalog.
• Connect external accounts using standard OAuth flows (e.g., Google Workspace / Gmail).
• Enable agents to trigger real-world communication actions from live app interfaces.

OVERVIEW
To become genuinely useful, AI agents must take actions in the tools your enterprise already relies on. Architect features a catalog of pre-built integrations covering communication, project management, and developer platforms. In this lesson, we connect Gmail to our Vendor Renewal Desk, complete user authorization, and execute a live renegotiation email sent directly from a real mailbox.

STEP-BY-STEP WALKTHROUGH
1. Open the Integrations catalog to inspect available connectors (Gmail, Slack, HubSpot, GitHub, Jira, etc.).
2. Click 'Connect with Google' to initiate standard OAuth permission granting.
3. Review required scopes and authenticate your organizational email account.
4. In the live app, generate a renegotiation email draft and click 'Send via Gmail'.
5. Inspect your real Gmail Sent mailbox to verify transmission with customized vendor terms and dates.

KEY TAKEAWAYS
• Pre-built catalog integrations provide instant, zero-code connectivity to core SaaS platforms.
• Live email transmission transforms passive analysis into proactive operational execution.
```

---

#### 📖 Lesson 06: The Human-in-the-Loop Approval Gate
- **Lesson Title to Copy:** `📖 Lesson 06: The Human-in-the-Loop Approval Gate`
- **Video Filename:** `06a The Human-in-the-Loop Approval Gate.mp4`
- **Duration & Size:** 0m 17s (17.0s) · 28.7 MB
- **Descript Cut Range:** `06:39.77 to 06:56.78`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Implement Human-in-the-Loop (HITL) approval gates for sensitive agent actions.
• Prevent unverified external emails or financial commitments from firing autonomously.
• Design user-friendly review and confirmation interfaces for human operators.

OVERVIEW
Autonomous agents should never take irreversible real-world actions without explicit human oversight. In this lesson, we highlight an indispensable architectural pattern: the Human-in-the-Loop gate. The agent performs research, drafts negotiation copy, and prepares payloads—but transmission requires human inspection and button approval.

STEP-BY-STEP WALKTHROUGH
1. Observe the two-stage execution pattern: 'Draft renegotiation email' followed by 'Approve & Send'.
2. Inspect the review dialog showing recipient, subject line, proposed terms, and notice dates.
3. Enforce approval gates on all external write operations (emails, database updates, payment calls).

KEY TAKEAWAYS
• Anything that touches the outside world must sit behind a human approval gate.
• Human-in-the-Loop design builds organizational trust and eliminates accidental spam or legal exposure.
```

---

#### 📖 Lesson 07: Beyond the Catalog - MCP Servers & Custom APIs
- **Lesson Title to Copy:** `📖 Lesson 07: Beyond the Catalog - MCP Servers & Custom APIs`
- **Video Filename:** `07a Beyond the Catalog - MCP Servers & Custom APIs.mp4`
- **Duration & Size:** 1m 30s (89.6s) · 62.1 MB
- **Descript Cut Range:** `06:56.78 to 08:26.41`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Connect private internal APIs and vertical SaaS tools outside the standard catalog.
• Configure Model Context Protocol (MCP) servers with URL and authentication tokens.
• Import OpenAPI / Swagger schemas to automatically generate custom tool interfaces.

OVERVIEW
When your workflow requires proprietary internal microservices, internal ERPs, or niche SaaS platforms, Architect provides two universal extension doors: Model Context Protocol (MCP) servers and custom OpenAPI/HTTP tools. In this lesson, we explore how both doors allow agents to interact with any arbitrary software service with zero bespoke glue code.

STEP-BY-STEP WALKTHROUGH
1. Click the Plus (+) button in the Architect chat and select 'Add MCP Server'.
2. Configure server name, endpoint URL, and authentication headers (Bearer token, API key).
3. Alternatively, select 'Add Custom Tool' and provide an OpenAPI / Swagger JSON/YAML schema.
4. Instruct the agent in plain English how and when to invoke the newly connected tool.

KEY TAKEAWAYS
• The integration ladder runs from Catalog Tool → MCP Server → Custom OpenAPI Schema.
• All three integration styles share the same natural language orchestration interface.
```

---


================================================================================
### 📂 Chapter 04: Act 3 — Ship It (Production, Sharing & Governance)
**Chapter Name to Copy:** `📂 Chapter 04: Act 3 — Ship It (Production, Sharing & Governance)`

================================================================================

#### 📖 Lesson 08: One-Click Cloud Deployment & Sharing Doors
- **Lesson Title to Copy:** `📖 Lesson 08: One-Click Cloud Deployment & Sharing Doors`
- **Video Filename:** `08a One-Click Cloud Deployment & Sharing Doors.mp4`
- **Duration & Size:** 1m 53s (112.7s) · 50.6 MB
- **Descript Cut Range:** `08:26.41 to 10:19.10`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Graduate applications from local sandboxes to managed production cloud URLs.
• Master the Three Sharing Doors: Teammate Builder, Client Web Link, and Public Marketplace.
• Configure role-based permissions and public listing visibility toggles.

OVERVIEW
Once your application is fed with data and connected to tools, it is ready to ship. Architect eliminates DevOps complexity through one-click cloud deployment, instantly provisioning managed hosting, database replication, and agent infrastructure. We then examine the Three Sharing Doors to govern who accesses the application and under what permissions.

STEP-BY-STEP WALKTHROUGH
1. Click the 'Deploy' button in the upper right corner of the workspace.
2. Confirm environment settings and launch the live application to its unique public URL.
3. Explore Door 1 (Teammates): Grant edit/builder privileges via email invitation.
4. Explore Door 2 (Clients/Users): Share the clean end-user application URL for read/run access.
5. Explore Door 3 (Marketplace): Toggle public listing to feature your app across the global Lyzr directory.

KEY TAKEAWAYS
• Deployment handles frontend hosting, relational databases, and multi-agent backends with a single click.
• Three distinct sharing models ensure appropriate boundaries between creators, users, and the public.
```

---

#### 📖 Lesson 09: Eject to Code - GitHub Sync & Full-Stack Next.js
- **Lesson Title to Copy:** `📖 Lesson 09: Eject to Code - GitHub Sync & Full-Stack Next.js`
- **Video Filename:** `09a Eject to Code - GitHub Sync & Full-Stack Next.js.mp4`
- **Duration & Size:** 0m 40s (40.1s) · 39.4 MB
- **Descript Cut Range:** `10:19.10 to 10:59.19`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Export the entire Architect application as a standard Next.js, React, and Tailwind codebase.
• Synchronize application source code directly to your GitHub repository.
• Eliminate vendor lock-in by allowing engineering teams to extend and self-host the code.

OVERVIEW
The biggest fear with visual no-code builders is outgrowing the platform. Lyzr Architect solves this completely through code ejectability: every application is a legitimate, idiomatic Next.js web application with Tailwind CSS and clean React components. In this lesson, we connect our GitHub account and push the entire codebase to a private repository.

STEP-BY-STEP WALKTHROUGH
1. Click the GitHub sync option in the application settings drawer.
2. Authorize your GitHub organization and select the target repository name.
3. Inspect the synchronized repository containing clean Next.js pages, API routes, and agent orchestration calls.
4. Clone the repository locally to run `npm run dev` or integrate custom CI/CD pipelines.

KEY TAKEAWAYS
• You never hit a ceiling with Architect—applications are real, idiomatic Next.js codebases.
• Engineers can clone, extend, and deploy the application anywhere without proprietary runtimes.
```

---

#### 📖 Lesson 10: Enterprise Guardrails, Credit Habits & Wrap-up
- **Lesson Title to Copy:** `📖 Lesson 10: Enterprise Guardrails, Credit Habits & Wrap-up`
- **Video Filename:** `10a Enterprise Guardrails, Credit Habits & Wrap-up.mp4`
- **Duration & Size:** 1m 46s (106.4s) · 44.3 MB
- **Descript Cut Range:** `10:59.19 to 12:45.56`

**Copy the exact block below into Thinkific Lesson Text Block:**
```text
LEARNING OBJECTIVES
• Enforce enterprise security, compliance, and PII guardrails via the Lyzr Studio engine.
• Adopt the 4 Golden Habits for optimizing Agent Processing Credit (APC) consumption.
• Review the complete journey from prompt idea to governed enterprise software.

OVERVIEW
To satisfy enterprise procurement and security teams, applications must be governed and cost-controlled. In this final lesson, we examine how Architect agents inherit Studio guardrails (PII masking, hallucination filters, deterministic schemas) and establish 4 practical operational habits to keep credit consumption predictable and lean.

STEP-BY-STEP WALKTHROUGH
1. Review the underlying Lyzr Agent Studio engine powering your Architect agents.
2. Verify automated safety guardrails: PII detection, topic adherence, and hallucination containment.
3. Practice Credit Habit 1: Keep agents lean with targeted, 4-5 line system prompts.
4. Practice Credit Habit 2: Use fast, lightweight models for classification; reserve frontier models for synthesis.
5. Practice Credit Habit 3: Enforce strict human approval gates on external write actions.
6. Practice Credit Habit 4: Regularly prune outdated documents from your Knowledge Bases.

KEY TAKEAWAYS
• Architect agents inherit enterprise-grade Lyzr Studio governance out of the box.
• Disciplined prompt scoping and model routing ensure cost-effective, predictable APC economics.
```

---

## ⚙️ Course Settings & Publishing Directives

1. **Course Description (for storefront / card):**
   > Master the complete craft of building full-stack AI applications with Lyzr Architect. Learn the Three Acts of production deployment: feed your app multi-page contracts and structured databases, connect it to live SaaS tools like Gmail and custom MCP servers, and ship production Next.js code with enterprise guardrails and APC credit habits.
2. **Category:** `Tracks` > `Architect`
3. **Lesson Player Layout:** All-in-One Lesson Layout (Video player on top, formatted objectives and walkthrough directly below).
4. **Default Status:** Keep in `Draft` until final QA approval.