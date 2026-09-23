import os

brain_dir = '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61'
report_path = os.path.join(brain_dir, 'thinkific_official_api_courses_report.md')

courses_list = [
  {"id": 3407697, "name": "AI Agent Management on Lyzr Certification", "slug": "ai-agents-certification", "type": "Certification"},
  {"id": 3427138, "name": "Building Production-Ready AI Agents", "slug": "ai-agent-development-course", "type": "Course"},
  {"id": 3429997, "name": "Lyzr for Developers — the SDK Track", "slug": "lyzr-devs", "type": "Track"},
  {"id": 3443591, "name": "ADK: Knowledge & Memory", "slug": "code-knowledge", "type": "Modular Course"},
  {"id": 3443592, "name": "ADK: Multimodal", "slug": "code-multimodal", "type": "Modular Course"},
  {"id": 3443593, "name": "ADK: Getting Started", "slug": "code-foundations", "type": "Modular Course"},
  {"id": 3445031, "name": "ADK: Tools & Workflows", "slug": "adk-tools-and-workflows", "type": "Modular Course"},
  {"id": 3447255, "name": "[Legacy] Lyzr Agent Building", "slug": "legacy-1", "type": "Legacy Track"},
  {"id": 3447258, "name": "[Legacy] Lyzr Agent Engineering for Developers", "slug": "legacy-2", "type": "Legacy Track"},
  {"id": 3447264, "name": "[Legacy] Lyzr Value Enablement for Business Users", "slug": "legacy-3", "type": "Legacy Track"},
  {"id": 3451858, "name": "Studio: The Agent Lifecycle", "slug": "studio-foundations-the-agent-lifecycle", "type": "Modular Course"},
  {"id": 3458141, "name": "Studio: Design & Create", "slug": "studio-design-create", "type": "Modular Course"},
  {"id": 3462713, "name": "Cohort 1 - Build and Sell Agentic Solutions to Enterprises", "slug": "bns-cohort1", "type": "Cohort Track"},
  {"id": 3467905, "name": "Studio: Knowledge & RAG", "slug": "studio-knowledge-rag", "type": "Modular Course"},
  {"id": 3486360, "name": "Studio: Building & Orchestrating Agents", "slug": "studio-building-orchestrating-agents", "type": "Modular Course"},
  {"id": 3486361, "name": "Studio: Grounding Agents in Knowledge", "slug": "studio-grounding-agents-in-knowledge", "type": "Modular Course"},
  {"id": 3486366, "name": "Studio: Governing & Testing Agents", "slug": "studio-governing-testing-agents", "type": "Modular Course"},
  {"id": 3486420, "name": "Lyzr Overview and Offerings", "slug": "lyzr-overview-and-offerings", "type": "Modular Course"},
  {"id": 3489968, "name": "Lyzr Foundations", "slug": "new-course-3", "type": "New Master Course 1"},
  {"id": 3489969, "name": "Lyzr Studio Architect & Builder Course", "slug": "new-course-4", "type": "New Master Course 2 (Architect)"},
  {"id": 3489970, "name": "Lyzr for Developers", "slug": "new-course-5", "type": "New Master Course 3"},
  {"id": 3490173, "name": "Lyzr for Business Professionals", "slug": "new-course-6", "type": "New Master Course 2 (Business)"}
]

md_content = f"""# 🌐 Thinkific Official API Course & Asset Inventory Report

**API Endpoint:** `https://api.thinkific.com/api/public/v1/courses`  
**Authentication:** Authorization Bearer JWT Token (`subdomain: lyzr`)  
**Total Retrieved Courses:** {len(courses_list)}  

---

## 1. Master Courses (New Consolidated Architecture)

| Master Course | Course ID | Slug | Status |
| :--- | :---: | :--- | :---: |
| 🎓 **Lyzr Foundations** | `#3489968` | `new-course-3` | 🟡 Draft |
| 💼 **Lyzr for Business Professionals** | `#3490173` / `#3489969` | `new-course-6` | 🟡 Draft |
| 🛠️ **Lyzr for Developers** | `#3489970` | `new-course-5` | 🟡 Draft |

---

## 2. Published & Modular Courses Catalog

| Course Title | Course ID | API Slug | Classification |
| :--- | :---: | :--- | :--- |
{chr(10).join([f"| **{c['name']}** | `#{c['id']}` | `{c['slug']}` | {c['type']} |" for c in courses_list if 'New Master' not in c['type']])}
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Generated API report artifact: {report_path}")
