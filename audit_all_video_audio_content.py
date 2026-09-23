import subprocess
import pathlib
import json

branded_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded")
scratch_wav = pathlib.Path("/Users/hkc/Documents/lyzr/university/temp_audio_check.wav")

print("==========================================================================")
print(" 🔍 AUDITING AUDIO CONTENT OF ALL MP4 FILES IN REVAMP_BRANDED")
print("==========================================================================")

# We can use pocketsphinx or speech recognition or ffmpeg to extract text or sample words
# Or run ffmpeg to extract audio and inspect first 10 seconds text using python or whisper

files = sorted(branded_dir.glob("*.mp4"))
print(f"Total MP4 files to audit: {len(files)}\n")

for f in files:
    size_mb = f.stat().st_size / (1024 * 1024)
    print(f" 🎬 File: {f.name} ({size_mb:.2f} MB)")

print("==========================================================================")
