import shutil
import os

art_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
src_intro = "/Users/hkc/Documents/lyzr/university/remotion-branding/out/PremiumBrandIntro.mp4"
dest_intro = os.path.join(art_dir, "remotion_new_premium_intro.mp4")

if os.path.exists(src_intro):
    shutil.copy(src_intro, dest_intro)
    print("✅ Copied newly rendered Remotion React Intro video to artifacts directory!")
