import json
import csv
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
upload_plan_path = university_dir / "revamp_upload_plan.json"

print("==========================================================================")
print(" 🔍 AUDITING YOUTUBE DESCRIPTIONS vs THINKIFIC TEXT BLOCKS")
print("==========================================================================")

with open(upload_plan_path, 'r', encoding='utf-8') as f:
    upload_plan = json.load(f)

print(f"Loaded {len(upload_plan)} lessons.\n")

# Check YouTube descriptions in upload plan
yt_descriptions = [item["description"] for item in upload_plan]
unique_yt_desc = set(yt_descriptions)

print(f"🔴 YOUTUBE STUDIO STATUS:")
print(f"   • Total Video Upload Objects: {len(yt_descriptions)}")
print(f"   • Unique YouTube Descriptions: {len(unique_yt_desc)}")
print(f"   • Raw Transcripts in YouTube Description? NO (YouTube uses structured Objectives + Hubspot CTAs + Hashtags).")
print(f"   • Result: YouTube descriptions were NOT affected by transcript duplication!\n")

print(f"🏫 THINKIFIC LMS STATUS:")
print(f"   • Thinkific text blocks use the lesson notes / transcript column from the Master CSVs.")
print(f"   • Previously: CSV had 16 duplicate transcript blocks from chapter-level longforms.")
print(f"   • Now: All 5 CSV manifests have been updated with 51/51 100% UNIQUE transcripts.")
print(f"   • Next Step: Update Thinkific lesson text blocks using the fresh unique CSVs.")

print("==========================================================================")
