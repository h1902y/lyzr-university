import os
import zipfile
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
theme_dir = university_dir / "thinkific-theme"
zip_path = university_dir / "thinkific-theme-v3.1.4.zip"
artifact_zip_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/thinkific-theme-v3.1.4.zip")

print("==========================================================================")
print(" 📦 PACKAGING THINKIFIC THEME v3.1.4 UPLOAD ZIP")
print("==========================================================================")

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file_path in theme_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            arcname = file_path.relative_to(theme_dir)
            zipf.write(file_path, arcname)

size_kb = zip_path.stat().st_size / 1024
print(f"  ✓ Packaged Upload ZIP: {zip_path} ({size_kb:.1f} KB)")

# Copy to artifacts directory
with zipfile.ZipFile(artifact_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file_path in theme_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            arcname = file_path.relative_to(theme_dir)
            zipf.write(file_path, arcname)

print(f"  ✓ Packaged Artifact ZIP: {artifact_zip_path}")
print("\n==========================================================================")
print(" 🎉 THINKIFIC THEME v3.1.4 ZIP IS 100% READY FOR UPLOAD!")
print("==========================================================================")
