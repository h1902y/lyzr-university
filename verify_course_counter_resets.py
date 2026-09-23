import os

master_md_path = "/Users/hkc/Documents/lyzr/university/revamp/MASTER_CURRICULUM_MANIFEST.md"

with open(master_md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "Course: Lyzr for Business Professionals" in l or "Course: Lyzr for Technical Professionals" in l:
        print(f"Line {i+1}: {l.strip()}")
        for k in range(i, min(len(lines), i+30)):
            print(f"  {k+1}: {lines[k].strip()}")
        print("=" * 60)
