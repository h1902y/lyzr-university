import os
import json
import re

university_dir = "/Users/hkc/Documents/lyzr/university"
upload_dir = os.path.join(university_dir, "thinkific-upload")

print("==========================================================================")
print(" 🔍 DEEP INSPECTION OF ALL LOCAL MP4 VIDEOS & RAW DESCRIPT METADATA")
print("==========================================================================")

# 1. Collect all local MP4 files
all_mp4_files = []
for root, dirs, files in os.walk(university_dir):
    for f in files:
        if f.endswith('.mp4'):
            fp = os.path.join(root, f)
            all_mp4_files.append({"filename": f, "path": fp, "dir": os.path.relpath(root, university_dir)})

print(f"Total Local MP4 Video Files Found: {len(all_mp4_files)}")

# 2. Inspect raw JSON transcript files for Descript metadata
raw_descript_metadata = {}
for root, dirs, files in os.walk(university_dir):
    for f in files:
        if f.endswith('.json'):
            fp = os.path.join(root, f)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as jf:
                    data = json.load(jf)
                    # Check if Descript json structure
                    if isinstance(data, dict):
                        descript_id = data.get("descript_id") or data.get("id") or data.get("share_url")
                        url = data.get("share_url") or data.get("url")
                        if not url:
                            # search regex in json text
                            raw_txt = json.dumps(data)
                            m = re.search(r'https://share\.descript\.com/view/[a-zA-Z0-9]+', raw_txt)
                            if m:
                                url = m.group(0)
                        if url or descript_id:
                            raw_descript_metadata[f] = {"url": url, "id": descript_id, "file": os.path.relpath(fp, university_dir)}
            except Exception as e:
                pass

print(f"Found Descript Metadata in {len(raw_descript_metadata)} raw JSON transcript files.")

# 3. List all MP4 filenames and check matching transcript/notes
print("\n--- Complete List of All Local MP4 Video Assets ---")
for idx, mp4 in enumerate(sorted(all_mp4_files, key=lambda x: x["filename"])):
    fname = mp4["filename"]
    rel_dir = mp4["dir"]
    print(f" {idx + 1:2d}. `{fname}` (Location: {rel_dir})")
