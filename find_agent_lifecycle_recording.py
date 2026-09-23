import os
import pathlib
import subprocess

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")

print("==========================================================================")
print(" 🔍 SEARCHING FOR AGENT LIFECYCLE / BUILD CHOOSE TYPE RECORDING")
print("==========================================================================")

def get_dur(path):
    res = subprocess.run(["ffmpeg", "-i", str(path)], capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            return line.strip()
    return "Unknown"

for p in sorted(university_dir.rglob("*.mp4")):
    if "Lifecycle" in str(p) or "Lifecycle" in p.name or "06 Studio" in str(p) or "02a Build" in p.name:
        size_mb = p.stat().st_size / (1024 * 1024)
        print(f" 🎬 {p.relative_to(university_dir)} | Size: {size_mb:6.2f} MB | {get_dur(p)}")

print("==========================================================================")
