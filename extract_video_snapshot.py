import subprocess
import pathlib

vpath = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4")
out_img = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/c02_l02_frame.jpg")

print("==========================================================================")
print(" 📸 EXTRACTING FRAME SNAPSHOT FROM C02_CH01_L02")
print("==========================================================================")

cmd = ["ffmpeg", "-y", "-ss", "00:00:10", "-i", str(vpath), "-vframes", "1", str(out_img)]
res = subprocess.run(cmd, capture_output=True, text=True)

if out_img.exists():
    print(f"  ✓ Saved snapshot to: {out_img}")
else:
    print(f"  ❌ Failed to extract frame: {res.stderr}")

print("==========================================================================")
