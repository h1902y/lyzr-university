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
print(" 🔍 CURRENT DESCRIPT SHARE LINKS SUMMARY ACROSS ALL 49 LESSON ROWS")
print("==========================================================================")

descript_summary = {}

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    for row in reader:
        c_name = row[0]
        l_title = row[2]
        d_url = row[4]
        
        if d_url not in descript_summary:
            descript_summary[d_url] = []
        descript_summary[d_url].append(f"[{c_name}] {l_title}")

print(f"Total Unique Descript Share URLs in Sheet: {len(descript_summary)}\n")
for url, lessons in descript_summary.items():
    print(f"🔗 {url} ({len(lessons)} lessons):")
    for l in lessons[:3]:
        print(f"   • {l}")
    if len(lessons) > 3:
        print(f"   ... and {len(lessons)-3} more lessons")
    print()
