import os
import zipfile
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
theme_dir = university_dir / "thinkific-theme"
zip_path = university_dir / "thinkific-theme-v3.1.4.zip"
artifact_zip_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/thinkific-theme-v3.1.4.zip")

print("==========================================================================")
print(" 📦 PACKAGING THINKIFIC THEME v3.1.4 ZIP WITH REQUIRED .version FILE")
print("==========================================================================")

# Ensure .version file exists inside thinkific-theme
version_file = theme_dir / ".version"
if not version_file.exists():
    with open(version_file, 'w', encoding='utf-8') as f:
        f.write("2.7.0")

def add_theme_to_zip(z_path):
    with zipfile.ZipFile(z_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in sorted(theme_dir.rglob('*')):
            if file_path.is_file():
                # Allow .version file explicitly! Ignore git/ds_store hidden files
                if file_path.name == '.version' or not file_path.name.startswith('.'):
                    arcname = file_path.relative_to(theme_dir)
                    zipf.write(file_path, arcname)

add_theme_to_zip(zip_path)
print(f"  ✓ Packaged Upload ZIP: {zip_path} ({zip_path.stat().st_size / 1024:.1f} KB)")

add_theme_to_zip(artifact_zip_path)
print(f"  ✓ Packaged Artifact ZIP: {artifact_zip_path}")

# Verify .version file is inside ZIP
with zipfile.ZipFile(zip_path, 'r') as z:
    if '.version' in z.namelist():
        print(f"  ✅ Verified: '.version' file is present inside ZIP archive! Content: '{z.read('.version').decode('utf-8').strip()}'")

print("\n==========================================================================")
print(" 🎉 THINKIFIC THEME v3.1.4 ZIP ARCHIVE PACKAGED WITH .version FILE!")
print("==========================================================================")
