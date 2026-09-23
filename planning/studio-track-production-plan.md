# Studio Track — Production Plan (Agent-Lifecycle model)

> Recording plan for the 14-course / 71-lesson Studio Track (see `studio-track-plan.md`). Per-lesson Studio feature + objective + recording minutes, pipeline-viability check, and a week-wise schedule. Authored 2026-06-02. No Studio recordings yet — this is the plan to record against.

> *Final* = finished runtime; *Record* = raw capture (~2.4× final). Post ≈ 30 min/lesson via the `descript-to-thinkific` pipeline.


## Studio: The Agent Lifecycle · Foundations

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Welcome to Agent Studio & the lifecycle | Home · Control Plane → Agent Registry | tour the nav and the Build→Govern→Test→Deploy→Monitor loop; find agents in the Registry. | 9m | 20m |
| 02 | Build: choose a type & create an agent | Create Agent → Agent | pick an agent type and create one from role, goal, instructions. | 9m | 20m |
| 03 | Equip: model, tool, knowledge | Connections → Models, Tools · Knowledge → Knowledge Base | connect an LLM, attach a tool, add a knowledge base. | 9m | 20m |
| 04 | Govern: add guardrails | Connections → Guardrails | apply basic input/output guardrails before it goes anywhere. | 9m | 20m |
| 05 | Test: run the Simulation Engine | Safety & Evaluations → Simulation Engine | validate behaviour against scenarios pre-ship. | 9m | 20m |
| 06 | Deploy: ship it | Control Plane → Deployment Configs, Environments | deploy to an environment and go live. | 9m | 20m |
| 07 | Project: one agent, full lifecycle | Monitoring → Traces (+ all above) | carry one agent through every stage; read its first traces. | 15m | 35m |

*7 lessons · 69m final · 155m record · ~210m post*


## Studio: Choosing & Building Agents · Design & Create

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | What agent type should I build? | Create Agent (Agent · Voice Agent · SuperFlow · Proxy Agent) | decision framework: single Agent vs Manager vs SuperFlow vs Workflow vs Proxy vs Voice. | 9m | 20m |
| 02 | Build a single Agent | Create Agent → Agent | configure role/goal/instructions and run it. | 9m | 20m |
| 03 | The Proxy Agent — when & how | Create Agent → Proxy Agent | front an external/hosted agent via a proxy, and when that's right. | 9m | 20m |
| 04 | Custom logic with the Code IDE | Safety & Evaluations → Code IDE | write and debug custom agent logic in-product. | 9m | 20m |
| 05 | From idea to architecture | Create Agent / Orchestrate (overview) | translate a use case into the right single/multi-agent composition. | 9m | 20m |
| 06 | Project: build the right agent | Create Agent → Agent/Proxy | choose a type and build it end-to-end for a brief. | 15m | 35m |

*6 lessons · 60m final · 135m record · ~180m post*


## Studio: Orchestration & Multi-Agent · Design & Create

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | When one agent isn't enough | Orchestrate (overview) | patterns for splitting work across agents. | 9m | 20m |
| 02 | Lyzr Manager | Orchestrate → Lyzr Manager | coordinate sub-agents with a manager agent. | 9m | 20m |
| 03 | Workflow | Orchestrate → Workflow | deterministic multi-step pipelines. | 9m | 20m |
| 04 | SuperFlow | Orchestrate → SuperFlow | dynamic multi-agent flows, routing, parallelism. | 9m | 20m |
| 05 | Project: a multi-agent system | Orchestrate → Manager/SuperFlow | compose a team of agents to a goal. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Tools, Models & MCP · Equip & Connect

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Models in depth | Connections → Models | providers, parameters, routing. | 9m | 20m |
| 02 | Build custom Tools | Connections → Tools | tool schemas, auth, testing. | 9m | 20m |
| 03 | MCP integration | Connections → Tools (MCP) | connect external MCP tool servers. | 9m | 20m |
| 04 | Skills | Knowledge → Skills | package reusable capabilities across agents. | 9m | 20m |
| 05 | Project: an action agent | Connections → Tools | an agent that reliably calls real systems. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Voice Agents · Equip & Connect

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Voice agent architecture | Voice (top-level) | how voice works in Studio end-to-end. | 9m | 20m |
| 02 | Build your first voice agent | Create Agent → Voice Agent | create and configure a voice agent. | 9m | 20m |
| 03 | Telephony | Connections → Telephony | phone/SIP for inbound & outbound. | 9m | 20m |
| 04 | Tuning & the Beta surface | Safety & Evaluations → Voice Agent (Beta) | tune latency/config; use the Beta surface. | 9m | 20m |
| 05 | Project: customer-service voice agent | Voice · Create Agent → Voice Agent | ship a working voice line. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Knowledge & RAG · Ground in Knowledge

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | RAG in Studio | Knowledge → Knowledge Base | how retrieval-augmented generation works here. | 9m | 20m |
| 02 | Build a Knowledge Base | Knowledge → Knowledge Base | create, structure, attach a KB. | 9m | 20m |
| 03 | Document parsing & ingestion | Knowledge → Knowledge Base | file types, chunking, parse quality. | 9m | 20m |
| 04 | Data Connectors as live sources | Connections → Data Connectors | keep a KB synced from external systems. | 9m | 20m |
| 05 | Agent memory in depth | Connections → Memory | memory types, configuration, retrieval. | 9m | 20m |
| 06 | Project: document Q&A agent with memory | Knowledge → Knowledge Base · Connections → Memory | end-to-end RAG + memory build. | 15m | 35m |

