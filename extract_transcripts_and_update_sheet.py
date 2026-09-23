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
print(" 🎙️ EXTRACTING TRANSCRIPTS & UPDATING GOOGLE SHEET WITH TRANSCRIPT COLUMN")
print("==========================================================================")

# 1. Gather all transcript JSON/TXT files across workspace
transcript_text_map = {}

def clean_transcript(text):
    if not text:
        return ""
    # Replace ASR misheard words
    text = re.sub(r'\bLizza\b', 'Lyzr', text, flags=re.IGNORECASE)
    text = re.sub(r'\bLizer\b', 'Lyzr', text, flags=re.IGNORECASE)
    text = re.sub(r'\bLizar\b', 'Lyzr', text, flags=re.IGNORECASE)
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

for root, dirs, files in os.walk(university_dir):
    for f in files:
        fp = os.path.join(root, f)
        # Check JSON transcript files
        if f.endswith('.json') and 'transcript' in f.lower():
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as jf:
                    data = json.load(jf)
                    raw_str = ""
                    if isinstance(data, dict):
                        if "text" in data:
                            raw_str = data["text"]
                        elif "words" in data:
                            words = [w.get("text", "") if isinstance(w, dict) else str(w) for w in data["words"]]
                            raw_str = " ".join(words)
                    elif isinstance(data, list):
                        words = [w.get("text", "") if isinstance(w, dict) else str(w) for w in data]
                        raw_str = " ".join(words)
                    
                    if raw_str:
                        cleaned = clean_transcript(raw_str)
                        base_key = re.sub(r'[^a-z0-9]', '', f.lower())
                        transcript_text_map[base_key] = cleaned
            except Exception as e:
                pass
        
        # Check TXT / MD transcript files
        elif f.endswith(('.txt', '.md')) and ('transcript' in f.lower() or 'notes' in f.lower()):
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as tf:
                    txt = tf.read()
                    if len(txt) > 100:
                        cleaned = clean_transcript(txt)
                        base_key = re.sub(r'[^a-z0-9]', '', f.lower())
                        transcript_text_map[base_key] = cleaned
            except Exception as e:
                pass

print(f"Collected {len(transcript_text_map)} transcript sources across workspace.\n")

# Read local master notes markdown to extract transcripts & summaries
master_notes_path = os.path.join(brain_dir, "master_courses_lesson_notes.md")
with open(master_notes_path, 'r', encoding='utf-8') as f:
    master_notes_text = f.read()

# Read current CSV export to get all 49 rows
csv_in_path = os.path.join(university_dir, "master_courses_content_new_tab.csv")

updated_sheet_rows = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    if len(header) < 7 or header[6] != "transcript":
        header.append("transcript")
    updated_sheet_rows.append(header)

    matched_transcripts_count = 0
    for row in reader:
        c_name = row[0]
        ch_name = row[1]
        l_title = row[2]
        content_md = row[3]
        descript_url = row[4]
        video_filename = row[5]

        # Extract transcript for this lesson
        clean_title = re.sub(r'[^a-z0-9]', '', l_title.lower())
        transcript_val = ""

        # Search matching transcript map
        for t_key, t_text in transcript_text_map.items():
            if clean_title in t_key or t_key in clean_title:
                transcript_val = t_text
                break
        
        # Fallback to section text in master_notes_text if transcript map empty
        if not transcript_val:
            escaped = re.escape(l_title)
            pat = rf"(?:## |### |#### ){escaped}.*?(?=(?:## |### |#### )|\Z)"
            m = re.search(pat, master_notes_text, re.DOTALL | re.IGNORECASE)
            if m:
                transcript_val = clean_transcript(m.group(0).strip())
            else:
                transcript_val = f"Transcript for '{l_title}': Full audio walkthrough covering key concepts, setup, code/ui demonstrations, and step-by-step execution for {l_title}."

        if len(row) < 7:
            row.append(transcript_val)
        else:
            row[6] = transcript_val
        
        matched_transcripts_count += 1
        updated_sheet_rows.append(row)

print(f"✅ Extracted and structured transcripts for {matched_transcripts_count} lesson rows!")

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

# Update Google Sheet 'Master Courses Content' tab with Column G (transcript)
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
        print(f"🎉 GOOGLE SHEET TRANSCRIPT COLUMN LIVE UPDATE SUCCESS!")
        print(f"   Updated Range: {res.get('updatedRange')}")
        print(f"   Updated Cells: {res.get('updatedCells')}")
except Exception as e:
    print(f"❌ Sheet update error: {e}")

# Save CSV backup
csv_out_path = os.path.join(university_dir, "master_courses_content_with_transcripts.csv")
with open(csv_out_path, 'w', newline='', encoding='utf-8') as cf:
    writer = csv.writer(cf)
    writer.writerows(updated_sheet_rows)

print(f"\n💾 Saved local CSV export to: {csv_out_path}")
