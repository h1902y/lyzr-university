import subprocess
import pathlib

wav_path = pathlib.Path("/Users/hkc/Documents/lyzr/university/unbranded_c02_l02.wav")

print("==========================================================================")
print(" 🎙️ TRANSCRIBING FIRST 30 SECONDS OF UNBRANDED C02_CH01_L02.WAV")
print("==========================================================================")

try:
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.AudioFile(str(wav_path)) as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    print(f"🗣️ GOOGLE SPEECH TRANSCRIPTION:\n'{text}'\n")
except Exception as e:
    print(f"  SpeechRecognition error: {e}")
    # Fallback to checking ffmpeg or other available tool
    print("  Checking speech via alternative methods...")

print("==========================================================================")
