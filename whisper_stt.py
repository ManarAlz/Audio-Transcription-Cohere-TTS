import os

# حدّد مسار ffmpeg الكامل
os.environ["PATH"] = "/opt/homebrew/bin:" + os.environ["PATH"]

import whisper

model = whisper.load_model("base")
audio_path = "assets/audio.mp3"
result = model.transcribe(audio_path, language="en")
print(result["text"])

