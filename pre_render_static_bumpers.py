import os
import sys
import subprocess
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
remotion_dir = university_dir / "remotion-branding"
temp_dir = university_dir / "scratch_remotion_temp"
temp_dir.mkdir(parents=True, exist_ok=True)

intro_static = temp_dir / "remotion_intro_static.mp4"
outro_static = temp_dir / "remotion_outro_static.mp4"

print("==========================================================================")
print(" 🎨 PRE-RENDERING COURSE-AGNOSTIC REMOTION INTRO & OUTRO BUMPERS")
print("==========================================================================")

# 1. Render Intro
print("Rendering 3s Agnostic Remotion Intro Bumper...")
cmd_intro = [
    "npx", "remotion", "render", "src/index.ts", "IntroBumper",
    "--props={\"title\":\"Enterprise Agent Platform\",\"subtitle\":\"Master Courses · Autonomous AI Workflows\"}",
    str(intro_static)
]
res1 = subprocess.run(cmd_intro, cwd=remotion_dir, capture_output=True, text=True)
if res1.returncode == 0 and intro_static.exists():
    print(f" ✅ Rendered Agnostic Intro: {intro_static.name} ({intro_static.stat().st_size / 1024:.1f} KB)")
else:
    print(f" ❌ Error rendering intro: {res1.stderr}")

# 2. Render Outro
print("\nRendering 5s Agnostic Remotion Outro Bumper...")
cmd_outro = [
    "npx", "remotion", "render", "src/index.ts", "OutroBumper",
    str(outro_static)
]
res2 = subprocess.run(cmd_outro, cwd=remotion_dir, capture_output=True, text=True)
if res2.returncode == 0 and outro_static.exists():
    print(f" ✅ Rendered Agnostic Outro: {outro_static.name} ({outro_static.stat().st_size / 1024:.1f} KB)")
else:
    print(f" ❌ Error rendering outro: {res2.stderr}")

print("\n🎉 Course-Agnostic Remotion Bumpers Pre-rendered Successfully!")
