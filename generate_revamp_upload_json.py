import os
import sys
import json
import csv
import re

csv.field_size_limit(sys.maxsize)

university_dir = "/Users/hkc/Documents/lyzr/university"
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")
json_out_path = os.path.join(university_dir, "revamp_upload_plan.json")

print("==========================================================================")
print(" 🏷️ UPDATING YOUTUBE TITLES WITH ONE-WORD PREFIX (Foundation/Business/Technical CN LM | Title)")
print("==========================================================================")

COURSE_PREFIX_MAP = {
    "Lyzr Foundations": "Foundation",
    "Lyzr for Business Professionals": "Business",
    "Lyzr for Technical Professionals": "Technical"
}

PLAYLIST_NAME_MAP = {
    "Lyzr Foundations": "Lyzr Foundations — Master Course",
    "Lyzr for Business Professionals": "Lyzr for Business Professionals — Master Course",
    "Lyzr for Technical Professionals": "Lyzr for Technical Professionals — Master Course"
}

def clean_name_no_numbers(text):
    if not text:
        return ""
    text = re.sub(r'^\s*Chapter\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*Lesson\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*C\d+_CH\d+_L\d+\s*', '', text)
    return text.strip()

def parse_cn_lm(ch_name, l_title, v_name):
    # Extract Chapter Number (C1, C2...) and Lesson Number (L1, L2...) from video filename or names
    m = re.search(r'C(\d+)_CH(\d+)_L(\d+)', v_name)
    if m:
        c_num = int(m.group(2))
        l_num = int(m.group(3))
        return f"C{c_num} L{l_num}"
    
    # Fallback regex on chapter/lesson names
    ch_m = re.search(r'Chapter\s*(\d+)', ch_name, re.I)
    l_m = re.search(r'Lesson\s*(\d+)', l_title, re.I)
    c_val = ch_m.group(1) if ch_m else "1"
    l_val = l_m.group(1) if l_m else "1"
    return f"C{int(c_val)} L{int(l_val)}"

def generate_clean_metadata(course_name, chapter_name, lesson_title, lesson_content_md, video_filename):
    clean_course = course_name.strip()
    clean_chapter = clean_name_no_numbers(chapter_name)
    clean_title = clean_name_no_numbers(lesson_title)

    one_word_prefix = COURSE_PREFIX_MAP.get(clean_course, "Lyzr")
    cn_lm = parse_cn_lm(chapter_name, lesson_title, video_filename)

    # Title: "Foundation C1 L1 | Introduction to Lyzr Platform"
    title = f"{one_word_prefix} {cn_lm} | {clean_title}"
    if len(title) > 95:
        title = title[:95]

    clean_notes = re.sub(r'#+\s*', '', lesson_content_md)
    clean_notes = re.sub(r'\*\*(.*?)\*\*', r'\1', clean_notes)
    lines = [l.strip() for l in clean_notes.split('\n') if l.strip()]
    
    summary_bullets = []
    for l in lines[:8]:
        if l.startswith('-') or l.startswith('•') or re.match(r'^\d+\.', l):
            l_clean = re.sub(r'^\d+\.\s*', '', l)
            summary_bullets.append(f"  • {l_clean.lstrip('-• ')}")

    bullets_text = "\n".join(summary_bullets) if summary_bullets else "  • Comprehensive technical & operational walkthrough."

    description = f"""Course: {clean_course}
Chapter: {clean_chapter}
Lesson: {clean_title}

============================================================
📚 LESSON OVERVIEW & OBJECTIVES
============================================================
{bullets_text}

============================================================
🔗 Important Links:
Build with Architect: https://hubs.ly/Q043pWTs0
Build your own AI agent → https://hubs.ly/Q03wb5Md0
Explore our website → https://hubs.ly/Q03wbGVt0
Build agents for your company (Book a demo) → https://hubs.ly/Q03wbH0k0
Learn how to build agents with Lyzr Academy → https://hubs.ly/Q03wqxFR0

============================================================
🏷️ HASHTAGS
============================================================
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI"""

    return title, description, PLAYLIST_NAME_MAP.get(clean_course, "")

items = []
with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    for idx, r in enumerate(reader, 1):
        c_name = r[0]
        ch_name = r[1]
        l_title = r[2]
        content_md = r[3]
        v_name = r[5]
        
        t, d, p_name = generate_clean_metadata(c_name, ch_name, l_title, content_md, v_name)
        v_path = os.path.join(university_dir, "revamp", v_name)
        thumb_path = os.path.join(university_dir, "revamp", "thumbnails", f"{v_name.replace('.mp4', '')}.png")
        
        items.append({
            "index": idx,
            "course": c_name,
            "chapter": ch_name,
            "lesson": l_title,
            "filename": v_name,
            "filepath": v_path,
            "thumbnail_path": thumb_path if os.path.exists(thumb_path) else "",
            "title": t,
            "description": d,
            "playlist": p_name,
            "exists": os.path.exists(v_path)
        })

with open(json_out_path, 'w', encoding='utf-8') as jf:
    json.dump(items, jf, indent=2)

print(f"✅ Updated plan JSON with new title prefixes for {len(items)} lessons:")
print(f"   {json_out_path}")
