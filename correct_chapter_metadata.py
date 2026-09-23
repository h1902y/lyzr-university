import os
import sys
import json
import re

university_dir = "/Users/hkc/Documents/lyzr/university"
manifest_md_path = os.path.join(university_dir, "revamp", "MASTER_CURRICULUM_MANIFEST.md")
plan_json_path = os.path.join(university_dir, "revamp_upload_plan.json")
guide_md_path = os.path.join(university_dir, "THINKIFIC_MANUAL_UPLOAD_GUIDE.md")

print("==========================================================================")
print(" 🛠️ CORRECTING CHAPTER 04 METADATA TO 'Tools & MCP'")
print("==========================================================================")

# 1. Update revamp_upload_plan.json
plan_data = json.load(open(plan_json_path))

for item in plan_data:
    if item['filename'] == "C03_CH04_L03_gitagent_harness.mp4":
        item['chapter'] = "Chapter 04: Tools & MCP"
        item['title'] = "Technical C4 L3 | GitAgent Harness: Repo as Source of Truth"

with open(plan_json_path, 'w', encoding='utf-8') as f:
    json.dump(plan_data, f, indent=2)

print("  ✓ Updated revamp_upload_plan.json with correct Chapter 04: Tools & MCP")

# 2. Update MASTER_CURRICULUM_MANIFEST.md
manifest_text = open(manifest_md_path, 'r', encoding='utf-8').read()
manifest_text = manifest_text.replace(
    'chapter: "Chapter 04: Lyzr ADK & Open Source"',
    'chapter: "Chapter 04: Tools & MCP"'
).replace(
    'Chapter 04: Lyzr ADK & Open Source',
    'Chapter 04: Tools & MCP'
)

with open(manifest_md_path, 'w', encoding='utf-8') as f:
    f.write(manifest_text)

print("  ✓ Updated MASTER_CURRICULUM_MANIFEST.md with correct Chapter 04: Tools & MCP")

# 3. Update THINKIFIC_MANUAL_UPLOAD_GUIDE.md
guide_text = open(guide_md_path, 'r', encoding='utf-8').read()
guide_text = guide_text.replace(
    'Lyzr ADK & Open Source',
    'Tools & MCP'
)

with open(guide_text_path if 'guide_text_path' in locals() else guide_md_path, 'w', encoding='utf-8') as f:
    f.write(guide_text)

print("  ✓ Updated THINKIFIC_MANUAL_UPLOAD_GUIDE.md with correct Chapter 04: Tools & MCP")

print("\n==========================================================================")
print(" 🎉 ALL MANIFESTS & GUIDES CORRECTED WITH EXACT THINKIFIC CHAPTER NAMES!")
print("==========================================================================")
