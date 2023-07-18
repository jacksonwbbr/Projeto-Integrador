import cv2
import pytesseract
from gtts import gTTS
import os 

language = "pt"

imagem = cv2.imread("Logo-Test.png")

path = r"C:\Program Files\Tesseract-OCR"

pytesseract.pytesseract.tesseract_cmd = path + r"\tesseract.exe"
text = pytesseract.image_to_string(imagem,lang ='por')

print(text)

mytext = text

oi = gTTS(text=mytext, lang=language, slow=False)

oi.save("audio.mp3")
os.system("audio.mp3")