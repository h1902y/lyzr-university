import os
import pathlib

p1 = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-upload/1 - Tracks/Studio")
p2 = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-upload/02 Lyzr for Business Teams")

print("==========================================================================")
print(" 📁 LISTING ALL SUBFOLDERS IN THINKIFIC UPLOAD STUDIO TRACK")
print("==========================================================================")

if p1.exists():
    print(f"Path 1: {p1}")
    for item in sorted(p1.iterdir()):
        print(f"  📂 {item.name}")

print("\n" + "-"*60 + "\n")

if p2.exists():
    print(f"Path 2: {p2}")
    for item in sorted(p2.iterdir()):
        print(f"  📂 {item.name}")

print("==========================================================================")
