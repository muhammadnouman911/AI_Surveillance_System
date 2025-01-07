import pytesseract
from PIL import Image

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load and OCR the test image
image = Image.open('test_image.png')
text = pytesseract.image_to_string(image, config='--psm 6')
print("Extracted Text:", text)
