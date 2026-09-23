import subprocess
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
master_rec = university_dir / "thinkific-upload/01 Lyzr Foundations/Chapter 03 Connecting Agents with MCP Servers and Tools/master_recording.mp4"
branded_dir = university_dir / "revamp_branded"
unbranded_dir = university_dir / "revamp"
intro_bumper = university_dir / "remotion-branding/public/intro_bumper.mp4"
outro_bumper = university_dir / "remotion-branding/public/outro_bumper.mp4"

print("==========================================================================")
print(" ✂️ SLICING LONGFORM RECORDING FOR C01 CHAPTER 05 LESSONS")
print("==========================================================================")

# Lesson offsets:
# L01: Intro to Tools & MCP (00:00 -> 02:30)
# L02: Configuring Tavily MCP Server (02:30 -> 05:00)
# L03: Integrating Gmail Tools (05:00 -> 07:50)

slices = [
    ("C01_CH05_L01_introduction_to_tools_and_mcp.mp4", "00:00:00", "00:02:30"),
    ("C01_CH05_L02_configuring_tavily_mcp_server.mp4", "00:02:30", "00:02:30"),
    ("C01_CH05_L03_integrating_gmail_email_tools.mp4", "00:05:00", "00:02:50")
]

for fname, start, duration in slices:
    u_path = unbranded_dir / fname
    b_path = branded_dir / fname
    
    print(f"\n✂️ Slicing {fname} (Start: {start}, Duration: {duration})...")
    slice_cmd = [
        "ffmpeg", "-y", "-ss", start, "-i", str(master_rec), "-t", duration,
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        str(u_path)
    ]
    subprocess.run(slice_cmd, capture_output=True, text=True)
    
    # Re-stitch Remotion bumpers
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
    
    u_dur = subprocess.run(["ffmpeg", "-i", str(u_path)], capture_output=True, text=True).stderr
    for line in u_dur.splitlines():
        if "Duration:" in line:
            print(f"   ✓ Unbranded Duration: {line.strip()}")
            break

print("\n==========================================================================")
print(" 🎉 C01 CHAPTER 05 SLICING & BUMPER STITCHING COMPLETED SUCCESSFULLY!")
print("==========================================================================")
