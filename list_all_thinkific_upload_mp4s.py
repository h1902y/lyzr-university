import os

upload_dir = "/Users/hkc/Documents/lyzr/university/thinkific-upload"

print("==========================================================================")
print(" 📁 SEARCHING ALL SUBDIRECTORIES OF THINKIFIC-UPLOAD FOR MP4 FILES")
print("==========================================================================")

found_files = {}
for root, dirs, files in os.walk(upload_dir):
    for f in files:
        if f.endswith('.mp4'):
            rel = os.path.relpath(os.path.join(root, f), upload_dir)
            found_files[f] = os.path.join(root, f)
            print(f" • {f} -> {rel}")

print(f"\nTotal MP4 files under thinkific-upload: {len(found_files)}")
