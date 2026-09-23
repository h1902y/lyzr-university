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
csv_in_path = os.path.join(university_dir, "master_courses_content_descript_transcripts_final.csv")

print("==========================================================================")
print(" 🧹 EXTRACTING ONLY PURE SPOKEN BODY TEXT (ZERO METADATA / ZERO JSON)")
print("==========================================================================")

def extract_only_spoken_body_text(raw_transcript):
    if not raw_transcript:
        return ""
    
    # Extract all 'body' field values from Descript transcript payload
    # Pattern matching 'body': '...' or 'body': "..." or 'body' '...'
    body_words = re.findall(r"'body'\s*[:']\s*'?([^',]+)'?", raw_transcript)
    if not body_words:
        body_words = re.findall(r'"body"\s*:\s*"([^"]+)"', raw_transcript)
    
    if body_words:
        # Join words into continuous text
        spoken_text = " ".join([w.strip("'\"") for w in body_words if w.strip("'\"")])
    else:
        # If no body regex match, strip all JSON keys & numbers
        spoken_text = re.sub(r"'(?:version|segments|speaker|startTime|endTime|id|type|offset|duration)'\s*[^,]*,?", "", raw_transcript)
        spoken_text = re.sub(r'"(?:version|segments|speaker|startTime|endTime|id|type|offset|duration)"\s*:[^,]*,?', "", spoken_text)
        spoken_text = re.sub(r'[{}[\]":]', ' ', spoken_text)
        spoken_text = re.sub(r'\b\d+\.\d+\b', '', spoken_text) # remove float timestamps

    # Fix ASR term errors
    spoken_text = re.sub(r'\bLizza\b', 'Lyzr', spoken_text, flags=re.IGNORECASE)
    spoken_text = re.sub(r'\bLizer\b', 'Lyzr', spoken_text, flags=re.IGNORECASE)
    spoken_text = re.sub(r'\bLizar\b', 'Lyzr', spoken_text, flags=re.IGNORECASE)

    # Clean double spaces and punctuation formatting
    spoken_text = re.sub(r'\s+', ' ', spoken_text).strip()

    # Cap safe cell size at 40,000 chars
    if len(spoken_text) > 40000:
        spoken_text = spoken_text[:40000] + " ..."

    return spoken_text

updated_rows = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_rows.append(header)

    for idx, row in enumerate(reader, 1):
        c_name = row[0]
        l_title = row[2]
        raw_t = row[6] if len(row) > 6 else ""

        pure_t = extract_only_spoken_body_text(raw_t)

        if len(row) > 6:
            row[6] = pure_t
        else:
            row.append(pure_t)

        if idx <= 5:
            print(f"Row {idx:2d} | [{c_name}] {l_title}")
            print(f"       Clean Spoken Text Sample ({len(pure_t)} chars): {pure_t[:150]}...\n")

        updated_rows.append(row)

print(f"✅ Extracted pure spoken text for all {len(updated_rows)-1} lesson rows!\n")

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
        print(f"🎉 GOOGLE SHEET PURE TRANSCRIPTS LIVE UPDATE SUCCESS!")
        print(f"   Updated Range: {res.get('updatedRange')}")
        print(f"   Updated Cells: {res.get('updatedCells')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")

# Save CSV backup
csv_out_path = os.path.join(university_dir, "master_courses_content_pure_transcripts.csv")
with open(csv_out_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(updated_rows)

print(f"💾 Saved pure transcript CSV export to: {csv_out_path}")
