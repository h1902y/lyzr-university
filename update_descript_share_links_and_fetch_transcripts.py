import urllib.request
import urllib.parse
import json
import os
import csv
import re

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
university_dir = "/Users/hkc/Documents/lyzr/university"

print("==========================================================================")
print(" 🔄 UPDATING DESCRIPT SHARE LINKS & FETCHING TRANSCRIPTS FROM DESCRIPT")
print("==========================================================================")

# Replacement rules for Descript web URLs -> share URLs
link_replacements = {
    "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8": "https://share.descript.com/view/M7ktDjS5XE4",
    "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9": "https://share.descript.com/view/xYNw4wPwzjT"
}

# Function to fetch raw transcript text from Descript share URL
def fetch_descript_transcript(share_url):
    if not share_url or not share_url.startswith("https://share.descript.com/view/"):
        return None
    try:
        req = urllib.request.Request(share_url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # Search for transcript JSON / __NEXT_DATA__ / window.__INITIAL_STATE__
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
            if m:
                next_data = json.loads(m.group(1))
                # Traverse next_data for transcript text or words
                raw_str = json.dumps(next_data)
                # Find all text segments
                paragraphs = re.findall(r'"text":"([^"]+)"', raw_str)
                if paragraphs:
                    full_text = " ".join([p for p in paragraphs if len(p) > 2 and not p.startswith('http')])
                    # Clean ASR mistakes
                    full_text = re.sub(r'\bLizza\b', 'Lyzr', full_text, flags=re.IGNORECASE)
                    full_text = re.sub(r'\bLizer\b', 'Lyzr', full_text, flags=re.IGNORECASE)
                    full_text = re.sub(r'\s+', ' ', full_text).strip()
                    return full_text
    except Exception as e:
        print(f" ⚠️ Could not fetch live transcript for {share_url}: {e}")
    return None

# Read current CSV export
csv_in_path = os.path.join(university_dir, "master_courses_content_with_transcripts.csv")
updated_rows = []

replaced_links_count = 0
fetched_transcripts_count = 0

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_rows.append(header)

    for row in reader:
        c_name = row[0]
        ch_name = row[1]
        l_title = row[2]
        content_md = row[3]
        descript_url = row[4]
        video_filename = row[5]
        transcript_val = row[6] if len(row) > 6 else ""

        # Apply link replacement rule
        for old_web_url, new_share_url in link_replacements.items():
            if old_web_url in descript_url:
                descript_url = new_share_url
                row[4] = new_share_url
                replaced_links_count += 1
                break
        
        # Try fetching live transcript from Descript share URL if transcript_val is short/generic
        if descript_url.startswith("https://share.descript.com/view/"):
            live_t = fetch_descript_transcript(descript_url)
            if live_t and len(live_t) > 50:
                row[6] = live_t
                fetched_transcripts_count += 1

        updated_rows.append(row)

print(f"✅ Replaced web URLs with public Descript Share URLs for {replaced_links_count} rows.")
print(f"✅ Fetched live Descript transcripts for {fetched_transcripts_count} rows.\n")

# Refresh Google OAuth Access Token
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

# Update Google Sheet 'Master Courses Content' tab live
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

print(f"\n💾 Saved updated CSV export to: {csv_out_path}")
