import urllib.request
import urllib.parse
import json
import os
import csv
import sys

csv.field_size_limit(sys.maxsize)

token_file = "/Users/hkc/.gemini/antigravity-ide/google_token.json"
sheet_id = "1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk"
university_dir = "/Users/hkc/Documents/lyzr/university"

print("==========================================================================")
print(" 🔍 AUDITING SCRAPED TRANSCRIPTS ACROSS ALL 49 LESSON ROWS IN GOOGLE SHEET")
print("==========================================================================")

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

read_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/'{encoded_tab_name}'!A1:G100"
read_req = urllib.request.Request(read_url, headers={
    "Authorization": f"Bearer {access_token}"
})

with urllib.request.urlopen(read_req) as rresp:
    res_data = json.loads(rresp.read().decode('utf-8'))
    sheet_values = res_data.get("values", [])

print(f"Total Rows in Sheet Tab '{tab_name}': {len(sheet_values)-1}\n")

course_counts = {}
transcript_lengths = []

for idx, r in enumerate(sheet_values[1:], 1):
    c_name = r[0] if len(r) > 0 else ""
    l_title = r[2] if len(r) > 2 else ""
    t_val = r[6] if len(r) > 6 else ""
    
    course_counts[c_name] = course_counts.get(c_name, 0) + 1
    transcript_lengths.append((c_name, l_title, len(t_val)))

print("📊 Lesson Count by Course:")
for c, cnt in course_counts.items():
    print(f" • {c}: {cnt} lessons")

print(f"\n📊 Transcript Length Audit (Total {len(transcript_lengths)} rows):")
empty_transcripts = [t for t in transcript_lengths if t[2] == 0]
valid_transcripts = [t for t in transcript_lengths if t[2] > 0]

print(f" ✅ Rows with Scraped Transcripts: {len(valid_transcripts)} / {len(transcript_lengths)}")
print(f" ❌ Empty Transcript Rows:          {len(empty_transcripts)}")
if valid_transcripts:
    avg_len = sum(t[2] for t in valid_transcripts) // len(valid_transcripts)
    print(f" 📏 Average Transcript Character Length: {avg_len:,} chars per cell")
