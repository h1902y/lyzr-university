# Master Tracker — Studio Track (single sheet, paste-ready)

> Studio Track only · one row per lesson · 14 courses / 69 lessons. Mirrors `master-tracker.xlsx` (single tab 'Studio Track'). Originally generated 2026-06-02 from `catalog-data.json`. **Design & Create (folder 07) recorded + shipped 2026-06-16** — 5 lessons live; the plan's two P1 courses merged into one and the deferred topics moved to coming-soon *Advanced Agent Patterns* (folder 08). Foundations (folder 06) packaged. ⚠️ The binary `master-tracker.xlsx` is **not** auto-updated — re-sync it from this markdown when convenient.

| Phase | Course | # | Lesson | Studio feature / tab | Description | Capstone | Est. min | Status | Owner |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Foundations | The Agent Lifecycle | 01 | Welcome to Agent Studio & the lifecycle | Home · Control Plane → Agent Registry | Tour the nav and the Build→Govern→Test→Deploy→Monitor loop; find agents in the Registry. | No | 9 | Not started | TBD |
| Foundations | The Agent Lifecycle | 02 | Build: choose a type & create an agent | Create Agent → Agent | Pick an agent type and create one from role, goal, instructions. | No | 9 | Not started | TBD |
| Foundations | The Agent Lifecycle | 03 | Equip: model, tool, knowledge | Connections → Models, Tools · Knowledge → Knowledge Base | Connect an LLM, attach a tool, add a knowledge base. | No | 9 | Not started | TBD |
| Foundations | The Agent Lifecycle | 04 | Govern: add guardrails | Connections → Guardrails | Apply basic input/output guardrails before it goes anywhere. | No | 9 | Not started | TBD |
| Foundations | The Agent Lifecycle | 05 | Test: run the Simulation Engine | Safety & Evaluations → Simulation Engine | Validate behaviour against scenarios pre-ship. | No | 9 | Not started | TBD |
| Foundations | The Agent Lifecycle | 06 | Deploy: ship it | Control Plane → Deployment Configs, Environments | Deploy to an environment and go live. | No | 9 | Not started | TBD |
| Foundations | The Agent Lifecycle | 07 | Project: one agent, full lifecycle | Monitoring → Traces (+ all above) | Carry one agent through every stage; read its first traces. | Yes | 15 | Not started | TBD |
| Design & Create | Design & Create | 01 | What agent type should I build? | Create Agent — agent-type framework | Choose the simplest architecture that reliably solves it: single Agent vs Manager vs SuperFlow vs Voice. | No | 9 | Live (2026-06-16) | Felipe |
| Design & Create | Design & Create | 02 | Lyzr Manager | Orchestrate → Manager | Compose a team of specialists on the canvas; the manager routes between them itself. | No | 9 | Live (2026-06-16) | Felipe |
| Design & Create | Design & Create | 03 | Managers, part 2 — editing from the agent page | Agent page → Managed Agents | A manager is just an agent — grow its team from the agent page; prove it via the event trail. | No | 9 | Live (2026-06-16) | Felipe |
| Design & Create | Design & Create | 04 | SuperFlow: Invoice Reconciliation | Create Agent → SuperFlow | Document-AI parse, an if-branch, an AI summary, and a durable human approval. | No | 12 | Live (2026-06-16) | Felipe |
| Design & Create | Design & Create | 05 | SuperFlow: Loops | SuperFlow → loop node | Batch a whole list through one flow with the loop node's loop/done outputs. | No | 9 | Live (2026-06-16) | Felipe |
| Design & Create | Advanced Agent Patterns | 01 | The Proxy Agent — when & how | Create Agent → Proxy Agent | Front an external/hosted agent via a proxy, and when that's right. | No | 9 | Not started | TBD |
| Design & Create | Advanced Agent Patterns | 02 | Custom logic with the Code IDE | Code IDE | Write and debug custom agent logic in-product. | No | 9 | Not started | TBD |
| Design & Create | Advanced Agent Patterns | 03 | Workflow — deterministic pipelines | Orchestrate → Workflow | Wire fixed, deterministic multi-step pipelines when the sequence is known up front. | No | 9 | Not started | TBD |
| Design & Create | Advanced Agent Patterns | 04 | From idea to architecture | Create Agent / Orchestrate (overview) | Translate a use case into the right single/multi-agent composition. | No | 9 | Not started | TBD |
| Equip & Connect | Tools, Models & MCP | 01 | Models in depth | Connections → Models | Providers, parameters, routing. | No | 9 | Not started | TBD |
| Equip & Connect | Tools, Models & MCP | 02 | Build custom Tools | Connections → Tools | Tool schemas, auth, testing. | No | 9 | Not started | TBD |
| Equip & Connect | Tools, Models & MCP | 03 | MCP integration | Connections → Tools (MCP) | Connect external MCP tool servers. | No | 9 | Not started | TBD |
| Equip & Connect | Tools, Models & MCP | 04 | Skills | Knowledge → Skills | Package reusable capabilities across agents. | No | 9 | Not started | TBD |
| Equip & Connect | Tools, Models & MCP | 05 | Project: an action agent | Connections → Tools | An agent that reliably calls real systems. | Yes | 15 | Not started | TBD |
| Equip & Connect | Voice Agents | 01 | Voice agent architecture | Voice (top-level) | How voice works in Studio end-to-end. | No | 9 | Not started | TBD |
| Equip & Connect | Voice Agents | 02 | Build your first voice agent | Create Agent → Voice Agent | Create and configure a voice agent. | No | 9 | Not started | TBD |
| Equip & Connect | Voice Agents | 03 | Telephony | Connections → Telephony | Phone/SIP for inbound & outbound. | No | 9 | Not started | TBD |
| Equip & Connect | Voice Agents | 04 | Tuning & the Beta surface | Safety & Evaluations → Voice Agent (Beta) | Tune latency/config; use the Beta surface. | No | 9 | Not started | TBD |
| Equip & Connect | Voice Agents | 05 | Project: customer-service voice agent | Voice · Create Agent → Voice Agent | Ship a working voice line. | Yes | 15 | Not started | TBD |
| Ground in Knowledge | Knowledge & RAG | 01 | RAG in Studio | Knowledge → Knowledge Base | How retrieval-augmented generation works here. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge & RAG | 02 | Build a Knowledge Base | Knowledge → Knowledge Base | Create, structure, attach a KB. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge & RAG | 03 | Document parsing & ingestion | Knowledge → Knowledge Base | File types, chunking, parse quality. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge & RAG | 04 | Data Connectors as live sources | Connections → Data Connectors | Keep a KB synced from external systems. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge & RAG | 05 | Agent memory in depth | Connections → Memory | Memory types, configuration, retrieval. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge & RAG | 06 | Project: document Q&A agent with memory | Knowledge → Knowledge Base · Connections → Memory | End-to-end RAG + memory build. | Yes | 15 | Not started | TBD |
| Ground in Knowledge | Knowledge Graph & Semantic Model | 01 | Beyond vectors: structured knowledge | Knowledge → Knowledge Graph | When a graph/semantic model beats plain RAG. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge Graph & Semantic Model | 02 | Build a Knowledge Graph | Knowledge → Knowledge Graph | Model entities and relationships. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge Graph & Semantic Model | 03 | The Semantic Model | Knowledge → Semantic Model | Define a domain schema for grounded answers. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge Graph & Semantic Model | 04 | Global Context | Knowledge → Global Context | Standing knowledge shared across agents. | No | 9 | Not started | TBD |
| Ground in Knowledge | Knowledge Graph & Semantic Model | 05 | Project: graph-backed analytics agent | Knowledge → Knowledge Graph/Semantic Model | Answer relational questions over structured data. | Yes | 15 | Not started | TBD |
| Govern | Responsible AI & Guardrails | 01 | Responsible AI in Studio | Safety & Evaluations → Responsible AI | The safety surface, overview. | No | 9 | Not started | TBD |
| Govern | Responsible AI & Guardrails | 02 | Guardrails | Connections → Guardrails | Configure input/output guardrails. | No | 9 | Not started | TBD |
| Govern | Responsible AI & Guardrails | 03 | Content safety | Safety & Evaluations → Responsible AI | Toxicity, bias, PII handling. | No | 9 | Not started | TBD |
| Govern | Responsible AI & Guardrails | 04 | Prompt-injection & jailbreak defense | Connections → Guardrails · Responsible AI | Detect and block adversarial input. | No | 9 | Not started | TBD |
| Govern | Responsible AI & Guardrails | 05 | Project: harden an agent | Responsible AI + Guardrails | Apply a full safety layer. | Yes | 15 | Not started | TBD |
| Govern | Policies, Access & Org Governance | 01 | Identity & access | Agent Gateway → IDP Configs · Safety & Evaluations → Groups | SSO via IDP Configs; RBAC via Groups. | No | 9 | Not started | TBD |
| Govern | Policies, Access & Org Governance | 02 | Agent Policies | Safety & Evaluations → Agent Policies | Define and enforce governance policies. | No | 9 | Not started | TBD |
| Govern | Policies, Access & Org Governance | 03 | Approval Flows | Safety & Evaluations → Approval Flows | Human-in-the-loop approvals. | No | 9 | Not started | TBD |
| Govern | Policies, Access & Org Governance | 04 | OGI | Safety & Evaluations → OGI | Org-wide governance intelligence. | No | 9 | Not started | TBD |
| Govern | Policies, Access & Org Governance | 05 | Project: govern an agent for an org | Agent Policies · Groups · IDP Configs | Apply policies, access, approvals to a deployment. | Yes | 15 | Not started | TBD |
| Test & Improve | Test & Simulate | 01 | Why test before you ship | Safety & Evaluations (overview) | The quality loop and Studio's tooling. | No | 9 | Not started | TBD |
| Test & Improve | Test & Simulate | 02 | The Simulation Engine | Safety & Evaluations → Simulation Engine | Test agents against scenarios pre-ship. | No | 9 | Not started | TBD |
| Test & Improve | Test & Simulate | 03 | Building test scenarios | Safety & Evaluations → Simulation Engine | Author scenario suites that exercise edge cases. | No | 9 | Not started | TBD |
| Test & Improve | Test & Simulate | 04 | Agent Eval — defining metrics | Safety & Evaluations → Agent Eval | Define metrics and what 'good' means. | No | 9 | Not started | TBD |
| Test & Improve | Test & Simulate | 05 | Project: a pre-ship test suite | Simulation Engine + Agent Eval | Stand up a test+eval suite for an agent. | Yes | 15 | Not started | TBD |
| Test & Improve | Evaluate & Improve | 01 | Running evaluations at scale | Safety & Evaluations → Agent Eval | Run evals across datasets and versions. | No | 9 | Not started | TBD |
| Test & Improve | Evaluate & Improve | 02 | Reading eval results & regressions | Safety & Evaluations → Agent Eval | Interpret results; catch regressions. | No | 9 | Not started | TBD |
| Test & Improve | Evaluate & Improve | 03 | The Improvement Engine | Safety & Evaluations → Improvement Engine | Close the loop; iterate on failures. | No | 9 | Not started | TBD |
| Test & Improve | Evaluate & Improve | 04 | Project: eval-driven improvement cycle | Agent Eval + Improvement Engine | Measure → fix → re-measure. | Yes | 15 | Not started | TBD |
| Deploy & Operate | Deploy & Scale | 01 | Deployment Configs | Control Plane → Deployment Configs | Ship an agent — the how and why it matters. | No | 9 | Not started | TBD |
| Deploy & Operate | Deploy & Scale | 02 | Environments & promotion | Control Plane → Environments | Promote dev → staging → prod. | No | 9 | Not started | TBD |
| Deploy & Operate | Deploy & Scale | 03 | The Agent Gateway | Agent Gateway → Bundles, Agents | Expose agents as governed APIs via bundles. | No | 9 | Not started | TBD |
| Deploy & Operate | Deploy & Scale | 04 | The Control Plane Dashboard | Control Plane → Dashboard | Operate your fleet from the dashboard. | No | 9 | Not started | TBD |
| Deploy & Operate | Deploy & Scale | 05 | Project: multi-env, gateway deployment | Environments + Agent Gateway | Promote and expose an agent end-to-end. | Yes | 15 | Not started | TBD |
| Deploy & Operate | Monitor & Observe | 01 | Traces | Monitoring → Traces | Read spans; debug a single run. | No | 9 | Not started | TBD |
| Deploy & Operate | Monitor & Observe | 02 | Transcripts | Monitoring → Transcripts | Review conversations at scale. | No | 9 | Not started | TBD |
| Deploy & Operate | Monitor & Observe | 03 | Reports | Monitoring → Reports | Operational dashboards and metrics. | No | 9 | Not started | TBD |
| Deploy & Operate | Monitor & Observe | 04 | Project: diagnose & fix from traces | Monitoring → Traces | Find and fix a misbehaving agent. | Yes | 15 | Not started | TBD |
| Deploy & Operate | Reuse & Distribute | 01 | Agent Templates | Control Plane → Agent Templates | Start an agent from a template. | No | 9 | Not started | TBD |
| Deploy & Operate | Reuse & Distribute | 02 | Blueprints | Blueprints | Reusable agent blueprints. | No | 9 | Not started | TBD |
| Deploy & Operate | Reuse & Distribute | 03 | Lyzr App Store | Lyzr App Store | Discover and install prebuilt agents. | No | 9 | Not started | TBD |
| Deploy & Operate | Reuse & Distribute | 04 | Publish your own | Lyzr App Store · Blueprints | Package and publish an agent for reuse. | No | 9 | Not started | TBD |
