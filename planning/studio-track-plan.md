# Studio Track — Course Plan (Agent-Lifecycle model)

> Restructured 2026-06-02 around the **agent lifecycle** a builder lives: **Build → Govern → Test → Deploy → Monitor**, rebalanced into **6 phases + a Foundations journey course** so no phase is jumbo and none is thin. Levels (101/201/401) retired. Mapped against the live Agent Studio surface (`studio-feature-map.md`).

> **14 courses · 71 lessons.** Every lesson is tagged with the **Studio feature/tab** it covers — coverage is verifiable lesson-by-lesson (41/41 screens, zero orphans). Status: curriculum design; no Studio recordings yet.


## Lifecycle → phases

| Your step | Phase(s) | Courses |
|---|---|---|
| Build | Design & Create · Equip & Connect · Ground in Knowledge | 6 |
| Govern | Govern | 2 |
| Test | Test & Improve | 2 |
| Deploy + Monitor | Deploy & Operate | 3 |
| *(orientation)* | Foundations journey | 1 |

**Phase balance (lessons):** Design&Create 11 · Equip&Connect 10 · Ground 11 · Govern 10 · Test&Improve 9 · Deploy&Operate 13 (+ Foundations 7).


## ◆ Foundations

### Studio: The Agent Lifecycle (7) · `track-studio-foundations`
*The whole agent lifecycle on one agent — orient in Studio, then build, govern, test, deploy, and monitor a single agent end to end.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Welcome to Agent Studio & the lifecycle | Home · Control Plane → Agent Registry | Tour the nav and the Build→Govern→Test→Deploy→Monitor loop; find agents in the Registry. |
| 02 | Build: choose a type & create an agent | Create Agent → Agent | Pick an agent type and create one from role, goal, instructions. |
| 03 | Equip: model, tool, knowledge | Connections → Models, Tools · Knowledge → Knowledge Base | Connect an LLM, attach a tool, add a knowledge base. |
| 04 | Govern: add guardrails | Connections → Guardrails | Apply basic input/output guardrails before it goes anywhere. |
| 05 | Test: run the Simulation Engine | Safety & Evaluations → Simulation Engine | Validate behaviour against scenarios pre-ship. |
| 06 | Deploy: ship it | Control Plane → Deployment Configs, Environments | Deploy to an environment and go live. |
| 07 | Project: one agent, full lifecycle | Monitoring → Traces (+ all above) | Carry one agent through every stage; read its first traces. |


## Phase · Design & Create

> **As shipped (2026-06-16).** Recorded as **one** course — **Studio: Design & Create** (folder 07, `track-studio-choosing-building`, 5 lessons, live) — not the two planned below. Per Felipe: SuperFlow split into a main walkthrough (Invoice Reconciliation) + a short Loops video; the "Project" slot became a second Manager video (agent-page editing); the standalone single-Agent lesson was dropped (covered in Foundations), so it opens with the agent-type framework. As-built lessons: **01** What agent type should I build? · **02** Lyzr Manager · **03** Managers, part 2 (agent-page editing) · **04** SuperFlow: Invoice Reconciliation · **05** SuperFlow: Loops. The deferred topics (Proxy Agent, Code IDE, Workflow, idea→architecture) moved to a coming-soon **Studio: Advanced Agent Patterns** (folder 08, `track-studio-orchestration`). Course count stays 14; phase total is now 9 lessons (was 11). `catalog-data.json` + `master-tracker-replacement.md` are source of truth for shipped state; the two tables below are the original design record.

### Studio: Choosing & Building Agents (6) · `track-studio-choosing-building`
*Decide what to build and build it — the agent-type decision framework, building a single agent, the Proxy Agent, and custom logic in the Code IDE.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | What agent type should I build? | Create Agent (Agent · Voice Agent · SuperFlow · Proxy Agent) | Decision framework: single Agent vs Manager vs SuperFlow vs Workflow vs Proxy vs Voice. |
| 02 | Build a single Agent | Create Agent → Agent | Configure role/goal/instructions and run it. |
| 03 | The Proxy Agent — when & how | Create Agent → Proxy Agent | Front an external/hosted agent via a proxy, and when that's right. |
| 04 | Custom logic with the Code IDE | Safety & Evaluations → Code IDE | Write and debug custom agent logic in-product. |
| 05 | From idea to architecture | Create Agent / Orchestrate (overview) | Translate a use case into the right single/multi-agent composition. |
| 06 | Project: build the right agent | Create Agent → Agent/Proxy | Choose a type and build it end-to-end for a brief. |

### Studio: Orchestration & Multi-Agent (5) · `track-studio-orchestration`
*Build systems of agents — orchestration patterns, the Lyzr Manager, deterministic Workflows, and dynamic SuperFlow.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | When one agent isn't enough | Orchestrate (overview) | Patterns for splitting work across agents. |
| 02 | Lyzr Manager | Orchestrate → Lyzr Manager | Coordinate sub-agents with a manager agent. |
| 03 | Workflow | Orchestrate → Workflow | Deterministic multi-step pipelines. |
| 04 | SuperFlow | Orchestrate → SuperFlow | Dynamic multi-agent flows, routing, parallelism. |
| 05 | Project: a multi-agent system | Orchestrate → Manager/SuperFlow | Compose a team of agents to a goal. |


