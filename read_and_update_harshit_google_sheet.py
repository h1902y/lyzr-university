import urllib.request
import urllib.parse
import json
import os

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"

print("==========================================================================")
print(" 📊 UPDATING HARSHIT'S GOOGLE SHEET (1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk)")
print("==========================================================================")

with open(token_file, 'r', encoding='utf-8') as f:
    tok_data = json.load(f)

# Refresh access token
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
    print("✅ Successfully refreshed Google API Access Token!")

# 1. Fetch current Sheet1 values
read_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1!A1:Z200"
read_req = urllib.request.Request(read_url, headers={
    "Authorization": f"Bearer {access_token}"
})

with urllib.request.urlopen(read_req) as rresp:
    data = json.loads(rresp.read().decode('utf-8'))
    rows = data.get("values", [])
    print(f"Read {len(rows)} rows from Harshit's Google Sheet.\n")
    if rows:
        print("Current Header Row:", rows[0])
        for idx in range(min(5, len(rows))):
            print(f" Row {idx+1}: {rows[idx]}")

# Save backup copy locally
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
backup_path = os.path.join(brain_dir, "harshit_google_sheet_backup.json")
with open(backup_path, 'w', encoding='utf-8') as bf:
    json.dump(rows, bf, indent=2)
print(f"\n💾 Saved sheet backup to: {backup_path}")
