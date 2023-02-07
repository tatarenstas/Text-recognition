import cv2
import PIL.Image
import pytesseract

myconfig = r'--psm 6 oem 3'

text = pytesseract.image_to_string(PIL.Image.open("test.png"), config = myconfig)
print(text)
