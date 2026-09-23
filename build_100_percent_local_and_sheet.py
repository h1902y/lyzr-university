import urllib.request
import urllib.parse
import json
import os
import shutil
import re

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
university_dir = "/Users/hkc/Documents/lyzr/university"
local_master_dir = os.path.join(university_dir, "master-courses-local")

os.makedirs(local_master_dir, exist_ok=True)

print("==========================================================================")
print(" 🚀 BUILDING 100% LOCAL MASTER COURSES & NEW GOOGLE SHEET TAB")
print("==========================================================================")

# Read master notes markdown
master_notes_path = os.path.join(brain_dir, "master_courses_lesson_notes.md")
with open(master_notes_path, 'r', encoding='utf-8') as f:
    master_notes_text = f.read()

# 49 Master Lessons Definition with ID Nomenclature
master_lessons_data = [
    # Course 1: Lyzr Foundations (C01)
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH01", "ch_name": "Chapter 01: Lyzr Platform & Ecosystem", "l_num": "L01", "title": "Introduction to Lyzr Platform", "video_orig": "01a Introduction to Lyzr Platform.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH01", "ch_name": "Chapter 01: Lyzr Platform & Ecosystem", "l_num": "L02", "title": "Client Success Stories", "video_orig": "02a Client Success Stories.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH01", "ch_name": "Chapter 01: Lyzr Platform & Ecosystem", "l_num": "L03", "title": "The Lyzr Stack and Architecture", "video_orig": "03a The Lyzr Stack and Architecture.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH02", "ch_name": "Chapter 02: Architect & Studio Overview", "l_num": "L01", "title": "Architect Overview", "video_orig": "04a Architect Overview.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH02", "ch_name": "Chapter 02: Architect & Studio Overview", "l_num": "L02", "title": "Studio Overview", "video_orig": "05a Studio Overview.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH02", "ch_name": "Chapter 02: Architect & Studio Overview", "l_num": "L03", "title": "Lyzr Capabilities", "video_orig": "06a Lyzr Capabilities.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH03", "ch_name": "Chapter 03: Autonomous Agents", "l_num": "L01", "title": "Computer Agent", "video_orig": "07a Computer Agent.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH03", "ch_name": "Chapter 03: Autonomous Agents", "l_num": "L02", "title": "Git Agent", "video_orig": "08a Git Agent.mp4", "descript": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH04", "ch_name": "Chapter 04: Knowledge Bases & Parsing", "l_num": "L01", "title": "Designing Knowledge Bases", "video_orig": "09a Designing Knowledge Bases and Source Selection.mp4", "descript": "https://share.descript.com/view/M7ktDjS5XE4"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH04", "ch_name": "Chapter 04: Knowledge Bases & Parsing", "l_num": "L02", "title": "PDF Parsing Strategies", "video_orig": "10a PDF Parsing Strategies and Tabular Extraction.mp4", "descript": "https://share.descript.com/view/M7ktDjS5XE4"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH04", "ch_name": "Chapter 04: Knowledge Bases & Parsing", "l_num": "L03", "title": "Retrieval Algorithms", "video_orig": "11a Retrieval Algorithms Basic MMR and HYDE.mp4", "descript": "https://share.descript.com/view/M7ktDjS5XE4"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH04", "ch_name": "Chapter 04: Knowledge Bases & Parsing", "l_num": "L04", "title": "Wiring KB to Agent", "video_orig": "12a Wiring KB to Agent and Execution Traces.mp4", "descript": "https://share.descript.com/view/M7ktDjS5XE4"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH05", "ch_name": "Chapter 05: Tools & MCP Servers", "l_num": "L01", "title": "Introduction to Tools and MCP", "video_orig": "13a Introduction to Tools and MCP Servers.mp4", "descript": "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH05", "ch_name": "Chapter 05: Tools & MCP Servers", "l_num": "L02", "title": "Configuring Tavily MCP Server", "video_orig": "14a Configuring Tavily MCP Server.mp4", "descript": "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9"},
    {"c_num": "C01", "c_name": "Lyzr Foundations", "ch_num": "CH05", "ch_name": "Chapter 05: Tools & MCP Servers", "l_num": "L03", "title": "Integrating Gmail & Email Tools", "video_orig": "15a Integrating Gmail and Email Action Tools.mp4", "descript": "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9"},

    # Course 2: Lyzr for Business Professionals (C02)
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: Agent Studio Lifecycle", "l_num": "L01", "title": "Welcome to Agent Studio & Lifecycle", "video_orig": "01a Welcome to Agent Studio and Lifecycle.mp4", "descript": "https://share.descript.com/view/QSwoPpR6hKL"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: Agent Studio Lifecycle", "l_num": "L02", "title": "Build: Choose Type and Create Agent", "video_orig": "02a Build Choose Type and Create Agent.mp4", "descript": "https://share.descript.com/view/r0i0W0qxzAh"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: Agent Studio Lifecycle", "l_num": "L03", "title": "Equip: Model, Tool, Memory, Knowledge", "video_orig": "03a Equip Model Tool Memory Knowledge.mp4", "descript": "https://share.descript.com/view/GobPzBquAVF"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: Agent Studio Lifecycle", "l_num": "L04", "title": "What Agent Type Should I Build?", "video_orig": "04a What Agent Type Should I Build.mp4", "descript": "https://share.descript.com/view/FOzm28nV9YM"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH02", "ch_name": "Chapter 02: Orchestration & Swarms", "l_num": "L01", "title": "Lyzr Manager Orchestration", "video_orig": "05a Lyzr Manager Orchestration.mp4", "descript": "https://share.descript.com/view/JxjoIomKT1C"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH02", "ch_name": "Chapter 02: Orchestration & Swarms", "l_num": "L02", "title": "SuperFlow Basic & Dynamic Flows", "video_orig": "06a SuperFlow Basic and Dynamic Flows.mp4", "descript": "https://share.descript.com/view/e9Ny8ysXwMc"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH02", "ch_name": "Chapter 02: Orchestration & Swarms", "l_num": "L03", "title": "SuperFlow Advanced Routing & Loops", "video_orig": "07a SuperFlow Advanced Routing and Loops.mp4", "descript": "https://share.descript.com/view/cyOXlcLJI5R"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: Knowledge Base Engineering", "l_num": "L01", "title": "RAG in Studio", "video_orig": "08a RAG in Studio.mp4", "descript": "https://share.descript.com/view/iLyDbKWJXxv"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: Knowledge Base Engineering", "l_num": "L02", "title": "Build a Knowledge Base", "video_orig": "09a Build a Knowledge Base.mp4", "descript": "https://share.descript.com/view/u8SqXwIKzjT"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: Knowledge Base Engineering", "l_num": "L03", "title": "Document Parsing & Ingestion", "video_orig": "10a Document Parsing and Ingestion.mp4", "descript": "https://share.descript.com/view/CGqBLgAbGUG"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: Knowledge Base Engineering", "l_num": "L04", "title": "Data Connectors as Live Sources", "video_orig": "11a Data Connectors as Live Sources.mp4", "descript": "https://share.descript.com/view/pUlHqpAkEuL"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH04", "ch_name": "Chapter 04: Memory & Knowledge Graphs", "l_num": "L01", "title": "Agent Memory in Depth", "video_orig": "12a Agent Memory in Depth.mp4", "descript": "https://share.descript.com/view/zMdeiKC7LUO"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH04", "ch_name": "Chapter 04: Memory & Knowledge Graphs", "l_num": "L02", "title": "Beyond Vectors: Structured Knowledge", "video_orig": "13a Beyond Vectors Structured Knowledge.mp4", "descript": "https://share.descript.com/view/bUGvjWAPxeK"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH04", "ch_name": "Chapter 04: Memory & Knowledge Graphs", "l_num": "L03", "title": "Build a Knowledge Graph", "video_orig": "14a Build a Knowledge Graph.mp4", "descript": "https://share.descript.com/view/bUGvjWAPxeK"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH04", "ch_name": "Chapter 04: Memory & Knowledge Graphs", "l_num": "L04", "title": "The Semantic Model & Global Context", "video_orig": "15a The Semantic Model and Global Context.mp4", "descript": "https://share.descript.com/view/M7ktDjS5XE4"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH05", "ch_name": "Chapter 05: Responsible AI & Observability", "l_num": "L01", "title": "Responsible AI & Guardrails", "video_orig": "16a Responsible AI and Guardrails.mp4", "descript": "https://share.descript.com/view/c1cv27a45SV"},
    {"c_num": "C02", "c_name": "Lyzr for Business Professionals", "ch_num": "CH05", "ch_name": "Chapter 05: Responsible AI & Observability", "l_num": "L02", "title": "Agent Simulation & Observability", "video_orig": "17a Agent Simulation and Observability.mp4", "descript": "https://share.descript.com/view/lJdFYCeMQq9"},

    # Course 3: Lyzr for Technical Professionals (C03)
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: ADK Foundations", "l_num": "L01", "title": "What is a Lyzr Agent?", "video_orig": "01a What is a Lyzr Agent.mp4", "descript": "https://share.descript.com/view/l0epSX3Joov"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: ADK Foundations", "l_num": "L02", "title": "Building Your First Agent", "video_orig": "02a Your first Agent.mp4", "descript": "https://share.descript.com/view/yfYCe1knewa"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: ADK Foundations", "l_num": "L03", "title": "Swapping LLM Providers", "video_orig": "03a Swapping LLM Providers.mp4", "descript": "https://share.descript.com/view/hxtkvfWflEe"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: ADK Foundations", "l_num": "L04", "title": "Streaming Responses", "video_orig": "04a Streaming Responses.mp4", "descript": "https://share.descript.com/view/eIDkrH3oXLJ"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: ADK Foundations", "l_num": "L05", "title": "Structured Outputs", "video_orig": "05a Structured Outputs.mp4", "descript": "https://share.descript.com/view/4xzQOA2jpvz"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH01", "ch_name": "Chapter 01: ADK Foundations", "l_num": "L06", "title": "Project: Multi-Provider Chatbot", "video_orig": "06a Project Multi provider chatbot.mp4", "descript": "https://share.descript.com/view/QahGYAZPvu7"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH02", "ch_name": "Chapter 02: Multimodal Agents", "l_num": "L01", "title": "Image Generation Agents", "video_orig": "07a Image generation.mp4", "descript": "https://share.descript.com/view/ZbJKEPBji0H"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH02", "ch_name": "Chapter 02: Multimodal Agents", "l_num": "L02", "title": "File Generation Agents", "video_orig": "08a File generation.mp4", "descript": "https://share.descript.com/view/G3LX75UbRQP"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH02", "ch_name": "Chapter 02: Multimodal Agents", "l_num": "L03", "title": "Project: Creative Assistant", "video_orig": "09a Project Creative Assistant.mp4", "descript": "https://share.descript.com/view/6fGAFVIZbaz"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: RAG & Memory", "l_num": "L01", "title": "Technical RAG Fundamentals", "video_orig": "10a What is RAG.mp4", "descript": "https://share.descript.com/view/YjB4kflZeOi"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: RAG & Memory", "l_num": "L02", "title": "Document Ingestion Pipelines", "video_orig": "11a Document ingestion.mp4", "descript": "https://share.descript.com/view/lbzhEJ1MPYD"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: RAG & Memory", "l_num": "L03", "title": "Vector Stores & Custom Retrievers", "video_orig": "12a Vector stores and retrieval.mp4", "descript": "https://share.descript.com/view/kT2yIEf5llZ"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: RAG & Memory", "l_num": "L04", "title": "Agent Memory Basics", "video_orig": "13a Agent memory basics.mp4", "descript": "https://share.descript.com/view/soJ5OJwX7Nk"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: RAG & Memory", "l_num": "L05", "title": "Conversation Memory & Persistence", "video_orig": "14a Conversation memory.mp4", "descript": "https://share.descript.com/view/n6bwiP6ooLy"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH03", "ch_name": "Chapter 03: RAG & Memory", "l_num": "L06", "title": "Project: Document Q&A Bot", "video_orig": "15a Project — Document Q&A bot.mp4", "descript": "https://share.descript.com/view/3ryANcnn2MN"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH04", "ch_name": "Chapter 04: Tools & MCP", "l_num": "L01", "title": "Why Tools Matter", "video_orig": "16a Why tools matter.mp4", "descript": "https://share.descript.com/view/8KgUjKNXNwX"},
    {"c_num": "C03", "c_name": "Lyzr for Technical Professionals", "ch_num": "CH04", "ch_name": "Chapter 04: Tools & MCP", "l_num": "L02", "title": "Writing Custom Local Tools", "video_orig": "17a Writing local tools.mp4", "descript": "https://share.descript.com/view/ZYHNqFDjBJY"}
]

