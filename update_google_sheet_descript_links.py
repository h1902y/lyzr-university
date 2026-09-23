import urllib.request
import urllib.parse
import json
import os
import re

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
backup_path = os.path.join(brain_dir, "harshit_google_sheet_backup.json")

# Load backup rows
with open(backup_path, 'r', encoding='utf-8') as bf:
    rows = json.load(bf)

# Descript links map from SDK and Studio READMEs
descript_map = {
    # SDK Track Lessons
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
    "introduction to tools and mcp": "https://share.descript.com/view/dfJuVXwrXqd",
    "tavily mcp": "https://share.descript.com/view/zBBNFo83hvv",

    # Studio Track Lessons
    "welcome to agent studio": "https://share.descript.com/view/QSwoPpR6hKL",
    "build: choose a type": "https://share.descript.com/view/r0i0W0qxzAh",
    "equip: model, tool": "https://share.descript.com/view/GobPzBquAVF",
    "govern: add guardrails": "https://share.descript.com/view/c1cv27a45SV",
    "test: run it in the playground": "https://share.descript.com/view/lJdFYCeMQq9",
    "deploy: ship it": "https://share.descript.com/view/s9Pgt7FDngv",
    "one agent, full lifecycle": "https://share.descript.com/view/W02dpgBGWAM",
    "what agent type should i build": "https://share.descript.com/view/FOzm28nV9YM",
    "lyzr manager": "https://share.descript.com/view/JxjoIomKT1C",
    "managers, part 2": "https://share.descript.com/view/HapNcaeURx7",
    "superflow: invoice": "https://share.descript.com/view/e9Ny8ysXwMc",
    "superflow: loops": "https://share.descript.com/view/cyOXlcLJI5R",
    "rag in studio": "https://share.descript.com/view/iLyDbKWJXxv",
    "build a knowledge base": "https://share.descript.com/view/u8SqXwIKzjT",
    "document parsing & ingestion": "https://share.descript.com/view/CGqBLgAbGUG",
    "data connectors as live sources": "https://share.descript.com/view/pUlHqpAkEuL",
    "agent memory in depth": "https://share.descript.com/view/zMdeiKC7LUO",
    "capstone": "https://share.descript.com/view/bUGvjWAPxeK"
}

# Process & Update Rows
updated_rows = []
header = list(rows[0])
if "Descript Link" not in header:
    header.append("Descript Link")

updated_rows.append(header)

updated_count = 0

for i in range(1, len(rows)):
    row = list(rows[i])
    # Pad row to match length
    while len(row) < len(header) - 1:
        row.append("")
    
    phase = row[0] if len(row) > 0 else ""
    course_name = row[1] if len(row) > 1 else ""
    lesson_name = row[3] if len(row) > 3 else ""
    master_course = row[7] if len(row) > 7 else ""

    # Update Master Course Nomenclature
    if master_course == "Lyzr for Developers" or "SDK" in phase or "Code" in phase or "ADK" in phase:
        row[7] = "Lyzr for Technical Professionals"
    elif master_course == "Lyzr for Business Teams" or "Studio" in phase or "Lifecycle" in course_name:
        row[7] = "Lyzr for Business Professionals"
    elif "Foundations" in phase or "Overview" in course_name:
        row[7] = "Lyzr Foundations"

    # Find matching Descript link
    matched_link = ""
    clean_l = lesson_name.lower()
    for key, url in descript_map.items():
        if key in clean_l or clean_l in key:
            matched_link = url
            break
    
    if len(row) < len(header):
        row.append(matched_link)
    else:
        row[len(header)-1] = matched_link
    
    if matched_link:
        updated_count += 1
    
    updated_rows.append(row)

print(f"Mapped Descript Links for {updated_count} lesson rows!")

# Refresh access token
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

# Update Google Sheet via Google Sheets API v4
update_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1!A1?valueInputOption=USER_ENTERED"
update_payload = json.dumps({
    "values": updated_rows
}).encode('utf-8')

update_req = urllib.request.Request(update_url, data=update_payload, headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}, method="PUT")

try:
    with urllib.request.urlopen(update_req) as uresp:
        result = json.loads(uresp.read().decode('utf-8'))
        print(f"🎉 GOOGLE SHEET LIVE UPDATE SUCCESS!")
        print(f"   Updated Cells: {result.get('updatedCells')}")
        print(f"   Updated Range: {result.get('updatedRange')}")
except Exception as e:
    print(f"❌ Failed updating Google Sheet: {e}")