## Phase · Equip & Connect

### Studio: Tools, Models & MCP (5) · `track-studio-tools-models-mcp`
*Give agents intelligence and actions — models in depth, custom tools, MCP integration, and reusable skills.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Models in depth | Connections → Models | Providers, parameters, routing. |
| 02 | Build custom Tools | Connections → Tools | Tool schemas, auth, testing. |
| 03 | MCP integration | Connections → Tools (MCP) | Connect external MCP tool servers. |
| 04 | Skills | Knowledge → Skills | Package reusable capabilities across agents. |
| 05 | Project: an action agent | Connections → Tools | An agent that reliably calls real systems. |

### Studio: Voice Agents (5) · `track-studio-voice`
*Build agents that talk — voice architecture, your first voice agent, telephony, and tuning the Beta surface.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Voice agent architecture | Voice (top-level) | How voice works in Studio end-to-end. |
| 02 | Build your first voice agent | Create Agent → Voice Agent | Create and configure a voice agent. |
| 03 | Telephony | Connections → Telephony | Phone/SIP for inbound & outbound. |
| 04 | Tuning & the Beta surface | Safety & Evaluations → Voice Agent (Beta) | Tune latency/config; use the Beta surface. |
| 05 | Project: customer-service voice agent | Voice · Create Agent → Voice Agent | Ship a working voice line. |


## Phase · Ground in Knowledge

### Studio: Knowledge & RAG (6) · `track-studio-knowledge-rag`
*Ground agents in your data — RAG, knowledge bases, document parsing, live data connectors, and agent memory.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | RAG in Studio | Knowledge → Knowledge Base | How retrieval-augmented generation works here. |
| 02 | Build a Knowledge Base | Knowledge → Knowledge Base | Create, structure, attach a KB. |
| 03 | Document parsing & ingestion | Knowledge → Knowledge Base | File types, chunking, parse quality. |
| 04 | Data Connectors as live sources | Connections → Data Connectors | Keep a KB synced from external systems. |
| 05 | Agent memory in depth | Connections → Memory | Memory types, configuration, retrieval. |
| 06 | Project: document Q&A agent with memory | Knowledge → Knowledge Base · Connections → Memory | End-to-end RAG + memory build. |

### Studio: Knowledge Graph & Semantic Model (5) · `track-studio-knowledge-graph`
*Structured knowledge — when graphs beat vectors, building a knowledge graph, the semantic model, and global context.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Beyond vectors: structured knowledge | Knowledge → Knowledge Graph | When a graph/semantic model beats plain RAG. |
| 02 | Build a Knowledge Graph | Knowledge → Knowledge Graph | Model entities and relationships. |
| 03 | The Semantic Model | Knowledge → Semantic Model | Define a domain schema for grounded answers. |
| 04 | Global Context | Knowledge → Global Context | Standing knowledge shared across agents. |
| 05 | Project: graph-backed analytics agent | Knowledge → Knowledge Graph/Semantic Model | Answer relational questions over structured data. |


## Phase · Govern

### Studio: Responsible AI & Guardrails (5) · `track-studio-responsible-ai`
*Make agents safe — the Responsible AI surface, guardrails, content safety, and prompt-injection defense.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Responsible AI in Studio | Safety & Evaluations → Responsible AI | The safety surface, overview. |
| 02 | Guardrails | Connections → Guardrails | Configure input/output guardrails. |
| 03 | Content safety | Safety & Evaluations → Responsible AI | Toxicity, bias, PII handling. |
| 04 | Prompt-injection & jailbreak defense | Connections → Guardrails · Responsible AI | Detect and block adversarial input. |
| 05 | Project: harden an agent | Responsible AI + Guardrails | Apply a full safety layer. |

### Studio: Policies, Access & Org Governance (5) · `track-studio-governance`
*Govern agents across an org — identity & access, agent policies, human approval flows, and org-wide governance intelligence.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Identity & access | Agent Gateway → IDP Configs · Safety & Evaluations → Groups | SSO via IDP Configs; RBAC via Groups. |
| 02 | Agent Policies | Safety & Evaluations → Agent Policies | Define and enforce governance policies. |
| 03 | Approval Flows | Safety & Evaluations → Approval Flows | Human-in-the-loop approvals. |
| 04 | OGI | Safety & Evaluations → OGI | Org-wide governance intelligence. |
| 05 | Project: govern an agent for an org | Agent Policies · Groups · IDP Configs | Apply policies, access, approvals to a deployment. |


## Phase · Test & Improve

