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
print(" 🔗 UPDATING DESCRIPT SHARE LINK FOR TOOLS & MCP SERVERS (JYCOaor01EZ)")
print("==========================================================================")

# Target Descript share URL for Tools & MCP lessons
jyco_url = "https://share.descript.com/view/JYCOaor01EZ"

mcp_lesson_keywords = [
    "tools and mcp",
    "configuring tavily",
    "integrating gmail",
    "why tools matter",
    "writing custom local tools",
    "writing local tools"
]

updated_rows = []
matched_count = 0

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_rows.append(header)

    for row in reader:
        c_name = row[0]
        ch_name = row[1]
        l_title = row[2]
        d_url = row[4]

        # Check if lesson is a Tools & MCP Server lesson
        l_title_lower = l_title.lower()
        if any(kw in l_title_lower for kw in mcp_lesson_keywords):
            row[4] = jyco_url
            matched_count += 1
            print(f" [{matched_count}] Updated '{l_title}' -> {jyco_url}")
        
        updated_rows.append(row)

print(f"\n✅ Updated Descript Link to '{jyco_url}' for {matched_count} Tools & MCP lesson rows.")

# Refresh Access Token
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

print(f"💾 Saved updated CSV backup to: {csv_out_path}")
