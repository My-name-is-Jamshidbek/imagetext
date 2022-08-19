from email.mime import image
from pytesseract import pytesseract
from PIL import Image

img = 'photo1.jpg'

img = Image.open(img)

text = pytesseract.image_to_string(img)

print(text)