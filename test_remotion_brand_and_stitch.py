import os
import sys
import subprocess
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
remotion_dir = university_dir / "remotion-branding"
revamp_dir = university_dir / "revamp"
output_dir = university_dir / "revamp_branded"
output_dir.mkdir(parents=True, exist_ok=True)

print("==========================================================================")
print(" 🚀 TESTING REMOTION REACT VIDEO BRANDING & STITCHING PIPELINE")
print("==========================================================================")

input_video = revamp_dir / "C01_CH01_L01_introduction_to_lyzr_platform.mp4"
output_video = output_dir / "C01_CH01_L01_introduction_to_lyzr_platform.mp4"

stitch_script = pathlib.Path("/Users/hkc/Documents/lyzr/.agents/skills/remotion/scripts/brand_and_stitch.py")

cmd = [
    "python3", str(stitch_script),
    "--input", str(input_video),
    "--title", "Introduction to Lyzr Platform",
    "--subtitle", "Lyzr Foundations · Master Course",
    "--template", "vox",
    "--output", str(output_video)
]

print(f"Executing: {' '.join(cmd)}\n")
res = subprocess.run(cmd, text=True)

if res.returncode == 0 and output_video.exists():
    print(f"\n🎉 REMOTION BRANDED VIDEO CREATED SUCCESSFULLY!")
    print(f"   📁 Branded File: {output_video}")
    print(f"   MB Size:       {output_video.stat().st_size / (1024*1024):.2f} MB")
else:
    print(f"\n❌ Error building Remotion branded video.")
