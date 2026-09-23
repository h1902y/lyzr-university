import os
import pathlib

root_dir = pathlib.Path("/Users/hkc/Documents/lyzr")

print("==========================================================================")
print(" 🔍 FINDING ALL FILES MATCHING '02a' OR 'Build Choose'")
print("==========================================================================")

for p in root_dir.rglob("*.mp4"):
    name = p.name.lower()
    if "02a" in name or "choose" in name or "agent" in name:
        rel = p.relative_to(root_dir)
        size_mb = p.stat().st_size / (1024 * 1024)
        print(f" 🎬 {rel} ({size_mb:.2f} MB)")

print("==========================================================================")
