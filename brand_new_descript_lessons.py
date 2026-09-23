import os
import sys
import subprocess
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
scratch_dir = university_dir / "scratch_descript"
branded_dir = university_dir / "revamp_branded"
thumbnails_dir = university_dir / "revamp" / "thumbnails"

branded_dir.mkdir(parents=True, exist_ok=True)
thumbnails_dir.mkdir(parents=True, exist_ok=True)

intro_mp4 = university_dir / "remotion-branding" / "out" / "PremiumBrandIntro.mp4"
outro_mp4 = university_dir / "remotion-branding" / "out" / "PremiumBrandOutro.mp4"

print("==========================================================================")
print(" 🎬 BRANDING NEW DESCRIPT LESSON VIDEOS WITH REMOTION BUMPERS")
print("==========================================================================")

def get_dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)], capture_output=True, text=True).stdout.strip())

dur_intro = get_dur(intro_mp4)
dur_outro = get_dur(outro_mp4)

new_lessons = [
    {
        "slug": "C01_CH01_L04_lyzr_platform_pricing",
        "title": "Foundation C1 L4 | Lyzr Platform Pricing & Token Economics",
        "input": scratch_dir / "pricing.mp4",
        "output": branded_dir / "C01_CH01_L04_lyzr_platform_pricing.mp4"
    },
    {
        "slug": "C03_CH04_L03_gitagent_harness",
        "title": "Technical C4 L3 | GitAgent Harness: Repo as Source of Truth",
        "input": scratch_dir / "gitagent_harness.mp4",
        "output": branded_dir / "C03_CH04_L03_gitagent_harness.mp4"
    }
]

for item in new_lessons:
    inp = item['input']
    out = item['output']
    title = item['title']

    if not inp.exists():
        print(f"❌ Input video missing: {inp}")
        continue

    print(f"\nStitching '{title}'...")
    dur_lesson = get_dur(inp)
    o1 = dur_intro - 1.0
    o2 = (dur_intro + dur_lesson - 1.0) - 1.0

    cmd = [
        "ffmpeg", "-y",
        "-i", str(intro_mp4),
        "-i", str(inp),
        "-i", str(outro_mp4),
        "-filter_complex", (
            f"[0:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p[v0];"
            f"[1:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p[v1];"
            f"[2:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p[v2];"
            f"[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];"
            f"[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];"
            f"[2:a]aformat=sample_rates=44100:channel_layouts=stereo[a2];"
            f"[v0][v1]xfade=transition=fade:duration=1.0:offset={o1}[v01];"
            f"[v01][v2]xfade=transition=fade:duration=1.0:offset={o2}[v];"
            f"[a0][a1]acrossfade=d=1.0[a01];"
            f"[a01][a2]acrossfade=d=1.0[a]"
        ),
        "-map", "[v]",
        "-map", "[a]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
        str(out)
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and out.exists():
        size_mb = out.stat().st_size / (1024 * 1024)
        print(f"  🎉 SUCCESS! Rendered: {out.name} ({size_mb:.2f} MB)")
    else:
        print(f"  ❌ Error stitching video: {res.stderr[:300]}")

print("\n==========================================================================")
print(" 🎉 NEW LESSON VIDEOS BRANDED SUCCESSFULLY!")
print("==========================================================================")
