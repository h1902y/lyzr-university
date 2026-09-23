import os
import pathlib
import subprocess

p2 = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-upload/02 Lyzr for Business Teams")

print("==========================================================================")
print(" 🎬 LISTING ALL FILES IN C02 CHAPTER FOLDERS")
print("==========================================================================")

def get_dur(path):
    res = subprocess.run(["ffmpeg", "-i", str(path)], capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            return line.strip()
    return "Unknown"

for sub in sorted(p2.iterdir()):
    if sub.is_dir():
        print(f"\n📂 {sub.name}:")
        for f in sorted(sub.iterdir()):
            size_mb = f.stat().st_size / (1024 * 1024)
            dur = get_dur(f) if f.suffix == '.mp4' else ""
            print(f"   📄 {f.name:<60} | {size_mb:6.2f} MB | {dur}")

print("\n==========================================================================")
