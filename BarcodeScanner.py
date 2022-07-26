import cv2
import os
from pyzbar.pyzbar import decode

# This is just to make the terminal look clean
os.system('clear')
print("==================================================== Marker ====================================================")

picture = 'test.png'
img = cv2.imread(f'{picture}')

# This is to get all the data from the scan
code = decode(img)
print(code)

# After printing, there will be different tags to look at: from data to polygon. 
# For this project, we'll extract the barcode, which is the 'data' tag
for barcode in code:
    print(barcode.data.decode('utf-8'))
    
# Adding decode('utf-8') to extract the string

