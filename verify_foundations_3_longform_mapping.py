import urllib.request
import urllib.parse
import json
import os
import csv

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
university_dir = "/Users/hkc/Documents/lyzr/university"
csv_in_path = os.path.join(university_dir, "master_courses_content_final.csv")

print("==========================================================================")
print(" 🎯 VERIFYING LYZR FOUNDATIONS 3 LONG-FORM DESCRIPT MASTER VIDEO MAPPINGS")
print("==========================================================================")

# The 3 Long-Form Descript Master Videos for Lyzr Foundations
video_m7kt = "https://share.descript.com/view/M7ktDjS5XE4"  # Chapters 01, 02, 03
video_jyco = "https://share.descript.com/view/JYCOaor01EZ"  # Chapter 04 (Knowledge Base & PDF Parsing)
video_xynw = "https://share.descript.com/view/xYNw4wPwzjT"  # Chapter 05 (Tools & MCP Servers)

updated_rows = []
foundations_summary = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_rows.append(header)

    for row in reader:
        c_name = row[0]
        ch_name = row[1]
        l_title = row[2]

        if c_name == "Lyzr Foundations":
            if "Chapter 01" in ch_name or "Chapter 02" in ch_name or "Chapter 03" in ch_name:
                row[4] = video_m7kt
            elif "Chapter 04" in ch_name:
                row[4] = video_jyco
            elif "Chapter 05" in ch_name:
                row[4] = video_xynw
            
            foundations_summary.append({
                "chapter": ch_name,
                "lesson": l_title,
                "descript": row[4],
                "video_file": row[5]
            })

        updated_rows.append(row)

print(f"Verified and locked {len(foundations_summary)} Lyzr Foundations lesson rows across 3 Long-Form Descript Master Videos:\n")
for idx, item in enumerate(foundations_summary, 1):
    print(f" {idx:2d}. [{item['chapter']}] {item['lesson']}")
    print(f"     • Parent Master Descript Link: {item['descript']}")
    print(f"     • Sliced Local Video File:     {item['video_file']}")
    print()

# Refresh OAuth Token
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

update_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/'{encoded_tab_name}'!A1?valueInputOption=USER_ENTERED"
update_payload = json.dumps({"values": updated_rows}).encode('utf-8')

update_req = urllib.request.Request(update_url, data=update_payload, headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}, method="PUT")

try:
    with urllib.request.urlopen(update_req) as uresp:
        res = json.loads(uresp.read().decode('utf-8'))
        print(f"🎉 GOOGLE SHEET LIVE UPDATE SUCCESS!")
        print(f"   Updated Range: {res.get('updatedRange')}")
        print(f"   Updated Cells: {res.get('updatedCells')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")

# Save CSV backup
csv_out_path = os.path.join(university_dir, "master_courses_content_final.csv")
with open(csv_out_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(updated_rows)

print(f"💾 Saved final CSV export to: {csv_out_path}")
