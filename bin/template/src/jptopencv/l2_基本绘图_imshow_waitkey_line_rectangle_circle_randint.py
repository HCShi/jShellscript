#!/usr/bin/python3
# coding: utf-8
import numpy as np
import cv2
canvas = np.zeros((300, 300, 3), dtype="uint8")  # 300 matrixs of 300 x 3, 三维, uint8 对应灰度图像
green, red, blue, white = (0, 255, 0), (0, 0, 255), (255, 0, 0), (255,255,255)  # USE BGR standard
# line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
# img: 在img上绘图; pt1, pt2: 终点 起点 eg:(0,0); color: 线的颜色 eg:(0,255,0); thickness: 线的粗细程度 eg: -1,1,2,3 ...
cv2.line(canvas, (0, 0), (300, 300), green, 2)
cv2.imshow("Canvas", canvas)  # cv2.imshow(winname, mat)
cv2.waitKey(0)  # cv2.waitKey([delay]), The function waits for a key event infinitely when delay<= 0
# rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None); lineType=-1 表示实心; 其他和 line 相同
cv2.rectangle(canvas, (10, 10), (60, 60), green)  # 会在上一个图形的基础上接着画, 不会清空
cv2.imshow("Canvas", canvas); cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")  # 重新初始化变量 canvas (三维的矩阵)
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2) # 获取图像中心
# 画圆 1: 有规律的画圆
# circle(img, center, radius, color, thickness=None, lineType=None, shift=None); lineType=-1 will fill the circle
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("Canvas", canvas); cv2.waitKey(0)
# 画圆 2: 随机画圆
for i in range(0, 25):
    radius, color, pt = np.random.randint(5, 200), np.random.randint(0, 256, (3,)).tolist(), np.random.randint(0, 300, (2,)) # 1个[5, 200), 3个[0, 256)
    cv2.circle(canvas, tuple(pt), radius, color, -1)  # 这里 point 必须用 tuple, 上面用 tolist() 不知道为什么
cv2.imshow("Canvas", canvas); cv2.waitKey(0)
