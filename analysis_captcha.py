# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_name = 'captcha/1.jpg'
img = mpimg.imread(img_name)
fig = plt.figure()
fig.add_subplot(121)
plt.imshow(img)
fig.add_subplot(122)
plt.hist(img.ravel(), bins=256)
plt.show()