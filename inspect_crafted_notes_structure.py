import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
notes_files = list(university_dir.rglob("*.md"))

print("==========================================================================")
print(" 🔍 INSPECTING CRAFTED LESSON NOTES STRUCTURE")
print("==========================================================================")

for p in notes_files:
    if "notes" in str(p) and "scratch" not in str(p) and "system" not in str(p):
        print(f"\n📄 {p.relative_to(university_dir)}:")
        text = open(p, 'r', encoding='utf-8').read().strip()
        print(text[:400])
        print("-" * 50)
        break

print("==========================================================================")