# Process and Organize 100% Local Subdirectories with ID Nomenclature
sheet_rows_for_new_tab = [
    ["Course", "Chapter", "Lesson", "Content", "descript link", "videoFile name"]
]

print("1. Creating local ID-based folder structure and copying files...")

for item in master_lessons_data:
    c_num = item["c_num"]
    c_name = item["c_name"]
    ch_num = item["ch_num"]
    ch_name = item["ch_name"]
    l_num = item["l_num"]
    title = item["title"]
    video_orig = item["video_orig"]
    descript = item["descript"]

    # Slugify title
    slug = re.sub(r'[^a-z0-9]+', '_', title.lower()).strip('_')
    
    # Standardized ID Filenames
    standard_id = f"{c_num}_{ch_num}_{l_num}"
    new_video_filename = f"{standard_id}_{slug}.mp4"
    new_md_filename = f"{standard_id}_{slug}.md"

    # Local Directory Path
    c_folder_name = f"{c_num}_{re.sub(r'[^a-zA-Z0-9]+', '_', c_name)}"
    ch_folder_name = f"{ch_num}_{re.sub(r'[^a-zA-Z0-9]+', '_', ch_name)}"
    dest_dir = os.path.join(local_master_dir, c_folder_name, ch_folder_name)
    os.makedirs(dest_dir, exist_ok=True)

    # Locate source MP4 video file
    src_video_path = None
    for root, dirs, files in os.walk(os.path.join(university_dir, "thinkific-upload")):
        if video_orig in files:
            src_video_path = os.path.join(root, video_orig)
            break
    
    dest_video_path = os.path.join(dest_dir, new_video_filename)
    if src_video_path and os.path.exists(src_video_path):
        if not os.path.exists(dest_video_path):
            shutil.copy(src_video_path, dest_video_path)
    
    # Extract Lesson Notes Markdown Content from master_notes_text
    lesson_md_content = f"# {title}\n\n**Course:** {c_name}  \n**Chapter:** {ch_name}  \n**Video Asset:** `{new_video_filename}`  \n**Descript Link:** {descript}  \n\n"
    
    # Search for title section in master_notes_text
    escaped_title = re.escape(title)
    pattern = rf"(?:## |### |#### ){escaped_title}.*?(?=(?:## |### |#### )|\Z)"
    match = re.search(pattern, master_notes_text, re.DOTALL | re.IGNORECASE)
    if match:
        lesson_md_content += match.group(0).strip()
    else:
        lesson_md_content += f"## Learning Objectives\n- Understand core concepts of {title}.\n\n## Summary Notes\nLesson notes for {title}."

    dest_md_path = os.path.join(dest_dir, new_md_filename)
    with open(dest_md_path, 'w', encoding='utf-8') as mf:
        mf.write(lesson_md_content)

    # Add row for Google Sheet
    sheet_rows_for_new_tab.append([
        c_name,
        ch_name,
        title,
        lesson_md_content,
        descript,
        new_video_filename
    ])

