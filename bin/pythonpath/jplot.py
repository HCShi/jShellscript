#!/usr/bin/python3
# coding: utf-8
# 使用方法:
# import jplot
# jplot.xy_axis_center()

import matplotlib.pyplot as plt

def xy_axis_center():
    """X轴 和 Y轴, 设置居中"""
    jplot_ax = plt.gca()
    jplot_ax.spines['right'].set_color('none')
    jplot_ax.spines['top'].set_color('none')
    jplot_ax.xaxis.set_ticks_position('bottom')
    jplot_ax.spines['bottom'].set_position(('data', 0))
    jplot_ax.yaxis.set_ticks_position('left')
    jplot_ax.spines['left'].set_position(('data', 0))
