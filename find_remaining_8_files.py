import os
import shutil

university_dir = "/Users/hkc/Documents/lyzr/university"
bulk_dir = os.path.join(university_dir, "bulk-video-upload")

missing_targets = [
    ("C02_CH01_L01_welcome_to_agent_studio_lifecycle.mp4", ["welcome"]),
    ("C02_CH01_L02_build_choose_type_and_create_agent.mp4", ["build", "choose"]),
    ("C02_CH01_L03_equip_model_tool_memory_knowledge.mp4", ["equip"]),
    ("C02_CH01_L04_what_agent_type_should_i_build.mp4", ["what agent type"]),
    ("C02_CH02_L01_lyzr_manager_orchestration.mp4", ["manager"]),
    ("C02_CH02_L02_superflow_basic_dynamic_flows.mp4", ["superflow"]),
    ("C02_CH02_L03_superflow_advanced_routing_loops.mp4", ["loops"]),
    ("C03_CH04_L02_writing_custom_local_tools.mp4", ["writing local"])
]

all_mp4s = {}
for root, dirs, files in os.walk(university_dir):
    if "bulk-video-upload" in root:
        continue
    for f in files:
        if f.endswith('.mp4'):
            all_mp4s[f.lower()] = os.path.join(root, f)

print("Searching non-bulk MP4 files:")
for target_name, keywords in missing_targets:
    matched = None
    for f_lower, f_path in all_mp4s.items():
        if any(kw in f_lower for kw in keywords):
            matched = f_path
            break
    
    if matched:
        dest_path = os.path.join(bulk_dir, target_name)
        shutil.copy(matched, dest_path)
        print(f" ✅ Copied '{target_name}' from '{os.path.relpath(matched, university_dir)}'")
    else:
        print(f" ⚠️ Could not locate MP4 for '{target_name}' with keywords {keywords}")

print(f"\nTotal MP4s present in bulk-video-upload: {len(os.listdir(bulk_dir))}")
