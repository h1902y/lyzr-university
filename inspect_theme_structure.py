import os
import pathlib

theme_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-theme")

print("==========================================================================")
print(" 🔍 INSPECTING THINKIFIC THEME STRUCTURE")
print("==========================================================================")

for p in sorted(theme_dir.rglob("*")):
    if p.is_file():
        rel = p.relative_to(theme_dir)
        print(f"  📄 {rel}")

print("==========================================================================")
