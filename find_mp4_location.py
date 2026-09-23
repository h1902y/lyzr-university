import os
import pathlib

target = "C02_CH01_L02_build_choose_type_and_create_agent.mp4"
root_dir = pathlib.Path("/Users/hkc/Documents/lyzr")

print("==========================================================================")
print(f" 🔍 SEARCHING FOR DISK LOCATION OF {target}")
print("==========================================================================")

matches = []
for p in root_dir.rglob(target):
    matches.append(p)

# Also check raw video name: 02a Build Choose Type and Create Agent.mp4
raw_target = "02a Build Choose Type and Create Agent.mp4"
for p in root_dir.rglob(raw_target):
    matches.append(p)

for m in matches:
    size_mb = m.stat().st_size / (1024 * 1024)
    print(f" 🎬 File: {m} ({size_mb:.2f} MB)")

print("==========================================================================")
