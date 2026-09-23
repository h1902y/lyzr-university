import os
import sys
import json

university_dir = "/Users/hkc/Documents/lyzr/university"
json_path = os.path.join(university_dir, "revamp_upload_plan.json")

print("==========================================================================")
print(" 🔍 VERIFYING LYZR FOR BUSINESS PROFESSIONALS LESSON COUNT")
print("==========================================================================")

plan_data = json.load(open(json_path))

biz_items = [item for item in plan_data if item['course'].strip() == "Lyzr for Business Professionals"]

print(f"Total Business Course Lessons in Master Plan: {len(biz_items)}\n")

for idx, item in enumerate(biz_items, 1):
    b_path = os.path.join(university_dir, "revamp_branded", item['filename'])
    exists = os.path.exists(b_path)
    size_mb = (os.path.getsize(b_path)/(1024*1024)) if exists else 0
    print(f"  {idx:02d}. [Index {item['index']:02d}] {item['title']} | File: {item['filename']} ({size_mb:.1f} MB, Exists: {exists})")
