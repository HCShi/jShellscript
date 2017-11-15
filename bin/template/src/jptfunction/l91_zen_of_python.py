#!/usr/bin/python3
# coding: utf-8
##################################################################
## 读文件, 这里不能执行
data = np.array([[float(x) for x in re.split(r'\s+', line.strip())] for line in fileinput.input('TSP_Data')])  # jptalgorithm 中用到的读取文件处理的命令
# 通常会使用 line.strip().split()
##################################################################
## if 高级写法
a = 1 if 1 > 2 else 3; print(a)
##################################################################
## for ... else
for x in range(1, 5):
    if x == 5: print('find 5');
else: print('can not find 5!') # can not find 5!
##################################################################
## * 去掉第一层 list 的外套
print(*[1, 2]); print(*[[1, 2]])  # 1 2; [1, 2]
print(*([(1, 2)]))  # (1, 2)
