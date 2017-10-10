#!/usr/bin/python3
# coding: utf-8
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('./building.jpg', 0); print(img.shape)
laplacian = cv2.Laplacian(img, cv2.CV_64F)  # CV_32F CV_64FC1 CV_64FC2 CV_64FC3 CV_64FC4
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(3, 2, 1), plt.imshow(img); plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 2), plt.imshow(img, cmap='gray'); plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 3), plt.imshow(laplacian); plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 4), plt.imshow(laplacian, cmap='gray'); plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 5), plt.imshow(sobelx, cmap = 'gray'); plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 6), plt.imshow(sobely, cmap = 'gray'); plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
