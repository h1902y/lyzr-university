import os
import csv
import sys

csv.field_size_limit(sys.maxsize)

university_dir = "/Users/hkc/Documents/lyzr/university"
revamp_dir = os.path.join(university_dir, "revamp")
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")
master_md_path = os.path.join(revamp_dir, "MASTER_CURRICULUM_MANIFEST.md")

os.makedirs(revamp_dir, exist_ok=True)

print("==========================================================================")
print(" 📝 GENERATING MASTER CURRICULUM MARKDOWN FILE IN REVAMP DIRECTORY")
print("==========================================================================")

md_output_lines = [
    "# 🎓 Lyzr University — Master Courses Curriculum Manifest",
    "",
    "> [!NOTE]",
    "> **Unified Master Curriculum Dossier**  ",
    "> This document contains the complete hierarchical structure (Course > Chapter > Lesson) with YAML frontmatter metadata, video file paths, Descript share links, and full lesson content across all 49 master lessons.",
    "",
    "---",
    ""
]

current_course = None
current_chapter = None

lesson_count = 0

with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    
    for row in reader:
        c_name = row[0]
        ch_name = row[1]
        l_title = row[2]
        content_md = row[3]
        descript_url = row[4]
        video_filename = row[5]

        # Check Course Header
        if c_name != current_course:
            current_course = c_name
            current_chapter = None
            md_output_lines.append(f"\n# 🏛️ Course: {current_course}\n")

        # Check Chapter Header
        if ch_name != current_chapter:
            current_chapter = ch_name
            md_output_lines.append(f"\n## 📂 {current_chapter}\n")

        lesson_count += 1
        video_path = f"university/revamp/{video_filename}"

        # Frontmatter and Lesson Section
        md_output_lines.append("---")
        md_output_lines.append(f"course: \"{c_name}\"")
        md_output_lines.append(f"chapter: \"{ch_name}\"")
        md_output_lines.append(f"lesson_number: {lesson_count:02d}")
        md_output_lines.append(f"title: \"{l_title}\"")
        md_output_lines.append(f"video_file_name: \"{video_filename}\"")
        md_output_lines.append(f"video_file_path: \"{video_path}\"")
        md_output_lines.append(f"descript_link: \"{descript_url}\"")
        md_output_lines.append("---")
        md_output_lines.append("")
        md_output_lines.append(content_md)
        md_output_lines.append("\n\n")

with open(master_md_path, 'w', encoding='utf-8') as mf:
    mf.write("\n".join(md_output_lines))

print(f"✅ Successfully compiled Master Curriculum Dossier ({lesson_count} lessons) to:")
print(f"   {master_md_path}")
