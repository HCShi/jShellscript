#!/usr/bin/python3
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
img = np.zeros((512, 512, 3), np.uint8)  # 创建一张黑色图像, 不过是三通道的
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 270, (255, 255, 0), -1)
# 画多边形, n 个顶点坐标要给出来, 数组形状 (n,1,2), 类型必须是 int32 的
pts = np.array([[20, 10], [60, 120], [120, 60], [80, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255), 2)
# 在图片上放置文字, 要指定字体
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)
plt.imshow(img, cmap='gray')
plt.show()
# 下面三句在 Ubuntu 上执行不了
# cv2.imshow('draw', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
