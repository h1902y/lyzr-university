import os
import pathlib
import subprocess

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")

print("==========================================================================")
print(" 🔍 SEARCHING FOR ALL MP4 FILES AND THEIR EXACT DURATIONS")
print("==========================================================================")

def get_dur(path):
    res = subprocess.run(["ffmpeg", "-i", str(path)], capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            return line.strip()
    return "Unknown"

for p in sorted(university_dir.rglob("*.mp4")):
    if "scratch" not in str(p) and "revamp_branded" not in str(p):
        rel = p.relative_to(university_dir)
        size_mb = p.stat().st_size / (1024 * 1024)
        dur = get_dur(p)
        print(f" 🎬 {rel} | Size: {size_mb:6.2f} MB | {dur}")

print("==========================================================================")
