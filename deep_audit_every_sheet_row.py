import os
import json
import re

brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
backup_path = os.path.join(brain_dir, "harshit_google_sheet_backup.json")
university_dir = "/Users/hkc/Documents/lyzr/university"

with open(backup_path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

# 1. Gather all local MP4 files
local_mp4s = {}
for root, dirs, files in os.walk(university_dir):
    for file in files:
        if file.endswith('.mp4'):
            fp = os.path.join(root, file)
            local_mp4s[file.lower()] = os.path.relpath(fp, university_dir)

# 2. Gather all Descript URLs across workspace files
descript_urls = {}
for root, dirs, files in os.walk(university_dir):
    for file in files:
        if file.endswith(('.md', '.csv', '.json', '.txt')):
            fp = os.path.join(root, file)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = re.finditer(r'(https://share\.descript\.com/view/[a-zA-Z0-9]+)', content)
                    for m in matches:
                        url = m.group(1)
                        if url not in descript_urls:
                            descript_urls[url] = os.path.relpath(fp, university_dir)
            except Exception as e:
                pass

print(f"Total Local MP4 Videos Found: {len(local_mp4s)}")
print(f"Total Unique Descript URLs Found: {len(descript_urls)}\n")

# Audit every row in Google Sheet
audit_results = []

for idx, r in enumerate(rows[1:], 2):
    phase = r[0] if len(r) > 0 else ""
    course = r[1] if len(r) > 1 else ""
    num = r[2] if len(r) > 2 else ""
    lesson = r[3] if len(r) > 3 else ""
    master_course = r[7] if len(r) > 7 else ""
    master_chapter = r[8] if len(r) > 8 else ""
    mp4_elem = r[9] if len(r) > 9 else ""
    descript_link = r[12] if len(r) > 12 else ""

    if not lesson.strip():
        continue

    # Check MP4 local presence
    mp4_status = "❌ Missing Local MP4"
    matched_mp4_path = ""
    if mp4_elem:
        clean_mp4 = mp4_elem.lower().strip()
        for f, rel in local_mp4s.items():
            if clean_mp4 in f or f in clean_mp4:
                mp4_status = "✅ Present on Disk"
                matched_mp4_path = rel
                break
    
    # Check Descript status
    desc_status = "✅ Descript Share Link Available" if descript_link else "⚠️ No Descript Link Recorded"

    audit_results.append({
        "row": idx,
        "phase": phase,
        "course": course,
        "num": num,
        "lesson": lesson,
        "master_course": master_course,
        "master_chapter": master_chapter,
        "mp4_elem": mp4_elem,
        "mp4_status": mp4_status,
        "mp4_path": matched_mp4_path,
        "descript_link": descript_link,
        "desc_status": desc_status
    })

print(f"Audited {len(audit_results)} lesson rows in Google Sheet.\n")

# Summary stats
with_descript = [a for a in audit_results if a['descript_link']]
with_mp4 = [a for a in audit_results if 'Present' in a['mp4_status']]

print(f"📊 Summary of {len(audit_results)} Lesson Rows:")
print(f"  • Rows with Active Descript Links: {len(with_descript)}")
print(f"  • Rows with Verified Local MP4 Files: {len(with_mp4)}")
print(f"  • Rows with NO Descript Link: {len(audit_results) - len(with_descript)}")

# Write comprehensive audit artifact
report_path = os.path.join(brain_dir, "exhaustive_sheet_114_rows_audit.md")
md_lines = [
    "# 🔍 Exhaustive 114-Row Sheet & Asset Coverage Audit Report",
    "",
    f"**Execution Timestamp:** {os.popen('date').read().strip()}  ",
    f"**Total Lesson Rows Audited:** {len(audit_results)}  ",
    f"**Rows with Active Descript Links:** {len(with_descript)}  ",
    f"**Rows with Verified Local MP4 Videos:** {len(with_mp4)}  ",
    "",
    "---",
    "",
    "## Complete Row-by-Row Asset Verification Table",
    "",
    "| Row # | Legacy Phase & Course | Lesson Title | Master Course Target | Local MP4 Video Asset Status | Descript Share Link Status | Descript Link |",
    "| :---: | :--- | :--- | :--- | :--- | :--- | :--- |"
]

for a in audit_results:
    desc_md = f"[{a['descript_link']}]({a['descript_link']})" if a['descript_link'] else "❌ Unrecorded"
    md_lines.append(f"| Row {a['row']} | **{a['phase']}**<br>({a['course']} #{a['num']}) | **{a['lesson']}** | `{a['master_course']}` | {a['mp4_status']}<br>`{a['mp4_path']}` | {a['desc_status']} | {desc_md} |")

with open(report_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md_lines))

print(f"\n📝 Saved exhaustive row audit report to: {report_path}")
