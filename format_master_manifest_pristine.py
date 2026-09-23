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
print(" 🎨 FORMATTING MASTER CURRICULUM MANIFEST TO HIGH-END AGENCY DESIGN")
print("==========================================================================")

# Read all rows from CSV
rows_list = []
with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    rows_list = list(reader)

# Group by Course > Chapter
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

lines.append("\n---\n")

lesson_counter = 0

# Build Detailed Content
for c_name, chapters in curriculum_tree.items():
    c_anchor = re.sub(r'[^a-z0-9]+', '-', c_name.lower()).strip('-')
    lines.append(f"# <a id=\"{c_anchor}\"></a>🏛️ Course: {c_name}\n")
    lines.append(f"> [!TIP]")
    lines.append(f"> **Master Course Overview:** Comprehensive curriculum for `{c_name}`. Contains verified video assets and lesson notes.\n")

    for ch_name, lessons in chapters.items():
        ch_anchor = re.sub(r'[^a-z0-9]+', '-', ch_name.lower()).strip('-')
        lines.append(f"## <a id=\"{ch_anchor}\"></a>📂 {ch_name}\n")

        for l in lessons:
            lesson_counter += 1
            l_num_str = f"{lesson_counter:02d}"
            
            lines.append("```yaml")
            lines.append(f"---")
            lines.append(f"course: \"{c_name}\"")
            lines.append(f"chapter: \"{ch_name}\"")
            lines.append(f"lesson_id: \"L{l_num_str}\"")
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
            lines.append("\n---\n")

with open(master_md_path, 'w', encoding='utf-8') as mf:
    mf.write("\n".join(lines))

print(f"✅ Pristine formatting applied! Master Curriculum Manifest ({lesson_counter} lessons) saved to:")
print(f"   {master_md_path}")