### Studio: Test & Simulate (5) · `track-studio-test-simulate`
*Validate before you ship — why testing matters, the Simulation Engine, building scenarios, and defining eval metrics.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Why test before you ship | Safety & Evaluations (overview) | The quality loop and Studio's tooling. |
| 02 | The Simulation Engine | Safety & Evaluations → Simulation Engine | Test agents against scenarios pre-ship. |
| 03 | Building test scenarios | Safety & Evaluations → Simulation Engine | Author scenario suites that exercise edge cases. |
| 04 | Agent Eval — defining metrics | Safety & Evaluations → Agent Eval | Define metrics and what 'good' means. |
| 05 | Project: a pre-ship test suite | Simulation Engine + Agent Eval | Stand up a test+eval suite for an agent. |

### Studio: Evaluate & Improve (4) · `track-studio-evaluate-improve`
*Close the quality loop — run evals at scale, read results and regressions, and iterate with the Improvement Engine.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Running evaluations at scale | Safety & Evaluations → Agent Eval | Run evals across datasets and versions. |
| 02 | Reading eval results & regressions | Safety & Evaluations → Agent Eval | Interpret results; catch regressions. |
| 03 | The Improvement Engine | Safety & Evaluations → Improvement Engine | Close the loop; iterate on failures. |
| 04 | Project: eval-driven improvement cycle | Agent Eval + Improvement Engine | Measure → fix → re-measure. |


## Phase · Deploy & Operate

### Studio: Deploy & Scale (5) · `track-studio-deploy-scale`
*Ship and scale — deployment configs, environment promotion, the Agent Gateway, and the control-plane dashboard.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Deployment Configs | Control Plane → Deployment Configs | Ship an agent — the how and why it matters. |
| 02 | Environments & promotion | Control Plane → Environments | Promote dev → staging → prod. |
| 03 | The Agent Gateway | Agent Gateway → Bundles, Agents | Expose agents as governed APIs via bundles. |
| 04 | The Control Plane Dashboard | Control Plane → Dashboard | Operate your fleet from the dashboard. |
| 05 | Project: multi-env, gateway deployment | Environments + Agent Gateway | Promote and expose an agent end-to-end. |

### Studio: Monitor & Observe (4) · `track-studio-observability`
*See what agents do in production — traces, transcripts, and operational reports.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Traces | Monitoring → Traces | Read spans; debug a single run. |
| 02 | Transcripts | Monitoring → Transcripts | Review conversations at scale. |
| 03 | Reports | Monitoring → Reports | Operational dashboards and metrics. |
| 04 | Project: diagnose & fix from traces | Monitoring → Traces | Find and fix a misbehaving agent. |

### Studio: Reuse & Distribute (4) · `track-studio-reuse-distribute`
*Scale through reuse — agent templates, blueprints, the Lyzr App Store, and publishing your own agents.*

| # | Lesson | Studio feature / tab | Description |
|---|---|---|---|
| 01 | Agent Templates | Control Plane → Agent Templates | Start an agent from a template. |
| 02 | Blueprints | Blueprints | Reusable agent blueprints. |
| 03 | Lyzr App Store | Lyzr App Store | Discover and install prebuilt agents. |
| 04 | Publish your own | Lyzr App Store · Blueprints | Package and publish an agent for reuse. |


## Coverage matrix — screen → course

Every lesson's `Studio feature / tab` column above cites its screen. All 41 nav leaf-screens appear as a primary feature on ≥1 lesson. Summary by area:

- **Create Agent** Agent→Foundations/Choosing · Voice Agent→Voice · SuperFlow→Orchestration · Proxy Agent→Choosing
- **Orchestrate** Lyzr Manager/Workflow/SuperFlow→Orchestration
- **Knowledge** Knowledge Base→Knowledge&RAG · Knowledge Graph/Semantic Model/Global Context→Knowledge Graph & Semantic · Skills→Tools/Models/MCP
- **Safety & Evaluations** Responsible AI→Responsible AI · Guardrails→Responsible AI · Simulation Engine/Agent Eval→Test & Simulate · Improvement Engine→Evaluate & Improve · Agent Policies/Approval Flows/Groups/OGI→Governance · Code IDE→Choosing · Voice Agent (Beta)→Voice
- **Monitoring** Traces/Transcripts/Reports→Monitor & Observe
- **Connections** Models/Tools→Tools/Models/MCP · Data Connectors/Memory→Knowledge&RAG · Guardrails→Responsible AI · Telephony→Voice
- **Control Plane** Dashboard/Deployment Configs/Environments→Deploy & Scale · Agent Registry→Foundations · Agent Templates→Reuse & Distribute
- **Agent Gateway** Bundles/Agents→Deploy & Scale · IDP Configs→Governance
- **Blueprints · Lyzr App Store**→Reuse & Distribute

## Rollout (phase-wise)

Record in lifecycle order — **Foundations → Design&Create → Equip → Ground → Govern → Test → Deploy&Operate** — publishing in waves. Record the fast-moving 'New' screens last (Simulation Engine, OGI, Code IDE, Voice Agent Beta, SuperFlow); expect re-cuts. Per-course capstone projects throughout; Foundations ends in a full-lifecycle project.
