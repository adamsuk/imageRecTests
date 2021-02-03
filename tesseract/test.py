import pytesseract
import os
import sys

curDir = os.getcwd()
imageName = ' '.join(sys.argv[1:])
print('Processing image: {}'.format(imageName))
imageLoc = os.path.abspath(os.path.join(curDir, imageName))
print(imageLoc)

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
print(pytesseract.image_to_string(imageLoc))
