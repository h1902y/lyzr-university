import subprocess
import pathlib

unbranded_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp/C02_CH01_L02_build_choose_type_and_create_agent.mp4")
branded_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4")

print("==========================================================================")
print(" 🔍 COMPARING UNBRANDED vs BRANDED C02_CH01_L02 MP4 FILES")
print("==========================================================================")

def get_duration(p):
    cmd = ["ffmpeg", "-i", str(p)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            return line.strip()
    return "Unknown"

print(f"Unbranded ({unbranded_path.name}): Size = {unbranded_path.stat().st_size / (1024*1024):.2f} MB | {get_duration(unbranded_path)}")
print(f"Branded   ({branded_path.name}):   Size = {branded_path.stat().st_size / (1024*1024):.2f} MB | {get_duration(branded_path)}")

# Extract 10-second audio clip from unbranded to test
wav_out = pathlib.Path("/Users/hkc/Documents/lyzr/university/unbranded_c02_l02.wav")
cmd = ["ffmpeg", "-y", "-i", str(unbranded_path), "-ss", "00:00:05", "-t", "30", "-ar", "16000", "-ac", "1", str(wav_out)]
subprocess.run(cmd, capture_output=True, text=True)

print("\n==========================================================================")
