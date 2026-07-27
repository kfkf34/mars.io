from PIL import Image,ImageEnhance
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = Image.open("text on a book.webp")
text.show()
print(text)
gray = text.convert("L")
gray.save("gray.webp")
print(gray)
gray.show()
contrast = ImageEnhance.Contrast(gray)
text_contrast = contrast.enhance(2)
text_contrast.save("text_contrast.webp")
#print(pytesseract.image_to_string(text_contrast))
home=pytesseract.image_to_string(text_contrast)













































































