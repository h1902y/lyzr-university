import urllib.request
import urllib.parse
import json
import os
import csv
import re
from concurrent.futures import ThreadPoolExecutor

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
university_dir = "/Users/hkc/Documents/lyzr/university"

print("==========================================================================")
print(" 🚀 FAST PARALLEL DESCRIPT SHARE LINK & TRANSCRIPT UPDATE")
print("==========================================================================")

link_replacements = {
    "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8": "https://share.descript.com/view/M7ktDjS5XE4",
    "https://web.descript.com/8ece633a-8635-4160-b524-0879d46eaa70/27cc9": "https://share.descript.com/view/xYNw4wPwzjT"
}

transcript_cache = {}

def fetch_single_url(share_url):
    if not share_url or not share_url.startswith("https://share.descript.com/view/"):
        return share_url, None
    if share_url in transcript_cache:
        return share_url, transcript_cache[share_url]
    try:
        req = urllib.request.Request(share_url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
            if m:
                next_data = json.loads(m.group(1))
                raw_str = json.dumps(next_data)
                paragraphs = re.findall(r'"text":"([^"]+)"', raw_str)
                if paragraphs:
                    full_text = " ".join([p for p in paragraphs if len(p) > 2 and not p.startswith('http')])
                    full_text = re.sub(r'\bLizza\b', 'Lyzr', full_text, flags=re.IGNORECASE)
                    full_text = re.sub(r'\bLizer\b', 'Lyzr', full_text, flags=re.IGNORECASE)
                    full_text = re.sub(r'\s+', ' ', full_text).strip()
                    transcript_cache[share_url] = full_text
                    return share_url, full_text
    except Exception as e:
        pass
    return share_url, None

csv_in_path = os.path.join(university_dir, "master_courses_content_with_transcripts.csv")
updated_rows = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    updated_rows.append(header)
    rows_list = list(reader)

# Collect unique Descript share URLs to fetch in parallel
unique_urls = set()
for r in rows_list:
    d_url = r[4]
    for old_url, new_url in link_replacements.items():
        if old_url in d_url:
            d_url = new_url
            break
    if d_url.startswith("https://share.descript.com/view/"):
        unique_urls.add(d_url)

print(f"Fetching Descript transcripts in parallel for {len(unique_urls)} unique share URLs...")

with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(fetch_single_url, unique_urls)
    for url, t_text in results:
        if t_text:
            transcript_cache[url] = t_text

print(f"✅ Fetched transcripts for {len(transcript_cache)} unique share URLs.")

# Rebuild rows with updated links and fetched transcripts
replaced_count = 0
for r in rows_list:
    c_name = r[0]
    ch_name = r[1]
    l_title = r[2]
    content_md = r[3]
    d_url = r[4]
    v_name = r[5]
    t_val = r[6] if len(r) > 6 else ""

    for old_url, new_url in link_replacements.items():
        if old_url in d_url:
            d_url = new_url
            r[4] = new_url
            replaced_count += 1
            break
    
    if d_url in transcript_cache and len(transcript_cache[d_url]) > 50:
        if len(r) > 6:
            r[6] = transcript_cache[d_url]
        else:
            r.append(transcript_cache[d_url])
    
    updated_rows.append(r)

print(f"✅ Replaced Descript web links for {replaced_count} rows.")

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

# Update Google Sheet tab 'Master Courses Content'
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
