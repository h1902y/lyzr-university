import os
import sys
import subprocess
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
downloads_video = pathlib.Path("/Users/hkc/Downloads/lyzr-adk-track-launch_2.mp4")
outro_video = university_dir / "scratch_remotion_temp" / "remotion_outro_static.mp4"
input_video = university_dir / "revamp" / "C01_CH01_L01_introduction_to_lyzr_platform.mp4"
output_video = university_dir / "revamp_branded" / "C01_CH01_L01_introduction_to_lyzr_platform.mp4"
output_video.parent.mkdir(parents=True, exist_ok=True)

print("==========================================================================")
print(" 🎥 STITCHING SAMPLE VIDEO WITH PREMIUM HIGH-PRODUCTION INTRO BUMPER")
print("==========================================================================")

def get_dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)], capture_output=True, text=True).stdout.strip())

d0 = get_dur(downloads_video)
d1 = get_dur(input_video)
d2 = get_dur(outro_video)

o1 = d0 - 1.0
o2 = (d0 + d1 - 1.0) - 1.0

print(f"Intro: {d0:.2f}s | Lesson: {d1:.2f}s | Outro: {d2:.2f}s")

cmd = [
    'ffmpeg', '-y',
    '-i', str(downloads_video),
    '-i', str(input_video),
    '-i', str(outro_video),
    '-filter_complex', (
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
    '-map', '[v]', '-map', '[a]',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac',
    str(output_video)
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and output_video.exists():
    size_mb = output_video.stat().st_size / (1024 * 1024)
    print(f"\n🎉 SUCCESS! Generated Branded Video with Premium Intro: {output_video.name} ({size_mb:.2f} MB)")
else:
    print(f"\n❌ Error stitching video: {res.stderr}")
