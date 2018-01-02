# -*- coding:utf-8 -*-
"""

"""
from PIL import Image
import pytesseract
im = Image.open('6.png')

#将图像转化成灰度
im = im.convert('L')

#图片降噪
def initTable(threshold=140):
 table = []
 for i in range(256):
     if i < threshold:
         table.append(0)
     else:
         table.append(1)

 return table

binaryImage = im.point(initTable(), '1')
binaryImage.show()

print(pytesseract.image_to_string(binaryImage, config= '-psm 6'))
