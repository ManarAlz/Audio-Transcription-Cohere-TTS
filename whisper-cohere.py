import os
os.environ["PATH"] = "/opt/homebrew/bin:" + os.environ["PATH"]
import whisper
import cohere
from gtts import gTTS
import os

# مفاتيح Cohere
COHERE_API_KEY = "CMMjgh15Yellyy7jnK2299L0o6zzVrviHSIc9OEu"

# تحميل نموذج Whisper
model = whisper.load_model("base")

# تحديد الملف الصوتي
audio_path = "/Users/manar/Desktop/AudioProject/assets/audio.mp3"


# تحويل الصوت إلى نص
print("Transcribing with Whisper...")
result = model.transcribe(audio_path, language="en")
transcription = result["text"]
print("Whisper transcription:", transcription)

# إرسال النص إلى Cohere
co = cohere.Client(COHERE_API_KEY)

response = co.generate(
    model='command',
    prompt=transcription,
    max_tokens=100,
    temperature=0.7
)

reply = response.generations[0].text.strip()
print("Cohere reply:", reply)

# تحويل الرد إلى صوت باستخدام gTTS
tts = gTTS(text=reply, lang='en')
tts.save("response.mp3")

# تشغيل الصوت باستخدام afplay على macOS
os.system("afplay response.mp3")
