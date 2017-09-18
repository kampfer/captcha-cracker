# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np

# 打开图片
img_name = 'captcha/1.jpg'
img = Image.open(img_name)
w, h = img.size

# https://pillow.readthedocs.io/en/4.2.x/handbook/concepts.html#concept-modes
img = img.convert('L')

# 二值化
# http://blog.csdn.net/jia20003/article/details/8074627
imgData = list(img.getdata())
for x in range(0, w):
    for y in range(0, h):
        if imgData[w * y + x] < 25:
            img.putpixel((x,y), 0)  # 黑色
        else:
            img.putpixel((x,y), 255)    # 白色
img.show()
exit(0)

# 去噪
# 第一步采用洪水填充法去噪
# http://blog.csdn.net/jia20003/article/details/8908464
def filterPoint(data, mid_point):
    point = [mid_point]
    if (mid_point[0] != 0 and mid_point[0] != (w-1)) and (mid_point[1] != 0 and mid_point[1] != (h-1)):
        if data[w * (mid_point[1] - 1) + mid_point[0]] == 0:
            point.append(filterPoint(data, (mid_point[0], mid_point[1] - 1)))
        if data[w * mid_point[1] + mid_point[0] - 1] == 0:
            point.append(filterPoint(data, (mid_point[0] - 1, mid_point[1])))
        if data[w * (mid_point[1] + 1) + mid_point[0]] == 0:
            point.append(filterPoint(data, (mid_point[0], mid_point[1] + 1)))
        if data[w * mid_point[1] + mid_point[0] + 1] == 0:
            point.append(filterPoint(data, (mid_point[0] + 1, mid_point[1])))
    return point


point_arr = []
for x in xrange(1, w - 2):
    for y in xrange(1, h - 2):
        mid_pixel = data[w * y + x] #中央像素点像素值
        if mid_pixel == 0:
            print(x, y)
            print filterPoint(data, (x, y))
            break

# img.show()
