import urllib.request
import urllib.parse
import json
import os
import csv
import sys
import re

csv.field_size_limit(sys.maxsize)

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
university_dir = "/Users/hkc/Documents/lyzr/university"
csv_in_path = os.path.join(university_dir, "master_courses_content_final_clean.csv")

print("==========================================================================")
print(" 🧹 CONVERTING CONTENT TO CLEAN PLAIN TEXT (NO HTML, NO MARKDOWN TAGS)")
print("==========================================================================")

def to_clean_plain_text(md_or_html):
    if not md_or_html:
        return ""
    
    text = md_or_html

    # Remove HTML tags completely
    text = re.sub(r'<[^>]+>', '', text)

    # Remove markdown headers #, ##, ###
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)

    # Remove markdown bold/italic asterisks **bold** -> bold
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)

    # Remove inline backticks `code` -> code
    text = re.sub(r'`([^`]+)`', r'\1', text)

    # Replace markdown bullet dashes - -> •
    lines = text.split('\n')
    cleaned_lines = []
    for l in lines:
        l_s = l.strip()
        if l_s.startswith('- ') or l_s.startswith('* '):
            cleaned_lines.append(f"• {l_s[2:].strip()}")
        else:
            cleaned_lines.append(l_s)

    text = '\n'.join(cleaned_lines)

    # Remove multiple consecutive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

updated_rows = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_rows.append(header)

    cleaned_count = 0
    for row in reader:
        raw_c = row[3] if len(row) > 3 else ""

        clean_c = to_clean_plain_text(raw_c)
        row[3] = clean_c
        cleaned_count += 1

        if cleaned_count <= 3:
            print(f"Row {cleaned_count} Clean Plain Text Preview:")
            print(clean_c[:250])
            print("-" * 60)

        updated_rows.append(row)

print(f"\n✅ Converted lesson notes content to clean plain text for all {cleaned_count} rows.\n")

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

# Push live update to Google Sheet
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
        print(f"🎉 GOOGLE SHEET CLEAN PLAIN TEXT LIVE UPDATE SUCCESS!")
        print(f"   Updated Range: {res.get('updatedRange')}")
        print(f"   Updated Cells: {res.get('updatedCells')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")

# Save CSV backup
csv_out_path = os.path.join(university_dir, "master_courses_content_plain_text.csv")
with open(csv_out_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(updated_rows)

print(f"💾 Saved clean plain text CSV export to: {csv_out_path}")
