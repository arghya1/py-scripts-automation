#!/usr/bin/python3

# Extract text from images
# install pillow/ pytesseract

import pytesseract as tess
from PIL import Image, ImageFilter, ImageEnhance

def image_to_text(img_file):
    img = Image.open(img_file)
    img = img.filter(ImageFilter.MedianFilter())
    enh = ImageEnhance.Contrast(img)
    img = enh.enhance(2)
    img = img.convert('1')
    img.save('tmp.png')
    text = tess.image_to_string(Image.open('tmp.png'))
    return text
string = image_to_text('screenshot.png')
print(string)
