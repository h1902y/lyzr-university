# Theme v3 Landing Page Visual Blueprint & Technical Spec (Updated)

This document details the exact layout, hero section updates, expandable course card drawers, and footer architecture for **Lyzr University Theme v3**.

---

## 🧭 Header Navigation Layout

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  [↗ Lyzr]            [ Lyzr Foundations ]  [ Business Teams ]  [ Developers ]   [ Community ]│
│  (studio.lyzr.ai)                   (The 3 Master Courses)                      (Forum)     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📐 Landing Page Master Diagram (`home_landing_page.liquid`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. HEADER NAV: [↗ Lyzr]  |  Foundations  Business  Devs  |  Community        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. HERO SECTION                                                             │
│    Heading: Lyzr University                                                 │
│    Sub: Learn to build production AI agents — visually in Studio or code.  │
│    Single Primary CTA:                                                      │
│    [ New to Agent Building? Get the Foundations → ] (links to Foundations)  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. STAT ROW (100% Preserved)                                                │
│    3 Master Courses  |  100% Free  |  Self-Paced  |  Certificates          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. WHY LYZR (100% Preserved)                                                │
│    Always free  |  Learn by building  |  Two paths, one destination         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. MASTER COURSES CATALOG GRID (3 Cards with Expandable Curriculum Drawers) │
│    Subhead: "Select an audience-led course below to begin"                  │
│                                                                             │
│    ┌─────────────────────────────────────────────────────────────────────┐  │
│    │ 🎓 CARD 1: LYZR FOUNDATIONS                                        │  │
│    │ Dynamic Meta: {{ product.chapter_count }} Chaps ·                  │  │
│    │               {{ product.lesson_count }} Lessons · {{ metadata }}  │  │
│    │ Button: [ View Curriculum / Chapters ▼ ]                            │  │
│    │ ┌─────────────────────────────────────────────────────────────────┐ │  │
│    │ │ 🔽 EXPANDED DRAWER:                                            │ │  │
│    │ │    • Chapter 1: Lyzr Platform & Offerings Overview              │ │  │
│    │ │    • Chapter 2: Enterprise Knowledge Base Masterclass           │ │  │
│    │ │    • Chapter 3: Connecting Agents with MCP Servers & Tools      │ │  │
│    │ └─────────────────────────────────────────────────────────────────┘ │  │
│    │ Button: [ Enroll in Course → ]                                      │  │
│    └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│    ┌─────────────────────────────────────────────────────────────────────┐  │
│    │ 🎨 CARD 2: LYZR FOR BUSINESS TEAMS                                 │  │
│    │ Dynamic Meta: {{ product.chapter_count }} Chaps ·                  │  │
│    │               {{ product.lesson_count }} Lessons · {{ metadata }}  │  │
│    │ Button: [ View Curriculum / Chapters ▼ ]                            │  │
│    │ ┌─────────────────────────────────────────────────────────────────┐ │  │
│    │ │ 🔽 EXPANDED DRAWER:                                            │ │  │
│    │ │    • Chapter 1: The Agent Lifecycle & Core Concepts             │ │  │
│    │ │    • Chapter 2: Building & Orchestrating Agents                 │ │  │
│    │ │    • Chapter 3: Grounding Agents in Knowledge & RAG             │ │  │
│    │ │    • Chapter 4: Governing & Testing Enterprise Agents           │ │  │
│    │ └─────────────────────────────────────────────────────────────────┘ │  │
│    │ Button: [ Enroll in Course → ]                                      │  │
│    └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│    ┌─────────────────────────────────────────────────────────────────────┐  │
│    │ 💻 CARD 3: LYZR FOR DEVELOPERS                                     │  │
│    │ Dynamic Meta: {{ product.chapter_count }} Chaps ·                  │  │
│    │               {{ product.lesson_count }} Lessons · {{ metadata }}  │  │
│    │ Button: [ View Curriculum / Chapters ▼ ]                            │  │
│    │ ┌─────────────────────────────────────────────────────────────────┐ │  │
│    │ │ 🔽 EXPANDED DRAWER:                                            │ │  │
│    │ │    • Chapter 1: ADK Python SDK Getting Started                  │ │  │
│    │ │    • Chapter 2: Multimodal Agents (Vision & Audio)              │ │  │
│    │ │    • Chapter 3: Knowledge, Vector Stores & Agent Memory         │ │  │
│    │ │    • Chapter 4: Custom Tools & Multi-Step Workflows             │ │  │
│    │ └─────────────────────────────────────────────────────────────────┘ │  │
│    │ Button: [ Enroll in Course → ]                                      │  │
│    └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. HOW IT WORKS (100% Preserved)                                            │
│    01 Choose your course ──> 02 Learn by building ──> 03 Ship in AI Studio  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 7. FAQ ACCORDION (100% Preserved)                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 8. PRODUCT CALLOUT (100% Preserved - studio.lyzr.ai)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 9. COMMUNITY BLOCK (100% Preserved - lyzr community)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│10. BEYOND THE CLASSROOM (100% Preserved - partner & demo cards)             │
├─────────────────────────────────────────────────────────────────────────────┤
│11. FOOTER (100% Preserved - Corporate Footer)                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🦶 Current Footer Inventory (`sections/footer.liquid`)

Our hand-coded corporate footer contains 4 main columns plus bottom legal bar:

1. **Brand Column:** Wordmark (`Lyzr University`), Tagline, and 4 Social Icons (LinkedIn, YouTube, X, Instagram).
2. **Product Column:** `AI Studio` (`studio.lyzr.ai`), `Architect` (`architect.new`), `ADK` (`docs.lyzr.ai`), `Pricing` (`lyzr.ai/pricing`).
3. **Learn Column:** `All Courses` (`/collections`), `Foundations` (`/collections/foundations`), `Docs` (`docs.lyzr.ai`), `Community` (`/hub/community/415845`).
4. **Company Column:** `About` (`lyzr.ai`), `Blog` (`lyzr.ai/blog`), `Contact` (`lyzr.ai/book-demo`).
5. **Bottom Bar:** Copyright notice + Thinkific white-label link.
