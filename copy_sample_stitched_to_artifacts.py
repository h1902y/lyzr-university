import shutil
import os

art_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
src_video = "/Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH01_L01_introduction_to_lyzr_platform.mp4"
dest_video = os.path.join(art_dir, "sample_stitched_video_01.mp4")

if os.path.exists(src_video):
    shutil.copy(src_video, dest_video)
    print("✅ Copied sample stitched video to artifacts directory!")
