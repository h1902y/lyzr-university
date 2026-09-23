import pathlib
import subprocess

unbranded_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp/C02_CH01_L02_build_choose_type_and_create_agent.mp4")
branded_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4")
intro_bumper = pathlib.Path("/Users/hkc/Documents/lyzr/university/remotion-branding/public/intro_bumper.mp4")
outro_bumper = pathlib.Path("/Users/hkc/Documents/lyzr/university/remotion-branding/public/outro_bumper.mp4")

print("==========================================================================")
print(" 🎬 STITCHING REMOTION BUMPERS FOR C02_CH01_L02")
print("==========================================================================")

concat_list = pathlib.Path("/Users/hkc/Documents/lyzr/university/c02_l02_concat.txt")
with open(concat_list, 'w') as f:
    f.write(f"file '{intro_bumper}'\n")
    f.write(f"file '{unbranded_path}'\n")
    f.write(f"file '{outro_bumper}'\n")
    
stitch_cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
    "-c:v", "libx264", "-preset", "fast", "-crf", "22",
    "-c:a", "aac", "-b:a", "192k",
    str(branded_path)
]
subprocess.run(stitch_cmd, capture_output=True, text=True)

b_size_mb = branded_path.stat().st_size / (1024 * 1024)
print(f"  🎉 REBRANDED MP4 CREATED SUCCESSFULLY! ({b_size_mb:.2f} MB)")

def get_dur(p):
    res = subprocess.run(["ffmpeg", "-i", str(p)], capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            return line.strip()
    return "Unknown"

print(f"  ⏱️ Final Branded Duration: {get_dur(branded_path)}")

print("==========================================================================")
