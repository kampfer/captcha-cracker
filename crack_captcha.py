# -*- coding: utf-8 -*-

from PIL import Image
import math
import numpy as np

# 打开图片
img_name = 'captcha/1.jpg'
img = Image.open(img_name)
w, h = img.size

# 二值化
# https://pillow.readthedocs.io/en/4.2.x/handbook/concepts.html#concept-modes
# http://blog.csdn.net/jia20003/article/details/8074627
img = img.convert('L')
imgData = list(img.getdata())
for x in range(0, w):
    for y in range(0, h):
        if imgData[w * y + x] < 25:
            img.putpixel((x, y), 0)  # 黑色
        else:
            img.putpixel((x, y), 255)    # 白色

# 采用洪水填充法去噪
# http://blog.csdn.net/jia20003/article/details/8908464
def getPointValue(data, point):
    i = w * point[1] + point[0]
    if (i >= 0) and (i < len(data)):
        return data[i]

def floodFilter(data, origin, filterMap):
    filterMap.append(origin)
    ret = [origin]

    topLeft = (origin[0] - 1, origin[1] - 1)
    top = (origin[0], origin[1] - 1)
    topRight = (origin[0] + 1, origin[1] - 1)
    right = (origin[0] + 1, origin[1])
    bottomRight = (origin[0] + 1, origin[1] + 1)
    bottom = (origin[0], origin[1] + 1)
    bottomLeft = (origin[0] - 1, origin[1] + 1)
    left = (origin[0] - 1, origin[1])

    for p in [topLeft, top, topRight, right, bottomRight, bottom, bottomLeft, left]:
        if (p not in filterMap) and (getPointValue(data, p) == 0):
            ret.extend(floodFilter(data, p, filterMap))

    return ret

imgData = list(img.getdata())
ps = []
for y in xrange(1, h):
    for x in xrange(1, w):
        if (x, y) not in ps:
            mid_pixel = imgData[w * y + x] #中央像素点像素值
            if mid_pixel == 0:
                pp = floodFilter(imgData, (x, y), ps)
                print '>>>>', len(pp), pp
                if len(pp) < 10:
                    for p in pp:
                        img.putpixel(p, 255)

img.show()