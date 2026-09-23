import os
import re
import csv

brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
university_dir = "/Users/hkc/Documents/lyzr/university"

sdk_readme = os.path.join(university_dir, "SDK-track/README.md")
studio_readme = os.path.join(university_dir, "Studio-track/README.md")

descript_map = {}

def parse_readme_table(filepath, track_name):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_section = "General"
    for line in lines:
        if line.startswith("## ") or line.startswith("### "):
            current_section = line.strip("# \n")
        if "|" in line and "share.descript.com" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4:
                title = parts[2].replace('*', '').strip()
                descript_match = re.search(r'https://share\.descript\.com/view/[a-zA-Z0-9]+', line)
                if descript_match:
                    url = descript_match.group(0)
                    descript_map[title.lower()] = {
                        "title": title,
                        "url": url,
                        "section": current_section,
                        "track": track_name
                    }

parse_readme_table(sdk_readme, "SDK Track")
parse_readme_table(studio_readme, "Studio Track")

print(f"Extracted {len(descript_map)} structured Descript link mappings from README manifests.")

# Master Curriculum Mapping (Target Master Courses)
master_lessons = [
    # Lyzr Foundations
    {"master": "Lyzr Foundations", "chapter": "Ch 1. Platform Overview", "title": "Introduction to Lyzr Platform", "video": "01a Introduction to Lyzr Platform.mp4", "descript_title": "what is a lyzr agent"},
    {"master": "Lyzr Foundations", "chapter": "Ch 1. Platform Overview", "title": "Client Success Stories", "video": "02a Client Success Stories.mp4", "descript_title": "client success stories"},
    {"master": "Lyzr Foundations", "chapter": "Ch 1. Platform Overview", "title": "The Lyzr Stack and Architecture", "video": "03a The Lyzr Stack and Architecture.mp4", "descript_title": "the lyzr stack and architecture"},
    {"master": "Lyzr Foundations", "chapter": "Ch 2. Architect & Studio Overview", "title": "Architect Overview", "video": "04a Architect Overview.mp4", "descript_title": "architect overview"},
    {"master": "Lyzr Foundations", "chapter": "Ch 2. Architect & Studio Overview", "title": "Studio Overview", "video": "05a Studio Overview.mp4", "descript_title": "welcome to agent studio & the lifecycle"},
    {"master": "Lyzr Foundations", "chapter": "Ch 2. Architect & Studio Overview", "title": "Lyzr Capabilities", "video": "06a Lyzr Capabilities.mp4", "descript_title": "lyzr capabilities"},
    {"master": "Lyzr Foundations", "chapter": "Ch 3. Enterprise Autonomous Agents", "title": "Computer Agent", "video": "07a Computer Agent.mp4", "descript_title": "computer agent"},
    {"master": "Lyzr Foundations", "chapter": "Ch 3. Enterprise Autonomous Agents", "title": "Git Agent", "video": "08a Git Agent.mp4", "descript_title": "git agent"},

    # Lyzr for Business Professionals
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 1. Agent Studio Lifecycle", "title": "Welcome to Agent Studio & Lifecycle", "video": "01a Welcome to Agent Studio and Lifecycle.mp4", "descript_title": "welcome to agent studio & the lifecycle"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 1. Agent Studio Lifecycle", "title": "Build: Choose Type and Create Agent", "video": "02a Build Choose Type and Create Agent.mp4", "descript_title": "build — choose a type & create an agent"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 1. Agent Studio Lifecycle", "title": "Equip: Model, Tool, Memory, Knowledge", "video": "03a Equip Model Tool Memory Knowledge.mp4", "descript_title": "equip — model, tool, knowledge"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 1. Agent Studio Lifecycle", "title": "What Agent Type Should I Build?", "video": "04a What Agent Type Should I Build.mp4", "descript_title": "what agent type should i build?"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 2. Orchestration & Swarms", "title": "Lyzr Manager Orchestration", "video": "05a Lyzr Manager Orchestration.mp4", "descript_title": "lyzr manager"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 2. Orchestration & Swarms", "title": "SuperFlow Basic & Dynamic Flows", "video": "06a SuperFlow Basic and Dynamic Flows.mp4", "descript_title": "superflow: invoice reconciliation"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 2. Orchestration & Swarms", "title": "SuperFlow Advanced Routing & Loops", "video": "07a SuperFlow Advanced Routing and Loops.mp4", "descript_title": "superflow: loops"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 3. Knowledge Base Engineering", "title": "RAG in Studio", "video": "08a RAG in Studio.mp4", "descript_title": "rag in studio"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 3. Knowledge Base Engineering", "title": "Build a Knowledge Base", "video": "09a Build a Knowledge Base.mp4", "descript_title": "build a knowledge base"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 3. Knowledge Base Engineering", "title": "Document Parsing & Ingestion", "video": "10a Document Parsing and Ingestion.mp4", "descript_title": "document parsing & ingestion"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 3. Knowledge Base Engineering", "title": "Data Connectors as Live Sources", "video": "11a Data Connectors as Live Sources.mp4", "descript_title": "data connectors as live sources"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 4. Memory & Knowledge Graphs", "title": "Agent Memory in Depth", "video": "12a Agent Memory in Depth.mp4", "descript_title": "agent memory in depth"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 4. Memory & Knowledge Graphs", "title": "Beyond Vectors: Structured Knowledge", "video": "13a Beyond Vectors Structured Knowledge.mp4", "descript_title": "beyond vectors: structured knowledge"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 4. Memory & Knowledge Graphs", "title": "Build a Knowledge Graph", "video": "14a Build a Knowledge Graph.mp4", "descript_title": "build a knowledge graph"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 4. Memory & Knowledge Graphs", "title": "The Semantic Model & Global Context", "video": "15a The Semantic Model and Global Context.mp4", "descript_title": "the semantic model & global context"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 5. Responsible AI & Testing", "title": "Responsible AI & Guardrails", "video": "16a Responsible AI and Guardrails.mp4", "descript_title": "govern — add guardrails"},
    {"master": "Lyzr for Business Professionals", "chapter": "Ch 5. Responsible AI & Testing", "title": "Agent Simulation & Observability", "video": "17a Agent Simulation and Observability.mp4", "descript_title": "test — run it in the playground"},

    # Lyzr for Technical Professionals
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 1. ADK Foundations", "title": "What is a Lyzr Agent?", "video": "01a What is a Lyzr Agent.mp4", "descript_title": "what is a lyzr agent"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 1. ADK Foundations", "title": "Building Your First Agent", "video": "02a Your first Agent.mp4", "descript_title": "your first agent"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 1. ADK Foundations", "title": "Swapping LLM Providers", "video": "03a Swapping LLM Providers.mp4", "descript_title": "swapping llm providers"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 1. ADK Foundations", "title": "Streaming Responses", "video": "04a Streaming Responses.mp4", "descript_title": "streaming responses"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 1. ADK Foundations", "title": "Structured Outputs", "video": "05a Structured Outputs.mp4", "descript_title": "structured outputs"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 1. ADK Foundations", "title": "Project: Multi-Provider Chatbot", "video": "06a Project Multi provider chatbot.mp4", "descript_title": "project: multi-provider chatbot"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 2. Multimodal Agents", "title": "Image Generation Agents", "video": "07a Image generation.mp4", "descript_title": "image generation"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 2. Multimodal Agents", "title": "File Generation Agents", "video": "08a File generation.mp4", "descript_title": "file generation"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 2. Multimodal Agents", "title": "Project: Creative Assistant", "video": "09a Project Creative Assistant.mp4", "descript_title": "project: creative assistant"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 3. RAG & Memory", "title": "Technical RAG Fundamentals", "video": "10a What is RAG.mp4", "descript_title": "what is rag?"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 3. RAG & Memory", "title": "Document Ingestion Pipelines", "video": "11a Document ingestion.mp4", "descript_title": "document ingestion"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 3. RAG & Memory", "title": "Vector Stores & Custom Retrievers", "video": "12a Vector stores and retrieval.mp4", "descript_title": "vector stores and retrieval"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 3. RAG & Memory", "title": "Agent Memory Basics", "video": "13a Agent memory basics.mp4", "descript_title": "agent memory basics"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 3. RAG & Memory", "title": "Conversation Memory & Persistence", "video": "14a Conversation memory.mp4", "descript_title": "conversation memory"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 3. RAG & Memory", "title": "Project: Document Q&A Bot", "video": "15a Project — Document Q&A bot.mp4", "descript_title": "project: document q&a bot"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 4. Tools & MCP", "title": "Why Tools Matter", "video": "16a Why tools matter.mp4", "descript_title": "why tools matter"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 4. Tools & MCP", "title": "Writing Custom Local Tools", "video": "17a Writing local tools.mp4", "descript_title": "writing local tools"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 4. Tools & MCP", "title": "Introduction to Tools & MCP Servers", "video": "13a Introduction to Tools and MCP Servers.mp4", "descript_title": "introduction to tools and mcp servers"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 4. Tools & MCP", "title": "Configuring Tavily MCP Server", "video": "14a Configuring Tavily MCP Server.mp4", "descript_title": "configuring tavily mcp server"},
    {"master": "Lyzr for Technical Professionals", "chapter": "Ch 4. Tools & MCP", "title": "Integrating Gmail & Email Tools", "video": "15a Integrating Gmail and Email Action Tools.mp4", "descript_title": "integrating gmail and email action tools"}
]

