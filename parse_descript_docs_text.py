import re
import html

doc_file = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/.system_generated/steps/5293/content.md"

with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Strip HTML tags to extract plain text documentation
clean_text = re.sub(r'<[^>]+>', '\n', content)
clean_text = html.unescape(clean_text)
lines = [l.strip() for l in clean_text.split('\n') if l.strip()]

print("==========================================================================")
print(" 📖 DESCRIPT API DOCUMENTATION (https://docs.descriptapi.com/)")
print("==========================================================================")

# Search for Authentication, Endpoints, Headers, Tokens
keywords = ["auth", "token", "bearer", "secret", "header", "endpoint", "v1", "import", "export", "project"]

relevant_lines = []
for i, line in enumerate(lines):
    if any(kw in line.lower() for kw in keywords):
        relevant_lines.append(line)

print(f"Total Relevant Documentation Lines: {len(relevant_lines)}\n")
for l in relevant_lines[:50]:
    print(" •", l)
