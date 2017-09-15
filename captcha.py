# -*- coding: utf-8 -*-

from PIL import Image

# 打开图片
img_name = 'captcha/1.jpg'
img = Image.open(img_name)

# 二值化
img = img.convert('L')
img = img.convert('1')

# 保存图片数据（图片数据是一维数组）
data = list(img.getdata())

# 去噪
# 第一步采用洪水填充法去噪
# http://blog.csdn.net/jia20003/article/details/8908464
w,h = img.size
black_point = 0
for x in xrange(1,w-1):
    for y in xrange(1,h-1):
        mid_pixel = data[w*y+x] #中央像素点像素值
        if mid_pixel == 0: #找出上下左右四个方向像素点像素值
            top_pixel = data[w*(y-1)+x]
            left_pixel = data[w*y+(x-1)]
            down_pixel = data[w*(y+1)+x]
            right_pixel = data[w*y+(x+1)]

            #判断上下左右的黑色像素点总个数
            if top_pixel == 1:
                black_point += 1
            if left_pixel == 1:
                black_point += 1
            if down_pixel == 1:
                black_point += 1
            if right_pixel == 1:
                black_point += 1
            if black_point >= 3:
                img.putpixel((x,y),1)
            #print black_point
            black_point = 0

img.show()
