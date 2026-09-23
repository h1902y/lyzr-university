import os
import re
import csv

brain_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
conv_path = os.path.join(brain_dir, "complete_conversation.md")
university_dir = "/Users/hkc/Documents/lyzr/university"

print("==========================================================================")
print(" 🔍 EXTRACTING DESCRIPT LINKS FROM CONVERSATION & MANIFESTS")
print("==========================================================================")

descript_links = []

# 1. Search in complete_conversation.md
if os.path.exists(conv_path):
    with open(conv_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        links = re.findall(r'https?://[^\s]*descript[^\s]*', text, re.IGNORECASE)
        for link in links:
            clean_link = link.rstrip(')`*"\',;')
            descript_links.append({"source": "complete_conversation.md", "link": clean_link})

# 2. Search across university/ files (.csv, .json, .md)
for root, dirs, files in os.walk(university_dir):
    for file in files:
        if file.endswith(('.csv', '.json', '.md', '.py')):
            fp = os.path.join(root, file)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    links = re.findall(r'https?://[^\s]*descript[^\s]*', content, re.IGNORECASE)
                    for link in links:
                        clean_link = link.rstrip(')`*"\',;')
                        descript_links.append({"source": os.path.relpath(fp, university_dir), "link": clean_link})
            except Exception as e:
                pass

print(f"Found {len(descript_links)} total Descript links across workspace files.\n")

unique_links = {}
for d in descript_links:
    url = d["link"]
    if url not in unique_links:
        unique_links[url] = d["source"]

for i, (url, src) in enumerate(unique_links.items()):
    print(f"{i+1}. {url} (Source: {src})")
