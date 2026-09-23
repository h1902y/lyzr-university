import subprocess
import pathlib

vpath = pathlib.Path("/Users/hkc/Documents/lyzr/university/revamp_branded/C02_CH01_L02_build_choose_type_and_create_agent.mp4")
wav_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/c02_l02_test.wav")

print("==========================================================================")
print(" 🎙️ EXTRACTING & TRANSCRIBING AUDIO FROM C02_CH01_L02 MP4 FILE")
print("==========================================================================")

cmd = ["ffmpeg", "-y", "-i", str(vpath), "-ss", "00:00:05", "-t", "30", "-ar", "16000", "-ac", "1", str(wav_path)]
subprocess.run(cmd, capture_output=True, text=True)

try:
    import whisper
    model = whisper.load_model("tiny")
    result = model.transcribe(str(wav_path))
    print(f"\n🗣️ ACTUAL SPEECH TRANSCRIPTION FROM DISK FILE:\n'{result['text'].strip()}'\n")
except Exception as e:
    print(f"  (Whisper not installed or failed: {e})")

print("==========================================================================")
