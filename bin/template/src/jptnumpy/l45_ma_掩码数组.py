#!/usr/bin/python3
# coding: utf-8
# numpy.ma 模块中提供掩码数组的处理, 这个模块中几乎完整复制了 numpy 中的所有函数, 并提供掩码数组的功能
# 一个掩码数组由一个正常数组和一个布尔数组组成, 布尔数组中值为 True 的元素表示正常数组中对应下标的值无效, False 表示有效
import numpy.ma as ma
x = np.array([1, 2, 3, 5, 7, 4, 3, 2, 8, 0])
mask = x < 5
mx = ma.array(x, mask=mask)
print(mask)  # [ True, True, True, False, False, True, True, True, False, True]
print(mx)  # [-- -- -- 5 7 -- -- -- 8 --]
print(mx.filled())  # [999999 999999 999999      5      7 999999 999999 999999      8 999999]
# 掩码数组具有三个属性: data、mask、fill_value；data 表示原始数值数组, mask 表示获得掩码用的布尔数组, fill_value 表示的填充值替代无效值之后的数组, 该数组通过 filled() 方法查看
# 掩码数组可以使用各种下标对象对其进行存取, 在被掩码的部分值为 masked, 可以设置某个位置值为 ma.masked 使其失效
##################################################################
## 根据大矩阵的部分生成 mask
a = np.random.randint(0, 2, size=(4, 4)); print(a)
x_start, x_end, y_start, y_end = 2, 4, 2, 4
mt = np.ma.array(np.ones((x_end - x_start, y_end - y_start)), mask=(a[x_start:x_end, y_start:y_end] == 0))
print(mt)
