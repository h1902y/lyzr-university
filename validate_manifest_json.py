import json
import pathlib

manifest_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-theme/manifest.json")

print("==========================================================================")
print(" 🔍 VALIDATING MANIFEST.JSON SYNTAX")
print("==========================================================================")

try:
    data = json.load(open(manifest_path, 'r', encoding='utf-8'))
    print(" ✅ manifest.json is 100% VALID JSON!")
    print(f"    Name: {data.get('info', {}).get('name')}")
    print(f"    Version: {data.get('info', {}).get('version')}")
    print(f"    Author: {data.get('info', {}).get('author')}")
except Exception as e:
    print(f" ❌ JSON Syntax Error: {e}")

print("==========================================================================")
