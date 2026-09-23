import shutil
import os

art_dir = "/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61"
uni_scratch = "/Users/hkc/Documents/lyzr/university/scratch_remotion_temp"
src_outro = "/Users/hkc/Documents/lyzr/university/remotion-branding/out/PremiumBrandOutro.mp4"

if os.path.exists(src_outro):
    shutil.copy(src_outro, os.path.join(uni_scratch, "remotion_premium_outro_rendered.mp4"))
    shutil.copy(src_outro, os.path.join(art_dir, "remotion_new_premium_outro.mp4"))
    print("✅ Copied newly rendered 2s Remotion React Outro video to artifacts directory & scratch!")
