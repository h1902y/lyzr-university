import urllib.request
import urllib.parse
import json
import os
import re

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
backup_path = os.path.join(brain_dir, "harshit_google_sheet_backup.json")

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
    print("✅ Refreshed Google Access Token!")

# Fetch live sheet rows
read_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1!A1:Z200"
read_req = urllib.request.Request(read_url, headers={
    "Authorization": f"Bearer {access_token}"
})

with urllib.request.urlopen(read_req) as rresp:
    data = json.loads(rresp.read().decode('utf-8'))
    rows = data.get("values", [])
    print(f"Read {len(rows)} live rows from Sheet1.")

# Exact Title -> Descript URL mapping extracted from READMEs
exact_descript_map = {
    "what is a lyzr agent": "https://share.descript.com/view/l0epSX3Joov",
    "your first agent": "https://share.descript.com/view/yfYCe1knewa",
    "swapping llm providers": "https://share.descript.com/view/hxtkvfWflEe",
    "streaming responses": "https://share.descript.com/view/eIDkrH3oXLJ",
    "structured outputs": "https://share.descript.com/view/4xzQOA2jpvz",
    "multi-provider chatbot": "https://share.descript.com/view/QahGYAZPvu7",
    "project: multi-provider chatbot": "https://share.descript.com/view/QahGYAZPvu7",
    "image generation": "https://share.descript.com/view/ZbJKEPBji0H",
    "file generation": "https://share.descript.com/view/G3LX75UbRQP",
    "project: creative assistant": "https://share.descript.com/view/6fGAFVIZbaz",
    "creative assistant": "https://share.descript.com/view/6fGAFVIZbaz",
    "what is rag?": "https://share.descript.com/view/YjB4kflZeOi",
    "what is rag": "https://share.descript.com/view/YjB4kflZeOi",
    "document ingestion": "https://share.descript.com/view/lbzhEJ1MPYD",
    "vector stores and retrieval": "https://share.descript.com/view/kT2yIEf5llZ",
    "agent memory basics": "https://share.descript.com/view/soJ5OJwX7Nk",
    "conversation memory": "https://share.descript.com/view/n6bwiP6ooLy",
    "project: document q&a bot": "https://share.descript.com/view/3ryANcnn2MN",
    "document q&a bot": "https://share.descript.com/view/3ryANcnn2MN",
    "why tools matter": "https://share.descript.com/view/8KgUjKNXNwX",
    "writing local tools": "https://share.descript.com/view/ZYHNqFDjBJY",
    "agent context": "https://share.descript.com/view/dfJuVXwrXqd",
    "multi-step workflows": "https://share.descript.com/view/zBBNFo83hvv",
    "welcome to agent studio & the lifecycle": "https://share.descript.com/view/QSwoPpR6hKL",
    "build — choose a type & create an agent": "https://share.descript.com/view/r0i0W0qxzAh",
    "build: choose a type & create an agent": "https://share.descript.com/view/r0i0W0qxzAh",
    "equip — model, tool, knowledge": "https://share.descript.com/view/GobPzBquAVF",
    "equip: model, tool, memory, knowledge": "https://share.descript.com/view/GobPzBquAVF",
    "govern — add guardrails": "https://share.descript.com/view/c1cv27a45SV",
    "govern: add guardrails": "https://share.descript.com/view/c1cv27a45SV",
    "test — run it in the playground": "https://share.descript.com/view/lJdFYCeMQq9",
    "test: run it in the playground": "https://share.descript.com/view/lJdFYCeMQq9",
    "deploy — ship it": "https://share.descript.com/view/s9Pgt7FDngv",
    "deploy: ship it": "https://share.descript.com/view/s9Pgt7FDngv",
    "project: one agent, full lifecycle": "https://share.descript.com/view/W02dpgBGWAM",
    "one agent, full lifecycle": "https://share.descript.com/view/W02dpgBGWAM",
    "what agent type should i build?": "https://share.descript.com/view/FOzm28nV9YM",
    "what agent type should i build": "https://share.descript.com/view/FOzm28nV9YM",
    "lyzr manager": "https://share.descript.com/view/JxjoIomKT1C",
    "managers, part 2 — editing from the agent page": "https://share.descript.com/view/HapNcaeURx7",
    "superflow: invoice reconciliation": "https://share.descript.com/view/e9Ny8ysXwMc",
    "superflow: loops": "https://share.descript.com/view/cyOXlcLJI5R",
    "rag in studio": "https://share.descript.com/view/iLyDbKWJXxv",
    "build a knowledge base": "https://share.descript.com/view/u8SqXwIKzjT",
    "document parsing & ingestion": "https://share.descript.com/view/CGqBLgAbGUG",
    "data connectors as live sources": "https://share.descript.com/view/pUlHqpAkEuL",
    "agent memory in depth": "https://share.descript.com/view/zMdeiKC7LUO",
    "project: document q&a agent with memory": "https://share.descript.com/view/bUGvjWAPxeK"
}

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

normalized_dict = {normalize(k): v for k, v in exact_descript_map.items()}

# Header row
header = list(rows[0])

# Find or ensure Descript Link column (Column M index 12)
col_idx = 12
if len(header) <= col_idx:
    while len(header) <= col_idx:
        header.append("")
header[col_idx] = "Descript Link"

updated_rows = [header]
exact_matches_count = 0
blank_count = 0

for i in range(1, len(rows)):
    row = list(rows[i])
    while len(row) <= col_idx:
        row.append("")
    
    phase = row[0] if len(row) > 0 else ""
    course_name = row[1] if len(row) > 1 else ""
    lesson_name = row[3] if len(row) > 3 else ""

    # Exact normalized matching
    norm_lesson = normalize(lesson_name)
    descript_url = ""

    if norm_lesson in normalized_dict:
        descript_url = normalized_dict[norm_lesson]
        exact_matches_count += 1
    else:
        # Check substring match only if norm_lesson is sufficiently long
        for norm_key, url in normalized_dict.items():
            if (len(norm_key) > 8 and norm_key in norm_lesson) or (len(norm_lesson) > 8 and norm_lesson in norm_key):
                descript_url = url
                exact_matches_count += 1
                break
    
    if not descript_url:
        blank_count += 1

    row[col_idx] = descript_url
    updated_rows.append(row)

print(f"\nExact Matched Descript Links: {exact_matches_count}")
print(f"Unmatched/Blank Rows: {blank_count}")

# Push exact updates to Google Sheet
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
        print(f"   Updated Range: {result.get('updatedRange')}")
        print(f"   Updated Cells: {result.get('updatedCells')}")
except Exception as e:
    print(f"❌ Failed updating Google Sheet: {e}")
