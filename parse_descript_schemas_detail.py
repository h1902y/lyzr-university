import re
import json

doc_file = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/.system_generated/steps/5293/content.md"

with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
    raw_content = f.read()

print("==========================================================================")
print(" 🔍 PARSING EXACT JSON SCHEMAS FOR EDIT-IN-DESCRIPT & EXPORT")
print("==========================================================================")

# Search for spec object or Redoc store initialization
matches = re.findall(r'spec:\s*(\{.*?\});\s*Redoc', raw_content, re.DOTALL)
if not matches:
    # Search for specUrl or spec JSON inline
    matches = re.findall(r'"postEditInDescriptSchema":\s*(\{.*?\})', raw_content, re.DOTALL)

print(f"Found {len(matches)} schema matches.")

# Extract sections mentioning postEditInDescriptSchema
pos = raw_content.find("postEditInDescriptSchema")
if pos != -1:
    section = raw_content[max(0, pos-200):min(len(raw_content), pos+3000)]
    # Strip HTML tags
    clean_sec = re.sub(r'<[^>]+>', ' ', section)
    clean_sec = re.sub(r'\s+', ' ', clean_sec).strip()
    print("\n--- Documentation Section around postEditInDescriptSchema ---")
    print(clean_sec[:1500])
else:
    print("postEditInDescriptSchema text position not found in raw content.")
