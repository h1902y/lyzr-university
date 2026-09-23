import os
import sys
import json
import sqlite3
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
root_dir = pathlib.Path("/Users/hkc/Documents/lyzr")

print("==========================================================================")
print(" 🔄 EXECUTING MASTER COURSE RENAMING ACROSS ALL FILES & MANIFESTS")
print("==========================================================================")

# Old vs New Name Mappings
course_map = {
    "Lyzr for Business Professionals": "Lyzr Platform Studio",
    "Lyzr for Technical Professionals": "Lyzr Code Libraries",
    "Business C": "Studio C",
    "Technical C": "Code C"
}

# 1. Update revamp_upload_plan.json
plan_json = university_dir / "revamp_upload_plan.json"
if plan_json.exists():
    data = json.load(open(plan_json))
    for item in data:
        c = item['course'].strip()
        if c in course_map:
            item['course'] = course_map[c]
        if "Lyzr for Business Professionals" in item.get('playlist', ''):
            item['playlist'] = "Lyzr Platform Studio — Master Course"
        elif "Lyzr for Technical Professionals" in item.get('playlist', ''):
            item['playlist'] = "Lyzr Code Libraries — Master Course"
        
        t = item.get('title', '')
        if t.startswith("Business C"):
            item['title'] = t.replace("Business C", "Studio C")
        elif t.startswith("Technical C"):
            item['title'] = t.replace("Technical C", "Code C")

    with open(plan_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"  ✓ Updated {plan_json.name}")

# 2. Update MASTER_CURRICULUM_MANIFEST.md
manifest_md = university_dir / "revamp" / "MASTER_CURRICULUM_MANIFEST.md"
if manifest_md.exists():
    text = open(manifest_md, 'r', encoding='utf-8').read()
    text = text.replace("Lyzr for Business Professionals", "Lyzr Platform Studio")
    text = text.replace("Lyzr for Technical Professionals", "Lyzr Code Libraries")
    with open(manifest_md, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"  ✓ Updated {manifest_md.name}")

# 3. Update master_courses_content_markdown_reverted.csv
csv_path = university_dir / "master_courses_content_markdown_reverted.csv"
if csv_path.exists():
    text = open(csv_path, 'r', encoding='utf-8').read()
    text = text.replace("Lyzr for Business Professionals", "Lyzr Platform Studio")
    text = text.replace("Lyzr for Technical Professionals", "Lyzr Code Libraries")
    with open(csv_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"  ✓ Updated {csv_path.name}")

# 4. Update SQLite personal-desk.db
db_path = root_dir / "personal-desk.db"
if db_path.exists():
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("UPDATE partners SET notes = REPLACE(notes, 'Lyzr for Business Professionals', 'Lyzr Platform Studio') WHERE notes LIKE '%Lyzr for Business Professionals%'")
        cur.execute("UPDATE partners SET notes = REPLACE(notes, 'Lyzr for Technical Professionals', 'Lyzr Code Libraries') WHERE notes LIKE '%Lyzr for Technical Professionals%'")
        conn.commit()
        conn.close()
        print(f"  ✓ Updated SQLite DB: {db_path.name}")
    except Exception as e:
        print(f"  ⚠️ SQLite DB note: {e}")

# 5. Update Liquid Theme files
theme_dir = university_dir / "thinkific-theme"
for l_file in theme_dir.rglob("*.liquid"):
    t = open(l_file, 'r', encoding='utf-8').read()
    t_mod = t.replace("Lyzr for Business Professionals", "Lyzr Platform Studio")
    t_mod = t_mod.replace("Lyzr for Technical Professionals", "Lyzr Code Libraries")
    t_mod = t_mod.replace("Lyzr Business", "Lyzr Platform Studio")
    t_mod = t_mod.replace("Lyzr ADK", "Lyzr Code Libraries")
    if t != t_mod:
        with open(l_file, 'w', encoding='utf-8') as f:
            f.write(t_mod)
        print(f"  ✓ Updated Liquid Theme file: {l_file.name}")

# 6. Update AGENTS.md
agents_md = root_dir / "AGENTS.md"
if agents_md.exists():
    t = open(agents_md, 'r', encoding='utf-8').read()
    t = t.replace("`Lyzr for Business Professionals`", "`Lyzr Platform Studio`")
    t = t.replace("`Lyzr for Technical Professionals`", "`Lyzr Code Libraries`")
    with open(agents_md, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"  ✓ Updated AGENTS.md")

print("\n==========================================================================")
print(" 🎉 MASTER RENAMING EXECUTED SUCCESSFULLY ACROSS ALL MANIFESTS & THEMES!")
print("==========================================================================")
