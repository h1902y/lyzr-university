import subprocess
import pathlib

p1 = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-upload/1 - Tracks/Studio/06 Studio The Agent Lifecycle/02a Build Choose Type and Create Agent.mp4")
p2 = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4")

print("==========================================================================")
print(" 🔍 INSPECTING DURATION & METADATA OF C02_CH01_L02 MP4 FILES")
print("==========================================================================")

def get_duration(path):
    if not path.exists():
        return "File not found"
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprintwrappers=1:nokey=1", str(path)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout.strip()

print(f"Raw source video ({p1.name}): Duration = {get_duration(p1)} s")
print(f"Branded video ({p2.name}): Duration = {get_duration(p2)} s")

print("==========================================================================")
