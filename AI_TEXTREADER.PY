from PIL import Image,ImageEnhance
import pytesseract
import subprocess
import pyaudio
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = Image.open("red.jpg")
text.show()
print(text)
gray = text.convert("L")
gray.save("gray.jpg")
print(gray)
gray.show()
contrast = ImageEnhance.Contrast(gray)
text_contrast = contrast.enhance(2)
text_contrast.save("text_contrast.jpg")
#print(pytesseract.image_to_string(text_contrast))
home=pytesseract.image_to_string(text_contrast)
print(home)
with open("text.txt","w") as f:
    f.write(home)











































































