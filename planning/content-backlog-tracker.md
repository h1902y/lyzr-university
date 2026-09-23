# Content Backlog Tracker (Docs + Tutorials + Academy)

> Source: [Google Sheet](https://docs.google.com/spreadsheets/d/1Q8FTzaD1fumY8hvn8MZa66Z6IzWukZRfyUElfXif1IA/edit?gid=1261942771#gid=1261942771)
> Snapshot: 2026-05-26

---

## Product Overview

| Track | Product | Who It's For | What You Build | Technical Skill | Output | Docs Pages | Tutorials | Academy Modules | Status |
|---|---|---|---|---|---|---|---|---|---|
| Architect | Lyzr Architect | Business users, non-technical builders | Full-stack agentic apps with UI (React/Next.js) | None required | Deployed app URL | ~30 pages | 25 (20 video + 5 new) | 8 modules | Docs 60% exist |
| Studio | Lyzr Agent Studio | Power users, ops teams, product managers | Agents, workflows, and knowledge for org deployment | Low-code | Running agents via UI or API | ~110 pages | 23 (all new) | 24 modules | ~60% exists |
| ADK | Lyzr ADK (Python) | Developers, engineers | Agents embedded in your own codebase | Python proficiency | Python SDK / REST API endpoint | ~54 pages | 19 (all new) | 14 modules | Docs ~50% exist |

> **COGNIS** — 4th standalone product | docs.lyzr.ai/cognis/ | 20+ pages: Memory Operations API, Claude-Cognis plugin, Cookbooks (CrewAI, LangGraph, LangChain, Agno) | Open-source (lyzr-cognis) + Hosted (lyzr-adk) | NOT duplicated in Studio/ADK — link cross-reference only

### Product Routing Guide

| Question | Answer → Track | One-line description | Best for |
|---|---|---|---|
| Do you want to describe your app in plain English and have Lyzr build it? | → Architect | Text-to-App: describe it, Architect builds the frontend + agents | Business users, no-code builders, rapid prototyping |
| Do you want to configure agents visually with full control over every setting? | → Studio | Visual agent builder: configure intelligence without writing code | Power users, ops teams, enterprise deployments |
| Do you want to write Python code to build and integrate agents into your product? | → ADK | Python SDK: programmatic control, embed agents in your own codebase | Developers, engineers, custom integrations |
| Can you combine them? | Yes — they're a stack | Architect builds in Studio. Studio resources usable via ADK. Not competing. | Start anywhere, go deeper as needed |

### Status Legend

- **Exists** — Content already published and accurate; may need minor review
- **Enrich** — Content exists but needs expansion, depth, or accuracy improvements
- **New** — Net new; needs to be created from scratch

---

## Architect Track

### Docs: Overview & Platform

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Docs | Overview & Platform | Introduction / What is Architect | Suyash/Yash | Exists | P2 | Wk 1 | Written | 0.5d | docs.architect.new/introduction |
| 2 | Docs | Overview & Platform | Why Architect? | | Exists | P2 | Wk 1 | Written | 0.5d | |
| 3 | Docs | Overview & Platform | Best Use Cases | | Enrich | P1 | Wk 1 | Written | 1d | Needs more industry-specific examples |
| 4 | Docs | Overview & Platform | How It Works (3-phase build) | | Exists | P2 | Wk 1 | Written | 0.5d | |
| 5 | Docs | Overview & Platform | AI Consultant | | Exists | P2 | Wk 1 | Written | 0.5d | |
| 6 | Docs | Overview & Platform | Agentlets Marketplace | | Enrich | P1 | Wk 2 | Written | 1d | Needs: publish your own, cloning rules, attribution |
| 7 | Docs | Overview & Platform | Architect + Studio (bridge page) | | Enrich | P1 | Wk 2 | Written | 2d | Critical bridge — needs full expansion |
| 8 | Docs | Overview & Platform | Usage & Credits | | Enrich | P1 | Wk 2 | Written | 1d | What consumes credits, estimation guidance |
| 9 | Docs | Overview & Platform | Getting Ready / Prerequisites | | Exists | P3 | Wk 1 | Written | 0.5d | |
| 10 | Docs | Overview & Platform | Plans & Credits | | Exists | P2 | Wk 1 | Written | 0.5d | |
| 11 | Docs | Overview & Platform | Help & Support | | Exists | P3 | Wk 1 | Written | 0.5d | |

### Docs: Build & Integrations

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 12 | Docs | Build & Integrations | How to Build an App (Build Guide) | Suyash/Yash | Exists | P1 | Wk 1 | Written | 0.5d | |
| 13 | Docs | Build & Integrations | Database & Authentication | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 14 | Docs | Build & Integrations | Deployment & Publishing | | Exists | P1 | Wk 2 | Written | 0.5d | |
| 15 | Docs | Build & Integrations | Connecting GitHub | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 16 | Docs | Build & Integrations | Prompt Library | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 17 | Docs | Build & Integrations | Sharing an App | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 18 | Docs | Build & Integrations | Integration: Gmail | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 19 | Docs | Build & Integrations | Integration: Slack | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 20 | Docs | Build & Integrations | Integration: GitHub | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 21 | Docs | Build & Integrations | Integration: Notion | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 22 | Docs | Build & Integrations | Integration: Google Calendar | | Enrich | P2 | Wk 3 | Written | 1d | Needs dedicated page |
| 23 | Docs | Build & Integrations | Integration: Linear / Jira | | New | P3 | Wk 3 | Written | 1d | |

### Docs: New Pages Needed

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 24 | Docs | New Pages | Custom Integrations (beyond built-ins) | Suyash/Yash | New | P1 | Wk 3 | Written | 2d | Companion to existing video tutorial |
| 25 | Docs | New Pages | Voice Agents in Architect | | New | P1 | Wk 3 | Written | 1.5d | Companion to existing video tutorial |
| 26 | Docs | New Pages | Agent Simulation Engine (Studio crossover) | | New | P1 | Wk 3 | Written | 1.5d | Crossover with Studio — needs coordination |
| 27 | Docs | New Pages | Troubleshooting & Debugging Guide | | New | P1 | Wk 4 | Written | 2d | Companion to existing video tutorial |
| 28 | Docs | New Pages | Security & Data Handling in Architect | | New | P1 | Wk 4 | Written | 2d | Enterprise concern — not currently documented |
| 29 | Docs | New Pages | Architect for Teams (Enterprise) | | New | P2 | Wk 4 | Written | 1.5d | Team sharing, permissions, client delivery |
| 30 | Docs | New Pages | Credit Consumption Best Practices | | New | P2 | Wk 4 | Written | 1d | Companion to existing video tutorial |
| 31 | Docs | New Pages | FAQs (expanded) | | Enrich | P2 | Wk 4 | Written | 1d | Seed from real support tickets |

### Tutorials: Tier 1 — Getting Started (all have existing video)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 32 | Tutorial | How to write your first prompt and build an app from scratch | Suyash/Yash | Exists | P1 | Wk 2 | Video + Written | 0.5d | Video exists — write companion text |
| 33 | Tutorial | How to use 'What should I build?' for inspiration | | Exists | P1 | Wk 2 | Video + Written | 0.5d | Video exists |
| 34 | Tutorial | How to use the Prompt Library to get started faster | | Exists | P1 | Wk 2 | Video + Written | 0.5d | Video exists |
| 35 | Tutorial | How to iterate the PRD before building agents | | Exists | P1 | Wk 2 | Video + Written | 0.5d | Video exists |
| 36 | Tutorial | How to iterate your app after the first build | | Exists | P1 | Wk 3 | Video + Written | 0.5d | Video exists |
| 37 | Tutorial | How to deploy and publish your app with one click | | Exists | P1 | Wk 3 | Video + Written | 0.5d | Video exists |

### Tutorials: Tier 2 — Feature How-Tos (all have existing video)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 38 | Tutorial | How to connect tools and integrations (Gmail, Slack, GitHub, Notion) | Suyash/Yash | Exists | P1 | Wk 3 | Video + Written | 0.5d | Video exists |
| 39 | Tutorial | How to upload a knowledge base to your app | | Exists | P1 | Wk 3 | Video + Written | 0.5d | Video exists |
| 40 | Tutorial | How to add database and user authentication to your app | | Exists | P1 | Wk 3 | Video + Written | 0.5d | Video exists |
| 41 | Tutorial | How to enable PII redaction / Responsible AI for agents | | Exists | P1 | Wk 3 | Video + Written | 0.5d | Video exists |
| 42 | Tutorial | How to create a voice agent in Architect | | Exists | P1 | Wk 4 | Video + Written | 0.5d | Video exists |
| 43 | Tutorial | How to do custom integrations beyond built-in connectors | | Exists | P1 | Wk 4 | Video + Written | 0.5d | Video exists |
| 44 | Tutorial | How to edit agent instructions in Architect + Studio | | Exists | P1 | Wk 4 | Video + Written | 0.5d | Video exists |

### Tutorials: Tier 3 — Managing & Sharing (all have existing video)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 45 | Tutorial | How to share your app with teammates or clients | Suyash/Yash | Exists | P2 | Wk 4 | Video + Written | 0.5d | Video exists |
| 46 | Tutorial | How to publish, clone and use apps from Agentlets | | Exists | P2 | Wk 4 | Video + Written | 0.5d | Video exists |
| 47 | Tutorial | How to get the GitHub code of your app | | Exists | P2 | Wk 5 | Video + Written | 0.5d | Video exists |
| 48 | Tutorial | How to debug and fix issues in your Architect-built app | | Exists | P2 | Wk 5 | Video + Written | 0.5d | Video exists |
| 49 | Tutorial | How to test agents using the Agent Simulation Engine in Studio | | Exists | P2 | Wk 5 | Video + Written | 0.5d | Video exists — Studio crossover |
| 50 | Tutorial | Best practices to keep credit consumption low | | Exists | P2 | Wk 5 | Video + Written | 0.5d | Video exists |

### Tutorials: Tier 4 — Strategy & Projects

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 51 | Tutorial | Which use cases work best with Architect | Suyash/Yash | Exists | P1 | Wk 5 | Video + Written | 1d | Video exists — expand into use case library |
| 52 | Tutorial | End-to-end: HR Onboarding App (start to finish) | | New | P1 | Wk 7 | Written | 3d | New project tutorial |
| 53 | Tutorial | End-to-end: Sales Intelligence Dashboard | | New | P2 | Wk 8 | Written | 3d | |
| 54 | Tutorial | End-to-end: Internal Knowledge Base App | | New | P2 | Wk 9 | Written | 3d | |
| 55 | Tutorial | From Architect → Studio → ADK: the progression guide | | New | P1 | Wk 6 | Written | 2d | Critical bridge tutorial — cross-track |
| 56 | Tutorial | Enterprise: deploying Architect apps to a team | | New | P2 | Wk 10 | Written | 2d | |

### Academy: Build with Architect (Path — 8 Modules)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 57 | Academy | Module 1: What Architect is and how it thinks | Felipe | New | P1 | Wk 6 | Module (Video + Quiz) | 1.5d | Platform intro + AI Consultant |
| 58 | Academy | Module 2: Writing prompts that work | | New | P1 | Wk 6 | Module (Video + Quiz) | 1.5d | Prompting guide + PRD iteration |
| 59 | Academy | Module 3: Your first app, end to end | | New | P1 | Wk 7 | Module (Video + Quiz) | 1.5d | Uses Tier 1 tutorials |
| 60 | Academy | Module 4: Giving your app capabilities | | New | P1 | Wk 7 | Module (Video + Quiz) | 1.5d | Tools, integrations, KB |
| 61 | Academy | Module 5: Security and data handling | | New | P1 | Wk 8 | Module (Video + Quiz) | 1.5d | RAI, PII, authentication |
| 62 | Academy | Module 6: Deploying and sharing | | New | P2 | Wk 8 | Module (Video + Quiz) | 1.5d | Deployment, Agentlets, team sharing |
| 63 | Academy | Module 7: Iterating and debugging | | New | P2 | Wk 9 | Module (Video + Quiz) | 1.5d | Refinement, Studio editing, simulation |
| 64 | Academy | Module 8: Going further | | New | P2 | Wk 9 | Module (Video + Quiz) | 1.5d | GitHub, custom integrations, when to move to Studio |

---

## Studio Track

### S1 — Docs: Platform Orientation & Getting Started

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Docs | S1 | What is Lyzr Agent Studio | Prasad | Enrich | P1 | Wk 1 | Written | 0.5d | URL: docs.lyzr.ai/introduction/getting-started/intro | Rewrite intro — remove AI-gen artefacts, add architecture diagram |
| 2 | Docs | S1 | Why Lyzr? / What makes it unique | | Exists | P2 | Wk 1 | Written | 0.25d | URL: docs.lyzr.ai/introduction/getting-started/what-makes-us-unique | Review accuracy against current positioning |
| 3 | Docs | S1 | What You Can Build | | Exists | P2 | Wk 1 | Written | 0.25d | URL: docs.lyzr.ai/introduction/getting-started/what-can-you-build-on-lyzr | Verify examples are current |
| 4 | Docs | S1 | What are Credits? | | Exists | P2 | Wk 1 | Written | 0.25d | URL: docs.lyzr.ai/introduction/getting-started/credits | Verify pricing accuracy |
| 5 | Docs | S1 | Quick Start | | Exists | P1 | Wk 1 | Written | 0.25d | URL: docs.lyzr.ai/introduction/getting-started/quickstarts | Check if end-to-end example still works |
| 6 | Docs | S1 | Interface navigation and layout | | New | P1 | Wk 1 | Written | 1d | No dedicated page exists | Create from scratch — annotated screenshot of main UI areas |
| 7 | Docs | S1 | Using Lyzr — Components overview | | Exists | P2 | Wk 1 | Written | 0.25d | URL: docs.lyzr.ai/introduction/using-lyzr/components | Review for completeness |

### S2 — Docs: Agents (Manual Builder, Config, Features)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Docs | S2 | Conversational Agent Builder (Studio home) | Prasad | Exists | P1 | Wk 1 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/build-paths/agentbuilder/build | Minor enrichment: add note about when to use vs manual builder |
| 9 | Docs | S2 | Studio Builder (Manual Agent Builder) | | Exists | P1 | Wk 2 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/build-paths/studio/studiopath | Verify all sections match current UI |
| 10 | Docs | S2 | Studio Agent intro | | Exists | P2 | Wk 2 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agents/introduction | Review for accuracy |
| 11 | Docs | S2 | Agent configuration: Role, Goal, Instructions | | Enrich | P1 | Wk 2 | Written | 1d | Partially covered | Create dedicated page: prompting guide, examples |
| 12 | Docs | S2 | Generate with AI (prompt improvement) | | New | P2 | Wk 2 | Written | 0.5d | Not documented | Document feature, show before/after prompt examples |
| 13 | Docs | S2 | Agent Settings (max tokens, temperature, etc.) | | Exists | P2 | Wk 2 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/max | Review parameter descriptions |
| 14 | Docs | S2 | Testing your agent (Test Agent Inference panel) | | Enrich | P1 | Wk 2 | Written | 0.5d | URL: simulation page exists | Add section covering right-panel test interface, streaming, activity view |
| 15 | Docs | S2 | File upload and parser settings (VLM, tables) | | New | P2 | Wk 2 | Written | 1d | Not documented | Document all file types, Extract Tables toggle, VLM selection |
| 16 | Docs | S2 | Agent versioning and rollback | | New | P2 | Wk 3 | Written | 1d | Not documented | Document version history UI, restore flow |
| 17 | Docs | S2 | Publishing and sharing agents | | New | P1 | Wk 3 | Written | 1d | Not documented | Document share flows, visibility options |
| 18 | Docs | S2 | Agent visibility: Private / Public / Organization | | New | P2 | Wk 3 | Written | 0.5d | Not documented | Short reference page, note Org requires Enterprise plan |
| 19 | Docs | S2 | Image Output | | Exists | P2 | Wk 3 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/Image output | Review for completeness |
| 20 | Docs | S2 | PPT File Output | | Exists | P2 | Wk 3 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/ppt | Review for completeness |
| 21 | Docs | S2 | Real-time Session Monitoring (WebSocket) | | Exists | P2 | Wk 3 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/web socket | Review for completeness |
| 22 | Docs | S2 | Agent Events | | Exists | P2 | Wk 3 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/agent events | Review for completeness |

### S3 — Docs: Models

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 23 | Docs | S3 | Model selection guide (choosing the right model) | Prasad | Exists | P1 | Wk 2 | Written | 0.25d | URL: docs.lyzr.ai/cookbooks/Choosing Model | Move or cross-link — currently buried in Cookbooks |
| 24 | Docs | S3 | Models intro | | Exists | P2 | Wk 2 | Written | 0.25d | URL: docs.lyzr.ai/introduction/models/overview | Review accuracy of provider list |
| 25 | Docs | S3 | OpenAI models reference | | Exists | P2 | Wk 2 | Written | 0.25d | URL: docs.lyzr.ai/introduction/models/gpt | Verify model names match current (gpt-5, o3, o4-mini) |
| 26 | Docs | S3 | Anthropic models reference | | Exists | P2 | Wk 2 | Written | 0.25d | URL: docs.lyzr.ai/introduction/models/claude | Verify latest Claude 4.x models listed |
| 27 | Docs | S3 | Google models reference | | Exists | P2 | Wk 2 | Written | 0.25d | URL: docs.lyzr.ai/introduction/models/google | Verify Gemini 3.x models listed |
| 28 | Docs | S3 | Groq / Perplexity / Bedrock models | | Exists | P2 | Wk 2 | Written | 0.25d | URLs: introduction/models/groq, /perplexity, /aws-bedrock | Verify latest models across all three |
| 29 | Docs | S3 | Bringing your own model (BYOM) | | New | P2 | Wk 3 | Written | 1d | Mentioned in product guide — Enterprise only | Document BYOM flow |

### S4 — Docs: Memory

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | Docs | S4 | Memory overview: why it matters | Parshva | Exists | P1 | Wk 3 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/agent features/memory | Enrich with decision guide |
| 31 | Docs | S4 | Lyzr Cognis — overview | | Exists | P1 | Wk 3 | Written | 0.25d | URL: docs.lyzr.ai/cognis/overview (20+ pages) | Add cross-reference from Studio memory page |
| 32 | Docs | S4 | Lyzr Cognis — quickstart and configuration | | Exists | P1 | Wk 3 | Written | 0.25d | URL: docs.lyzr.ai/cognis/quickstart + /configuration | Review Studio-specific steps |
| 33 | Docs | S4 | Lyzr Cognis — cross-session memory | | Exists | P2 | Wk 3 | Written | 0.25d | URL: docs.lyzr.ai/cognis/ (Memory Operations) | Verify Studio UI steps match API docs |
| 34 | Docs | S4 | Lyzr Memory (short-term / long-term summarization) | | Enrich | P2 | Wk 4 | Written | 0.5d | Lyzr Memory was precursor to Cognis | Clarify relationship, document slider UI |
| 35 | Docs | S4 | Amazon Bedrock AgentCore Memory | | New | P2 | Wk 4 | Written | 1d | Requires BYOA AWS credentials | Document setup: Studio > Memory > Bedrock option |
| 36 | Docs | S4 | When to use which memory type (decision guide) | | New | P1 | Wk 4 | Written | 1d | Common confusion point | Decision table: Cognis vs Lyzr Memory vs Bedrock |

### S5 — Docs: Knowledge (KB, Knowledge Graph, Semantic Model)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 37 | Docs | S5 | Knowledge overview: KB vs KG vs Semantic Model | Parshva | Enrich | P1 | Wk 4 | Written | 1d | URL: docs.lyzr.ai/agent-lab/knowledgebase/introduction | Expand into full decision guide |
| 38 | Docs | S5 | Knowledge Base: creating and configuring | | Exists | P1 | Wk 4 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/knowledgebase/studiokb | Verify config steps are current |
| 39 | Docs | S5 | Knowledge Base: uploading files and websites | | Enrich | P1 | Wk 4 | Written | 0.5d | Covered in studiokb | Add: live source types, URL scraping |
| 40 | Docs | S5 | Knowledge Base: live sources (Sharepoint, Website) | | New | P2 | Wk 5 | Written | 1d | Not documented | Document sync frequency, delta changes, setup |
| 41 | Docs | S5 | Knowledge Base: chunking strategy | | New | P2 | Wk 5 | Written | 1d | Not documented | Document chunk size, overlap, number of chunks |
| 42 | Docs | S5 | Knowledge Base: retrieval types (Basic, MMR, HyDE) | | New | P1 | Wk 5 | Written | 1.5d | Not documented | Document each mode, score threshold guidance |
| 43 | Docs | S5 | Knowledge Base: query, test and score threshold | | Enrich | P2 | Wk 5 | Written | 0.5d | Partially in studiokb | Document KB test panel |
| 44 | Docs | S5 | Knowledge Base: connecting to agents (RAG) | | Enrich | P1 | Wk 5 | Written | 0.5d | Partially in studiokb | Add clear step-by-step |
| 45 | Docs | S5 | Knowledge Base as a Service (external access) | | New | P2 | Wk 5 | Written | 1d | Not documented | Document API access, external framework integration |
| 46 | Docs | S5 | Knowledge Graph: overview and when to use | | Exists | P1 | Wk 5 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/knowledgebase/studiokg | Enrich: add KB vs KG comparison |
| 47 | Docs | S5 | Knowledge Graph: Neo4j setup and connection | | Enrich | P1 | Wk 5 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/dataconnectors/neo | Add step-by-step: Aura > credentials > config |
| 48 | Docs | S5 | Knowledge Graph: uploading and parsing documents | | New | P2 | Wk 6 | Written | 1d | Not documented | Document entity extraction, relationship ID |
| 49 | Docs | S5 | Knowledge Graph: connecting to agents | | Enrich | P2 | Wk 6 | Written | 0.5d | Partially in studiokg | Add clear step-by-step |
| 50 | Docs | S5 | Knowledge Graph as a Service | | New | P3 | Wk 6 | Written | 1d | Not documented | Document interop pattern |
| 51 | Docs | S5 | Semantic Model: overview and when to use | | Exists | P1 | Wk 6 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/knowledgebase/studiosem | Enrich: add comparison with KB/KG |
| 52 | Docs | S5 | Semantic Model: database connection setup | | Enrich | P1 | Wk 6 | Written | 1d | URL: docs.lyzr.ai/agent-lab/dataconnectors/ | Add per-DB step-by-step |
| 53 | Docs | S5 | Semantic Model: schema documentation agent | | New | P1 | Wk 6 | Written | 1.5d | Not documented | Document auto-schema agent, table config |
| 54 | Docs | S5 | Semantic Model: connecting to agents (Text-to-SQL) | | Enrich | P1 | Wk 6 | Written | 1d | Partially in studiosem | Also: docs.lyzr.ai/cookbooks/Data Analyst Agent |

### S6 — Docs: Tools, Skills & MCP

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 55 | Docs | S6 | Tools overview | Rasswanth | Exists | P1 | Wk 6 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/tools/tools overview | Review for completeness |
| 56 | Docs | S6 | Pre-built tools library (Studio ready tools) | | Exists | P1 | Wk 6 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/tools/Ready Tools | Verify full tool list |
| 57 | Docs | S6 | Adding tools to an agent | | Exists | P1 | Wk 6 | Written | 0.25d | Covered in tools pages + Tooling cookbook | Review clarity |
| 58 | Docs | S6 | Tool authentication: shared vs per-user login | | New | P1 | Wk 7 | Written | 1d | Not documented — critical for deployed agents | Document two auth modes |
| 59 | Docs | S6 | Custom tools: OpenAPI schema | | Exists | P1 | Wk 7 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/tools/Custom Tools | Verify schema example is current |
| 60 | Docs | S6 | MCP server integration (connect external MCP) | | Exists | P1 | Wk 7 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/tools/MCP | Review for completeness |
| 61 | Docs | S6 | Lyzr Agents as MCP Servers | | Exists | P2 | Wk 7 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/lyzr-mcp/ (3 pages) | Ensure visibility in navigation |
| 62 | Docs | S6 | A2A protocol (Agent-to-Agent cross-platform) | | New | P2 | Wk 7 | Written | 1.5d | Not documented | Document A2A setup, Workflow node, example |
| 63 | Docs | S6 | Skills: overview and SKILL.md format | | New | P1 | Wk 7 | Written | 1.5d | Not documented | Document Skills page, SKILL.md spec |
| 64 | Docs | S6 | Skills: default library (pptx, xlsx, slack-elf, etc.) | | New | P2 | Wk 7 | Written | 1d | Not documented — 17+ skills | Document each skill |
| 65 | Docs | S6 | Adding skills to agents | | New | P2 | Wk 7 | Written | 0.5d | Not documented | Short how-to page |

### S7 — Docs: Orchestration (Managerial & Workflow Builder & SuperFlow)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 66 | Docs | S7 | Orchestration overview (Managerial vs Workflow) | Sreehari | Exists | P1 | Wk 7 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/orchestration/.../comparison | Verify comparison table |
| 67 | Docs | S7 | Managerial orchestration: setup and manager agent | | Exists | P1 | Wk 7 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/orchestration/ | Enrich: add non-deterministic explanation |
| 68 | Docs | S7 | Managerial orchestration: adding worker agents | | Enrich | P1 | Wk 8 | Written | 0.5d | Partially in Manager Agent page | Add dedicated section |
| 69 | Docs | S7 | Managerial canvas view | | Enrich | P2 | Wk 8 | Written | 0.5d | Partially documented | Document canvas navigation |
| 70 | Docs | S7 | Workflow Builder: overview and canvas | | Exists | P1 | Wk 8 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/orchestration/ | Enrich: add canvas navigation |
| 71 | Docs | S7 | Workflow Builder: Agent node | | New | P1 | Wk 8 | Written | 1d | Not documented | Document node configuration modal |
| 72 | Docs | S7 | Workflow Builder: Conditional node | | New | P1 | Wk 8 | Written | 1d | Not documented | Document True/False branching |
| 73 | Docs | S7 | Workflow Builder: Router node | | New | P1 | Wk 8 | Written | 1d | Not documented | Document multi-path routing |
| 74 | Docs | S7 | Workflow Builder: API Call node | | New | P2 | Wk 8 | Written | 1d | Not documented | Document API Call node config |
| 75 | Docs | S7 | Workflow Builder: Default Inputs node | | New | P2 | Wk 8 | Written | 1d | Not documented | Document parameters, key-value |
| 76 | Docs | S7 | Workflow Builder: A2A node | | New | P2 | Wk 9 | Written | 1d | Not documented | Document A2A node |

### S8 — Docs: Automation (Triggers, Output, Global Context)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 77 | Docs | S8 | Time-based triggers (Scheduler) | Prasad | Exists | P1 | Wk 8 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/schedulers | Verify 5 timing modes documented |
| 78 | Docs | S8 | Webhook-based triggers | | Exists | P1 | Wk 8 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/webhooks | Verify secret key + monitoring documented |
| 79 | Docs | S8 | Structured Output (JSON schema) | | Exists | P1 | Wk 9 | Written | 0.5d | Two pages exist | Deduplicate — pick one canonical |
| 80 | Docs | S8 | Global Context | | Exists | P2 | Wk 9 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/agent features/global context | Review completeness |

### S9 — Docs: Voice Agents

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 81 | Docs | S9 | Voice agents overview | Someshwar | Exists | P1 | Wk 9 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/voice agent/voice | Verify Realtime vs Pipeline comparison |
| 82 | Docs | S9 | Voice: Realtime engine (Unified Model) | | Enrich | P1 | Wk 9 | Written | 0.5d | Partially in voice page | Add: sub-500ms latency, supported models, voice selection |
| 83 | Docs | S9 | Voice: Pipeline engine (STT → LLM → TTS) | | Enrich | P1 | Wk 9 | Written | 0.5d | Partially in voice page | Add: AssemblyAI STT, Cartesia TTS, Voice IDs |
| 84 | Docs | S9 | Voice: Behavioral configuration | | Enrich | P2 | Wk 9 | Written | 0.5d | Partially in voice page | Add: Who Speaks First, tone/constraints |
| 85 | Docs | S9 | Voice: SFX, Ambience and Tool-call sounds | | New | P2 | Wk 9 | Written | 1d | Not documented | Document SFX panel, ambience toggle |
| 86 | Docs | S9 | Voice: Dynamic variables and fallbacks | | New | P2 | Wk 9 | Written | 1d | Not documented | Document variables panel, API override |
| 87 | Docs | S9 | Voice: Pronunciation rules | | New | P2 | Wk 10 | Written | 0.5d | Not documented | Short reference with examples |
| 88 | Docs | S9 | Voice: Noise cancellation and advanced features | | New | P2 | Wk 10 | Written | 1d | Not documented | Document Krisp, Preemptive generation, Call Recording |
| 89 | Docs | S9 | Voice: Telephony (Telnyx, Twilio, Plivo) | | Exists | P1 | Wk 10 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/voice agent/monitor | Verify integration steps for all 3 |
| 90 | Docs | S9 | Voice: Transcripts and session analytics | | Enrich | P2 | Wk 10 | Written | 0.5d | Same page as telephony | Split out: Transcript view, Event Log, Global Metrics |
| 91 | Docs | S9 | Voice: WebSocket for custom deployment | | Exists | P2 | Wk 10 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/voice agent/web socket | Review for completeness |

### S10 — Docs: Safety & Responsible AI

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 92 | Docs | S10 | Responsible AI overview | Prasad | Exists | P1 | Wk 7 | Written | 0.5d | Two pages covering similar ground | Deduplicate or differentiate |
| 93 | Docs | S10 | Configuring a Responsible AI policy | | Enrich | P1 | Wk 7 | Written | 0.5d | In responsible AI page | Add step-by-step policy creation |
| 94 | Docs | S10 | Toxicity detection | | Enrich | P1 | Wk 7 | Written | 0.5d | Pre/post-check flow documented | Verify threshold guidance (default 0.4) |
| 95 | Docs | S10 | Prompt injection protection | | Enrich | P1 | Wk 7 | Written | 0.5d | In responsible AI page | Add screenshot of detected injection |
| 96 | Docs | S10 | PII detection and handling (9 data types) | | Enrich | P1 | Wk 8 | Written | 0.5d | All 9 PII types listed | Add Block vs Redact vs Disabled, GDPR/HIPAA callout |
| 97 | Docs | S10 | Secrets detection | | Enrich | P2 | Wk 8 | Written | 0.5d | In responsible AI page | Add MASK vs BLOCK actions |
| 98 | Docs | S10 | Allowed and banned topics | | Enrich | P2 | Wk 8 | Written | 0.5d | In responsible AI page | Add practical enterprise examples |
| 99 | Docs | S10 | Blocked keywords | | Enrich | P2 | Wk 8 | Written | 0.25d | In responsible AI page | Short reference |
| 100 | Docs | S10 | AWS Bedrock Guardrails (6 categories) | | New | P2 | Wk 8 | Written | 1d | Not documented | Document: requires BYOA AWS, 6 categories |
| 101 | Docs | S10 | Hallucination Manager overview | | Exists | P1 | Wk 8 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/responsible-safe-ai/Safe | Enrich: add latency tradeoff warning |
| 102 | Docs | S10 | Reflection | | Enrich | P1 | Wk 9 | Written | 0.5d | In hallucination manager page | Add cycle config, latency impact |
| 103 | Docs | S10 | Groundedness | | Enrich | P1 | Wk 9 | Written | 0.5d | In hallucination manager page | Add grounding context guidance |
| 104 | Docs | S10 | LLM as a Judge (Beta) | | New | P2 | Wk 9 | Written | 1d | Not documented | Document: beta status, scoring, roadmap |
| 105 | Docs | S10 | RAI Cookbook (reference) | | Exists | P3 | Wk 7 | Written | 0.25d | URL: docs.lyzr.ai/cookbooks/Responsible AI | Cross-link from RAI overview |

### S11 — Docs: Evaluation & Observability

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 106 | Docs | S11 | Agent Eval overview | Khush | Exists | P1 | Wk 10 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/agent eval/agentsimulation | Clarify terminology |
| 107 | Docs | S11 | Creating environments, scenarios and personas | | Enrich | P1 | Wk 10 | Written | 1d | In agentsimulation page | Add step-by-step |
| 108 | Docs | S11 | Configuring evaluation metrics | | Enrich | P1 | Wk 10 | Written | 1d | In agentsimulation page | Document all 7 agent metrics + Tool + KB metrics |
| 109 | Docs | S11 | Running test cases and scoring | | Enrich | P1 | Wk 10 | Written | 0.5d | In agentsimulation page | Add pass/fail interpretation |
| 110 | Docs | S11 | Agent Hardening | | Enrich | P1 | Wk 10 | Written | 1d | Mentioned but not fully documented | Document: select failed cases, submit, review |
| 111 | Docs | S11 | Traces: overview and how to use | | Exists | P1 | Wk 11 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/agent eval/tracing | Enrich: add step-by-step, debugging patterns |
| 112 | Docs | S11 | Analytics dashboard (credits, latency, sessions) | | New | P2 | Wk 11 | Written | 1d | Not documented | Document Analytics tab |

### S12 — Docs: Workspace & Administration

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 113 | Docs | S12 | Organization setup | Vaibhavi | Enrich | P1 | Wk 11 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/team-management | Add: sub-org creation, owner transfer |
| 114 | Docs | S12 | User roles and permissions (Owner/Admin/Member) | | Exists | P1 | Wk 11 | Written | 0.5d | URL: docs.lyzr.ai/agent-lab/team-management | Verify 9 actions × 3 roles matrix |
| 115 | Docs | S12 | Inviting team members | | Exists | P1 | Wk 11 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/team-management | Add note: Member can't see Models page |
| 116 | Docs | S12 | Plans & Pricing | | Exists | P2 | Wk 11 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/plans | Verify plan tiers |
| 117 | Docs | S12 | Accounts & Billing | | Exists | P2 | Wk 11 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/accounts-billing | Verify steps |
| 118 | Docs | S12 | Audit logs | | Exists | P1 | Wk 12 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/audit-logs | Verify filter options |
| 119 | Docs | S12 | Data connectors (SQL + NoSQL databases) | | Exists | P1 | Wk 12 | Written | 0.25d | URL: docs.lyzr.ai/agent-lab/dataconnectors/introduction | Verify 10 connectors; note Databricks/Snowflake Upcoming |
| 120 | Docs | S12 | Data connector pages (Qdrant, Weaviate, SingleStore, Neo4j, Milvus) | | Exists | P1 | Wk 12 | Written | 0.25d | 5 individual pages | Review each; note default credentials |
| 121 | Docs | S12 | Vector stores overview (concept page) | | Enrich | P2 | Wk 12 | Written | 1d | No unified concept page | Create: what a vector store is, defaults, BYOC options |

### Cookbooks (9 existing — review + cross-link)

| # | Type | Section | Title | Owner | Status | Priority | Phase | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|
| 122 | Docs | Cookbooks | Choosing the Right Model | Prasad | Exists | P1 | Wk 2 | Comprehensive 6-parameter framework | Cross-link from Studio S3 |
| 123 | Docs | Cookbooks | Text to SQL Agent | | Exists | P1 | Wk 6 | docs.lyzr.ai/cookbooks/Data Analyst Agent | Cross-link from Semantic Model |
| 124 | Docs | Cookbooks | Product Support Chatbot | | Exists | P2 | Wk 4 | | Cross-link from KB section |
| 125 | Docs | Cookbooks | Voice Agent | | Exists | P2 | Wk 9 | | Cross-link from Voice Agents |
| 126 | Docs | Cookbooks | Responsible AI | | Exists | P1 | Wk 7 | | Cross-link from RAI section |
| 127 | Docs | Cookbooks | Tooling | | Exists | P2 | Wk 6 | | Cross-link from Tools section |
| 128 | Docs | Cookbooks | Software Manager | | Exists | P3 | Wk 8 | | Review relevance |
| 130 | Docs | Cookbooks | External Integrations (section) | | Exists | P2 | Wk 7 | | Cross-link from Tools section |

### Key Concepts (7 existing — review + deduplicate)

| # | Type | Section | Title | Owner | Status | Priority | Phase | Notes | Action Required |
|---|---|---|---|---|---|---|---|---|---|
| 131 | Docs | Key Concepts | Glossary | Prasad | Exists | P2 | Wk 1 | | Add Agent, OGI, Cognis definitions |
| 132 | Docs | Key Concepts | Key Concepts: RAG | | Exists | P1 | Wk 4 | | Verify alignment with KB/KG/Semantic Model |
| 133 | Docs | Key Concepts | Key Concepts: Responsible AI | | Exists | P1 | Wk 7 | | Consolidate vs agent-lab RAI page |
| 134 | Docs | Key Concepts | Key Concepts: Manager Agent | | Exists | P1 | Wk 7 | | Ensure consistent with orchestration |
| 135 | Docs | Key Concepts | Key Concepts: Structured Outputs | | Exists | P2 | Wk 8 | | Deduplicate vs agent features page |
| 136 | Docs | Key Concepts | Community: Discord | | Exists | P3 | Wk 1 | | Verify Discord link |
| 137 | Docs | Key Concepts | Support: Contact & FAQs | | Exists | P2 | Wk 4 | | Seed FAQ from real tickets |

### Studio Tutorials

#### Tier 1: Quickstarts (7)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 138 | Tutorial | Build and test your first agent in Studio | Prasad | New | P1 | Wk 3 | Written + Video | 2d | Flagship tutorial |
| 139 | Tutorial | Connect a knowledge base (RAG in 15 minutes) | | New | P1 | Wk 4 | Written + Video | 2d | |
| 140 | Tutorial | Add a tool to your agent (pre-built library) | | New | P1 | Wk 4 | Written + Video | 2d | Cross-ref Tooling cookbook |
| 141 | Tutorial | Enable memory on an agent (Cognis setup) | | New | P1 | Wk 4 | Written + Video | 2d | Cross-ref Cognis docs |
| 142 | Tutorial | Set up Responsible AI guardrails | | New | P1 | Wk 5 | Written + Video | 2d | Cross-ref RAI cookbook |
| 143 | Tutorial | Create a scheduled automation with a trigger | | New | P2 | Wk 5 | Written + Video | 2d | |
| 144 | Tutorial | Build a simple multi-agent workflow (Managerial) | | New | P1 | Wk 6 | Written + Video | 2d | |

#### Tier 2: Feature How-Tos (9)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 145 | Tutorial | How to choose: KB vs KG vs Semantic Model | Prasad | New | P1 | Wk 6 | Written | 1.5d | Most searched question |
| 146 | Tutorial | How to configure chunking and retrieval for RAG | | New | P1 | Wk 6 | Written | 1.5d | |
| 147 | Tutorial | How to build a custom tool (OpenAPI schema) | | New | P1 | Wk 7 | Written | 1.5d | |
| 148 | Tutorial | Workflow Builder: Conditional and Router nodes | | New | P1 | Wk 7 | Written | 1.5d | |
| 149 | Tutorial | How to set up a Text-to-SQL agent | | New | P1 | Wk 7 | Written | 2d | Builds on existing cookbook |
| 150 | Tutorial | Voice Agent: Realtime vs Pipeline engine | | New | P2 | Wk 9 | Written | 1.5d | |
| 151 | Tutorial | How to run Agent Eval and use Agent Hardening | | New | P1 | Wk 10 | Written | 2d | |
| 152 | Tutorial | How to set up an MCP server integration | | New | P2 | Wk 7 | Written | 1.5d | |
| 153 | Tutorial | How to manage your org: roles, invites, audit logs | | New | P2 | Wk 11 | Written | 1.5d | |

#### Tier 3: End-to-End Projects (7)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 154 | Tutorial | Customer support agent: KB + RAI + memory + Slack | Vaibhavi | New | P1 | Wk 8 | Written + Video | 3d | |
| 155 | Tutorial | Research assistant: KG + web tool + structured output | | New | P1 | Wk 9 | Written + Video | 3d | Showcase tutorial |
| 156 | Tutorial | Multi-agent content pipeline: manager + writer + editor | | New | P1 | Wk 9 | Written + Video | 3d | |
| 157 | Tutorial | HR policy copilot: Sharepoint live source + guardrails | | New | P1 | Wk 10 | Written + Video | 3d | Enterprise showcase |
| 158 | Tutorial | Sales intelligence: Text-to-SQL + web research + scheduler | | New | P2 | Wk 10 | Written + Video | 3d | |
| 159 | Tutorial | IT helpdesk: managerial + escalation workflow | | New | P2 | Wk 11 | Written | 3d | |
| 160 | Tutorial | Voice agent for inbound support: Pipeline + KB + Twilio | | New | P2 | Wk 11 | Written | 3d | |

### Studio Academy

#### Path A: Agent Builder (10 modules)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|
| 161 | Academy | A1: How Agent Studio works — architecture, interface, concepts | Felipe | New | P1 | Wk 12 | Module | 1.5d |
| 162 | Academy | A2: Building your first agent — role, goal, instructions, test | | New | P1 | Wk 12 | Module | 1.5d |
| 163 | Academy | A3: Making agents smarter — models, memory, knowledge | | New | P1 | Wk 12 | Module | 1.5d |
| 164 | Academy | A4: Giving agents capabilities — tools, skills, MCP | | New | P1 | Wk 13 | Module | 1.5d |
| 165 | Academy | A5: Multi-agent systems — orchestration and workflows | | New | P1 | Wk 13 | Module | 1.5d |
| 166 | Academy | A6: Automation — triggers, structured output, webhooks | | New | P2 | Wk 13 | Module | 1.5d |
| 167 | Academy | A7: Voice agents — building and deploying | | New | P2 | Wk 14 | Module | 1.5d |
| 168 | Academy | A8: Making agents safe — Responsible AI, hallucination management | | New | P1 | Wk 14 | Module | 1.5d |
| 169 | Academy | A9: Evaluating and improving — Eval, Traces, Agent Hardening | | New | P1 | Wk 14 | Module | 1.5d |
| 170 | Academy | A10: Deploying agents — publishing, sharing, API access | | New | P1 | Wk 15 | Module | 1.5d |

#### Path B: Enterprise Administrator (8 modules)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|
| 171 | Academy | B1: Agent Studio for organizations — scale considerations | Felipe | New | P1 | Wk 14 | Module | 1.5d |
| 172 | Academy | B2: Workspace setup — org structure, sub-orgs, invites | | New | P1 | Wk 14 | Module | 1.5d |
| 173 | Academy | B3: Roles & permissions — Owner, Admin, Member | | New | P1 | Wk 15 | Module | 1.5d |
| 174 | Academy | B4: Security & data controls — RAI policies, PII, audit logs | | New | P1 | Wk 15 | Module | 1.5d |

---

## ADK Track

### S1 — Docs: Getting Started

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Docs | S1 | ADK overview: what it is and when to use vs Studio | Pradipta | Enrich | P1 | Wk 1 | Written | 1d | Add Studio comparison |
| 2 | Docs | S1 | Installation (pip install lyzr-adk) | | Exists | P1 | Wk 1 | Written | 0.5d | |
| 3 | Docs | S1 | Authentication: API key setup | | Exists | P1 | Wk 1 | Written | 0.5d | 3 methods documented |
| 4 | Docs | S1 | Studio class: init and config | | Exists | P2 | Wk 1 | Written | 0.5d | |
| 5 | Docs | S1 | Key concepts overview (quick reference) | | Enrich | P1 | Wk 1 | Written | 1d | Add visual diagram |

### S2 — Docs: Agents

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 6 | Docs | S2 | Agents overview | Pradipta | Exists | P1 | Wk 1 | Written | 0.5d | |
| 7 | Docs | S2 | Creating agents (role, goal, instructions) | | Exists | P1 | Wk 1 | Written | 1d | |
| 8 | Docs | S2 | Running agents | | Exists | P1 | Wk 1 | Written | 0.5d | |
| 9 | Docs | S2 | Managing agents (list, update, delete) | | Exists | P2 | Wk 2 | Written | 0.5d | |
| 10 | Docs | S2 | Agent features (memory, KB, tools, RAI) | | Enrich | P1 | Wk 2 | Written | 1d | Needs links to each feature section |

### S3 — Docs: Knowledge Bases

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|---|
| 11 | Docs | S3 | Knowledge bases overview | Pradipta | Exists | P1 | Wk 2 | Written | 0.5d |
| 12 | Docs | S3 | Creating a knowledge base | | Exists | P1 | Wk 2 | Written | 0.5d |
| 13 | Docs | S3 | Adding documents (PDF, DOCX, websites) | | Exists | P1 | Wk 2 | Written | 0.5d |
| 14 | Docs | S3 | Querying a knowledge base | | Exists | P2 | Wk 2 | Written | 0.5d |
| 15 | Docs | S3 | Managing a knowledge base | | Exists | P2 | Wk 2 | Written | 0.5d |

### S4 — Docs: Memory

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 16 | Docs | S4 | Memory overview | Pradipta | Exists | P1 | Wk 2 | Written | 0.5d | |
| 17 | Docs | S4 | Agent memory (in-session) | | Exists | P1 | Wk 2 | Written | 0.5d | |
| 18 | Docs | S4 | Cognis memory (cross-session) | | New | P1 | Wk 2 | Written | 2d | Page exists in nav but content is EMPTY — critical gap |

### S5 — Docs: Tools

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 19 | Docs | S5 | Tools overview | Pradipta | Exists | P1 | Wk 2 | Written | 0.5d | |
| 20 | Docs | S5 | Creating custom tools (Python function) | | Exists | P1 | Wk 2 | Written | 1d | |
| 21 | Docs | S5 | Tool execution and error handling | | Enrich | P1 | Wk 3 | Written | 1d | Needs error handling patterns |

### S6 — Docs: Contexts

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|---|
| 22 | Docs | S6 | Contexts: what they are and how to use | Pradipta | Exists | P2 | Wk 2 | Written | 0.5d |

### S7 — Docs: RAI Guardrails

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 23 | Docs | S7 | RAI guardrails overview | Pradipta | Exists | P1 | Wk 2 | Written | 0.5d | |
| 24 | Docs | S7 | Creating RAI policies | | Exists | P1 | Wk 2 | Written | 0.5d | |
| 25 | Docs | S7 | RAI features reference | | Exists | P1 | Wk 2 | Written | 0.5d | All 7 guardrail types documented |

### S8 — Docs: Outputs & Streaming

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 26 | Docs | S8 | Structured outputs | Pradipta | Exists | P1 | Wk 3 | Written | 0.5d | |
| 27 | Docs | S8 | File generation | | Exists | P2 | Wk 3 | Written | 0.5d | |
| 28 | Docs | S8 | Image generation | | Exists | P2 | Wk 3 | Written | 0.5d | |
| 29 | Docs | S8 | Streaming responses | | Enrich | P2 | Wk 3 | Written | 1d | Currently thin |

### S9 — Docs: Multi-Agent Patterns (NEW)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 30 | Docs | S9 | Multi-agent overview | Pradipta | New | P1 | Wk 3 | Written | 1.5d | Missing section — significant gap |
| 31 | Docs | S9 | Sequential agent pipelines | | New | P1 | Wk 3 | Written | 1.5d | |
| 32 | Docs | S9 | Parallel agent execution | | New | P1 | Wk 4 | Written | 1.5d | |
| 33 | Docs | S9 | Manager-worker pattern | | New | P1 | Wk 4 | Written | 2d | |
| 34 | Docs | S9 | Handoff and delegation logic | | New | P1 | Wk 4 | Written | 1.5d | |

### S10 — Docs: Studio Integration (NEW)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 35 | Docs | S10 | Using Studio-created KBs from ADK | Pradipta | New | P1 | Wk 4 | Written | 1.5d | Critical for Studio+ADK users |
| 36 | Docs | S10 | Using Studio-created agents from ADK | | New | P1 | Wk 4 | Written | 1.5d | |
| 37 | Docs | S10 | Bidirectional Studio-ADK workflows | | New | P1 | Wk 5 | Written | 2d | |

### S11 — Docs: Testing & Evaluation (NEW)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|---|
| 38 | Docs | S11 | Testing agents with pytest | Pradipta | New | P1 | Wk 5 | Written | 1.5d |
| 39 | Docs | S11 | Mocking tools for testing | | New | P1 | Wk 5 | Written | 1d |
| 40 | Docs | S11 | Integration with Agent Eval | | New | P2 | Wk 5 | Written | 1d |

### S12 — Docs: Deployment (NEW)

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|---|
| 41 | Docs | S12 | Containerizing an ADK agent | Pradipta | New | P1 | Wk 6 | Written | 1.5d |
| 42 | Docs | S12 | Serving via FastAPI endpoint | | New | P1 | Wk 6 | Written | 2d |
| 43 | Docs | S12 | Environment and secrets management | | New | P1 | Wk 6 | Written | 1d |
| 44 | Docs | S12 | Production configuration | | New | P1 | Wk 7 | Written | 1.5d |

### S13 — Docs: Reference

| # | Type | Section | Title / Page Name | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|---|
| 45 | Docs | S13 | Providers reference | Pradipta | Exists | P1 | Wk 1 | Written | 0.5d |
| 46 | Docs | S13 | Responses reference | | Exists | P1 | Wk 1 | Written | 0.5d |
| 47 | Docs | S13 | Exceptions reference | | Exists | P1 | Wk 1 | Written | 0.5d |

### ADK Cookbooks

| # | Type | Section | Title | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|---|
| 48 | Docs | Cookbooks | Choosing a model | Pradipta | Exists | P2 | Wk 2 | Code + Written | 0.5d |
| 49 | Docs | Cookbooks | Customer support agent cookbook | | New | P1 | Wk 5 | Code + Written | 2d |
| 50 | Docs | Cookbooks | Research assistant cookbook | | New | P1 | Wk 6 | Code + Written | 2d |
| 51 | Docs | Cookbooks | Document processing cookbook | | New | P2 | Wk 7 | Code + Written | 2d |
| 52 | Docs | Cookbooks | Multi-agent pipeline cookbook | | New | P1 | Wk 7 | Code + Written | 2d |
| 53 | Docs | Cookbooks | Text-to-SQL agent cookbook | | New | P2 | Wk 8 | Code + Written | 2d |

### ADK Tutorials

#### Tier 1: Quickstarts (6)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 54 | Tutorial | Install the ADK and run your first agent in 5 min | Prasad | New | P1 | Wk 3 | Code + Written | 1d | Fastest path to value |
| 55 | Tutorial | Add a tool to your agent (Python function) | | New | P1 | Wk 3 | Code + Written | 1d | |
| 56 | Tutorial | Connect a Knowledge Base for RAG | | New | P1 | Wk 4 | Code + Written | 1d | |
| 57 | Tutorial | Enable memory across conversations | | New | P1 | Wk 4 | Code + Written | 1d | |
| 58 | Tutorial | Apply RAI guardrails to your agent | | New | P1 | Wk 4 | Code + Written | 1d | |
| 59 | Tutorial | Use Structured Output to get JSON responses | | New | P1 | Wk 5 | Code + Written | 1d | |

#### Tier 2: Feature How-Tos (8)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 60 | Tutorial | How to use Cognis Memory for cross-session context | Prasad | New | P1 | Wk 5 | Code + Written | 1.5d | |
| 61 | Tutorial | How to create and manage KBs via ADK | | New | P2 | Wk 5 | Code + Written | 1.5d | |
| 62 | Tutorial | How to connect to an MCP server | | New | P1 | Wk 6 | Code + Written | 1.5d | |
| 63 | Tutorial | How to use a Studio-created KB from ADK | | New | P1 | Wk 6 | Code + Written | 1.5d | Cross-track tutorial |
| 64 | Tutorial | How to handle streaming responses | | New | P2 | Wk 6 | Code + Written | 1d | |
| 65 | Tutorial | How to generate files and images | | New | P2 | Wk 6 | Code + Written | 1d | |
| 66 | Tutorial | How to write tests for your agent with pytest | | New | P1 | Wk 7 | Code + Written | 2d | |
| 67 | Tutorial | How to deploy your agent as a REST API (FastAPI) | | New | P1 | Wk 7 | Code + Written | 2d | |

#### Tier 3: End-to-End Projects (5)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 68 | Tutorial | Customer support agent: RAI + KB + tool → deployed API | Vaibhavi | New | P1 | Wk 8 | Code + Written | 3d | Flagship ADK project |
| 69 | Tutorial | Research assistant: web search + structured output + memory | | New | P1 | Wk 9 | Code + Written | 3d | |
| 70 | Tutorial | Document processing pipeline: file input → JSON output | | New | P2 | Wk 9 | Code + Written | 3d | |
| 71 | Tutorial | Multi-agent workflow: sequential agents with handoff | | New | P1 | Wk 10 | Code + Written | 3d | |
| 72 | Tutorial | Data analysis agent: Studio Semantic Model + ADK | | New | P2 | Wk 10 | Code + Written | 3d | Studio-ADK integration showcase |

### ADK Academy

#### Path A: ADK Developer (9 modules)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|
| 73 | Academy | A1: ADK orientation — how it relates to Studio, when to use it | Felipe | New | P1 | Wk 9 | Module | 1.5d |
| 74 | Academy | A2: Installation, authentication, your first agent | | New | P1 | Wk 9 | Module | 1.5d |
| 75 | Academy | A3: Models, memory, and knowledge in code | | New | P1 | Wk 10 | Module | 1.5d |
| 76 | Academy | A4: Building and connecting tools | | New | P1 | Wk 10 | Module | 1.5d |
| 77 | Academy | A5: Multi-agent patterns in Python | | New | P1 | Wk 10 | Module | 1.5d |
| 78 | Academy | A6: Responsible AI and safety in code | | New | P1 | Wk 11 | Module | 1.5d |
| 79 | Academy | A7: Structured output, files, and streaming | | New | P2 | Wk 11 | Module | 1.5d |
| 80 | Academy | A8: Testing and evaluation | | New | P1 | Wk 12 | Module | 1.5d |
| 81 | Academy | A9: Deployment and production patterns | | New | P1 | Wk 12 | Module | 1.5d |

#### Path B: Studio + ADK Integration (5 modules)

| # | Type | Title | Owner | Status | Priority | Phase | Format | Est. Effort |
|---|---|---|---|---|---|---|---|---|
| 82 | Academy | B1: When and why to move from Studio to ADK | Felipe | New | P1 | Wk 13 | Module | 1.5d |
| 83 | Academy | B2: Accessing your Studio resources from ADK | | New | P1 | Wk 13 | Module | 1.5d |
| 84 | Academy | B3: Building tools that extend your Studio agents | | New | P1 | Wk 14 | Module | 1.5d |
| 85 | Academy | B4: Multi-agent patterns spanning Studio and ADK | | New | P1 | Wk 14 | Module | 1.5d |
| 86 | Academy | B5: Deployment options for hybrid Studio+ADK systems | | New | P2 | Wk 15 | Module | 1.5d |

---

## Cross-Track Gantt

| # | Track | Type | Milestone / Batch Deliverable | Wk 1 | Wk 2 | Wk 3 | Wk 4 | Wk 5 | Wk 6 | Wk 7 | Wk 8 | Wk 9 | Wk 10 | Wk 11 | Wk 12 | Wk 13 | Wk 14 | Wk 15 | Wk 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Shared | Docs | Product routing page + Core concepts glossary | ● | ● | | | | | | | | | | | | | | |
| 2 | Shared | Docs | Model reference + Security & Compliance Hub | | ● | ● | | | | | | | | | | | | | |
| 3 | Shared | Docs | Combining products guide + Changelog setup | | | ● | ● | | | | | | | | | | | | |
| 4 | Architect | Docs | Overview, Platform, Build, existing pages reviewed | ● | ● | | | | | | | | | | | | | | |
| 5 | Architect | Docs | Agentlets enriched, Architect+Studio bridge expanded | | ● | ● | | | | | | | | | | | | | |
| 6 | Architect | Docs | New pages: Custom integrations, Voice, Simulation | | | ● | ● | | | | | | | | | | | | |
| 7 | Architect | Docs | New pages: Debugging, Security, Teams, Credits FAQ | | | | ● | | | | | | | | | | | | |
| 8 | Architect | Tutorial | Tier 1: 6 video companions published (written text) | | ● | ● | | | | | | | | | | | | | |
| 9 | Architect | Tutorial | Tier 2: 7 video companions published (written text) | | | ● | ● | | | | | | | | | | | | |
| 10 | Architect | Tutorial | Tier 3: 6 video companions + use case guide | | | | ● | ● | | | | | | | | | | | |
| 11 | Architect | Tutorial | Tier 4: 3 new end-to-end project tutorials | | | | | | | ● | ● | ● | | | | | | | |
| 12 | Architect | Tutorial | Bridge tutorial: Architect → Studio → ADK | | | | | | ● | | | | | | | | | | |
| 13 | Architect | Academy | Modules 1–4 built and reviewed | | | | | | ● | ● | | | | | | | | | |
| 14 | Architect | Academy | Modules 5–8 built → Academy live | | | | | | | | ● | ● | ● | | | | | | |
| 15 | Studio | Docs | Phase 1: Orientation + Agents (S1–S2) | ● | ● | ● | | | | | | | | | | | | | |
| 16 | Studio | Docs | Phase 2: Models + Memory + Knowledge (S3–S5) | | | ● | ● | ● | ● | | | | | | | | | | |
| 17 | Studio | Docs | Phase 3: Tools, Skills, Orchestration (S6–S7) | | | | | ● | ● | ● | ● | | | | | | | | |
| 18 | Studio | Docs | Phase 4: Automation + Voice + Safety (S8–S10) | | | | | | | ● | ● | ● | ● | | | | | | |
| 19 | Studio | Docs | Phase 5: Eval + Observability + Admin (S11–S12) | | | | | | | | | ● | ● | ● | ● | | | | |
| 20 | Studio | Tutorial | Tier 1: 7 quickstart tutorials (written + video) | | | ● | ● | ● | ● | | | | | | | | | | |
| 21 | Studio | Tutorial | Tier 2: 9 feature how-to tutorials | | | | | | ● | ● | ● | ● | ● | | | | | | |
| 22 | Studio | Tutorial | Tier 3: 7 end-to-end project tutorials (written+vid) | | | | | | | | ● | ● | ● | ● | ● | ● | ● | | |
| 23 | Studio | Academy | Path A: Agent Builder — Modules 1–10 | | | | | | | | | | | | ● | ● | ● | ● | |
| 24 | Studio | Academy | Path B: Enterprise Admin — Modules 1–8 | | | | | | | | | | | | | | ● | ● | ● |
| 25 | Studio | Academy | Path C: AI Strategy for Business — Modules 1–6 | | | | | | | | | | | | | | ● | ● | ● |
| 26 | ADK | Docs | Fill gaps: Cognis Memory, tool error handling | ● | ● | | | | | | | | | | | | | | |
| 27 | ADK | Docs | Existing sections reviewed + enriched (S1–S8) | ● | ● | ● | | | | | | | | | | | | | |
| 28 | ADK | Docs | New: Multi-Agent Patterns section (S9) | | | ● | ● | | | | | | | | | | | | |
| 29 | ADK | Docs | New: Studio Integration section (S10) | | | | ● | ● | | | | | | | | | | | |
| 30 | ADK | Docs | New: Testing + Deployment sections (S11–S12) | | | | | ● | ● | ● | | | | | | | | | |
| 31 | ADK | Docs | Cookbooks: 5 new recipes added | | | | | ● | ● | ● | ● | | | | | | | | |
| 32 | ADK | Tutorial | Tier 1: 6 quickstart tutorials | | | ● | ● | ● | | | | | | | | | | | |
| 33 | ADK | Tutorial | Tier 2: 8 feature how-to tutorials | | | | | ● | ● | ● | | | | | | | | | |
| 34 | ADK | Tutorial | Tier 3: 5 end-to-end project tutorials (with repos) | | | | | | | | ● | ● | ● | | | | | | |
| 35 | ADK | Academy | Path A: ADK Developer — Modules 1–9 | | | | | | | | | ● | ● | ● | ● | ● | ● | | |
| 36 | ADK | Academy | Path B: Studio + ADK Integration — Modules 1–5 | | | | | | | | | | | | | ● | ● | ● | |
