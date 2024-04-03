from gtts import gTTS
import os
tts = gTTS(text="salam", lang='en')
tts.save("out.mp3")
os.system("out.mp3")
