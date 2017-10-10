#!/usr/bin/python3
# coding: utf-8
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('./sample.jpg', 1); print(img.shape)  # (128, 128, 3)
img1 = img[:, :, ::-1]  # BGR-RGB
RED = [255, 0, 0]
##################################################################
## copyMakeBorder()
# If you want to create a border around the image, something like a photo frame, you can use cv2.copyMakeBorder() function.
# But it has more applications for convolution operation, zero padding etc. This function takes following arguments:
# copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) -> dst
# src - input image
# top, bottom, left, right - border width in number of pixels in corresponding directions
# borderType - Flag defining what kind of border to be added. It can be following types:
#     cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
#     cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
#     cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
#     cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
#     cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg
# value - Color of border if border type is cv2.BORDER_CONSTANT
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE); print(replicate.shape)  # (148, 148, 3)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=RED)
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL');        plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE');  plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(reflect,'gray'),plt.title('REFLECT');        plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(reflect101,'gray'),plt.title('REFLECT_101'); plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(wrap,'gray'),plt.title('WRAP');              plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(constant,'gray'),plt.title('CONSTANT');      plt.xticks([]), plt.yticks([])
plt.show()
