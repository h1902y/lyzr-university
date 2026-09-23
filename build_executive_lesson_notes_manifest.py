import json
import csv
import pathlib
import re

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
upload_plan_path = university_dir / "revamp_upload_plan.json"
manifest_artifact_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/MASTER_CURRICULUM_MANIFEST.md")

print("==========================================================================")
print(" 📝 GENERATING EXECUTIVE LESSON NOTES (OVERVIEW - OBJECTIVES - TAKEAWAYS)")
print("==========================================================================")

with open(upload_plan_path, 'r', encoding='utf-8') as f:
    upload_plan = json.load(f)

md = []
md.append("# 📚 Master Lyzr University Curriculum Manifest & Lesson Schema\n")
md.append("> [!IMPORTANT]")
md.append("> **Executive Lesson Notes Standard:** Every lesson note block is wrapped inside ````notes` code fencing. Content strictly follows the **Overview → Key Objectives → Key Takeaways** structure in 100% pure plain text (zero HTML tags, zero Markdown symbols). Copy and paste directly into Thinkific's text editor!\n")

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
    
    # Formulate Executive Notes (Overview -> Objectives -> Takeaways)
    title_upper = lesson.strip()
    
    overview = f"Lesson Overview:\nIn this lesson, we explore {lesson} within the {course} curriculum ({chapter}). You will learn how to design, configure, and orchestrate production-grade AI agents with deterministic control, security, and enterprise scalability using the Lyzr Agent Platform."
    
    objectives = f"Key Objectives:\n1. Understand the core architecture and operational design of {lesson}.\n2. Configure step-by-step agent parameters, tool integrations, and memory layers.\n3. Implement enterprise guardrails, deterministic routing, and runtime observability."
    
    takeaways = f"Key Takeaways:\n• Deterministic Control: Ensure agents operate strictly within predefined boundaries and enterprise schemas.\n• Seamless Integration: Connect agents effortlessly to external tools, vector memory, and data sources.\n• Production Readiness: Apply best practices for logging, failure recovery, and enterprise deployment."
    
    full_executive_notes = f"{title_upper}\n\n{overview}\n\n{objectives}\n\n{takeaways}"
    
    md.append("#### 📝 Thinkific Text Block Content (Overview · Objectives · Takeaways):")
    md.append("````notes")
    md.append(full_executive_notes)
    md.append("````\n")
    md.append("---\n")

with open(manifest_artifact_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print(f"  ✓ Written Executive Manifest to Artifact: {manifest_artifact_path}")
print("==========================================================================")
