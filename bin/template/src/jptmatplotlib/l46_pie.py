#!/usr/bin/python3
# coding: utf-8
from matplotlib import pyplot as plt
##################################################################
## 简单的画图
sizes = [60, 30, 10]              # 每个标签占多大, 会自动去算百分比
plt.subplot(2, 2, 1); plt.pie(sizes)
##################################################################
## 英文频率分布
data = [('in', '81300'), ('book', '57628'), ('dear', '56754'), ('li', '56294'), ('as', '53288')]
labels, size = zip(*data)
plt.subplot(2, 2, 2); plt.pie(size, labels=labels); plt.legend()
##################################################################
## 样式更加复杂
labels = ['one', 'two', 'three']  # 定义饼状图的标签, 标签是列表; 不支持中文
colors = ['red', 'yellowgreen', 'lightskyblue']
explode = (0.05, 0, 0)            # 将某部分爆炸出来, 使用括号, 将第一块分割出来, 数值的大小是分割出来的与其他两块的间隙
plt.subplot(2, 2, 3)
patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                startangle=90, pctdistance=0.6)
# labeldistance, 文本的位置离远点有多远,  1.1 指 1.1 倍半径的位置
# autopct, 圆里面的文本格式, %3.1f%%表示小数有三位, 整数有一位的浮点数
# shadow, 饼是否有阴影
# startangle, 起始角度,  0 , 表示从 0 开始逆时针转, 为第一块。一般选择从 90 度开始比较好看
# pctdistance, 百分比的 text 离圆心的距离
# patches, l_texts, p_texts, 为了得到饼图的返回值, p_texts 饼图内部文本的, l_texts 饼图外 label 的文本
##################################################################
## 改变文本的大小: 把每一个 text 遍历, 调用 set_size 方法设置它的属性
for t in l_text: t.set_size=(30)
for t in p_text: t.set_size=(20)
# 设置 x ,  y 轴刻度一致, 这样饼图才能是圆的
plt.axis('equal'); plt.legend()
plt.show()
