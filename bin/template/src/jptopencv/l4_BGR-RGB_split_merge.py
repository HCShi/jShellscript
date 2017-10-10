#!/usr/bin/python3
# coding: utf-8
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('./sample.jpg'); print(img.shape)  # (128, 128, 3)
cv2.imshow('image', img)  # Ubuntu 不支持 imshow(), 还是用 plt.show()
##################################################################
## 拆分通道, 逆序合并; OpenCV 里边彩色顺序是 BGR, 但是 Matplotlib 是 RGB 顺序
# 方法一:
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.subplot(221).imshow(img)   # expects distorted color
plt.subplot(222).imshow(img2)  # expect true color
# cv2.split() is a costly operation (in terms of time), so only use it if necessary.
# Numpy indexing is much more efficient and should be used if possible.
# 方法二: 或者用一行解决
plt.subplot(223).imshow(img[:, :, ::-1])  # BGR-RGB, 速度更快
plt.show()
