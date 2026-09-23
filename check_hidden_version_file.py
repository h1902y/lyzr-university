import os
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")

print("==========================================================================")
print(" 🔍 SEARCHING FOR .version FILES IN THEME DIRECTORIES")
print("==========================================================================")

for p in university_dir.rglob("*"):
    if p.name == ".version":
        print(f" 📄 Found .version file: {p}")
        try:
            content = open(p, 'r', encoding='utf-8').read()
            print(f"    Content: '{content.strip()}'")
        except Exception as e:
            print(f"    Error reading: {e}")

print("==========================================================================")