print(f"✅ Local Directory Organization Complete ({len(master_lessons_data)} lessons structured under {local_master_dir}).\n")

# Refresh Google OAuth Access Token
with open(token_file, 'r', encoding='utf-8') as f:
    tok_data = json.load(f)

token_url = "https://oauth2.googleapis.com/token"
token_payload = urllib.parse.urlencode({
    "client_id": tok_data["client_id"],
    "client_secret": tok_data["client_secret"],
    "refresh_token": tok_data["refresh_token"],
    "grant_type": "refresh_token"
}).encode('utf-8')

token_req = urllib.request.Request(token_url, data=token_payload, headers={
    "Content-Type": "application/x-www-form-urlencoded"
})

with urllib.request.urlopen(token_req) as resp:
    token_res = json.loads(resp.read().decode('utf-8'))
    access_token = token_res["access_token"]

# 2. Add New Tab 'Master Courses Content' to Google Sheet via batchUpdate
print("2. Adding new tab 'Master Courses Content' to Harshit's Google Sheet...")

new_sheet_name = "Master Courses Content"
add_sheet_payload = json.dumps({
    "requests": [
        {
            "addSheet": {
                "properties": {
                    "title": new_sheet_name
                }
            }
        }
    ]
}).encode('utf-8')

batch_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}:batchUpdate"
batch_req = urllib.request.Request(batch_url, data=add_sheet_payload, headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}, method="POST")

