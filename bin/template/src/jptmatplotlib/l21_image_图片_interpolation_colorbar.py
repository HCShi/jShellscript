#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
##################################################################
## 这里我们打印出的是纯粹的数字, 而非自然图像; 我们今天用这样 3x3 的 2D-array 来表示点的颜色, 每一个点就是一个 pixel
# 这里我们使用的是内插法中的 Nearest-neighbor 的方法, 其他的方式也都可以随意取选
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
# 三行三列的格子, a 代表每一个值, 图像右边有一个注释, 白色代表值最大的地方, 颜色越深值越小
# cmap=plt.cmap.bone, 现在, 我们可以直接用单引号传入参数; origin='lower' 代表的就是选择的原点的位置
##################################################################
## 下面我们添加一个 colorbar, 其中我们添加一个 shrink 参数, 使 colorbar 的长度变短为原来的 92%
plt.colorbar(shrink=.92)  # 右侧添加类似于颜色试纸的东西
# 省略坐标轴
plt.xticks(())
plt.yticks(())
plt.show()
