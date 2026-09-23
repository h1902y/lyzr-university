import os
import re
import csv

brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
conv_path = os.path.join(brain_dir, "complete_conversation.md")
university_dir = "/Users/hkc/Documents/lyzr/university"
upload_dir = os.path.join(university_dir, "thinkific-upload")

print("==========================================================================")
print(" 🔍 AUDITING LOCAL VIDEO ASSETS AGAINST SHEET & CONVERSATION TRANSCRIPT")
print("==========================================================================")

# 1. Collect all local MP4 files under university/ and thinkific-upload/
local_mp4_files = {}
for root, dirs, files in os.walk(university_dir):
    for f in files:
        if f.endswith('.mp4'):
            full_path = os.path.join(root, f)
            size_mb = round(os.path.getsize(full_path) / (1024 * 1024), 2)
            local_mp4_files[f] = {
                "path": full_path,
                "size_mb": size_mb
            }

print(f"Total Local MP4 Video Files Found on Disk: {len(local_mp4_files)}")

# 2. Extract video references from complete_conversation.md if available
conv_mp4_refs = set()
if os.path.exists(conv_path):
    with open(conv_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        matches = re.findall(r'[\w\s\-—–\.\(\)]+\.mp4', text, re.IGNORECASE)
        for m in matches:
            clean_m = m.strip(' `*"\'')
            if clean_m:
                conv_mp4_refs.add(clean_m)

print(f"Extracted {len(conv_mp4_refs)} Unique Video Filenames Referenced in complete_conversation.md")

# 3. Check CSV manifests in university/
manifest_mp4_refs = set()
for root, dirs, files in os.walk(university_dir):
    for f in files:
        if f.endswith('.csv'):
            csv_path = os.path.join(root, f)
            try:
                with open(csv_path, 'r', encoding='utf-8', errors='ignore') as cf:
                    reader = csv.reader(cf)
                    for row in reader:
                        for cell in row:
                            if cell.endswith('.mp4'):
                                manifest_mp4_refs.add(cell.strip())
            except Exception as e:
                pass

print(f"Extracted {len(manifest_mp4_refs)} Video Filenames Referenced in Manifest CSVs")

# 4. Compare Local Existence
missing_from_disk = []
all_referenced_videos = conv_mp4_refs.union(manifest_mp4_refs)

print(f"\nTotal Combined Referenced Videos Across Sheet/Manifests/Transcript: {len(all_referenced_videos)}")

verified_present = []
for vid in sorted(all_referenced_videos):
    basename = os.path.basename(vid)
    found = False
    for local_f in local_mp4_files:
        if basename.lower() == local_f.lower() or vid.lower() == local_f.lower():
            found = True
            verified_present.append((vid, local_mp4_files[local_f]))
            break
    if not found:
        missing_from_disk.append(vid)

print(f"\n✅ Verified Present Locally on Disk: {len(verified_present)}")
print(f"❌ Missing from Disk: {len(missing_from_disk)}")

if missing_from_disk:
    print("\nMissing Videos List:")
    for m in missing_from_disk:
        print(f"  - {m}")

# Generate detailed audit artifact report
report_path = os.path.join(brain_dir, "local_video_assets_audit_report.md")
report_md = f"""# 📹 Complete Local Video Assets & Sheet Audit Report

**Audit Timestamp:** {os.popen('date').read().strip()}  
**Total Local MP4 Video Files on Disk:** {len(local_mp4_files)}  
**Total Combined Referenced Videos (Sheet/Manifests/Transcript):** {len(all_referenced_videos)}  
**Verified Present Locally:** {len(verified_present)}  
**Missing Videos:** {len(missing_from_disk)}  

---

## 1. Local Storage Breakdown

| Storage Location | Video Count | Total Size |
| :--- | :---: | :---: |
| `/Users/hkc/Documents/lyzr/university/thinkific-upload` | {len([f for f in local_mp4_files if 'thinkific-upload' in local_mp4_files[f]['path']])} | {sum([local_mp4_files[f]['size_mb'] for f in local_mp4_files if 'thinkific-upload' in local_mp4_files[f]['path']]):.2f} MB |
| Other Local Directories | {len([f for f in local_mp4_files if 'thinkific-upload' not in local_mp4_files[f]['path']])} | {sum([local_mp4_files[f]['size_mb'] for f in local_mp4_files if 'thinkific-upload' not in local_mp4_files[f]['path']]):.2f} MB |
| **TOTAL** | **{len(local_mp4_files)} Files** | **{sum([local_mp4_files[f]['size_mb'] for f in local_mp4_files]):.2f} MB** |

---

## 2. Complete Local Video Inventory List

| # | Video Asset Filename | Size (MB) | Verified Local Disk Path |
| :--- | :--- | :---: | :--- |
"""

for idx, (f_name, meta) in enumerate(sorted(local_mp4_files.items())):
    report_md += f"| {idx + 1} | `{f_name}` | {meta['size_mb']} MB | `file://{meta['path']}` |\n"

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_md)

print(f"\n📝 Saved complete video asset audit report to: {report_path}")
