import os
import zipfile
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
theme_dir = university_dir / "thinkific-theme"
zip_path = university_dir / "thinkific-theme-v3.1.4.zip"
artifact_zip_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/thinkific-theme-v3.1.4.zip")

print("==========================================================================")
print(" 📦 CREATING THINKIFIC THEME v3.1.4 ZIP ARCHIVE")
print("==========================================================================")

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file_path in theme_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            arcname = file_path.relative_to(theme_dir)
            zipf.write(file_path, arcname)

size_mb = zip_path.stat().st_size / (1024 * 1024)
print(f"  ✓ Created ZIP: {zip_path} ({size_mb:.2f} MB)")

# Copy to artifacts directory
with zipfile.ZipFile(artifact_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file_path in theme_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            arcname = file_path.relative_to(theme_dir)
            zipf.write(file_path, arcname)

print(f"  ✓ Created Artifact ZIP: {artifact_zip_path}")
print("\n==========================================================================")
print(" 🎉 THINKIFIC THEME v3.1.4 ZIP PACKAGED SUCCESSFULLY!")
print("==========================================================================")
