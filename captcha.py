# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image, ImageEnhance

img_name = 'captcha/1.jpg'
img = Image.open(img_name)
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)
img = img.convert('L')
data = img.getdata()
print(data)
img.show()
