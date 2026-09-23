import os
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")

print("==========================================================================")
print(" 🔍 LISTING ALL MP4 FILES ACROSS UNIVERSITY DIRECTORY")
print("==========================================================================")

all_mp4s = []
for root, dirs, files in os.walk(university_dir):
    for f in files:
        if f.endswith('.mp4') and not root.endswith('revamp_branded'):
            full_path = os.path.join(root, f)
            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            rel = os.path.relpath(full_path, university_dir)
            all_mp4s.append((f, rel, size_mb, full_path))

all_mp4s.sort()
print(f"Total raw/unbranded MP4 files found: {len(all_mp4s)}\n")

for name, rel, size_mb, full in all_mp4s:
    print(f" 📹 {name:<45} | Size: {size_mb:6.2f} MB | Path: {rel}")

print("==========================================================================")
