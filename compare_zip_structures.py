import zipfile
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
v3_zip = university_dir / "lyzr-university-theme-v3.zip"
v314_zip = university_dir / "thinkific-theme-v3.1.4.zip"

print("==========================================================================")
print(" 🔍 COMPARING WORKING v3 ZIP vs NEW v3.1.4 ZIP")
print("==========================================================================")

if v3_zip.exists():
    with zipfile.ZipFile(v3_zip, 'r') as z:
        print(f"📦 WORKING v3.zip Entries ({len(z.namelist())} files):")
        for name in z.namelist()[:15]:
            print(f"   {name}")

print("\n" + "-"*60 + "\n")

if v314_zip.exists():
    with zipfile.ZipFile(v314_zip, 'r') as z:
        print(f"📦 NEW v3.1.4.zip Entries ({len(z.namelist())} files):")
        for name in z.namelist()[:15]:
            print(f"   {name}")

print("==========================================================================")