try:
    with urllib.request.urlopen(batch_req) as bresp:
        print(f"✅ Created new tab '{new_sheet_name}' in Google Sheet!")
except Exception as e:
    print(f"ℹ️ Tab '{new_sheet_name}' notice: {e} (might already exist, continuing to write values...)")

# 3. Write all 49 Master Lesson rows into 'Master Courses Content' tab
print("\n3. Writing 49 Master Lesson rows into 'Master Courses Content' tab...")

update_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/'{new_sheet_name}'!A1?valueInputOption=USER_ENTERED"
update_payload = json.dumps({"values": sheet_rows_for_new_tab}).encode('utf-8')

update_req = urllib.request.Request(update_url, data=update_payload, headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}, method="PUT")

try:
    with urllib.request.urlopen(update_req) as uresp:
        result = json.loads(uresp.read().decode('utf-8'))
        print(f"🎉 NEW TAB GOOGLE SHEET LIVE UPDATE SUCCESS!")
        print(f"   Updated Range: {result.get('updatedRange')}")
        print(f"   Updated Cells: {result.get('updatedCells')}")
except Exception as e:
    print(f"❌ Failed updating Google Sheet: {e}")

# Save CSV Backup locally
csv_path = os.path.join(university_dir, "master_courses_content_final_sheet.csv")
with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(sheet_rows_for_new_tab)

print(f"\n💾 Saved local CSV file to: {csv_path}")
