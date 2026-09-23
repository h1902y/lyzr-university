import subprocess
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
master_rec = university_dir / "thinkific-upload/01 Lyzr Foundations/Chapter 03 Connecting Agents with MCP Servers and Tools/master_recording.mp4"
branded_dir = university_dir / "revamp_branded"
unbranded_dir = university_dir / "revamp"
intro_bumper = university_dir / "scratch_remotion_temp/remotion_intro.mp4"
outro_bumper = university_dir / "scratch_remotion_temp/remotion_outro.mp4"

fname = "C01_CH05_L02_configuring_tavily_mcp_server.mp4"
u_path = unbranded_dir / fname
b_path = branded_dir / fname

print("==========================================================================")
print(" ✂️ SLICING & STITCHING DISTINCT C01_CH05_L02 BRANDED MP4")
print("==========================================================================")

slice_cmd = [
    "ffmpeg", "-y", "-ss", "00:02:30", "-i", str(master_rec), "-t", "00:02:31",
    "-c:v", "libx264", "-preset", "fast", "-crf", "20",
    "-c:a", "aac", "-b:a", "192k",
    str(u_path)
]
subprocess.run(slice_cmd, capture_output=True, text=True)

concat_list = university_dir / f"concat_{fname}.txt"
with open(concat_list, 'w') as f:
    f.write(f"file '{intro_bumper}'\n")
    f.write(f"file '{u_path}'\n")
    f.write(f"file '{outro_bumper}'\n")
    
stitch_cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
    "-c:v", "libx264", "-preset", "fast", "-crf", "22",
    "-c:a", "aac", "-b:a", "192k",
    str(b_path)
]
subprocess.run(stitch_cmd, capture_output=True, text=True)

b_size_mb = b_path.stat().st_size / (1024 * 1024)
print(f"  🎉 Rebranded C01_CH05_L02 created: {b_size_mb:.2f} MB")
print("==========================================================================")
