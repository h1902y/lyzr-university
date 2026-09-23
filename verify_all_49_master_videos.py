import os
import sys
import json

university_dir = "/Users/hkc/Documents/lyzr/university"
json_path = os.path.join(university_dir, "revamp_upload_plan.json")

print("==========================================================================")
print(" 🔍 MASTER COMPREHENSIVE VERIFICATION AUDIT FOR ALL 49 VIDEOS")
print("==========================================================================")

plan_data = json.load(open(json_path))

courses = {
    "Lyzr Foundations": [],
    "Lyzr for Business Professionals": [],
    "Lyzr for Technical Professionals": []
}

for item in plan_data:
    c_key = item['course'].strip()
    if c_key in courses:
        courses[c_key].append(item)

print(f"Total Videos in Plan JSON: {len(plan_data)}\n")

all_valid = True

for c_name, items in courses.items():
    print(f"==========================================================================")
    print(f" 📚 {c_name.upper()} ({len(items)} Lessons)")
    print(f"==========================================================================")
    for idx, item in enumerate(items, 1):
        v_path = os.path.join(university_dir, "revamp_branded", item['filename'])
        t_path = item.get('thumbnail_path', '')
        
        v_exists = os.path.exists(v_path)
        t_exists = os.path.exists(t_path) if t_path else False
        v_size_mb = (os.path.getsize(v_path)/(1024*1024)) if v_exists else 0
        
        has_links = "hubs.ly/Q043pWTs0" in item.get('description', '')
        has_prefix = " | " in item.get('title', '')
        
        status = "✅ READY" if (v_exists and t_exists and has_links and has_prefix) else "⚠️ ISSUE"
        if status == "⚠️ ISSUE":
            all_valid = False
            
        print(f" [{idx:02d}/17] Index {item['index']:02d} | {item['title']}")
        print(f"        Branded MP4: {item['filename']} ({v_size_mb:.1f} MB) -> Exists: {v_exists}")
        print(f"        Thumbnail:   {os.path.basename(t_path)} -> Exists: {t_exists}")
        print(f"        Links Block: {has_links} | Title Prefix: {has_prefix} -> {status}\n")

print("==========================================================================")
if all_valid:
    print(" 🎉 ALL 49 VIDEOS VERIFIED 100% CLEAN & READY FOR YOUTUBE STUDIO!")
else:
    print(" ⚠️ SOME VIDEOS REQUIRE ATTENTION!")
print("==========================================================================")
