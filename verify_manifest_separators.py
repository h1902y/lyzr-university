import os
import re

master_md_path = "/Users/hkc/Documents/lyzr/university/revamp/MASTER_CURRICULUM_MANIFEST.md"

with open(master_md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Count occurrences of 3x separators, 2x separators, and 1x separators
triple_seps = len(re.findall(r'---\n\n---\n\n---', text))
double_seps = len(re.findall(r'---\n\n---', text)) - (triple_seps * 2)

print("==========================================================================")
print(" 🔍 VERIFYING HORIZONTAL SEPARATORS IN MANIFEST")
print("==========================================================================")
print(f" • 3x Horizontal Separators (Between Courses):  {triple_seps}")
print(f" • 2x Horizontal Separators (Between Chapters): {double_seps}")
print(f" • Total Lines in Manifest:                    {len(text.splitlines())}")
