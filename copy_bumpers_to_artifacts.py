import shutil
import os

art_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
src_intro = "/Users/hkc/Documents/lyzr/university/scratch_remotion_temp/remotion_intro_static.mp4"
src_outro = "/Users/hkc/Documents/lyzr/university/scratch_remotion_temp/remotion_outro_static.mp4"

shutil.copy(src_intro, os.path.join(art_dir, "remotion_intro_static.mp4"))
shutil.copy(src_outro, os.path.join(art_dir, "remotion_outro_static.mp4"))

print("✅ Copied Intro & Outro MP4 videos to artifacts directory!")
