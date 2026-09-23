import urllib.request
import urllib.parse
import json
import sys

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

read_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/'{encoded_tab_name}'!A1:G50"
read_req = urllib.request.Request(read_url, headers={
    "Authorization": f"Bearer {access_token}"
})

with urllib.request.urlopen(read_req) as rresp:
    res_data = json.loads(rresp.read().decode('utf-8'))
    sheet_values = res_data.get("values", [])

print("==========================================================================")
print(" 🔍 LIVE GOOGLE SHEET COLUMN G INSPECTION")
print("==========================================================================")

for idx, r in enumerate(sheet_values[:15], 1):
    c_name = r[0] if len(r) > 0 else ""
    l_title = r[2] if len(r) > 2 else ""
    t_val = r[6] if len(r) > 6 else ""
    print(f"Row {idx:2d} | [{c_name}] {l_title}")
    print(f"       Transcript (Length: {len(t_val)} chars): {t_val[:150]}...")
    print("-" * 70)
