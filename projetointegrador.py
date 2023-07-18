from gtts import gTTS
import os 

mytext = "meus amores eu não sabia tá, eu não sabia que eu tava com coviddddddddddddddd"
language = "pt"

oi = gTTS(text=mytext, lang=language, slow=False)

oi.save("audio.mp3")
os.system("audio.mp3")