import os
import csv
import sys
import re

csv.field_size_limit(sys.maxsize)

university_dir = "/Users/hkc/Documents/lyzr/university"
revamp_dir = os.path.join(university_dir, "revamp")
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")
master_md_path = os.path.join(revamp_dir, "MASTER_CURRICULUM_MANIFEST.md")

print("==========================================================================")
print(" 📏 APPLYING STRICT HORIZONTAL SEPARATORS (1x LESSON, 2x CHAPTER, 3x COURSE)")
print("==========================================================================")

course_descriptions = {
    "Lyzr Foundations": "Master the fundamentals of the Lyzr Enterprise Agent Platform. Learn how autonomous agents, private RAG knowledge bases, deterministic guardrails, and MCP tool servers interact to deliver production-ready AI workflows across your organization.",
    "Lyzr for Business Professionals": "Design, govern, and deploy enterprise AI agents visually using Lyzr Agent Studio. Build complex multi-agent SuperFlow orchestrations, attach knowledge bases, and simulate agent behaviors without writing a single line of code.",
    "Lyzr for Technical Professionals": "Build production-grade autonomous agent microservices using the Lyzr ADK Python SDK. Implement multi-provider model switching, custom RAG pipelines, Pydantic structured outputs, and Model Context Protocol (MCP) server integrations."
}

rows_list = []
with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    rows_list = list(reader)

curriculum_tree = {}
for r in rows_list:
    c_name = r[0]
    ch_name = r[1]
    l_title = r[2]
    content = r[3]
    d_link = r[4]
    v_name = r[5]

    if c_name not in curriculum_tree:
        curriculum_tree[c_name] = {}
    if ch_name not in curriculum_tree[c_name]:
        curriculum_tree[c_name][ch_name] = []
    
    curriculum_tree[c_name][ch_name].append({
        "title": l_title,
        "content": content,
        "descript": d_link,
        "video_file": v_name,
        "video_path": f"university/revamp/{v_name}"
    })

lines = [
    "# 🎓 Lyzr University — Master Curriculum Manifest & Asset Index",
    "",
    "> [!NOTE]",
    "> **Official Production Index & Curriculum Dossier**  ",
    "> This document serves as the single source of truth for Lyzr University's 3 Target Master Courses. It maps every lesson to its standardized local video asset in `revamp/`, Descript share link, and Thinkific-ready lesson content.",
    "",
    "---",
    "",
    "## 📌 Quick Navigation & Table of Contents",
    ""
]

# Build TOC
for c_name, chapters in curriculum_tree.items():
    c_anchor = re.sub(r'[^a-z0-9]+', '-', c_name.lower()).strip('-')
    lines.append(f"- [**{c_name}**](#{c_anchor})")
    for ch_name in chapters.keys():
        ch_anchor = re.sub(r'[^a-z0-9]+', '-', ch_name.lower()).strip('-')
        lines.append(f"  - [{ch_name}](#{ch_anchor})")

lines.append("\n---\n---\n---\n")

course_index = 0
total_courses = len(curriculum_tree)

for c_name, chapters in curriculum_tree.items():
    course_index += 1
    c_anchor = re.sub(r'[^a-z0-9]+', '-', c_name.lower()).strip('-')
    course_desc = course_descriptions.get(c_name, "")
    
    lines.append(f"# <a id=\"{c_anchor}\"></a>🏛️ Course: {c_name}\n")
    lines.append(f"> [!TIP]")
    lines.append(f"> **Course Description:** {course_desc}\n")

    course_lesson_counter = 0
    chapter_index = 0
    total_chapters = len(chapters)

    for ch_name, lessons in chapters.items():
        chapter_index += 1
        ch_anchor = re.sub(r'[^a-z0-9]+', '-', ch_name.lower()).strip('-')
        lines.append(f"## <a id=\"{ch_anchor}\"></a>📂 {ch_name}\n")

        lesson_in_chap_count = 0
        total_lessons_in_chap = len(lessons)

        for l in lessons:
            course_lesson_counter += 1
            lesson_in_chap_count += 1
            l_num_str = f"{course_lesson_counter:02d}"
            
            lines.append("```yaml")
            lines.append(f"---")
            lines.append(f"course: \"{c_name}\"")
            lines.append(f"chapter: \"{ch_name}\"")
            lines.append(f"lesson_id: \"L{l_num_str}\"")
            lines.append(f"lesson_number: {course_lesson_counter}")
            lines.append(f"title: \"{l['title']}\"")
            lines.append(f"video_file_name: \"{l['video_file']}\"")
            lines.append(f"video_file_path: \"{l['video_path']}\"")
            lines.append(f"descript_link: \"{l['descript']}\"")
            lines.append(f"---")
            lines.append("```")
            lines.append("")
            
            # Clean header in content if present
            c_text = l['content']
            c_text = re.sub(rf"^# {re.escape(l['title'])}\s*\n+", "", c_text)

            lines.append(f"### 📖 Lesson {l_num_str}: {l['title']}")
            lines.append(f"> [!IMPORTANT]")
            lines.append(f"> **Video Asset:** [`{l['video_file']}`]({l['video_path']}) | **Descript Share URL:** [{l['descript']}]({l['descript']})\n")
            lines.append(c_text)

            # Check if this is the last lesson in chapter or last in course
            if lesson_in_chap_count < total_lessons_in_chap:
                # 1 horizontal separator between lessons
                lines.append("\n---\n")
        
        if chapter_index < total_chapters:
            # 2 horizontal separators between chapters
            lines.append("\n---\n\n---\n")

    if course_index < total_courses:
        # 3 horizontal separators between courses
        lines.append("\n---\n\n---\n\n---\n")

with open(master_md_path, 'w', encoding='utf-8') as mf:
    mf.write("\n".join(lines))

print(f"✅ Successfully applied strict horizontal separators (1x lesson, 2x chapter, 3x course)!")
print(f"   Manifest saved to: {master_md_path}")
