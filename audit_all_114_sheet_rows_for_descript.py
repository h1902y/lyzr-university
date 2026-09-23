import json
import os
import re

brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
backup_path = os.path.join(brain_dir, "harshit_google_sheet_backup.json")
university_dir = "/Users/hkc/Documents/lyzr/university"

with open(backup_path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

# Find ALL Descript links in workspace with context
all_descript_sources = []

for root, dirs, files in os.walk(university_dir):
    for file in files:
        if file.endswith(('.md', '.csv', '.json', '.txt')):
            fp = os.path.join(root, file)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = re.findall(r'(?:[^\n]{0,60})(https://share\.descript\.com/view/[a-zA-Z0-9]+)(?:[^\n]{0,60})', content)
                    for m in re.finditer(r'https://share\.descript\.com/view/[a-zA-Z0-9]+', content):
                        url = m.group(0)
                        start = max(0, m.start() - 60)
                        end = min(len(content), m.end() + 60)
                        snippet = content[start:end].replace('\n', ' ')
                        all_descript_sources.append({"url": url, "snippet": snippet, "file": file})
            except Exception as e:
                pass

print(f"Total Descript Link References Found in Workspace Files: {len(all_descript_sources)}\n")

# Check rows in Google Sheet
non_empty_lesson_rows = []
for idx, r in enumerate(rows[1:], 1):
    phase = r[0] if len(r) > 0 else ""
    course = r[1] if len(r) > 1 else ""
    num = r[2] if len(r) > 2 else ""
    lesson = r[3] if len(r) > 3 else ""
    if lesson.strip():
        non_empty_lesson_rows.append((idx + 1, phase, course, num, lesson))

print(f"Total Non-Empty Lesson Rows in Harshit's Sheet: {len(non_empty_lesson_rows)} (out of {len(rows)-1} data rows)\n")
for r in non_empty_lesson_rows[:35]:
    print(f"Row {r[0]}: [{r[1]}] '{r[2]}' #{r[3]} — '{r[4]}'")
