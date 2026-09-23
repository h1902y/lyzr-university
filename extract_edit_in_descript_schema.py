import re
import html
import json

doc_file = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/.system_generated/steps/5293/content.md"

with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
    raw_content = f.read()

print("==========================================================================")
print(" 🔍 SEARCHING FOR Edit-in-Descript & postEditInDescriptSchema")
print("==========================================================================")

# Search for postEditInDescriptSchema or Edit-in-Descript in html
matches = re.finditer(r'(Edit-in-Descript|postEditInDescriptSchema|subtitles|caption|download_url|export)', raw_content, re.IGNORECASE)

found_snippets = []
for m in matches:
    idx = m.start()
    snippet = raw_content[max(0, idx-300):min(len(raw_content), idx+500)]
    clean_s = re.sub(r'<[^>]+>', ' ', snippet)
    clean_s = html.unescape(clean_s)
    clean_s = re.sub(r'\s+', ' ', clean_s).strip()
    found_snippets.append(clean_s)

print(f"Found {len(found_snippets)} documentation snippets matching search:\n")
for i, s in enumerate(found_snippets[:10], 1):
    print(f"Snippet {i}:")
    print(s[:350])
    print("-" * 60)
