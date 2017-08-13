#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
import matplotlib.pyplot as plt
##################################################################
## sklearn digits.images 很多二维数组
digits = datasets.load_digits()  # Load the digits dataset
print(digits)
print(digits.images.shape)  # (1797, 8, 8)
# Display the first digit
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.axis('off')  # 不加坐标系更干净一点
plt.show()
##################################################################
## Scipy misc.face() 一个三维数组, MxNx3
import scipy.misc
face = scipy.misc.face()
print(face.shape)  # (768, 1024, 3)
print(face.max())  # 255; 表示 0-255 的颜色值
print(face.dtype)  # dtype('uint8')
plt.gray()
plt.imshow(face)
plt.show()
##################################################################
## 总结:
# 1. imshow() 既可以是 MxN 为参数, 也可以是 MxNx3 为参数
# 2. plt.gray() 可以将默认的 colormap=None 设置为 gray
