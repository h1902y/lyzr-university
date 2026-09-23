import os
import re

university_dir = "/Users/hkc/Documents/lyzr/university"
sdk_readme = os.path.join(university_dir, "SDK-track/README.md")
studio_readme = os.path.join(university_dir, "Studio-track/README.md")

exact_map = {}

def extract_exact_mappings(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        if "|" in line and "share.descript.com" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4:
                # Title is in column 2 or 3
                raw_title = parts[2].replace('*', '').strip()
                descript_match = re.search(r'https://share\.descript\.com/view/[a-zA-Z0-9]+', line)
                if descript_match and raw_title:
                    url = descript_match.group(0)
                    exact_map[raw_title] = url

extract_exact_mappings(sdk_readme)
extract_exact_mappings(studio_readme)

print(f"Extracted {len(exact_map)} exact title -> Descript URL mappings:\n")
for title, url in exact_map.items():
    print(f" • '{title}' -> {url}")
