import os

master_file = '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/master_courses_lesson_notes.md'

with open(master_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Generate full detailed markdown content for Chapter 02 & Chapter 03 of Course 1
ch2_ch3_content = """

---

## 📄 File: `09-designing-knowledge-bases-and-source-selection.md`

# Designing Knowledge Bases & Source Selection

*Lesson 09 · Course 1 Chapter 2 — Enterprise Knowledge Base Masterclass*

## What you'll learn

- Understand how enterprise knowledge bases differ from standard vector databases.
- Select appropriate data sources (PDFs, Notion, SQL, Web Docs) for agent grounding.
- Architect domain-specific knowledge taxonomies to minimize retrieval hallucinations.

## Key concepts

- **Data Source Selection:** Categorizing enterprise data by update frequency, structure, and sensitivity.
- **Knowledge Taxonomy:** Structuring data collections into logical spaces (Finance, HR, Tech Specs) so agents query targeted namespaces.
- **Pre-Retrieval Cleaning:** Removing headers, footers, boilerplate disclaimers, and duplicate content before embedding.

## Hands-on Implementation

1. Identify unstructured documents (PDF manuals, SOPs) vs. structured tabular files (CSV, Excel).
2. Configure collection namespaces in Lyzr Studio or ADK.
3. Validate data cleanliness by inspecting raw extracted text chunks.

## Try this

1. Audit 3 document types in your department. Determine which require real-time syncing vs. static vector indexing.
2. Define metadata tags (department, classification level, date) for your primary document repository.

## Video Transcript

Welcome to Lesson 09 of the Enterprise Knowledge Base Masterclass. When building production agents, the quality of your agent's answers is directly capped by the quality of your knowledge base. In this lesson, we cover how to evaluate enterprise data sources, remove noise prior to ingestion, and design targeted knowledge taxonomies that eliminate retrieval hallucinations.

---

## 📄 File: `10-pdf-parsing-strategies-and-tabular-extraction.md`

# PDF Parsing Strategies & Tabular Extraction

*Lesson 10 · Course 1 Chapter 2 — Enterprise Knowledge Base Masterclass*

## What you'll learn

- Compare OCR, layout-aware parsing, and vision-based document extraction.
- Extract complex multi-column layouts, embedded images, and financial tables from PDFs.
- Standardize extracted tables into Markdown or JSON representations for vector indexing.

## Key concepts

- **Layout-Aware Parsing:** Preserving visual reading order, headers, and section hierarchies in complex PDF documents.
- **Tabular Extraction:** Converting grid tables into explicit Markdown tables (`| Header | Value |`) to maintain row-column relationships during chunking.
- **Vision-Based Parsing:** Utilizing vision models (Lyzr Vision / GPT-4o) for scanned, low-contrast, or handwriting-heavy PDFs.

## Hands-on Implementation

1. Ingest a financial report PDF containing complex data tables into Lyzr Knowledge Base.
2. Inspect the parsed Markdown output to ensure table rows are not split across arbitrary line breaks.
3. Apply chunking strategies that keep entire table blocks together inside a single retrieval context window.

## Try this

1. Upload a complex multi-column PDF into Lyzr Knowledge Base.
2. Verify that tabular numbers and column headers remain aligned in the chunk preview.

## Video Transcript

In Lesson 10, we address one of the toughest challenges in enterprise RAG: accurately parsing PDFs and financial tables. Standard text chunkers ruin tables by splitting rows across arbitrary character limits. We demonstrate how Lyzr uses layout-aware vision parsing to preserve table structure as clean Markdown, enabling your agents to accurately query financial metrics and tabular data.

---

## 📄 File: `11-retrieval-algorithms-basic-mmr-and-hyde.md`

# Retrieval Algorithms — Basic, MMR, and HYDE

*Lesson 11 · Course 1 Chapter 2 — Enterprise Knowledge Base Masterclass*

## What you'll learn

- Master dense vector similarity search (Cosine, Euclidean distance).
- Implement Maximal Marginal Relevance (MMR) to eliminate redundant search results.
- Utilize Hypothetical Document Embeddings (HyDE) for zero-shot complex query retrieval.

## Key concepts

- **Dense Retrieval:** Querying vector spaces using cosine similarity between prompt embeddings and chunk embeddings.
- **Maximal Marginal Relevance (MMR):** Balancing relevance with diversity to avoid returning 5 nearly identical chunks.
- **HyDE (Hypothetical Document Embeddings):** Prompting an LLM to generate a hypothetical answer first, then using that answer's vector to search the vector database.

## Hands-on Implementation

1. Configure retrieval strategy in Lyzr Knowledge Base settings (Cosine vs. MMR).
2. Set MMR diversity parameter (`lambda_mult=0.5`) to retrieve diverse context across multiple document sections.
3. Compare retrieval accuracy on ambiguous queries using HyDE vs. raw vector search.

## Try this

1. Test a multi-part query on your knowledge base.
2. Toggle MMR on and verify that the retrieved contexts cover different aspects of the topic rather than repeating the first paragraph.

## Video Transcript

Welcome to Lesson 11. Simply running basic vector similarity search often results in returning multiple copies of the exact same document section. In this lesson, we explore advanced retrieval algorithms: MMR for result diversity and HyDE for handling complex or abstract user prompts.

---

## 📄 File: `12-wiring-kb-to-agent-and-execution-traces.md`

# Wiring KB to Agent & Execution Traces

*Lesson 12 · Course 1 Chapter 2 — Enterprise Knowledge Base Masterclass*

## What you'll learn

- Connect a configured Knowledge Base to an autonomous Lyzr Agent.
- Inspect RAG execution traces, prompt injection buffers, and retrieval scores.
- Evaluate end-to-end RAG response precision, recall, and hallucination rates.

## Key concepts

- **Knowledge Binding:** Linking a Knowledge Base UUID to an Agent persona in Lyzr Studio or ADK.
- **Prompt Augmentation:** How retrieved chunks are automatically formatted into system context windows.
- **Execution Telemetry:** Tracing query latency, top-k similarity scores, and LLM token usage per query turn.

## Hands-on Implementation

1. Select your created Knowledge Base in the Agent configuration panel.
2. Execute test prompts and open the RAG Execution Trace log.
3. Review exact chunk matches, similarity percentages, and context utilization.

## Try this

1. Ask your agent a question outside the Knowledge Base domain.
2. Verify that guardrails and low similarity scores prevent the agent from fabricating answers.

## Video Transcript

In Lesson 12, we complete Chapter 2 by wiring our knowledge base into a live agent. We inspect the exact execution trace to see how chunks are retrieved, injected into the system prompt, and processed by the model—giving you full visibility into your agent's reasoning.

---

## 📄 File: `13-introduction-to-tools-and-mcp-servers.md`

# Introduction to Tools & MCP Servers

*Lesson 13 · Course 1 Chapter 3 — Connecting Agents with MCP Servers and Tools*

## What you'll learn

- Understand the Model Context Protocol (MCP) standard for AI agent tools.
- Differentiate between custom function calling and standardized MCP server integrations.
- Equip agents with external action capabilities (web search, databases, APIs).

## Key concepts

- **Model Context Protocol (MCP):** An open standard connecting AI models to external tools, data sources, and action endpoints securely.
- **Tool Capabilities:** Enabling agents to move beyond read-only text generation to executing real-world actions.
- **MCP Client-Server Model:** Agents act as MCP clients interacting with lightweight, reusable MCP servers.

## Hands-on Implementation

1. Explore available pre-built MCP servers in Lyzr Studio.
2. Bind an action tool to an agent persona.
3. Review tool definitions and parameter schemas.

## Try this

1. Identify 2 external APIs (e.g. Weather, CRM) that your business agent needs to interact with.
2. Map out the input parameters and expected output JSON for each API tool.

## Video Transcript

Welcome to Chapter 3 of Lyzr Foundations! In Lesson 13, we introduce Model Context Protocol (MCP) and agent tools. Learn how MCP transforms passive language models into active agents capable of executing software actions across your tech stack.

---

## 📄 File: `14-configuring-tavily-mcp-server.md`

# Configuring Tavily MCP Server

*Lesson 14 · Course 1 Chapter 3 — Connecting Agents with MCP Servers and Tools*

## What you'll learn

- Provision Tavily Search API keys and configure the Tavily MCP Server in Lyzr.
- Enable live web research, news extraction, and real-time facts retrieval.
- Scope search depth and domain filters for enterprise security.

## Key concepts

- **Live Web Research:** Equipping agents with search capabilities for information newer than LLM training cutoffs.
- **Domain Whitelisting:** Restricting agent web searches to trusted domains (e.g., official docs, news portals).
- **Search Result Structuring:** Automatic parsing of search snippets, page URLs, and publishing dates.

## Hands-on Implementation

1. Enter Tavily API Key in Lyzr Tool Integrations settings.
2. Attach Tavily Search Tool to your agent.
3. Test real-time prompts (e.g., "Summarize latest tech news from today").

## Try this

1. Prompt your agent for current market metrics.
2. Inspect the citation URLs returned by Tavily MCP to confirm accuracy.

## Video Transcript

In Lesson 14, we walk step-by-step through configuring the Tavily MCP Server. Watch how attaching live web search enables your agent to answer real-time questions with verified web citations.

---

## 📄 File: `15-integrating-gmail-and-email-action-tools.md`

# Integrating Gmail & Email Action Tools

*Lesson 15 · Course 1 Chapter 3 — Connecting Agents with MCP Servers and Tools*

## What you'll learn

- Set up OAuth 2.0 authentication for Gmail and email action tools.
- Enable draft creation, email searching, and guarded email sending.
- Implement Human-in-the-Loop approval workflows for outbound email actions.

## Key concepts

- **Email Automation:** Reading inbox messages, drafting responses, and sending notifications.
- **Guarded Write Paths:** Requiring human confirmation before an agent sends external emails.
- **OAuth Credentials:** Securing user tokens and managing access scopes safely.

## Hands-on Implementation

1. Connect Gmail OAuth integration in Lyzr settings.
2. Configure agent instructions for drafting follow-up emails.
3. Test drafting an email and verify it appears in your Gmail Drafts folder.

## Try this

1. Ask your agent to search recent emails from a specific sender and draft a summary response.
2. Confirm that the draft is created without sending automatically until approved.

## Video Transcript

In Lesson 15, we wrap up Course 1 by building an Email Action Agent. We configure Gmail OAuth, set up guarded write paths, and demonstrate how agents draft production emails safely with human-in-the-loop oversight.
"""

# Insert Chapter 2 and 3 into Course 1 section of master file
target_marker = "# 🎓 Course 2: Lyzr for Business Professionals"
if target_marker in content:
    parts = content.split(target_marker)
    updated_content = parts[0] + ch2_ch3_content + "\n\n# 🎓 Course 2: Lyzr for Business Professionals" + parts[1]
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("Successfully updated master_courses_lesson_notes.md with Chapter 2 & 3!")
else:
    print("Target marker not found")
