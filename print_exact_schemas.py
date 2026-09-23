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
    schemas = data.get("spec", {}).get("data", {}).get("components", {}).get("schemas", {})
    paths = data.get("spec", {}).get("data", {}).get("paths", {})
    
    print("==========================================================================")
    print(" 📋 SCHEMAS DEFINITION: EditInDescript & getPublishedProjectMetadata")
    print("==========================================================================")
    
    for s_name in ["EditInDescriptSchemaPostBody", "EditInDescriptSchemaPostResponse"]:
        if s_name in schemas:
            print(f"\n=== Schema: {s_name} ===")
            print(json.dumps(schemas[s_name], indent=2))

    print("\n=== GET /published_projects/{publishedProjectSlug} Definition ===")
    pub_path = paths.get("/published_projects/{publishedProjectSlug}", {})
    print(json.dumps(pub_path, indent=2))
