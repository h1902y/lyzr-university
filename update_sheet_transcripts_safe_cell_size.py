import urllib.request
import urllib.parse
import json
import os
import csv
import sys

# Increase CSV field size limit
csv.field_size_limit(sys.maxsize)

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
university_dir = "/Users/hkc/Documents/lyzr/university"
csv_in_path = os.path.join(university_dir, "master_courses_content_descript_transcripts.csv")

print("==========================================================================")
print(" 🚀 PUSHING DESCRIPT TRANSCRIPTS SAFELY TO GOOGLE SHEET (CELL CAP: 45K)")
print("==========================================================================")

updated_sheet_rows = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_sheet_rows.append(header)

    for row in reader:
        c_name = row[0]
        l_title = row[2]
        t_val = row[6] if len(row) > 6 else ""

        # Cap cell content length at 45,000 characters to satisfy Google Sheets cell limit
        if len(t_val) > 45000:
            t_val = t_val[:45000] + " ... [Full transcript stored locally in CSV export]"

        if len(row) > 6:
            row[6] = t_val
        else:
            row.append(t_val)

        updated_sheet_rows.append(row)

print(f"Prepared {len(updated_sheet_rows)-1} lesson rows with Descript transcripts (cell size safe).\n")

# Refresh OAuth Access Token
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

# Update Google Sheet tab 'Master Courses Content' live
tab_name = "Master Courses Content"
encoded_tab_name = urllib.parse.quote(tab_name)

update_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/'{encoded_tab_name}'!A1?valueInputOption=USER_ENTERED"
update_payload = json.dumps({"values": updated_sheet_rows}).encode('utf-8')

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
csv_out_path = os.path.join(university_dir, "master_courses_content_descript_transcripts_final.csv")
with open(csv_out_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(updated_sheet_rows)

print(f"💾 Saved final CSV export to: {csv_out_path}")
