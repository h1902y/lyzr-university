import os
import sys
import json
import csv
import time
import re

csv.field_size_limit(sys.maxsize)

university_dir = "/Users/hkc/Documents/lyzr/university"
csv_in_path = os.path.join(university_dir, "master_courses_content_markdown_reverted.csv")

print("==========================================================================")
print(" 🧹 CLEANING YOUTUBE METADATA: STRIPPING ALL CODES & NUMBERS")
print("==========================================================================")

def clean_name_no_numbers(text):
    if not text:
        return ""
    # Strip "Chapter 01: ", "Chapter 02: ", "Chapter 1: " etc.
    text = re.sub(r'^\s*Chapter\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    # Strip "Lesson 01: ", "Lesson 1: " etc.
    text = re.sub(r'^\s*Lesson\s*\d+\s*:\s*', '', text, flags=re.IGNORECASE)
    # Strip codes like C01_CH01_L01
    text = re.sub(r'^\s*C\d+_CH\d+_L\d+\s*', '', text)
    return text.strip()

def generate_clean_user_facing_metadata(course_name, chapter_name, lesson_title, lesson_content_md):
    clean_course = course_name.strip()
    clean_chapter = clean_name_no_numbers(chapter_name)
    clean_title = clean_name_no_numbers(lesson_title)

    # Clean User-Facing Title: "Introduction to Lyzr Platform — Lyzr Foundations"
    title = f"{clean_title} — {clean_course}"
    if len(title) > 95:
        title = title[:95]

    # Extract Objectives / Overview bullets from content markdown
    clean_notes = re.sub(r'#+\s*', '', lesson_content_md)
    clean_notes = re.sub(r'\*\*(.*?)\*\*', r'\1', clean_notes)
    lines = [l.strip() for l in clean_notes.split('\n') if l.strip()]
    
    summary_bullets = []
    for l in lines[:8]:
        if l.startswith('-') or l.startswith('•') or l.startswith('1.') or l.startswith('2.'):
            # Clean numbers from bullet line if present
            l_clean = re.sub(r'^\d+\.\s*', '', l)
            summary_bullets.append(f"  • {l_clean.lstrip('-• ')}")

    bullets_text = "\n".join(summary_bullets) if summary_bullets else "  • Comprehensive technical & operational walkthrough."

    # Clean User-Facing Description
    description = f"""Course: {clean_course}
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
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI
"""

    tags = [
        "Lyzr", "Lyzr AI", "Lyzr University", "AI Agents", "Autonomous Agents",
        "Enterprise AI", "Agent Studio", "Lyzr ADK", "Python SDK", "RAG",
        "Knowledge Base", "Model Context Protocol", "MCP Server", clean_course,
        clean_chapter, clean_title
    ]

    return title, description, tags

rows_list = []
with open(csv_in_path, 'r', encoding='utf-8') as cf:
    reader = csv.reader(cf)
    header = next(reader)
    rows_list = list(reader)

print("Sample Clean User-Facing Metadata:\n")
for r in rows_list[:3]:
    t, d, tg = generate_clean_user_facing_metadata(r[0], r[1], r[2], r[3])
    print(f"📌 TITLE: {t}")
    print(f"📝 DESCRIPTION:\n{d[:300]}...")
    print("-" * 70)
