import re
import json

doc_file = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/.system_generated/steps/5293/content.md"

with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'const __redoc_state = (\{.*?\});\n', html)
if not m:
    m = re.search(r'const __redoc_state = (\{.*?\});', html)

if m:
    data = json.loads(m.group(1))
    spec = data.get("spec", {}).get("data", {})
    paths = spec.get("paths", {})
    components = spec.get("components", {})
    
    print("==========================================================================")
    print(" 📜 OFFICIAL DESCRIPT OPENAPI 3.0.0 SPECIFICATION PARSED")
    print("==========================================================================")
    print(f"Title: {spec.get('info', {}).get('title')} (Version: {spec.get('info', {}).get('version')})")
    print(f"Total API Paths: {len(paths)}\n")
    
    for path, methods in paths.items():
        for method, details in methods.items():
            op_id = details.get("operationId", "")
            summary = details.get("summary", "")
            tags = details.get("tags", [])
            print(f" • {method.upper():6s} {path} (ID: {op_id} | Tags: {tags})")
            if "editindescript" in op_id.lower() or "export" in path.lower() or "postEditInDescriptSchema" in op_id:
                print(f"   Summary: {summary}")
                print(f"   Request Body: {json.dumps(details.get('requestBody', {}), indent=2)[:500]}")
                print(f"   Responses: {json.dumps(details.get('responses', {}), indent=2)[:500]}")
                print("-" * 60)

    # Inspect components schemas if postEditInDescriptSchema exists
    schemas = components.get("schemas", {})
    if "postEditInDescriptSchema" in schemas:
        print("\n=== postEditInDescriptSchema Definition ===")
        print(json.dumps(schemas["postEditInDescriptSchema"], indent=2))
else:
    print("Could not find __redoc_state in HTML.")