# Match Descript links
output_rows = []
for item in master_lessons:
    d_title = item["descript_title"].lower()
    url = "N/A"
    for k, v in descript_map.items():
        if d_title in k or k in d_title:
            url = v["url"]
            break
    output_rows.append({
        "Master Course": item["master"],
        "Chapter": item["chapter"],
        "Lesson Title": item["title"],
        "Video Asset Filename": item["video"],
        "Descript Link": url
    })

# Write CSV
csv_path = os.path.join(university_dir, "master_courses_with_descript_links.csv")
with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.DictWriter(cf, fieldnames=["Master Course", "Chapter", "Lesson Title", "Video Asset Filename", "Descript Link"])
    writer.writeheader()
    writer.writerows(output_rows)

print(f"\n✅ Created master CSV sheet at: {csv_path}")

# Write Markdown report artifact
report_path = os.path.join(brain_dir, "master_courses_descript_links_sheet.md")
md_lines = [
    "# 📋 Master Courses Curriculum & Descript Share Links Sheet",
    "",
    f"**Total Lessons Mapped:** {len(output_rows)}  ",
    "**CSV Export File:** `university/master_courses_with_descript_links.csv`  ",
    "",
    "---",
    "",
    "| Master Course | Chapter | Lesson Title | Video Asset Filename | Descript Share Link |",
    "| :--- | :--- | :--- | :--- | :--- |"
]

for r in output_rows:
    link_md = f"[{r['Descript Link']}]({r['Descript Link']})" if r['Descript Link'] != 'N/A' else 'N/A'
    md_lines.append(f"| **{r['Master Course']}** | {r['Chapter']} | {r['Lesson Title']} | `{r['Video Asset Filename']}` | {link_md} |")

with open(report_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md_lines))

print(f"✅ Created markdown sheet artifact at: {report_path}")
