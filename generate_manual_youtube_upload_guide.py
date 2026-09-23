import os
import csv
import sys
import re

csv.field_size_limit(sys.maxsize)

university_dir = "/Users/hkc/Documents/lyzr/university"
revamp_dir = os.path.join(university_dir, "revamp")
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")
guide_md_path = os.path.join(revamp_dir, "MANUAL_YOUTUBE_UPLOAD_GUIDE.md")

print("==========================================================================")
print(" 📝 GENERATING MANUAL YOUTUBE UPLOAD GUIDE IN REVAMP DIRECTORY")
print("==========================================================================")

def clean_name_no_numbers(text):
    if not text:
        return ""
    text = re.sub(r'^\s*Chapter\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*Lesson\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*C\d+_CH\d+_L\d+\s*', '', text)
    return text.strip()

PLAYLIST_MAP = {
    "Lyzr Foundations": ("PLNhUOcQ57yRU", "https://www.youtube.com/playlist?list=PLNhUOcQ57yRU"),
    "Lyzr for Business Professionals": ("PLJs-yamjL6bw", "https://www.youtube.com/playlist?list=PLJs-yamjL6bw"),
    "Lyzr for Technical Professionals": ("PLad3Pu7_rlUI", "https://www.youtube.com/playlist?list=PLad3Pu7_rlUI")
}

rows_list = []
with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    rows_list = list(reader)

lines = [
    "# 📺 Lyzr University — Manual YouTube Upload Guide & Metadata Cheat Sheet",
    "",
    "> [!NOTE]",
    "> **Step-by-Step Manual Upload Instructions**  ",
    "> This guide provides exact instructions, direct video asset paths in `revamp/`, and copy-pastable titles/descriptions for manually uploading the Master Course videos into YouTube Studio.",
    "",
    "---",
    "",
    "## 📌 Target Master Playlists Directory",
    "",
    "| Master Course | Target Playlist Name | Playlist ID | Live YouTube Link |",
    "| :--- | :--- | :---: | :--- |",
    "| 🏛️ **Lyzr Foundations** | `Lyzr Foundations — Master Course` | `PLNhUOcQ57yRU` | [View Playlist](https://www.youtube.com/playlist?list=PLNhUOcQ57yRU) |",
    "| 📊 **Lyzr for Business Professionals** | `Lyzr for Business Professionals — Master Course` | `PLJs-yamjL6bw` | [View Playlist](https://www.youtube.com/playlist?list=PLJs-yamjL6bw) |",
    "| 💻 **Lyzr for Technical Professionals** | `Lyzr for Technical Professionals — Master Course` | `PLad3Pu7_rlUI` | [View Playlist](https://www.youtube.com/playlist?list=PLad3Pu7_rlUI) |",
    "",
    "---",
    "",
    "## 🛠️ Step-by-Step Upload Instructions (YouTube Studio)",
    "",
    "1. **Open YouTube Studio:**  ",
    "   Navigate to [YouTube Studio Dashboard](https://studio.youtube.com/channel/UC2Wfn7eE6M8NyPOMKTCTpoA) or click **+ CREATE** $\rightarrow$ **Upload videos**.",
    "",
    "2. **Select Video File:**  ",
    "   Drag and drop the MP4 file from `/Users/hkc/Documents/lyzr/university/revamp/`.",
    "",
    "3. **Copy-Paste Title & Description:**  ",
    "   - Copy the clean **User-Facing Title** (e.g. `Introduction to Lyzr Platform — Lyzr Foundations`).",
    "   - Copy the pre-formatted **User-Facing Description**.",
    "",
    "4. **Select Playlist & Visibility:**  ",
    "   - Under **Playlists**, check the matching Master Course Playlist (`Lyzr Foundations`, `Lyzr for Business Professionals`, or `Lyzr for Technical Professionals`).",
    "   - Under **Visibility**, select **Unlisted** (or **Public**).",
    "",
    "5. **Save & Publish:**  ",
    "   Click **Save**.",
    "",
    "---",
    "",
    "## 📋 Lesson-by-Lesson Copy-Paste Cheat Sheet",
    ""
]

current_course = None

for idx, r in enumerate(rows_list, 1):
    c_name = r[0]
    ch_name = r[1]
    l_title = r[2]
    content_md = r[3]
    v_name = r[5]

    clean_course = c_name.strip()
    clean_chapter = clean_name_no_numbers(ch_name)
    clean_title = clean_name_no_numbers(l_title)

    pid, p_link = PLAYLIST_MAP.get(clean_course, ("", ""))

    if clean_course != current_course:
        current_course = clean_course
        lines.append(f"\n### 🏛️ Course: {current_course}\n")
        lines.append(f"> **Target Playlist:** [{current_course} — Master Course]({p_link})\n")

    user_title = f"{clean_title} — {clean_course}"
    if len(user_title) > 95:
        user_title = user_title[:95]

    # Extract Objectives / Overview bullets from content markdown
    clean_notes = re.sub(r'#+\s*', '', content_md)
    clean_notes = re.sub(r'\*\*(.*?)\*\*', r'\1', clean_notes)
    bullet_lines = [bl.strip() for bl in clean_notes.split('\n') if bl.strip()]
    
    summary_bullets = []
    for bl in bullet_lines[:8]:
        if bl.startswith('-') or bl.startswith('•') or bl.startswith('1.') or bl.startswith('2.'):
            bl_clean = re.sub(r'^\d+\.\s*', '', bl)
            summary_bullets.append(f"  • {bl_clean.lstrip('-• ')}")

    bullets_text = "\n".join(summary_bullets) if summary_bullets else "  • Comprehensive technical & operational walkthrough."

    user_desc = f"""Course: {clean_course}
Chapter: {clean_chapter}
Lesson: {clean_title}

============================================================
📚 LESSON OVERVIEW & OBJECTIVES
============================================================
{bullets_text}

============================================================
🔗 USEFUL LYZR RESOURCES & LINKS
============================================================
🌐 Lyzr Enterprise Agent Platform: https://lyzr.ai
📖 Official Lyzr Documentation:  https://docs.lyzr.ai
💻 Lyzr ADK Python SDK (GitHub): https://github.com/LyzrCore/lyzr-core
🚀 Lyzr Agent Studio:             https://studio.lyzr.ai

============================================================
🏷️ HASHTAGS
============================================================
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI"""

    lines.append(f"#### Lesson {idx:02d}: {clean_title}")
    lines.append(f"- **Local MP4 File:** `university/revamp/{v_name}`")
    lines.append(f"- **Target Playlist:** [{clean_course} — Master Course]({p_link})")
    lines.append("")
    lines.append("##### 📌 Copy-Pastable Title:")
    lines.append("```text")
    lines.append(user_title)
    lines.append("```")
    lines.append("")
    lines.append("##### 📝 Copy-Pastable Description:")
    lines.append("```text")
    lines.append(user_desc)
    lines.append("```")
    lines.append("\n---\n")

with open(guide_md_path, 'w', encoding='utf-8') as gf:
    gf.write("\n".join(lines))

print(f"✅ Successfully generated Manual Upload Guide to:")
print(f"   {guide_md_path}")
