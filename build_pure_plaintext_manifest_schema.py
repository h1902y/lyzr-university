import csv
import json
import re
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
csv_path = university_dir / "master_courses_content_markdown_reverted.csv"
upload_plan_path = university_dir / "revamp_upload_plan.json"
manifest_artifact_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/MASTER_CURRICULUM_MANIFEST.md")

print("==========================================================================")
print(" 📜 GENERATING PURE PLAIN-TEXT MANIFEST (NO HTML, NO MARKDOWN)")
print("==========================================================================")

with open(upload_plan_path, 'r', encoding='utf-8') as f:
    upload_plan = json.load(f)

# Load CSV text content
csv_content_map = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        if len(row) >= 6:
            fname = row[3].strip()
            content = row[5].strip()
            csv_content_map[fname] = content

def clean_to_pure_plaintext(text):
    # Strip HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Strip Markdown headers
    text = re.sub(r'#+\s*', '', text)
    # Strip Markdown bold/italic/bullet markers
    text = re.sub(r'\*{1,3}|_{1,3}', '', text)
    text = re.sub(r'^\s*[-•]\s*', '', text, flags=re.MULTILINE)
    # Strip inline code ticks
    text = re.sub(r'`', '', text)
    # Normalize spaces and empty lines
    lines = [line.strip() for line in text.splitlines()]
    paragraphs = [l for l in lines if l]
    return "\n\n".join(paragraphs)

md = []
md.append("# 📚 Master Lyzr University Curriculum Manifest & Lesson Schema\n")
md.append("> [!IMPORTANT]")
md.append("> **100% Pure Plain Text Rule:** Every lesson note block is wrapped inside ````notes` code fencing. The text inside ````notes` contains **NO HTML TAGS AND NO MARKDOWN SYMBOLS**. Copy and paste directly into Thinkific's text editor!\n")

current_course = None
current_chapter = None

for item in upload_plan:
    idx = item["index"]
    course = item["course"]
    chapter = item["chapter"]
    lesson = item["lesson"]
    fname = item["filename"]
    code_id = "_".join(fname.split("_")[:4])
    
    if course != current_course:
        current_course = course
        md.append(f"\n# 🏛️ COURSE TRACK: {current_course.upper()}\n")
        
    if chapter != current_chapter:
        current_chapter = chapter
        md.append(f"\n## 📂 {current_chapter}\n")
        
    md.append(f"### 📖 [{idx:02d}] {lesson} (`{code_id}`)\n")
    md.append(f"| Property | Defined Schema Value |")
    md.append(f"| :--- | :--- |")
    md.append(f"| **Lesson Code** | `{code_id}` |")
    md.append(f"| **Course Track** | {course} |")
    md.append(f"| **Chapter** | {chapter} |")
    md.append(f"| **Lesson Title** | {lesson} |")
    md.append(f"| **Video MP4 Path** | [`revamp_branded/{fname}`](file:///Users/hkc/Documents/lyzr/university/revamp_branded/{fname}) |")
    md.append(f"| **Thumbnail PNG Path** | [`revamp/thumbnails/{code_id}.png`](file:///Users/hkc/Documents/lyzr/university/revamp/thumbnails/{fname.replace('.mp4', '.png')}) |")
    md.append(f"| **Descript Link** | [View Source Recording](https://share.descript.com/view/{code_id}) |\n")
    
    raw_content = csv_content_map.get(fname, f"Lesson overview and notes for {lesson}.")
    
    # Generate 100% PURE PLAIN TEXT
    intro_p = f"{lesson}\n\nWelcome to this lesson in the Lyzr Master Class Series. Below are the key takeaways, step-by-step guidance, and execution notes for this topic."
    obj_p = f"Key Objectives and Takeaways:\n1. Master the architectural principles of {lesson}.\n2. Implement step-by-step agent configurations and tools in Lyzr.\n3. Apply production best practices for enterprise deployment."
    
    body_text = clean_to_pure_plaintext(raw_content)
    
    full_plain_text = f"{intro_p}\n\n{obj_p}\n\nLesson Notes and Transcript Summary:\n{body_text}"
    
    md.append("#### 📝 Thinkific Text Block Content (100% Pure Plain Text):")
    md.append("````notes")
    md.append(full_plain_text)
    md.append("````\n")
    md.append("---\n")

with open(manifest_artifact_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print(f"  ✓ Written 100% Pure Plain-Text Manifest to Artifact: {manifest_artifact_path}")
print("==========================================================================")
