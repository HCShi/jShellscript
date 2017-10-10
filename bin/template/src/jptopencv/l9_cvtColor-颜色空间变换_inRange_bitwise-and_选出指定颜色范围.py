#!/usr/bin/python3
# coding: utf-8
import cv2, colorsys
import numpy as np
import matplotlib.pyplot as plt
##################################################################
## 先运行一遍, 查看整体效果
img = cv2.imread('./sample.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 将图片从 BGR 空间转换到 HSV 空间
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])  # 定义在 HSV 空间中蓝色的范围
mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 根据以上定义的蓝色的阈值得到蓝色的部分

lower_white = np.array([0, 0, 200])  # HSV 定义白色范围
upper_white = np.array([0, 0, 255]); print(colorsys.rgb_to_hsv(255, 255, 255))  # (0.0, 0.0, 255)
mask = cv2.inRange(hsv, lower_white, upper_white)  # 这个定义的白色范围和下面的不一样, 虽然 RGB->HSV 转换结果正确

lower_white_RGB = np.array([200, 200, 200])
upper_white_RGB = np.array([255, 255, 255])  # RGB 定义白色范围
# inRange() 根据阈值返回
mask = cv2.inRange(img, lower_white_RGB, upper_white_RGB); print(mask.shape)  # (128, 128);
print(' '.join([str(item) for item in mask[np.nonzero(mask)]]))  # 查看 mask 中的非零值; 全是 255, 说明 mask 是 二值化图像

lower_blue_RGB = np.array([13, 16, 15])
upper_blue_RGB = np.array([23, 26, 25])  # RGB 定义白色范围
mask_dark = cv2.inRange(img, lower_blue_RGB, upper_blue_RGB); print(mask.shape)  # (128, 128);
mask += mask_dark  # 两个 mask 拼接

res = cv2.bitwise_and(img, img, mask=mask)
plt.subplot(2, 2, 1).imshow(img)
plt.subplot(2, 2, 2).imshow(mask)  # 发现在 RGB 中的白色范围最好用
plt.subplot(2, 2, 3).imshow(res)
plt.show()
##################################################################
## cv2.cvtColor(input_image, flag) 函数实现图片颜色空间的转换
# flag 参数决定变换类型; 如 BGR->Gray flag 就可以设置为 cv2.COLOR_BGR2GRAY
img = cv2.imread('./sample.jpg'); print(img.shape)  # (128, 128, 3)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV); print(hsv.shape)  # (128, 128, 3); 将图片从 BGR 空间转换到 HSV 空间
print(img[0, 0], hsv[0, 0])  # [12 13 23] [  3 122  23]
print(colorsys.rgb_to_hsv(23, 13, 12))  # (0.015151515151515157, 0.4782608695652174, 23)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); print(gray.shape)  # (128, 128); 将图片从 BGR 空间转换到 HSV 空间
gray_2 = cv2.imread('./sample.jpg', 0); print(np.array_equal(gray_2, gray))  # False; ...好尴尬, 居然不一样
##################################################################
## bitwise_and(src1, src2[, dst[, mask]])
# src1 – first input array or a scalar.
# src2 – second input array or a scalar.
# src – single input array.
# value – scalar value.
# dst – output array that has the same size and type as the input arrays.
# mask – optional operation mask, 8-bit single channel array, that specifies elements of the output array to be changed.

# dst(I) = src1(I) 交 src2(I); if mask(I) != 0
