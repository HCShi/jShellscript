#!/usr/bin/python3
# coding: utf-8
import numpy as np
import cv2
import matplotlib.pyplot as plt
print(cv2.__version__)

# 图6-1中的矩阵
img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)

# plt.imsave('img_pyplot.jpg', img)  # 用matplotlib存储
# cv2.imwrite('img_cv2.jpg', img)  # 用OpenCV存储
