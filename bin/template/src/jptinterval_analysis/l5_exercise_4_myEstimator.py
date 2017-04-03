#!/usr/bin/python3
# coding: utf-8
from vibes import *
from l4_exercise_4_myBox import *

def test(P):
    b = Interval(0, 0)
    for i in range(len(Y)):  # len(Y) == 4
        ti, Yi= T[i], Y[i]
        Fi = P.x * exp(ti * P.y)  # bounded-error: p1 * e ^ (p2 * t)
        if subset(Fi, Yi):  # 子集
            b.lb = b.lb + 1
        if not(disjoint(Fi, Yi)):  # 没有交集
            b.ub = b.ub + 1
    return b

def sivia(P):
    vibes.selectFigure('P')
    b = test(P)
    q = 0  # 很重要的一个控制变量, 要研究一下
    if b.ub < len(Y) - q:
        vibes.drawBox(P.x.lb, P.x.ub, P.y.lb, P.y.ub, '[cyan]')
    elif b.lb >= len(Y) - q:
        vibes.drawBox(P.x.lb, P.x.ub, P.y.lb, P.y.ub, '[red]')
    elif P.width() < 0.01:
        vibes.drawBox(P.x.lb, P.x.ub, P.y.lb, P.y.ub, 'yellow[yellow]')
        DrawOuput(P)
    else:
        sivia(P.left())
        sivia(P.right())
def DrawOuput(P):
    t, dt = 0, 0.05
    vibes.selectFigure('Y')
    while t < 5:
        T = Interval(t, t + dt)
        y = P.x * exp(T * P.y)
        vibes.drawBox(T.lb, T.ub, y.lb, y.ub, 'green[green]')
        t = t + dt
if __name__ == '__main__':
    vibes.beginDrawing()
    vibes.newFigure('P')
    vibes.setFigureProperties({'x':0, 'y':0, 'width':800, 'height':500})  # 控制窗口的位置和大小
    vibes.newFigure('Y')
    vibes.setFigureProperties({'x':700, 'y':0, 'width':800, 'height':500})

    T = [0.2, 1, 2, 4]  # 横坐标位置
    Y = [Interval(1.5, 2), Interval(0.7, 0.8), Interval(0.1, 0.3), Interval(-0.1, 0.03)]  # 纵坐标范围
    P = Box(Interval(-3, 3), Interval(-3, 3))  # 限定了最外层 cyan 区域
    sivia(P)  # sivia 算法
    vibes.selectFigure('Y')
    for i in range(len(Y)):
        vibes.drawBox(T[i] - 0.01, T[i] + 0.01, Y[i].lb, Y[i].ub, 'red[red]')  # 将上面的四条竖线画出来
    vibes.endDrawing()
