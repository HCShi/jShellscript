#!/usr/bin/python3
# coding: utf-8
import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
import cv2
a = tiff.imread('sample.tiff')
# a = cv2.imread('sample.tiff', cv2.IMREAD_UNCHANGED)  # opencv 读取的和 tiff 读取的不太一样
print(a.shape)  # (44, 63, 4) Width: 63 pixels; Height 44 pixels; 4 通道
print(a.dtype)  # uint8; 表示像素是用 8 位存储的
print(a[:2, :2, :2])  # [[[28 81] [28 81]] [[28 81] [28 81]]]; 下面将其转化为 **小数形式**
##################################################################
## 进行缩放, 同时转换为 0-1 表示
def scale_percentile(matrix):  # 缩放百分比, 可以降噪
    h, w, d = matrix.shape
    matrix = np.reshape(matrix, [h * w, d]).astype(np.int32)  # 转化为二维, 下面对 4 个通道依次找最大最小值
    # print(matrix.shape)  # (2772, 4)
    # Get 2nd and 98th percentile
    mins = np.percentile(matrix, 1, axis=0)  # 找出每个通道中的最小值
    maxs = np.percentile(matrix, 99, axis=0) - mins  # 找出每个通道中的最大值
    matrix = (matrix - mins) / maxs  # 转换为 0-1 之间, 外边的范围用 clip 删去
    matrix = np.reshape(matrix, [h, w, d])  # 转换回来
    matrix = matrix.clip(0, 1)  # 也可以将其最大最小值之外的数删去, 但是这样更方便
    return matrix
a2 = scale_percentile(a)
print(a2[:2, :2, :2])  # [[[ 0.09920635  0.12562814] [ 0.09920635  0.12562814]] [[ 0.09920635  0.12562814] [ 0.09920635  0.12562814]]]
print(a2 * 255)
print((a2 * 255).astype(int))  # 上面是小数形式, 这里转化为整形
##################################################################
## 结果对比
plt.subplot(221).imshow(a)  # 0-255 表示
plt.subplot(222).imshow(a2)  # 0-1 表示, 颜色更加深了
plt.subplot(223).imshow(a2 * 255)  # 这里加载会很难看, 用 opencv 保存, 再读入
# plt.subplot(223).imshow((a2 * 255).astype(int))  # plt.show() 会报错
plt.show()
##################################################################
## imsave;
tiff.imsave('tmp.tiff', (a2 * 255).astype(int))  # libtiff 存储文件不是很好用, 所以用 tifffile; 这个还是会错, 还是用 cv2 吧
cv2.imwrite("tmp.tiff", a2 * 255)  # 这个最好用, 会自动取整
cv2.imwrite('tmp-2.tiff', a)  # 和原来的不太一样...
tmp = tiff.imread('tmp-2.tiff')
tmp = tiff.imread('tmp.tiff')
print(tmp[:2, :2, :2])  # 用 opencv 保存过以后和上面的 a[:2, :2, :2] 不一样了..
plt.subplot(224).imshow(tmp)  # 保存再读入, 会有比较好的效果
plt.show()
##################################################################
## 总结:
# 1. plt.imshow() 可以接受两种类型的 matrix, 整形(1-2^n), 小数(0-1); 如果存在大于 1, 且为小数形式的会报错
# 2. tifffile 读取和存入 与 opencv 竟然不一样
# 3. opencv.imwrite() 更加方便
# 4. 各种图片读入以后返回的都是 numpy 的多维数组, 但是数值可能会不一样
# 5. 直接 plt.imshow(a2 * 255) 因为是小数, 所以会显示错误; 用 opencv 保存再读入, 就没事了
# 6. cv2.imread() 和 cv2.imwrite() 要配套使用才能正确保存, 中间用 plt.imshow() 会不一样, 还不知道为什么
