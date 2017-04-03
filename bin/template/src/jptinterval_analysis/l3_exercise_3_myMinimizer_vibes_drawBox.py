#!/usr/bin/python3
# coding: utf-8
from vibes import *
from l1_exercise_2_myInterval_plus_minux_multiplication_division_exp_log_sqr_min_max import *

def drawtube(tmin, tmax, dt, color):
    t = tmin
    m = Interval(oo, oo)
    while t < tmax:
        x = Interval(t, t + dt)
        # y = sqr(x) + 2 * x - exp(x)
        # y = sqr(x)
        y = sqr(x) - 1 * x
        vibes.drawBox(x.lb, x.ub, y.lb, y.ub, color)
        t = t + dt
        m = mini(m, y)  # 找到曲线上的最小值 (x.lb, x.ub)
    return m

if __name__ == '__main__':
    vibes.beginDrawing()
    vibes.newFigure('my minimizer')
    vibes.setFigureProperties({'x':0, 'y':0, 'width':1600, 'height':1000})  # 控制窗口的位置和大小
    tmp = drawtube(0, 1, 1, '[cyan]')
    print('tmp =', tmp)
    m1 = drawtube(-2, 2, 0.5, '[blue]')  # 第三个参数是步长
    print('m1 =', m1)
    m2 = drawtube(-2, 2, 0.05, '[yellow]')
    print('m2 =', m2)
    m3 = drawtube(-2, 2, 0.005, '[red]')
    print('m3 =', m3)
    m4 = drawtube(-2, 2, 0.0005, '[green]')  # 一层层的嵌套, 误差越来越小
    print('m4 =', m4)
    vibes.endDrawing()
