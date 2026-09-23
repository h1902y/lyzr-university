import urllib.request
import urllib.parse
import json
import os

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
backup_path = os.path.join(brain_dir, "harshit_google_sheet_backup.json")

with open(backup_path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

# Provenance-Based Descript Mapping:
# 1. Foundations Track -> Descript links from complete_conversation_part2.md
# 2. ADK & Studio Tracks -> Descript links from complete_conversation.md

foundations_part2_map = {
    "welcome to agent studio & the lifecycle": "https://share.descript.com/view/M7ktDjS5XE4",
    "build: choose a type": "https://share.descript.com/view/M7ktDjS5XE4",
    "equip: model, tool": "https://share.descript.com/view/M7ktDjS5XE4",
    "govern: add guardrails": "https://share.descript.com/view/M7ktDjS5XE4",
    "playground based testing": "https://share.descript.com/view/M7ktDjS5XE4",
    "deploy: ship it": "https://share.descript.com/view/M7ktDjS5XE4",
    "project: one agent, full lifecycle": "https://share.descript.com/view/M7ktDjS5XE4",
    "introduction to lyzr platform": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "client success stories": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "the lyzr stack and architecture": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "architect overview": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "studio overview": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "lyzr capabilities": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "computer agent": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "git agent": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "designing knowledge bases": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "pdf parsing strategies": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "retrieval algorithms": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "wiring kb to agent": "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8",
    "introduction to tools and mcp": "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9",
    "configuring tavily mcp": "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9",
    "integrating gmail": "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9"
}

adk_studio_part1_map = {
    # SDK Track
    "what is a lyzr agent": "https://share.descript.com/view/l0epSX3Joov",
    "your first agent": "https://share.descript.com/view/yfYCe1knewa",
    "swapping llm providers": "https://share.descript.com/view/hxtkvfWflEe",
    "streaming responses": "https://share.descript.com/view/eIDkrH3oXLJ",
    "structured outputs": "https://share.descript.com/view/4xzQOA2jpvz",
    "multi-provider chatbot": "https://share.descript.com/view/QahGYAZPvu7",
    "image generation": "https://share.descript.com/view/ZbJKEPBji0H",
    "file generation": "https://share.descript.com/view/G3LX75UbRQP",
    "creative assistant": "https://share.descript.com/view/6fGAFVIZbaz",
    "what is rag": "https://share.descript.com/view/YjB4kflZeOi",
    "document ingestion": "https://share.descript.com/view/lbzhEJ1MPYD",
    "vector stores and retrieval": "https://share.descript.com/view/kT2yIEf5llZ",
    "agent memory basics": "https://share.descript.com/view/soJ5OJwX7Nk",
    "conversation memory": "https://share.descript.com/view/n6bwiP6ooLy",
    "document q&a bot": "https://share.descript.com/view/3ryANcnn2MN",
    "why tools matter": "https://share.descript.com/view/8KgUjKNXNwX",
    "writing local tools": "https://share.descript.com/view/ZYHNqFDjBJY",

    # Studio Track
    "what agent type should i build": "https://share.descript.com/view/FOzm28nV9YM",
    "lyzr manager": "https://share.descript.com/view/JxjoIomKT1C",
    "managers, part 2": "https://share.descript.com/view/HapNcaeURx7",
    "superflow: basic": "https://share.descript.com/view/e9Ny8ysXwMc",
    "superflow: invoice": "https://share.descript.com/view/e9Ny8ysXwMc",
    "superflow: loops": "https://share.descript.com/view/cyOXlcLJI5R",
    "superflow: advanced": "https://share.descript.com/view/cyOXlcLJI5R",
    "rag in studio": "https://share.descript.com/view/iLyDbKWJXxv",
    "build a knowledge base": "https://share.descript.com/view/u8SqXwIKzjT",
    "document parsing & ingestion": "https://share.descript.com/view/CGqBLgAbGUG",
    "document parsing and ingestion": "https://share.descript.com/view/CGqBLgAbGUG",
    "data connectors as live sources": "https://share.descript.com/view/pUlHqpAkEuL",
    "agent memory in depth": "https://share.descript.com/view/zMdeiKC7LUO",
    "beyond vectors": "https://share.descript.com/view/bUGvjWAPxeK",
    "structured knowledge": "https://share.descript.com/view/bUGvjWAPxeK",
    "build a knowledge graph": "https://share.descript.com/view/bUGvjWAPxeK"
}

col_idx = 12
header = list(rows[0])
if len(header) <= col_idx:
    while len(header) <= col_idx:
        header.append("")
header[col_idx] = "Descript Link"

updated_rows = [header]
foundations_count = 0
adk_studio_count = 0

for idx, r in enumerate(rows[1:], 1):
    row = list(r)
    while len(row) <= col_idx:
        row.append("")
    
    phase = row[0] if len(row) > 0 else ""
    lesson = row[3] if len(row) > 3 else ""
    master_course = row[7] if len(row) > 7 else ""
    clean_l = lesson.lower().strip()

    matched_url = ""
    if clean_l:
        # Check Foundations (Part 2 Provenance)
        if "Foundations" in phase or master_course == "Lyzr Foundations" or "Lifecycle" in row[1]:
            for k, url in foundations_part2_map.items():
                if k in clean_l or clean_l in k:
                    matched_url = url
                    foundations_count += 1
                    break
        
        # Check ADK & Studio (Part 1 Provenance)
        if not matched_url:
            for k, url in adk_studio_part1_map.items():
                if k in clean_l or clean_l in k:
                    matched_url = url
                    adk_studio_count += 1
                    break
    
    row[col_idx] = matched_url
    updated_rows.append(row)

print(f"✅ Mapped Foundations Track Descript Links (from part2.md): {foundations_count}")
print(f"✅ Mapped ADK & Studio Track Descript Links (from part1.md): {adk_studio_count}")
print(f"Total Provenance-Verified Mapped Rows: {foundations_count + adk_studio_count}\n")

# Refresh Access Token
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

update_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1!A1?valueInputOption=USER_ENTERED"
update_payload = json.dumps({"values": updated_rows}).encode('utf-8')

update_req = urllib.request.Request(update_url, data=update_payload, headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}, method="PUT")

try:
    with urllib.request.urlopen(update_req) as uresp:
        res = json.loads(uresp.read().decode('utf-8'))
        print(f"🎉 PROVENANCE-BASED GOOGLE SHEET UPDATE SUCCESS! Range: {res.get('updatedRange')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")
