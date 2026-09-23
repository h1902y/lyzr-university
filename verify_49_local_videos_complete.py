import os
import csv

university_dir = "/Users/hkc/Documents/lyzr/university"
revamp_dir = os.path.join(university_dir, "revamp")
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")

print("==========================================================================")
print(" 🎬 FINAL AUDIT: VERIFYING 100% LOCAL MP4 VIDEO FILES IN REVAMP")
print("==========================================================================")

missing = []
found = []

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    for r in reader:
        v_name = r[5]
        v_path = os.path.join(revamp_dir, v_name)
        if os.path.exists(v_path):
            found.append((v_name, os.path.getsize(v_path)))
        else:
            missing.append(v_name)

print(f" ✅ Total Found Local Video Files: {len(found)} / 49")
print(f" ❌ Total Missing Video Files:     {len(missing)}")

if not missing:
    total_size_gb = sum(s for _, s in found) / (1024 * 1024 * 1024)
    print(f"\n🎉 100% OF ALL 49 MASTER VIDEO MP4 FILES ARE PRESENT IN REVAMP!")
    print(f" 📦 Total Video Storage Size: {total_size_gb:.2f} GB")
