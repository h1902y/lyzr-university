import urllib.request
import urllib.parse
import json

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"

with open(token_file, 'r', encoding='utf-8') as f:
    tok_data = json.load(f)

token_payload = urllib.parse.urlencode({
    "client_id": tok_data["client_id"],
    "client_secret": tok_data["client_secret"],
    "refresh_token": tok_data["refresh_token"],
    "grant_type": "refresh_token"
}).encode('utf-8')

token_req = urllib.request.Request("https://oauth2.googleapis.com/token", data=token_payload, headers={
    "Content-Type": "application/x-www-form-urlencoded"
})

with urllib.request.urlopen(token_req) as resp:
    access_token = json.loads(resp.read().decode('utf-8'))["access_token"]

tab_name = "Master Courses Content"
encoded_tab_name = urllib.parse.quote(tab_name)

read_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/'{encoded_tab_name}'!A1:D10"
read_req = urllib.request.Request(read_url, headers={
    "Authorization": f"Bearer {access_token}"
})

with urllib.request.urlopen(read_req) as rresp:
    res_data = json.loads(rresp.read().decode('utf-8'))
    sheet_values = res_data.get("values", [])

print("==========================================================================")
print(" 🔍 LIVE GOOGLE SHEET COLUMN D (CONTENT) INSPECTION")
print("==========================================================================")

for idx, r in enumerate(sheet_values[:5], 1):
    l_title = r[2] if len(r) > 2 else ""
    c_val = r[3] if len(r) > 3 else ""
    print(f"Row {idx:2d} | Lesson: {l_title}")
    print(f"Content Preview:\n{c_val[:300]}")
    print("=" * 70)
