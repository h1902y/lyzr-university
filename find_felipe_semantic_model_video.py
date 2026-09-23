import json
import csv
import pathlib
import os

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
upload_plan_path = university_dir / "revamp_upload_plan.json"

print("==========================================================================")
print(" 🔍 SEARCHING FOR FELIPE SEMANTIC DATA MODEL VIDEO")
print("==========================================================================")

with open(upload_plan_path, 'r', encoding='utf-8') as f:
    upload_plan = json.load(f)

matches = []

for item in upload_plan:
    idx = item["index"]
    course = item["course"]
    chapter = item["chapter"]
    lesson = item["lesson"]
    fname = item["filename"]
    
    # Check if lesson or chapter mentions semantic
    search_str = (lesson + " " + chapter + " " + item.get("description", "")).lower()
    if "semantic" in search_str or "data model" in search_str or "felipe" in search_str:
        matches.append(item)

print(f"Found {len(matches)} matching lesson objects:\n")
for m in matches:
    print(f" 🎬 [{m['index']:02d}] {m['course']} -> {m['chapter']}")
    print(f"    Title: {m['lesson']}")
    print(f"    Filename: {m['filename']}")
    print(f"    Video Path: {m['filepath']}")
    print("-" * 60)

print("==========================================================================")
