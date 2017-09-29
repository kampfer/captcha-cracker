# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
# import cv2

def binaryImage(img, threshold):
    w, h = img.size
    img = img.convert('L')
    imgData = list(img.getdata())
    for x in range(0, w):
        for y in range(0, h):
            if imgData[w * y + x] < threshold:
                img.putpixel((x, y), 0)  # 黑色
            else:
                img.putpixel((x, y), 255)  # 白色
    return img

img_name = 'captcha/1.jpg'
img = Image.open(img_name)
img = img.convert('L')

fig = plt.figure()
ax = fig.add_subplot(111)
# 检查直方图，发现二值化的阀值可以设置为30
ax.hist(list(img.getdata()), bins=256)
plt.show()

img = binaryImage(img, 30)
w, h = img.size
hValues = np.zeros(w)
vValues = np.zeros(h)
imgData = list(img.getdata())
for x in range(w):
    for y in range(h):
        if imgData[w * y + x] == 0:
            hValues[x] += 1
            vValues[y] += 1

print(w,h)
fig = plt.figure()
ax = fig.add_subplot(121)
ax.hist(hValues, bins=w)
ax = fig.add_subplot(122)
ax.hist(vValues, bins=h)
plt.show()