*6 lessons · 60m final · 135m record · ~180m post*


## Studio: Knowledge Graph & Semantic Model · Ground in Knowledge

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Beyond vectors: structured knowledge | Knowledge → Knowledge Graph | when a graph/semantic model beats plain RAG. | 9m | 20m |
| 02 | Build a Knowledge Graph | Knowledge → Knowledge Graph | model entities and relationships. | 9m | 20m |
| 03 | The Semantic Model | Knowledge → Semantic Model | define a domain schema for grounded answers. | 9m | 20m |
| 04 | Global Context | Knowledge → Global Context | standing knowledge shared across agents. | 9m | 20m |
| 05 | Project: graph-backed analytics agent | Knowledge → Knowledge Graph/Semantic Model | answer relational questions over structured data. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Responsible AI & Guardrails · Govern

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Responsible AI in Studio | Safety & Evaluations → Responsible AI | the safety surface, overview. | 9m | 20m |
| 02 | Guardrails | Connections → Guardrails | configure input/output guardrails. | 9m | 20m |
| 03 | Content safety | Safety & Evaluations → Responsible AI | toxicity, bias, PII handling. | 9m | 20m |
| 04 | Prompt-injection & jailbreak defense | Connections → Guardrails · Responsible AI | detect and block adversarial input. | 9m | 20m |
| 05 | Project: harden an agent | Responsible AI + Guardrails | apply a full safety layer. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Policies, Access & Org Governance · Govern

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Identity & access | Agent Gateway → IDP Configs · Safety & Evaluations → Groups | sSO via IDP Configs; RBAC via Groups. | 9m | 20m |
| 02 | Agent Policies | Safety & Evaluations → Agent Policies | define and enforce governance policies. | 9m | 20m |
| 03 | Approval Flows | Safety & Evaluations → Approval Flows | human-in-the-loop approvals. | 9m | 20m |
| 04 | OGI | Safety & Evaluations → OGI | org-wide governance intelligence. | 9m | 20m |
| 05 | Project: govern an agent for an org | Agent Policies · Groups · IDP Configs | apply policies, access, approvals to a deployment. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Test & Simulate · Test & Improve

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Why test before you ship | Safety & Evaluations (overview) | the quality loop and Studio's tooling. | 9m | 20m |
| 02 | The Simulation Engine | Safety & Evaluations → Simulation Engine | test agents against scenarios pre-ship. | 9m | 20m |
| 03 | Building test scenarios | Safety & Evaluations → Simulation Engine | author scenario suites that exercise edge cases. | 9m | 20m |
| 04 | Agent Eval — defining metrics | Safety & Evaluations → Agent Eval | define metrics and what 'good' means. | 9m | 20m |
| 05 | Project: a pre-ship test suite | Simulation Engine + Agent Eval | stand up a test+eval suite for an agent. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Evaluate & Improve · Test & Improve

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Running evaluations at scale | Safety & Evaluations → Agent Eval | run evals across datasets and versions. | 9m | 20m |
| 02 | Reading eval results & regressions | Safety & Evaluations → Agent Eval | interpret results; catch regressions. | 9m | 20m |
| 03 | The Improvement Engine | Safety & Evaluations → Improvement Engine | close the loop; iterate on failures. | 9m | 20m |
| 04 | Project: eval-driven improvement cycle | Agent Eval + Improvement Engine | measure → fix → re-measure. | 15m | 35m |

