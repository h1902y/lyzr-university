import csv
import json
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
csv_path = university_dir / "master_courses_content_markdown_reverted.csv"
upload_plan_path = university_dir / "revamp_upload_plan.json"
manifest_artifact_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/MASTER_CURRICULUM_MANIFEST.md")

print("==========================================================================")
print(" 📜 GENERATING MASTER CURRICULUM MANIFEST MD WITH ```notes FENCING")
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

md = []
md.append("# 📚 Master Lyzr University Curriculum Manifest & Lesson Schema\n")
md.append("> [!IMPORTANT]")
md.append("> **Thinkific Text Block Rule:** Every lesson note block is wrapped inside ````notes` code fencing. Copy the plain text inside the ````notes` block directly into Thinkific's text editor (it uses clean plain text and standard HTML tags `<h2>`, `<p>`, `<ul>`, `<li>` to ensure 100% rendering compatibility without raw markdown errors).\n")

current_course = None
current_chapter = None

for item in upload_plan:
    idx = item["index"]
    course = item["course"]
    chapter = item["chapter"]
    lesson = item["lesson"]
    fname = item["filename"]
    
    # Extract code identifier like C01_CH01_L01
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
    
    # Extract text content
    raw_content = csv_content_map.get(fname, f"Lesson overview and notes for {lesson}.")
    
    # Format clean plain text / HTML for Thinkific text block
    clean_notes = []
    clean_notes.append(f"<h2>{lesson}</h2>\n")
    clean_notes.append("<p>Welcome to this lesson in the <strong>Lyzr Master Class Series</strong>. Below are the key takeaways, step-by-step guidance, and execution notes for this topic.</p>\n")
    clean_notes.append("<h3>Key Objectives & Takeaways</h3>")
    clean_notes.append("<ul>")
    clean_notes.append(f"  <li>Master the architectural principles of {lesson}.</li>")
    clean_notes.append("  <li>Implement step-by-step agent configurations and tools in Lyzr.</li>")
    clean_notes.append("  <li>Apply production best practices for enterprise deployment.</li>")
    clean_notes.append("</ul>\n")
    clean_notes.append("<h3>Lesson Notes & Transcript Summary</h3>")
    
    # Add transcript lines as paragraph blocks
    paragraphs = [p.strip() for p in raw_content.split("\n\n") if p.strip() and not p.startswith("#")]
    for p in paragraphs[:5]:
        clean_notes.append(f"<p>{p}</p>")
        
    notes_str = "\n".join(clean_notes)
    
    md.append("#### 📝 Thinkific Text Block Content (Markdown-Free):")
    md.append("````notes")
    md.append(notes_str)
    md.append("````\n")
    md.append("---\n")

with open(manifest_artifact_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print(f"  ✓ Written Schema-Defined Manifest to Artifact: {manifest_artifact_path}")
print("==========================================================================")
