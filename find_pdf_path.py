import os
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")

print("==========================================================================")
print(" 🔍 SEARCHING FOR 'WHAT AGENT TYPE SHOULD I BUILD' PDF LOCATIONS")
print("==========================================================================")

found = []
for p in university_dir.rglob("*.pdf"):
    name_lower = p.name.lower()
    if "agent_type" in name_lower or "what_agent" in name_lower or "c02_ch01_l04" in name_lower or "build" in name_lower or "studio" in name_lower:
        found.append(p)

if not found:
    # search all pdfs
    for p in university_dir.rglob("*.pdf"):
        found.append(p)

print(f"Total PDFs found: {len(found)}\n")
for p in found:
    size_kb = p.stat().st_size / 1024
    print(f" 📁 PDF Path: {p} ({size_kb:.1f} KB)")

print("==========================================================================")
