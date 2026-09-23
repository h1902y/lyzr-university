import subprocess
import pathlib

p1 = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4")
p2 = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH04_L03_build_a_knowledge_graph.mp4")

def get_dur(path):
    res = subprocess.run(["ffmpeg", "-i", str(path)], capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            return line.strip()
    return "Unknown"

print("==========================================================================")
print(f"C02_CH01_L02 (Build Choose Type): {get_dur(p1)}")
print(f"C02_CH04_L03 (Knowledge Graph):   {get_dur(p2)}")
print("==========================================================================")
