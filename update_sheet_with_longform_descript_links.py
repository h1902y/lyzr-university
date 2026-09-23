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

# Master Descript Map mapping lesson / course names to exact Descript URLs (individual or long-form slice)
descript_master_map = {
    # 1. Course 1: Lyzr Foundations (Long-form Descript: l0epSX3Joov)
    "introduction to lyzr platform": "https://share.descript.com/view/l0epSX3Joov",
    "client success stories": "https://share.descript.com/view/l0epSX3Joov",
    "the lyzr stack and architecture": "https://share.descript.com/view/l0epSX3Joov",
    "architect overview": "https://share.descript.com/view/l0epSX3Joov",
    "studio overview": "https://share.descript.com/view/l0epSX3Joov",
    "lyzr capabilities": "https://share.descript.com/view/l0epSX3Joov",
    "computer agent": "https://share.descript.com/view/l0epSX3Joov",
    "git agent": "https://share.descript.com/view/l0epSX3Joov",
    "designing knowledge bases": "https://share.descript.com/view/M7ktDjS5XE4",
    "pdf parsing strategies": "https://share.descript.com/view/M7ktDjS5XE4",
    "retrieval algorithms": "https://share.descript.com/view/M7ktDjS5XE4",
    "wiring kb to agent": "https://share.descript.com/view/M7ktDjS5XE4",
    "introduction to tools and mcp": "https://share.descript.com/view/JYCOaor01EZ",
    "configuring tavily mcp": "https://share.descript.com/view/JYCOaor01EZ",
    "integrating gmail": "https://share.descript.com/view/JYCOaor01EZ",

    # 2. Course 2: Studio Track (Individual + Long-form Descript: M7ktDjS5XE4)
    "welcome to agent studio & the lifecycle": "https://share.descript.com/view/QSwoPpR6hKL",
    "welcome to agent studio": "https://share.descript.com/view/QSwoPpR6hKL",
    "build: choose a type": "https://share.descript.com/view/r0i0W0qxzAh",
    "build — choose a type": "https://share.descript.com/view/r0i0W0qxzAh",
    "equip: model, tool": "https://share.descript.com/view/GobPzBquAVF",
    "equip — model, tool": "https://share.descript.com/view/GobPzBquAVF",
    "govern: add guardrails": "https://share.descript.com/view/c1cv27a45SV",
    "govern — add guardrails": "https://share.descript.com/view/c1cv27a45SV",
    "playground based testing": "https://share.descript.com/view/lJdFYCeMQq9",
    "test: run it in the playground": "https://share.descript.com/view/lJdFYCeMQq9",
    "deploy: ship it": "https://share.descript.com/view/s9Pgt7FDngv",
    "deploy — ship it": "https://share.descript.com/view/s9Pgt7FDngv",
    "one agent, full lifecycle": "https://share.descript.com/view/W02dpgBGWAM",
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
    "build a knowledge graph": "https://share.descript.com/view/bUGvjWAPxeK",
    "the semantic model": "https://share.descript.com/view/M7ktDjS5XE4",
    "global context": "https://share.descript.com/view/M7ktDjS5XE4",
    "responsible ai in studio": "https://share.descript.com/view/c1cv27a45SV",
    "responsible ai & guardrails": "https://share.descript.com/view/c1cv27a45SV",
    "the simulation engine": "https://share.descript.com/view/lJdFYCeMQq9",
    "agent simulation & observability": "https://share.descript.com/view/lJdFYCeMQq9",

    # 3. Course 3: SDK Track (Individual Descript Share Links)
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
    "writing local tools": "https://share.descript.com/view/ZYHNqFDjBJY"
}

col_idx = 12
header = list(rows[0])
if len(header) <= col_idx:
    while len(header) <= col_idx:
        header.append("")
header[col_idx] = "Descript Link"

updated_rows = [header]
matched_count = 0

for idx, r in enumerate(rows[1:], 1):
    row = list(r)
    while len(row) <= col_idx:
        row.append("")
    
    lesson = row[3] if len(row) > 3 else ""
    clean_l = lesson.lower().strip()

    matched_url = ""
    if clean_l:
        for k, url in descript_master_map.items():
            if k in clean_l or clean_l in k:
                matched_url = url
                break
    
    row[col_idx] = matched_url
    if matched_url:
        matched_count += 1
    
    updated_rows.append(row)

print(f"Mapped Descript links for {matched_count} lesson rows!")

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

update_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1!A1?valueInputOption=USER_ENTERED"
update_payload = json.dumps({"values": updated_rows}).encode('utf-8')

update_req = urllib.request.Request(update_url, data=update_payload, headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}, method="PUT")

try:
    with urllib.request.urlopen(update_req) as uresp:
        res = json.loads(uresp.read().decode('utf-8'))
        print(f"🎉 GOOGLE SHEET LIVE UPDATE SUCCESS! Range: {res.get('updatedRange')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")
