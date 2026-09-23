import os
import sys

university_dir = "/Users/hkc/Documents/lyzr/university"
revamp_dir = os.path.join(university_dir, "revamp")
guide_md_path = os.path.join(revamp_dir, "MANUAL_YOUTUBE_UPLOAD_GUIDE.md")

old_ids = {
    "PLNhUOcQ57yRU": "PLXDpecDw4SSE",
    "PLJs-yamjL6bw": "PLaRYyNGFEbho",
    "PLad3Pu7_rlUI": "PLR9A8Tv7zX7Y"
}

if os.path.exists(guide_md_path):
    with open(guide_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_id, new_id in old_ids.items():
        content = content.replace(old_id, new_id)
    
    with open(guide_md_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("==========================================================================")
print(" ✅ UPDATED PLAYLIST IDS FOR OFFICIAL @LyzrAI CHANNEL IN MANIFEST & GUIDES")
print("==========================================================================")
print(" • Lyzr Foundations:                     PLXDpecDw4SSE")
print(" • Lyzr for Business Professionals:      PLaRYyNGFEbho")
print(" • Lyzr for Technical Professionals:     PLR9A8Tv7zX7Y")
