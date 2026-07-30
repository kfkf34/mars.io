#REQUIRED TO RUN:
# python -m piper.download_voices en_US-lessac-high.onnx

from PIL import Image,ImageEnhance
import pytesseract
import subprocess
#import pyaudio
import wave 
from piper import PiperVoice
import cv2
import numpy as np
#from playsound import playsound
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.resize(cv2.imread("look.jpg"), None, fx=2, fy=2)
cv2.imwrite("resized_image.jpg", img)
text = Image.open("resized_image.jpg")
text.show()
print(text)
gray = text.convert("L")
gray.save("gray.jpg")
print(gray)
gray.show()
img1 =np.array(gray)
thersh =cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 11)
cv2.imwrite("thersh.jpg", thersh)
contrast = ImageEnhance.Contrast(Image.open("thersh.jpg"))
text_contrast = contrast.enhance(2)
text_contrast.save("text_contrast.jpg")
#print(pytesseract.image_to_string(text_contrast))
denoised = cv2.medianBlur(cv2.imread("text_contrast.jpg"), 3)
cv2.imwrite("denoised.jpg", denoised)

home=pytesseract.image_to_string(thersh)
print(home)
stop = ""
while stop != "stop":
    notes = input ("press here to enter note")
    stop = input ("press here to stop to end notes entry")
with open ("notes.txt","a") as f:
    f.write(notes)
with open("text.txt","w") as f:
    f.write(home)
voice = PiperVoice.load("en_US-lessac-high.onnx")
with wave.open("text.wav","wb") as f:
    voice.synthesize_wav(home,f)
#playsound("text.wav")











#python -m piper.download_voices en_US-lessac-high.onnx



















    











































































