#!/usr/bin/python3
# coding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./sample.jpg', 0); print(img.shape)  # (128, 128); 读灰度图像进来, 准备处理成二值图像
##################################################################
## threshold(src, thresh, maxval, type[, dst]) -> retval, dst; 生成 0 和 255 的矩阵
# src: 为输入图像; thresh: 为阈值; maxval: 为输出图像的最大值;
# type: 为阈值的类型; dst: 为目标图像
# cv2.THRESH_BINARY (黑白二值)
# cv2.THRESH_BINARY_INV (黑白二值反转)
# cv2.THRESH_TRUNC  (得到的图像为多像素值)
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV
retval, img_bin = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY); print(img_bin.shape)  # (128, 128)
# 将阈值设置为 50, 阈值类型为 cv2.THRESH_BINARY, 则灰度在大于 50 的像素其值将设置为 255, 其它像素设置为 0
print(' '.join([str(item) for item in img_bin[np.nonzero(img_bin)]]))  # 满屏幕的 255
retval, img_bin = cv2.threshold(img * -1, 50, 255, cv2.THRESH_BINARY); print(img_bin.shape)  # (128, 128)
print(' '.join([str(item) for item in img_bin[np.nonzero(img_bin)]]))  # 没有输出
##################################################################
## matplotlib 画出来的可能不是 黑白的, 跟配置有关
cv2.imwrite('tmp.jpg', img_bin)
plt.imshow(img_bin); plt.show()
