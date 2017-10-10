#!/usr/bin/python3
# coding: utf-8
import cv2
import numpy as np
a = cv2.imread('./sample.tiff')
print(a.shape)  # (44, 63, 3)
im_size = 12  # 44 / 12 = 3...8; 63 / 12 = 5...3; height: 44, width: 63
##################################################################
## 分块
for i in range(len(a) // im_size + 1):  # 最后余 8, 多算一层
    for j in range(len(a[0]) // im_size + 1):  # 最后余 3, 舍去; 后来又加上了, 因为 opencv 会自动舍去透明部分
        im_name = 'tmp_' + str(i) + '_' + str(j) + '.jpg'
        cv2.imwrite(im_name, a[i*im_size:i*im_size+im_size, j*im_size:j*im_size+im_size])
##################################################################
## 合并; 各种判断太麻烦了, 最好使用一行来实现
h_flag, v_flag = 0, 0
for i in range(len(a) // im_size + 1):  # 再纵向连接
    for j in range(len(a[0]) // im_size + 1):  # 先横向连接
        tmp = cv2.imread('./tmp_' + str(i) + '_' + str(j) + '.jpg')
        if h_flag == 0:
            h_stack = tmp; h_flag = 1
            continue
        h_stack = np.hstack([h_stack, tmp])
    h_flag = 0
    h_stack = np.hstack([cv2.imread('./tmp_' + str(i) + '_' + str(j) + '.jpg') for j in range(len(a[0]) // im_size + 1)])
    if v_flag == 0:
        v_stack = h_stack; v_flag = 1
        continue
    v_stack = np.vstack([v_stack, h_stack])
cv2.imwrite('tmp_new.jpg', v_stack)
##################################################################
## 合并-2, 一行, python 好厉害
for i in range(len(a) // im_size + 1):
    h_stack = np.hstack([cv2.imread('./tmp_' + str(i) + '_' + str(j) + '.jpg') for j in range(len(a[0]) // im_size + 1)])
# 上面是每一个 h_stack 的单独表达形式, 下面是 **一行实现合并**
v_stack = np.vstack([np.hstack([cv2.imread('./tmp_' + str(i) + '_' + str(j) + '.jpg') for j in range(len(a[0]) // im_size + 1)])
                     for i in range(len(a) // im_size + 1)])
cv2.imwrite('tmp_new-2.jpg', v_stack)
