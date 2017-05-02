#!/usr/bin/python3
# coding: utf-8
# 用于执行算术运算的输入数组必须具有相同的形状或符合数组广播规则
import numpy as np
a = np.arange(9, dtype=np.float_).reshape(3,3); print(a)  # [[ 0. 1. 2.] [ 3. 4. 5.] [ 6. 7. 8.]]
b = np.array([10, 10, 10]); print(b)  # [10 10 10]
print(np.add(a, b))  # [[ 10. 11. 12.] [ 13. 14. 15.] [ 16. 17. 18.]]
print(np.subtract(a, b))  # [[-10. -9. -8.] [ -7. -6. -5.] [ -4. -3. -2.]]
print(np.multiply(a, b))  # [[ 0. 10. 20.] [ 30. 40. 50.] [ 60. 70. 80.]]
print(np.divide(a, b))  # [[ 0. 0.1 0.2] [ 0.3 0.4 0.5] [ 0.6 0.7 0.8]]
##################################################################
# numpy.reciprocal(); 此函数返回参数逐元素的倒数
# Python 处理整数除法的方式, 对于绝对值大于 1 的整数元素, 结果始终为 0,  对于整数 0, 则发出溢出警告
a = np.array([0.25, 1.33, 1, 0, 100]);  # [   0.25    1.33    1.      0.    100.  ]
print(np.reciprocal(a))  # [ 4. 0.7518797  1. inf  0.01]; RuntimeWarning: divide by zero encountered in reciprocal
b = np.array([100], dtype=int); print(b)  # [100]
print(np.reciprocal(b))  # [0]
##################################################################
# numpy.power(); 此函数将第一个输入数组中的元素作为底数, 计算它与第二个输入数组中相应元素的幂
a = np.array([10, 100, 1000]); print(a)  # [  10  100 1000]
print(np.power(a, 2))  # [100   10000 1000000]
b = np.array([1, 2, 3]); print(b)  # [1 2 3]
print(np.power(a, b))  # [10  10000 1000000000]
##################################################################
# numpy.mod(); 返回输入数组中相应元素的除法余数; 函数 numpy.remainder() 也产生相同的结果
a = np.array([10, 20, 30]); b = np.array([3, 5, 7])
print(np.mod(a, b))  # [1 0 2]
print(np.remainder(a, b))  # [1 0 2]
##################################################################
# 以下函数用于对含有复数的数组执行操作:
# numpy.real() 返回复数类型参数的实部; numpy.imag() 返回复数类型参数的虚部
# numpy.conj() 返回通过改变虚部的符号而获得的共轭复数
# numpy.angle(deg=flase) 返回复数参数的角度, degree 为 true, 返回的角度以角度制来表示, 否则为以弧度制来表示
a = np.array([-5.6j, 0.2j, 11.  , 1+1j]); print(a)  # [ 0.-5.6j 0.+0.2j 11.+0.j 1.+1.j ]
print(np.real(a))  # [ 0. 0. 11. 1.]
print(np.imag(a))  # [-5.6 0.2 0. 1. ]
print(np.conj(a))  # [ 0.+5.6j 0.-0.2j 11.-0.j 1.-1.j ]
print(np.angle(a))  # [-1.57079633 1.57079633 0. 0.78539816]
print(np.angle(a, deg=True))  # [-90. 90. 0. 45.]
