import csv
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
csv_path = university_dir / "master_courses_content_markdown_reverted.csv"
artifact_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/THINKIFIC_TEXT_BLOCKS_UPDATE_GUIDE.md")

print("==========================================================================")
print(" 📝 GENERATING THINKIFIC TEXT BLOCK COPY-PASTE GUIDE")
print("==========================================================================")

md = []
md.append("# 📝 Thinkific Text Block Copy-Paste Guide (51/51 Unique Lessons)\n")
md.append("This document contains the exact plain-text / markdown content to paste into the **Text Block** below each video lesson in Thinkific.\n")

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    current_course = None
    current_chapter = None
    
    for i, row in enumerate(reader, 1):
        if len(row) < 6:
            continue
        course, chapter, lesson, fname, dlink, content = row[0], row[1], row[2], row[3], row[4], row[5]
        
        if course != current_course:
            current_course = course
            md.append(f"\n# 🏛️ Course: {current_course}\n")
            
        if chapter != current_chapter:
            current_chapter = chapter
            md.append(f"\n## 📂 {current_chapter}\n")
            
        md.append(f"### 📖 Lesson {i:02d}: {lesson}")
        md.append(f"**Target Filename:** `{fname}`\n")
        md.append("```markdown")
        md.append(content)
        md.append("```\n")
        md.append("---\n")

with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print(f"  ✓ Generated {artifact_path}")
print("==========================================================================")
