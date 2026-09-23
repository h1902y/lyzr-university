import os
import shutil

university_dir = "/Users/hkc/Documents/lyzr/university"
old_dir = os.path.join(university_dir, "bulk-video-upload")
new_dir = os.path.join(university_dir, "revamp")

if os.path.exists(old_dir):
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    shutil.move(old_dir, new_dir)
    print(f"✅ Successfully renamed directory:")
    print(f"   From: {old_dir}")
    print(f"   To:   {new_dir}")
else:
    print(f"Directory {old_dir} does not exist. Current status of {new_dir}: {os.path.exists(new_dir)}")

print(f"\n📂 Total video files inside 'revamp': {len(os.listdir(new_dir)) if os.path.exists(new_dir) else 0}")
