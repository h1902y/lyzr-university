import os
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")

print("==========================================================================")
print(" 🔍 SEARCHING FOR INDIVIDUAL LESSON TRANSCRIPT FILES")
print("==========================================================================")

sdk_tx = list((university_dir / "SDK-track" / "transcripts").glob("*.txt")) if (university_dir / "SDK-track" / "transcripts").exists() else []
studio_tx = list((university_dir / "Studio-track" / "notes").rglob("*.md")) if (university_dir / "Studio-track" / "notes").exists() else []

print(f"SDK Track Transcripts Found: {len(sdk_tx)}")
for p in sdk_tx[:5]:
    print(f"  • {p.name}")

print(f"\nStudio Track Note Files Found: {len(studio_tx)}")
for p in studio_tx[:5]:
    print(f"  • {p.name}")

print("==========================================================================")
