import subprocess
import pathlib

vpath = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH04_L04_the_semantic_model_global_context.mp4")
raw_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-upload/1 - Tracks/Studio/11 Studio Grounding Agents in Knowledge/08a The Semantic Model.mp4")

print("==========================================================================")
print(" 🔍 INSPECTING THE SEMANTIC MODEL VIDEO & TRANSCRIPT")
print("==========================================================================")

def get_dur(path):
    cmd = ["ffmpeg", "-i", str(path)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            return line.strip()
    return "Unknown"

print(f"Branded Video: {vpath.name} | Size: {vpath.stat().st_size / (1024*1024):.2f} MB | {get_dur(vpath)}")
print(f"Raw Source:    {raw_path.name} | Size: {raw_path.stat().st_size / (1024*1024):.2f} MB | {get_dur(raw_path)}")

# Check Descript URL or transcript text for 08a The Semantic Model
csv_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/master_courses_content_all_crafted_notes.csv")
if csv_path.exists():
    import csv
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if "semantic" in str(row).lower():
                print(f"\n📋 CSV Row Entry:")
                print(f"   Lesson: {row[2] if len(row)>2 else ''}")
                print(f"   Filename: {row[3] if len(row)>3 else ''}")
                print(f"   Descript Link: {row[4] if len(row)>4 else ''}")

print("==========================================================================")
