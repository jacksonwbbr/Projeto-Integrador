from gtts import gTTS
import os 

mytext = "Trabalho do projeto integrador"
language = "pt"

oi = gTTS(text=mytext, lang=language, slow=False)

oi.save("audio.mp3")
os.system("audio.mp3")