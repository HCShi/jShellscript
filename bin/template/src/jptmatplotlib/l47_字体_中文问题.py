#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
print(matplotlib.matplotlib_fname())  # 将会获得 matplotlib 包所在文件夹
# 然后执行下面的操作
# sudo cp msyh.ttf /usr/share/fonts/
# cp msyh.ttf ~/anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf
# cd ~/anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data
# vim matplotlibrc  # 删除 font.family 和 font.sans-serif 两行前的 #, 并在 font.sans-serif 后添加中文字体 Microsoft YaHei, ...(其余不变)
# rm -rf ~/.cache/matplotlib/*
##################################################################
## 打印出可用的字体
## 系统可用中文字体
import subprocess
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
print( '*' * 10, '系统可用的中文字体', '*' * 10)
print(output)  # 编码有问题
zh_fonts = set(f.split(',', 1)[0] for f in output.decode('utf-8').split('\n'))
print(zh_fonts)

## matplotlib 可用所有字体
from matplotlib import font_manager
mat_fonts = set(f.name for f in font_manager.FontManager().ttflist)
available = mat_fonts & zh_fonts
print ('*' * 10, '可用的字体', '*' * 10)
for f in available: print (f)

## 另一种方法获得 matplotlib 可用所有字体
import pandas as pd
fonts = font_manager.findSystemFonts()
l = []
for f in fonts:
    try:
        font = matplotlib.font_manager.FontProperties(fname=f)
        l.append((f, font.get_name(), font.get_family(), font.get_weight()))
    except: pass
df = pd.DataFrame(l, columns=['path', 'name', 'family', 'weight'])
print(df)  # 我的电脑竟然有近 500 个字体
##################################################################
## 测试
x = np.arange(1, 11); y =  2 * x +  5
plt.plot(x, y, "ob"); plt.title("你好")
plt.show()
