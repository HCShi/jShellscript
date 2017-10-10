#!/usr/bin/python3
# coding: utf-8
import cv2
import numpy as np
##################################################################
## imread()
# Second argument is a flag which specifies the way image should be read.
#     cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
#     cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
#     cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
#     Note Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
a = cv2.imread('./sample.jpg', 0); print(a.shape)  # (128, 128)
a = cv2.imread('./sample.jpg', 1); print(a.shape)  # (128, 128, 3)
a = cv2.imread('./sample.jpg', -1); print(a.shape)  # (128, 128, 3)
a = cv2.imread('./sample.tiff'); print(a.shape)  # (44, 63, 3); default is 1
print(a[:, -1])  # 全为 0, 因为是透明区域
##################################################################
## imwrite()
cv2.imwrite('tmp-1.tiff', a)            # 自动删去空白区域(边缘全为 0); 原图右边有透明图区, 现在没有了
cv2.imwrite('tmp-1.jpg', a)             # 保存成不同类型的文件
cv2.imwrite('tmp-2.tiff', a * 12)       # 会自动执行 ceil() 操作, 放到 dtype 一般是 0-255 范围内
cv2.imwrite('tmp-3.tiff', a * 1.2)      # 自动取整
cv2.imwrite('tmp-4.jpg', a * -10)       # 复数会自动变为 0
print(cv2.imread('./tmp-4.jpg').max())  # 0
cv2.imwrite('tmp-5.jpg', a[:, :, 1] )   # 会自动将 1 维变为 3 维
print(cv2.imread('./tmp-5.jpg').shape)  # (44, 63, 3)

# imwrite() 保存二值图像是个坑...
mask = cv2.inRange(a, np.array([200, 200, 200]), np.array([255, 255, 255])); print(mask.shape)  # (44, 63)
print(mask[np.nonzero(mask)])  # 都是 255
cv2.imwrite('tmp-6.jpg', mask)
tmp = cv2.imread('tmp-6.jpg'); print(' '.join(str(item) for item in tmp[np.nonzero(tmp)]))  # 居然出现了 (0, 255) 之间的数...
tmp = cv2.imread('tmp-6.jpg', 0); print(' '.join(str(item) for item in tmp[np.nonzero(tmp)]))  # 还是会出现
# 解决办法是 使用二值化
retval, tmp_bin = cv2.threshold(tmp, 50, 255, cv2.THRESH_BINARY); print(tmp_bin.shape)  # (44, 63)
print(' '.join(str(item) for item in tmp_bin[np.nonzero(tmp_bin)]))  # 全部都是 255
##################################################################
## 总结:
# cv2.imwrite() 必须是整数矩阵, plt.imshow() 可以支持 0-1 小数型 和 0-255 整数型两种
