import os

files_to_update = [
    "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/master_courses_lesson_notes.md",
    "/Users/hkc/Documents/lyzr/university/THINKIFIC_API_CAPABILITIES.md",
    "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/THINKIFIC_API_CAPABILITIES.md",
    "/Users/hkc/Documents/lyzr/AGENTS.md"
]

replacements = [
    ("Lyzr for Developers", "Lyzr for Technical Professionals"),
    ("Lyzr Studio Architect & Builder Course", "Lyzr for Business Professionals")
]

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = content
        for old_str, new_str in replacements:
            updated = updated.replace(old_str, new_str)
        
        if updated != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"✅ Updated nomenclature in: {file_path}")
        else:
            print(f"ℹ️ No changes needed in: {file_path}")