*4 lessons · 42m final · 95m record · ~120m post*


## Studio: Deploy & Scale · Deploy & Operate

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Deployment Configs | Control Plane → Deployment Configs | ship an agent — the how and why it matters. | 9m | 20m |
| 02 | Environments & promotion | Control Plane → Environments | promote dev → staging → prod. | 9m | 20m |
| 03 | The Agent Gateway | Agent Gateway → Bundles, Agents | expose agents as governed APIs via bundles. | 9m | 20m |
| 04 | The Control Plane Dashboard | Control Plane → Dashboard | operate your fleet from the dashboard. | 9m | 20m |
| 05 | Project: multi-env, gateway deployment | Environments + Agent Gateway | promote and expose an agent end-to-end. | 15m | 35m |

*5 lessons · 51m final · 115m record · ~150m post*


## Studio: Monitor & Observe · Deploy & Operate

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Traces | Monitoring → Traces | read spans; debug a single run. | 9m | 20m |
| 02 | Transcripts | Monitoring → Transcripts | review conversations at scale. | 9m | 20m |
| 03 | Reports | Monitoring → Reports | operational dashboards and metrics. | 9m | 20m |
| 04 | Project: diagnose & fix from traces | Monitoring → Traces | find and fix a misbehaving agent. | 15m | 35m |

*4 lessons · 42m final · 95m record · ~120m post*


## Studio: Reuse & Distribute · Deploy & Operate

| # | Lesson | Studio feature / tab | Objective (learner can…) | Final | Record |
|---|---|---|---|---|---|
| 01 | Agent Templates | Control Plane → Agent Templates | start an agent from a template. | 9m | 20m |
| 02 | Blueprints | Blueprints | reusable agent blueprints. | 9m | 20m |
| 03 | Lyzr App Store | Lyzr App Store | discover and install prebuilt agents. | 9m | 20m |
| 04 | Publish your own | Lyzr App Store · Blueprints | package and publish an agent for reuse. | 9m | 20m |

*4 lessons · 36m final · 80m record · ~120m post*


## Totals

**71 lessons · 717m final (~11.9h) · 1615m record (~26.9h) · 2130m post (~35.5h).**


## Pipeline viability

The `descript-to-thinkific` pipeline is proven (shipped 19 ADK lessons). Studio lessons are screen-recorded product walkthroughs — simpler to capture than code-alongs. ~27h of raw recording for the whole track is modest; recording is not the constraint. Real constraints, in order: (1) **product churn on 'New' screens** — Simulation Engine, OGI, Code IDE, Voice Agent (Beta), SuperFlow — record last, version-stamp, budget re-cuts; (2) single-instructor throughput (Felipe) — independent courses can parallelize to a second SME; (3) **sandbox + demo-data readiness** (Week 0) — hard dependency; (4) editor capacity (~12–15 lessons/wk clears post). **Verdict: viable.**


## Week-wise schedule

> Lifecycle order; 'New'-heavy lessons recorded late within their week. Week-wise overrides the usual phase-wise convention (operational schedule).

| Week | Record | Lessons |
|---|---|---|
| W0 | Prep — sandbox org + demo data + templates | — |
| W1 | Foundations — The Agent Lifecycle | 7 |
| W2 | Choosing & Building Agents | 6 |
| W3 | Tools, Models & MCP + Voice Agents | 10 |
| W4 | Knowledge & RAG | 6 |
| W5 | Knowledge Graph & Semantic + Orchestration | 10 |
| W6 | Responsible AI & Guardrails + Policies/Access/Governance | 10 |
| W7 | Test & Simulate + Evaluate & Improve | 9 |
| W8 | Deploy & Scale + Monitor & Observe | 9 |
| W9 | Reuse & Distribute | 4 |
| W10 | QA, re-cuts, publish wave | — |

**71 lessons across 9 recording weeks** (~8/wk) + prep + QA → ~11-week program. Publish in waves: Foundations + Design&Create first.
