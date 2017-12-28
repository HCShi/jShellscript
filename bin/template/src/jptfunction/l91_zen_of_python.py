#!/usr/bin/python3
# coding: utf-8
##################################################################
## if 高级写法
a = 1 if 1 > 2 else 3; print(a)
##################################################################
## for ... else
for x in range(1, 5):
    if x == 5: print('find 5')
else: print('can not find 5!') # can not find 5!
##################################################################
## * 去掉第一层 list 的外套
print(*[1, 2]); print(*[[1, 2]])  # 1 2; [1, 2]
print(*([(1, 2)]))  # (1, 2)
##################################################################
## 心形字符
print('\n'.join([''.join([('LoveDaiRui'[(x-y)%10] if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))
##################################################################
## 一行代码画一个 Mandelbrot
print('\n'.join([''.join(['*'if abs((lambda a:lambda z, c, n:a(a, z, c, n))(lambda s, z, c, n:z if n==0else s(s, z*z+c, c, n-1))(0, 0.02*x+0.05j*y, 40))<2 else' 'for x in range(-80, 20)])for y in range(-20, 20)]))
##################################################################
## 一行代码打印九九乘法表
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))
##################################################################
## 一行代码计算出 1-1000 之间的素数
print(*(i for i in range(2, 1000) if all(tuple(i%j for j in range(2, int(i**.5))))))
##################################################################
## 一行代码可以输出前 100 项斐波那契数列的值
print([x[0] for x in [  (a[i][0], a.append((a[i][1], a[i][0]+a[i][1]))) for a in ([[1, 1]], ) for i in range(100) ]])
##################################################################
## 一行代码实现阶乘, 而且还带交互:
print(reduce(lambda x,y:x*y, range(1,input()+1)))
# 10  3628800
##################################################################
## 一行代码实现摄氏度与华氏度之间的转换器:
print((lambda i:i not in [1,2] and "Invalid input!" or i==1 and (lambda f:f<-459.67 and "Invalid input!" or f)(float(input("Please input a Celsius temperature:"))*1.8+32) or i==2 and (lambda c:c<-273.15 and "Invalid input!" or c)((float(input("Please input a Fahrenheit temperature:"))-32)/1.8))(int(input("1,Celsius to Fahrenheit\n2,Fahrenheit to Celsius\nPlease input 1 or 2\n"))))  1,Celsius to Fahrenheit  2,Fahrenheit to Celsius  Please input 1 or 2  1  Please input a Celsius temperature:28  82.4  >>>
##################################################################
## 至于字符串排序和快速排序更是手到擒来。
print("".join((lambda x:(x.sort(),x)[1])(list('string')))    qsort = lambda arr: len(arr) > 1 and  qsort(filter(lambda x: x<=arr[0], arr[1:] )) + arr[0:1] + qsort(filter(lambda x: x>arr[0], arr[1:] )) or arr)
