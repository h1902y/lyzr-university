import urllib.request
import urllib.parse
import json
import os
import csv
import re
import html
from concurrent.futures import ThreadPoolExecutor

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
university_dir = "/Users/hkc/Documents/lyzr/university"
csv_in_path = os.path.join(university_dir, "master_courses_content_final.csv")

print("==========================================================================")
print(" 🎙️ FETCHING FULL VERBATIM TRANSCRIPTS VIA DESCRIPT SIGNED TRANSCRIPT.JSON")
print("==========================================================================")

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

def find_signed_transcript_url(page_html: str) -> str | None:
    m = re.search(r'https://[^"\'\\ ]*?/transcript\.json\?[^"\'\\ ]+', page_html)
    if not m:
        return None
    return html.unescape(m.group(0))

def parse_descript_json_to_text(json_bytes: bytes) -> str:
    try:
        data = json.loads(json_bytes.decode('utf-8', errors='ignore'))
        words = []
        if isinstance(data, dict):
            # Check for words array or text array
            if "words" in data and isinstance(data["words"], list):
                for w in data["words"]:
                    if isinstance(w, dict) and "text" in w:
                        words.append(w["text"])
                    elif isinstance(w, str):
                        words.append(w)
            elif "events" in data and isinstance(data["events"], list):
                for ev in data["events"]:
                    if isinstance(ev, dict) and "text" in ev:
                        words.append(ev["text"])
        elif isinstance(data, list):
            for elem in data:
                if isinstance(elem, dict) and "text" in elem:
                    words.append(elem["text"])
                elif isinstance(elem, str):
                    words.append(elem)
        
        full_text = " ".join(words) if words else str(data)
        # Clean ASR errors
        full_text = re.sub(r'\bLizza\b', 'Lyzr', full_text, flags=re.IGNORECASE)
        full_text = re.sub(r'\bLizer\b', 'Lyzr', full_text, flags=re.IGNORECASE)
        full_text = re.sub(r'\s+', ' ', full_text).strip()
        return full_text
    except Exception as e:
        return ""

fetched_descript_cache = {}

def fetch_descript_transcript_direct(share_url: str):
    if not share_url or not share_url.startswith("https://share.descript.com/view/"):
        return share_url, None
    try:
        req = urllib.request.Request(share_url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as resp:
            page_html = resp.read().decode('utf-8', errors='ignore')
            t_url = find_signed_transcript_url(page_html)
            if t_url:
                t_req = urllib.request.Request(t_url, headers={"User-Agent": UA})
                with urllib.request.urlopen(t_req, timeout=15) as t_resp:
                    t_bytes = t_resp.read()
                    text = parse_descript_json_to_text(t_bytes)
                    if text:
                        return share_url, text
    except Exception as e:
        pass
    return share_url, None

# Read current CSV export
rows_list = []
with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    rows_list = list(reader)

unique_share_urls = set()
for r in rows_list:
    u = r[4]
    if u.startswith("https://share.descript.com/view/"):
        unique_share_urls.add(u)

print(f"Fetching signed transcript.json for {len(unique_share_urls)} unique Descript share links...")

with ThreadPoolExecutor(max_workers=8) as executor:
    results = executor.map(fetch_descript_transcript_direct, unique_share_urls)
    for url, text in results:
        if text:
            fetched_descript_cache[url] = text

print(f"✅ Successfully downloaded full transcripts for {len(fetched_descript_cache)} / {len(unique_share_urls)} Descript share links!\n")

# Update rows with newly downloaded Descript transcripts
updated_sheet_rows = [header]
updated_count = 0

for r in rows_list:
    c_name = r[0]
    ch_name = r[1]
    l_title = r[2]
    content_md = r[3]
    d_url = r[4]
    v_name = r[5]
    t_val = r[6] if len(r) > 6 else ""

    if d_url in fetched_descript_cache:
        t_val = fetched_descript_cache[d_url]
        updated_count += 1
        print(f" [{updated_count:2d}] Attached full Descript transcript ({len(t_val)} chars) for '{l_title}'")
    
    if len(r) > 6:
        r[6] = t_val
    else:
        r.append(t_val)

    updated_sheet_rows.append(r)

print(f"\n✅ Total lesson rows populated with verbatim Descript transcripts: {updated_count}")

# Refresh Google OAuth Access Token
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
csv_out_path = os.path.join(university_dir, "master_courses_content_descript_transcripts.csv")
with open(csv_out_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(updated_sheet_rows)

print(f"💾 Saved final CSV export to: {csv_out_path}")
