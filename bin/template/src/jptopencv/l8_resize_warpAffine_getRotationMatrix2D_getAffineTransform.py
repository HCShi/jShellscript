#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import cv2
import numpy as np
##################################################################
## resize() 缩放图像
img = cv2.imread('./sample.jpg'); print(img.shape)  # (128, 128, 3)
height, width = img.shape[:2]
res = cv2.resize(img, (width // 2, height // 2), interpolation = cv2.INTER_CUBIC); print(res.shape)  # (64, 64, 3); 要反过来写...
plt.subplot(121).imshow(img)
plt.subplot(122).imshow(res)
plt.show()
##################################################################
## warpAffine() 图像平移, 旋转, 放射; 区别是构造 M 矩阵
##################################################################
# 平移
img = cv2.imread('./sample.jpg', 0); rows, cols = img.shape; print(img.shape)  # (128, 128)
M = np.float32([[1, 0, 10], [0, 1, 20]])  # 1, 0 向右偏移, 0, 1 向下偏移
dst = cv2.warpAffine(img, M, (cols, rows))  # (src, M, dsize)
plt.subplot(121).imshow(img); plt.subplot(122).imshow(dst); plt.show()
##################################################################
# getRotationMatrix2D(center, angle, scale) 图像旋转
img = cv2.imread('./sample.jpg', 0); rows, cols = img.shape; print(img.shape)  # (128, 128)
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)  # 中心点, 90 度顺时针, 大小不变
dst = cv2.warpAffine(img, M, (cols, rows))
plt.subplot(121).imshow(img); plt.subplot(122).imshow(dst); plt.show()
##################################################################
# getAffineTransform(src, dst) 仿射变换
img = cv2.imread('./sample.jpg'); rows, cols, ch = img.shape; print(img.shape)  # (128, 128, 3)
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121).imshow(img); plt.subplot(122).imshow(dst); plt.show()
