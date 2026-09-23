import os
import sys
import json

university_dir = "/Users/hkc/Documents/lyzr/university"
json_path = os.path.join(university_dir, "revamp_upload_plan.json")

print("==========================================================================")
print(" 🔍 AUDITING YOUTUBE UPLOAD STATUS FOR LYZR FOUNDATIONS")
print("==========================================================================")

plan_data = json.load(open(json_path))

completed = [
    ("Video 1", "Foundation C1 L1 | Introduction to Lyzr Platform", "C01_CH01_L01_introduction_to_lyzr_platform.mp4"),
    ("Video 2", "Foundation C1 L2 | Client Success Stories", "C01_CH01_L02_client_success_stories.mp4"),
    ("Video 3", "Foundation C1 L3 | The Lyzr Stack and Architecture", "C01_CH01_L03_the_lyzr_stack_and_architecture.mp4")
]

print("✅ ALREADY COMPLETED (Videos 1 to 3):")
for num, title, fname in completed:
    print(f" • {num}: {title} ({fname})")

remaining_foundations = plan_data[3:15]

print(f"\n🚀 REMAINING TO UPLOAD IN LYZR FOUNDATIONS (Videos 4 to 15, Total: {len(remaining_foundations)}):")
for item in remaining_foundations:
    print(f" • Video #{item['index']}: {item['title']} ({item['filename']})")
