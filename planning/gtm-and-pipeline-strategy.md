# 🎓 Lyzr University — GTM & LMS Pipeline Strategy

> [!NOTE]
> **Operational Dashboard**  
> *   **Primary Owners:** Harshit Choudhary & Vaibhavi Pai  
> *   **Workspace Target:** [personal-assistant/university/](file:///Users/hkc/Documents/lyzr/personal-assistant/university/)  
> *   **Status:** Active GTM Engine  

---

## ─── PART 1: THE LMS PIPELINE ───

The LMS Pipeline is a structured, two-cycle ingestion and quality-assurance process that transforms raw recording links into published storefront lessons, followed by continuous metrics audits.

### 1. Two-Cycle Ingestion Workflow

> [!NOTE]
> **Cycle A: Ingestion & Publishing (Publishing Cycle)**  
> `1. Identify Lesson` $\rightarrow$ `2. Fetch Descript MP4/JSON` $\rightarrow$ `3. Clean & Flatten Transcript` $\rightarrow$ `4. Author Lesson Notes` $\rightarrow$ `5. Render PDF` $\rightarrow$ `6. Package Assets` $\rightarrow$ `7. Upload & Publish`
>
> **Cycle B: QA, Alignment & Auditing (Reviewing Cycle)**  
> `7. Upload & Publish` $\rightarrow$ `8. Run Manifest Verification` $\rightarrow$ `9. Weekly Progress & Metric Audits`

#### **Cycle A: Ingestion & Publishing**
1.  **Identify**: Map the incoming Descript share page to the official curriculum chapter.
2.  **Fetch**: Scrape the raw MP4 video and JSON word-level timings using [fetch_descript.py](file:///.agents/skills/descript-to-thinkific/scripts/fetch_descript.py).
3.  **Clean & Flatten**: Process the JSON transcript using [flatten_transcript.py](file:///.agents/skills/descript-to-thinkific/scripts/flatten_transcript.py) to strip filler words and correct names (e.g. `Lizza` $\rightarrow$ `Lyzr`).
4.  **Author Notes**: Draft the companion notes (`.md`) using the strict `## In Studio` click-by-click walkthrough formatting standard.
5.  **Render PDF**: Run [_render_pdfs.py](file:///Users/hkc/Documents/lyzr/personal-assistant/university/Studio-track/notes/_render_pdfs.py) (via headless Chrome) to generate a high-end, branded PDF dossier.
6.  **Package**: Move the video and note PDF assets to the course upload directory under the `NNa` / `NNb` sorting structure.
7.  **Publish**: Drag packaged assets into the Thinkific Admin interface, mark them as published, and cross-link them on the storefront.

#### **Cycle B: Quality Assurance & Auditing**
8.  **Verify & Align**: Run [build_manifest.py](file:///.agents/skills/descript-to-thinkific/scripts/build_manifest.py) and [thinkific_verify.py](file:///.agents/skills/descript-to-thinkific/scripts/thinkific_verify.py) to sync local indexes with the live site.
9.  **Audit & Track**: Perform weekly progress audits on active enrollments, course starts, completion metrics, and status configurations.

---

### 2. Active Course Status Ledger

| Chapter / Target Folder | Storefront Name | Syllabus | Ingestion Status / Reference Links |
| :--- | :--- | :---: | :--- |
| `01 ADK Foundations` | `ADK: Getting Started` | 6 Lessons | **100% Live** |
| `02 ADK Multimodal` | `ADK: Multimodal` | 3 Lessons | **100% Live** |
| `03 ADK Knowledge and Memory` | `ADK: Knowledge & Memory` | 6 Lessons | **Action Required**: Only 4 lessons live. Need to backfill Lessons 12–15. |
| `04 ADK Tools and Workflows` | `ADK: Tools & Workflows` | 4 Lessons | **100% Live** |
| `06 Studio The Agent Lifecycle` | `Studio: The Agent Lifecycle` | 7 Lessons | **100% Live** |
| `07 Studio Design and Create` | `Studio: Design & Create` | 5 Lessons | **100% Live** |
| `09 Studio Tools, Models and MCP` | `Studio: Tools, Models & MCP` | 2 Lessons | **Newly Completed (Ready to Ingest)**:<br>• L01: Models in depth ([Descript A1](https://share.descript.com/view/PprdehMU1gb))<br>• L02: Build custom Tools ([Descript C1b](https://share.descript.com/view/ln149mRj2Gg)) |
| `11 Studio Knowledge and RAG` | `Studio: Knowledge & RAG` | 6 Lessons | **100% Live** |
| `12 Studio Knowledge Graph...` | `Studio: Knowledge Graph...` | 2 Lessons | **Newly Completed (Ready to Ingest)**:<br>• L01: Beyond Vectors ([Descript D1](https://share.descript.com/view/rpNG9jXPKAC))<br>• L02: Build a Knowledge Graph ([Descript D2](https://share.descript.com/view/dgLU6Jv2bvo)) |

> [!IMPORTANT]
> Because Course 09 and Course 12 are not yet live on Thinkific, we mapped them explicitly in [thinkific_verify.py](file:///.agents/skills/descript-to-thinkific/scripts/thinkific_verify.py)'s `FOLDER_TO_LIVE_NAME` dictionary to bypass fuzzy-matching errors during storefront checks.

---

## ─── PART 2: GTM GROWTH PLAN ───

Our Growth Engine is built around a closed-loop system designed to turn discovery into verified certification, and certificate holders into organic multipliers.

```
                  ┌────────────── GROWTH LOOP ──────────────┐
                  │                                         │
              discover ──→ enroll ──→ complete ──→ certify
                  ▲                                         │
                  └────────────── share ←───────────────────┘
```

### 1. One-Time Structural Setups

This section covers the one-time development and marketing setups (Items 1.1 to 1.4) that lay the pipeline foundation for scale.

*   **Item 1.1: Proof-of-Work Certification & LinkedIn Virality**
    *   **Verifiable Credentials**: Partner with a credentialing platform (or use domain metadata) to allow 1-click **"Add to LinkedIn Profile"** integrations, anchoring Lyzr credentials directly on developers' CVs.
    *   **LinkedIn Share Cards**: Upon course completion, generate a personalized, high-contrast visual image showing the student's name, their certified badge, and their Capstone Project title.
    *   **Proof-of-Work Gateway**: Restructure certificate criteria so that students must submit a live deployed link to their Capstone Agent (proving they actually built it) to receive their credential.

*   **Item 1.2: Product-Led Growth (PLG) In-Product UI**
    *   **Contextual Tooltips**: Embed help icon buttons (`🎓 Learn this screen`) next to advanced controls in Agent Studio (Simulation Engine, Traces, Knowledge Graph). Clicking these launches a video modal playing the specific 90-second tutorial segment of the matching University lesson.
    *   **Developer Profile Badges**: Show earned certifications (e.g., *Certified RAG Architect*) inside the logged-in user profile dropdown in Agent Studio.

*   **Item 1.3: Discord Social-Proof Automation**
    *   **Brag Webhooks**: Configure a webhook that automatically posts to a `#community-brags` Discord channel whenever a developer completes a track:
        > *“🎉 Congratulations to **@username** for earning their **Studio: Design & Create** certification! Check out the invoice-parsing SuperFlow they built here: [link]”*
    *   **Support Helper Bot**: Program a Discord keyword-matching bot in helper channels to suggest specific 2-minute University lesson URLs when developers run into tool/model config issues.

*   **Item 1.4: Marketing Launchpad & Email Setup**
    *   **Site Nav & Footers**: Add `University` as a permanent resources dropdown option in the main navigation and footer of `lyzr.ai`.
    *   **Sign-Up Flow Integration**: Update the onboarding email campaign to trigger a dedicated "Start your Learning Path" email 1 hour after a developer registers a new Lyzr account.
    *   **Transactional Footers**: Append a clean banner to system emails (like API key issues, billing invoices): *"Want to build faster? Take the certified courses at university.lyzr.ai"*.

---

### 2. Recurring Growth Activities

This section details the ongoing weekly loops (Items 2.1 to 2.5) to maintain brand momentum.

*   **Item 2.1: GSI & Partner Enablement**
    *   **Tier Certification Requirements**: Include certified builder quotas in partner tiering agreements (e.g., Gold SIs require at least 10 certified developers on staff).
    *   **Monthly SI Enablement Reviews**: GSI Account Managers run monthly syncs to review training progress dashboards with Accenture/emerging partners.
    *   **Weekly Metric Snapshots**: Re-run our metrics script weekly to track and publish 6 core KPIs (Sign-ups, active learners, course starts, completion rate, certificates issued, and social shares sighted).

*   **Item 2.2: Multi-Track Leader Amplification Schedule**
    We maintain a rotating social calendar categorized by target audience to share University updates:
    *   **Leaders Track (Siva, CEO)**: Posts high-level strategy, enterprise ROI metrics, and workforce scaling insights on LinkedIn.
    *   **Developers Track (Felipe, Instructor)**: Posts code walk-throughs, SDK API updates, technical deep-dives, and hands-on coding challenges.
    *   **Business Track (Vaibhavi / Manoj, Marketing & Product)**: Posts visual workflow diagrams, SuperFlow loops, and customer success highlights.

*   **Item 2.3: "Learn-in-Public" Weekly Build Challenges**
    *   **Weekly Challenges**: Run micro-competitions on LinkedIn/X (e.g., *"Build an agent with HubSpot integrations that does X in under 10 minutes"*).
    *   **Social Amplification**: Winners get highlighted in the weekly newsletter and receive free Studio API credits. This encourages builders to post video recordings of their builds tagging `#Lyzr`.

*   **Item 2.4: Permanent Newsletter Slot**
    *   Add a standing `🎓 New in Lyzr University` section in the weekly newsletter, advertising the syllabus and value of newly unlocked courses.

*   **Item 2.5: Multi-Channel Video & Social Syndication**
    *   **YouTube Playlists & Shorts**: Structure full course tracks into YouTube playlists, and extract 60-second vertical **YouTube Shorts** demonstrating isolated features.
    *   **Twitter/X Developer Threads**: Convert lesson takeaways into highly visual step-by-step developer threads, posting GIFs of working agents and code snippets tagging `#Lyzr`.
    *   **Instagram (IG) Reels & Carousels**: Create high-quality visual reels and swipeable carousel cards detailing key concepts (e.g., *"Before/After: Doing RAG with/without Graph database"*) to capture emerging builders and tech enthusiasts.
