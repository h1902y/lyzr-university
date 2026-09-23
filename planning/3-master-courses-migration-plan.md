# Architectural Migration Plan: Consolidate to 3 Master Audience-Led Courses (All-in-One Lesson Standard)

This document details the architectural specification to eliminate legacy "Tracks" and "Collections" in favor of **3 Master Audience-Led Courses**, built using Thinkific's **All-in-One Single Lesson Standard** (Video + PDF Download + Text in 1 Lesson).

---

## 🎯 Architectural Goal & All-in-One Standard

### Why the All-in-One Lesson Architecture Wins:

| Metric | Legacy Fragmented Pattern | All-in-One Master Standard |
| :--- | :--- | :--- |
| **Lesson Count Per Topic** | 2 Separate Lessons (Video + PDF) | **1 Single Unified Lesson Page** |
| **Course Lesson Total** | 36+ Lessons (Exceeds Thinkific 25-cap) | **10–15 Lessons Total Per Course** (Cleanly under Thinkific 25-cap) |
| **Learner Experience** | Constant context-switching between pages | **Watch video & download PDF notes on the exact same page** |
| **Sidebar Navigation** | Bloated, cluttered sidebar | **Clean, premium, enterprise-grade navigation** |

---

## 📐 All-in-One Lesson Block Layout

Inside Thinkific's New Course Builder, each topic is built as a single lesson containing stacked content blocks:

```
┌─────────────────────────────────────────────────────────────┐
│  LESSON TITLE: 01 Introduction to Lyzr Platform             │
├─────────────────────────────────────────────────────────────┤
│  🎥 BLOCK 1: Video Player (MP4 playback)                    │
│     [01a Introduction to Lyzr.mp4]                          │
├─────────────────────────────────────────────────────────────┤
│  📑 BLOCK 2: Download Attachment (PDF Study Guide)          │
│     [01b Introduction to Lyzr Notes.pdf]                   │
├─────────────────────────────────────────────────────────────┤
│  📝 BLOCK 3: Key Takeaways Text / Summary                   │
│     [Markdown Summary & Documentation Links]                │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Master Course Inventory (All-in-One Schema)

### 1. 🎓 **`Lyzr Foundations` (Master Course #1 — `#3489968`)**
* **Chapter 01: Lyzr Platform Overview** (8 All-in-One Lessons)
  * `01 Introduction to Lyzr Platform` (Video + PDF Notes)
  * `02 Client Success Stories` (Video + PDF Notes)
  * `03 The Lyzr Stack & Architecture` (Video + PDF Notes)
  * `04 Architect Overview` (Video + PDF Notes)
  * `05 Studio Overview` (Video + PDF Notes)
  * `06 Lyzr Capabilities` (Video + PDF Notes)
  * `07 Computer Agent` (Video + PDF Notes)
  * `08 Git Agent` (Video + PDF Notes)
* **Chapter 02: Enterprise Knowledge Base Masterclass** (4 All-in-One Lessons)
  * `01 Designing Knowledge Bases & Source Selection` (Video + PDF Notes)
  * `02 PDF Parsing Strategies & Tabular Extraction` (Video + PDF Notes)
  * `03 Retrieval Algorithms — Basic, MMR, and HYDE` (Video + PDF Notes)
  * `04 Wiring KB to Agent & Execution Traces` (Video + PDF Notes)
* **Chapter 03: Connecting Agents with MCP Servers & Tools** (3 All-in-One Lessons)
  * `01 Introduction to Tools & MCP Servers` (Video + PDF Notes)
  * `02 Configuring Tavily Search MCP Server` (Video + PDF Notes)
  * `03 Integrating Gmail & Action Tools` (Video + PDF Notes)
* **Total Lessons in Course 1:** **15 Lessons** `[Strictly Draft]`

---

### 2. 💼 **`Lyzr for Business Teams` (Master Course #2 — `#3489969`)**
* **Chapter 01: The Agent Lifecycle & Core Concepts** (1 All-in-One Lesson + PDF Guide)
* **Chapter 02: Building & Orchestrating Agents** (2 All-in-One Lessons)
  * `01 Models & Tools in Production` (Video + PDF Notes)
  * `02 Multi-Agent Orchestration` (Video + PDF Notes)
* **Chapter 03: Grounding Agents in Knowledge & RAG** (5 All-in-One Lessons)
  * `01 RAG & Vector Stores` (Video + PDF Notes)
  * `02 Document Parsing & Ingestion` (Video + PDF Notes)
  * `03 Data Connectors as Live Sources` (Video + PDF Notes)
  * `04 Agent Memory in Depth` (Video + PDF Notes)
  * `05 Knowledge Graphs & Semantic Models` (Video + PDF Notes)
* **Chapter 04: Governing & Testing Enterprise Agents** (2 All-in-One Lessons)
  * `01 Responsible AI & Guardrails` (Video + PDF Notes)
  * `02 Agent Simulation & Observability` (Video + PDF Notes)
* **Total Lessons in Course 2:** **10 Lessons** `[Strictly Draft]`

---

### 3. 💻 **`Lyzr for Developers` (Master Course #3 — `#3489970`)**
* **Chapter 01: ADK Python SDK Getting Started** (4 All-in-One Lessons)
  * `01 Environment Setup & First Agent` (Video + PDF Notes)
  * `02 Single-Agent vs Multi-Agent SDK` (Video + PDF Notes)
  * `03 Agent Memory & Execution Logs` (Video + PDF Notes)
  * `04 Custom Tools in Python` (Video + PDF Notes)
* **Chapter 02: Multimodal Agents (Vision & Audio)** (3 All-in-One Lessons)
  * `01 Vision & Image Processing` (Video + PDF Notes)
  * `02 Audio Transcriptions & Voice AI` (Video + PDF Notes)
  * `03 Multimodal Document Extraction` (Video + PDF Notes)
* **Chapter 03: Knowledge, Vector Stores & Agent Memory** (4 All-in-One Lessons)
  * `01 Custom Vector Store Connectors` (Video + PDF Notes)
  * `02 Advanced Chunking & RAG Pipelines` (Video + PDF Notes)
  * `03 Hybrid Search & Re-ranking` (Video + PDF Notes)
  * `04 Graph RAG Integration` (Video + PDF Notes)
* **Chapter 04: Custom Tools & Multi-Step Workflows** (1 All-in-One Lesson)
  * `01 Multi-Step Agent Workflows` (Video + PDF Notes)
* **Total Lessons in Course 3:** **12 Lessons** `[Strictly Draft]`

---

## 🔒 Execution Directives

1. **Strict Draft Mode:** Do NOT publish any course live. Keep status in `Draft`.
2. **All-in-One Builder UI:** Each lesson is created via Thinkific's lesson drawer, stacking Video + PDF Download file on the same lesson page.
3. **Zero Lesson Bloat:** Keeps total lesson count per course under 15, completely resolving Thinkific's 25-element cap!
