#!/usr/bin/python3
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import cv2
##################################################################
## 检测稀疏图像中的非零值
img = cv2.imread('./sample.jpg')
print(' '.join([str(item) for item in img[np.nonzero(img)][:10]]))
