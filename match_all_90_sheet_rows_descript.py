import json
import os
import re
import urllib.request
import urllib.parse

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
backup_path = os.path.join(brain_dir, "harshit_google_sheet_backup.json")

with open(backup_path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

# Comprehensive Descript Title Matchers (Semantic & Keyword Matching)
descript_rules = [
    # SDK Track
    {"keywords": ["what is a lyzr agent"], "url": "https://share.descript.com/view/l0epSX3Joov"},
    {"keywords": ["your first agent"], "url": "https://share.descript.com/view/yfYCe1knewa"},
    {"keywords": ["swapping llm"], "url": "https://share.descript.com/view/hxtkvfWflEe"},
    {"keywords": ["streaming responses"], "url": "https://share.descript.com/view/eIDkrH3oXLJ"},
    {"keywords": ["structured outputs"], "url": "https://share.descript.com/view/4xzQOA2jpvz"},
    {"keywords": ["multi-provider chatbot", "multi provider chatbot"], "url": "https://share.descript.com/view/QahGYAZPvu7"},
    {"keywords": ["image generation"], "url": "https://share.descript.com/view/ZbJKEPBji0H"},
    {"keywords": ["file generation"], "url": "https://share.descript.com/view/G3LX75UbRQP"},
    {"keywords": ["creative assistant"], "url": "https://share.descript.com/view/6fGAFVIZbaz"},
    {"keywords": ["what is rag"], "url": "https://share.descript.com/view/YjB4kflZeOi"},
    {"keywords": ["document ingestion"], "url": "https://share.descript.com/view/lbzhEJ1MPYD"},
    {"keywords": ["vector stores"], "url": "https://share.descript.com/view/kT2yIEf5llZ"},
    {"keywords": ["agent memory basics"], "url": "https://share.descript.com/view/soJ5OJwX7Nk"},
    {"keywords": ["conversation memory"], "url": "https://share.descript.com/view/n6bwiP6ooLy"},
    {"keywords": ["document q&a bot", "document qa bot"], "url": "https://share.descript.com/view/3ryANcnn2MN"},
    {"keywords": ["why tools matter"], "url": "https://share.descript.com/view/8KgUjKNXNwX"},
    {"keywords": ["writing local tools"], "url": "https://share.descript.com/view/ZYHNqFDjBJY"},
    {"keywords": ["agent context", "tools and mcp", "tavily"], "url": "https://share.descript.com/view/dfJuVXwrXqd"},
    {"keywords": ["multi-step workflows", "gmail"], "url": "https://share.descript.com/view/zBBNFo83hvv"},

    # Studio Track
    {"keywords": ["welcome to agent studio"], "url": "https://share.descript.com/view/QSwoPpR6hKL"},
    {"keywords": ["build: choose a type", "build — choose a type"], "url": "https://share.descript.com/view/r0i0W0qxzAh"},
    {"keywords": ["equip: model, tool", "equip — model, tool"], "url": "https://share.descript.com/view/GobPzBquAVF"},
    {"keywords": ["govern: add guardrails", "govern — add guardrails"], "url": "https://share.descript.com/view/c1cv27a45SV"},
    {"keywords": ["playground based testing", "run it in the playground"], "url": "https://share.descript.com/view/lJdFYCeMQq9"},
    {"keywords": ["deploy: ship it", "deploy — ship it"], "url": "https://share.descript.com/view/s9Pgt7FDngv"},
    {"keywords": ["one agent, full lifecycle"], "url": "https://share.descript.com/view/W02dpgBGWAM"},
    {"keywords": ["what agent type should i build"], "url": "https://share.descript.com/view/FOzm28nV9YM"},
    {"keywords": ["lyzr manager"], "url": "https://share.descript.com/view/JxjoIomKT1C"},
    {"keywords": ["managers, part 2"], "url": "https://share.descript.com/view/HapNcaeURx7"},
    {"keywords": ["superflow: basic", "superflow: invoice reconciliation"], "url": "https://share.descript.com/view/e9Ny8ysXwMc"},
    {"keywords": ["superflow: loops", "superflow: advanced"], "url": "https://share.descript.com/view/cyOXlcLJI5R"},
    {"keywords": ["rag in studio"], "url": "https://share.descript.com/view/iLyDbKWJXxv"},
    {"keywords": ["build a knowledge base"], "url": "https://share.descript.com/view/u8SqXwIKzjT"},
    {"keywords": ["document parsing & ingestion", "document parsing and ingestion"], "url": "https://share.descript.com/view/CGqBLgAbGUG"},
    {"keywords": ["data connectors as live sources"], "url": "https://share.descript.com/view/pUlHqpAkEuL"},
    {"keywords": ["agent memory in depth"], "url": "https://share.descript.com/view/zMdeiKC7LUO"},
    {"keywords": ["structured knowledge", "beyond vectors"], "url": "https://share.descript.com/view/bUGvjWAPxeK"},
    {"keywords": ["responsible ai in studio"], "url": "https://share.descript.com/view/c1cv27a45SV"},
    {"keywords": ["simulation engine"], "url": "https://share.descript.com/view/lJdFYCeMQq9"}
]

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
    
    phase = row[0] if len(row) > 0 else ""
    course = row[1] if len(row) > 1 else ""
    lesson = row[3] if len(row) > 3 else ""

    matched_url = ""
    clean_l = lesson.lower().strip()

    if clean_l:
        for rule in descript_rules:
            for kw in rule["keywords"]:
                if kw in clean_l:
                    matched_url = rule["url"]
                    break
            if matched_url:
                break
    
    row[col_idx] = matched_url
    if matched_url:
        matched_count += 1
        print(f"Row {idx+1}: '{lesson}' -> {matched_url}")
    
    updated_rows.append(row)

print(f"\nTotal Matched Rows with Descript Links: {matched_count} out of {len(rows)-1} rows.")

# Update Google Sheet
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
        print(f"\n🎉 GOOGLE SHEET LIVE UPDATE SUCCESS! Range: {res.get('updatedRange')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")
