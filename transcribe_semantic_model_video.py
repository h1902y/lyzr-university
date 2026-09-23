import subprocess
import pathlib

vpath = pathlib.Path("/Users/hkc/Documents/lyzr/university/thinkific-upload/1 - Tracks/Studio/11 Studio Grounding Agents in Knowledge/08a The Semantic Model.mp4")
wav_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/semantic_model_speech.wav")

print("==========================================================================")
print(" 🎙️ EXTRACTING SPEECH TRANSCRIPT FROM 08a The Semantic Model.mp4")
print("==========================================================================")

cmd = ["ffmpeg", "-y", "-i", str(vpath), "-ss", "00:00:00", "-t", "30", "-ar", "16000", "-ac", "1", str(wav_path)]
subprocess.run(cmd, capture_output=True, text=True)

# Generate image snapshot
img_path = pathlib.Path("/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/semantic_model_frame.jpg")
cmd_img = ["ffmpeg", "-y", "-ss", "00:00:15", "-i", str(vpath), "-vframes", "1", str(img_path)]
subprocess.run(cmd_img, capture_output=True, text=True)

print(f"  ✓ Extracted image snapshot: {img_path}")
print("==========================================================================")
