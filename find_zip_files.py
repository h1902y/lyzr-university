import os
import pathlib

root_dir = pathlib.Path("/Users/hkc/Documents/lyzr")

print("==========================================================================")
print(" 🔍 SEARCHING FOR THINKIFIC THEME ZIP FILES")
print("==========================================================================")

found = []
for p in root_dir.rglob("*.zip"):
    found.append(p)

print(f"Total .zip files found: {len(found)}\n")
for p in found:
    size_mb = p.stat().st_size / (1024 * 1024)
    print(f" 📦 ZIP Path: {p} ({size_mb:.2f} MB)")

print("==========================================================================")
