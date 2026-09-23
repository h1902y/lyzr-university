import zipfile
import json
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
v3_zip = university_dir / "lyzr-university-theme-v3.zip"

print("==========================================================================")
print(" 🔍 INSPECTING WORKING v3.ZIP MANIFEST.JSON")
print("==========================================================================")

if v3_zip.exists():
    with zipfile.ZipFile(v3_zip, 'r') as z:
        if 'manifest.json' in z.namelist():
            m_content = z.read('manifest.json').decode('utf-8')
            m_json = json.loads(m_content)
            print(" ✅ v3.zip manifest.json info:")
            print(json.dumps(m_json.get('info'), indent=2))

print("==========================================================================")
