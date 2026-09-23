import os
import sys
import json
import subprocess
import pathlib
from concurrent.futures import ThreadPoolExecutor

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
revamp_dir = university_dir / "revamp"
branded_dir = university_dir / "revamp_branded"
json_path = university_dir / "revamp_upload_plan.json"

branded_dir.mkdir(parents=True, exist_ok=True)

intro_mp4 = university_dir / "remotion-branding" / "out" / "PremiumBrandIntro.mp4"
outro_mp4 = university_dir / "remotion-branding" / "out" / "PremiumBrandOutro.mp4"

print("==========================================================================")
print(" 🎬 FAST MULTI-THREADED REMOTION BRANDING & STITCHING FOR ALL 49 VIDEOS")
print("==========================================================================")

def get_duration(mp4_path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(mp4_path)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return float(res.stdout.strip())

dur_intro = get_duration(intro_mp4)
dur_outro = get_duration(outro_mp4)

plan_data = json.load(open(json_path))

def process_single_video(item):
    filename = item['filename']
    input_video = revamp_dir / filename
    output_video = branded_dir / filename

    if not input_video.exists():
        return (item['index'], filename, False, "Input file missing")

    try:
        dur_lesson = get_duration(input_video)
        offset1 = dur_intro - 1.0
        offset2 = (dur_intro + dur_lesson - 1.0) - 1.0

        cmd = [
            "ffmpeg", "-y",
            "-i", str(intro_mp4),
            "-i", str(input_video),
            "-i", str(outro_mp4),
            "-filter_complex", (
                f"[0:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p[v0];"
                f"[1:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p[v1];"
                f"[2:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p[v2];"
                f"[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];"
                f"[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];"
                f"[2:a]aformat=sample_rates=44100:channel_layouts=stereo[a2];"
                f"[v0][v1]xfade=transition=fade:duration=1.0:offset={offset1}[v01];"
                f"[v01][v2]xfade=transition=fade:duration=1.0:offset={offset2}[v];"
                f"[a0][a1]acrossfade=d=1.0[a01];"
                f"[a01][a2]acrossfade=d=1.0[a]"
            ),
            "-map", "[v]",
            "-map", "[a]",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
            str(output_video)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and output_video.exists():
            size_mb = output_video.stat().st_size / (1024 * 1024)
            return (item['index'], filename, True, f"{size_mb:.2f} MB")
        else:
            return (item['index'], filename, False, res.stderr[:200])
    except Exception as e:
        return (item['index'], filename, False, str(e))

print(f"Stitching {len(plan_data)} videos concurrently using pre-rendered Remotion Bumpers...\n")

# Use ThreadPoolExecutor for concurrent FFmpeg processing (4 workers)
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process_single_video, plan_data))

success_count = 0
for idx, fname, success, msg in results:
    if success:
        print(f"  ✓ [{idx:02d}/49] Branded & Stitched: {fname} ({msg})")
        success_count += 1
    else:
        print(f"  ❌ [{idx:02d}/49] Error on {fname}: {msg}")

# Update plan JSON to point to revamp_branded/
for item in plan_data:
    b_path = branded_dir / item['filename']
    if b_path.exists():
        item['filepath'] = str(b_path)

with open(json_path, 'w', encoding='utf-8') as jf:
    json.dump(plan_data, jf, indent=2)

print("\n==========================================================================")
print(f" 🎉 COMPLETED REMOTION BRANDING FOR {success_count}/49 VIDEOS!")
print(f"    Branded Output Folder: {branded_dir}")
print(f"    Updated Upload Plan:   {json_path}")
print("==========================================================================")
