#!/usr/bin/python3
# coding: utf-8
import cv2
img = cv2.imread('./sample.jpg'); print(img[10, 10])  # [28 31 39]; BGR
blue = img[10, 10, 0]; print(blue)  # 28
img[10, 10] = [255, 255, 255]; print(img[10, 10])  # [255 255 255]
##################################################################
## item(), itemset()
# Numpy is a optimized library for fast array calculations.
# So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.
print(img.item(10, 10, 2))  # 50; 必须对应于 标量, 不能获取向量
img.itemset((10, 10, 2), 100); print(img.item(10, 10, 2))  # 100
