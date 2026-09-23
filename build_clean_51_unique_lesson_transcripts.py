import os
import json
import csv
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
upload_plan_path = university_dir / "revamp_upload_plan.json"
csv_path = university_dir / "master_courses_content_markdown_reverted.csv"

print("==========================================================================")
print(" 🔧 RE-BUILDING UNIQUE TRANSCRIPTS FOR ALL 51 CURRICULUM LESSONS")
print("==========================================================================")

with open(upload_plan_path, 'r', encoding='utf-8') as f:
    upload_plan = json.load(f)

print(f"Loaded {len(upload_plan)} lessons from revamp_upload_plan.json\n")

# Index all available individual transcripts / notes
individual_transcripts = {}

# 1. SDK-track transcripts
sdk_dir = university_dir / "SDK-track" / "transcripts"
if sdk_dir.exists():
    for f in sdk_dir.glob("*.txt"):
        text = open(f, 'r', encoding='utf-8').read().strip()
        individual_transcripts[f.stem.lower()] = text

# 2. Studio-track notes (contains transcripts / notes)
studio_dir = university_dir / "Studio-track" / "notes"
if studio_dir.exists():
    for f in studio_dir.rglob("*.md"):
        text = open(f, 'r', encoding='utf-8').read().strip()
        individual_transcripts[f.stem.lower()] = text

print(f"Indexed {len(individual_transcripts)} individual source transcript/note files.")

# Match each lesson to its exact individual transcript
matched_count = 0
unique_snippets = set()

for item in upload_plan:
    lesson_name = item["lesson"].lower()
    fname = item["filename"].lower()
    
    # Try finding match in individual_transcripts
    matched_text = None
    for key, text in individual_transcripts.items():
        # Match by key substring
        clean_key = key.replace("-", " ").replace("_", " ")
        clean_lesson = lesson_name.replace("-", " ").replace("_", " ")
        
        # Key word matching
        words = [w for w in clean_lesson.split() if len(w) > 3 and w not in ["lyzr", "with", "from", "into", "your", "agent"]]
        if words and any(w in clean_key for w in words):
            matched_text = text
            break
            
    if matched_text:
        matched_count += 1
        snippet = matched_text[:50].replace("\n", " ")
        unique_snippets.add(snippet)
        item["transcript"] = matched_text
        print(f"  ✓ [{item['index']:02d}] {item['lesson']:<40} -> Matched transcript ({len(matched_text)} chars): '{snippet}...'")
    else:
        print(f"  ⚠️ [{item['index']:02d}] {item['lesson']:<40} -> No direct match found, using clean default transcript.")

print(f"\n==========================================================================")
print(f" Matched {matched_count} / {len(upload_plan)} lessons to unique individual transcripts.")
print(f" Unique snippet count: {len(unique_snippets)}")
print("==========================================================================")
