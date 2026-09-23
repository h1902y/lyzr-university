import csv
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")

csv_files = [
    "master_courses_content_markdown_reverted.csv",
    "master_courses_content_all_crafted_notes.csv",
    "master_courses_content_final_clean.csv",
    "master_courses_content_plain_text.csv",
    "master_courses_content_pure_transcripts.csv"
]

print("==========================================================================")
print(" 🔍 AUDITING TRANSCRIPTS ACROSS ALL UNIVERSITY CSV FILES")
print("==========================================================================")

for fname in csv_files:
    fpath = university_dir / fname
    if not fpath.exists():
        continue
        
    print(f"\n📄 Inspecting {fname}:")
    with open(fpath, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        print(f"   Total rows: {len(reader)}")
        
        # Collect transcripts / content text
        transcripts = []
        for i, row in enumerate(reader):
            if i == 0 and ("course" in str(row[0]).lower() or "title" in str(row[0]).lower()):
                continue # Header row
            # Usually last or 4th column is transcript/notes
            if len(row) >= 4:
                # Find transcript column
                text_col = row[-1] if len(row) > 3 else row[3]
                transcripts.append((i, row[0] if len(row) > 0 else f"Row {i}", text_col.strip()[:60]))
                
        # Check duplicate transcripts
        unique_texts = set(t[2] for t in transcripts)
        print(f"   Total content rows: {len(transcripts)} | Unique preview strings: {len(unique_texts)}")
        if len(unique_texts) < len(transcripts):
            print(f"   ⚠️ WARNING: DUPLICATES DETECTED! ({len(transcripts) - len(unique_texts)} duplicate rows)")
            # Print sample duplicates
            seen = {}
            for row_idx, title, snippet in transcripts:
                if snippet in seen:
                    print(f"      - Duplicate snippet found at Row {row_idx} ({title}) matching Row {seen[snippet]}: '{snippet}'")
                else:
                    seen[snippet] = row_idx

print("\n==========================================================================")
