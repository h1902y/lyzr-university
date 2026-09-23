import os
import pathlib

studio_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-upload/1 - Tracks/Studio")

print("==========================================================================")
print(" 🔍 INSPECTING ALL RAW MP4 FILES IN STUDIO TRACK")
print("==========================================================================")

for p in sorted(studio_dir.rglob("*.mp4")):
    rel = p.relative_to(studio_dir)
    size_mb = p.stat().st_size / (1024 * 1024)
    print(f" 🎬 {rel} ({size_mb:.2f} MB)")

print("==========================================================================")
