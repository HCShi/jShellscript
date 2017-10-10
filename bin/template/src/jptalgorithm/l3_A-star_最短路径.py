#!/usr/bin/python3
# coding: utf-8
# 参考 伯乐在线 的系列文章: 关于寻路算法的一些思考
# 代码参考: 某 CSDN 博客
import math
tm = [  # 地图
'############################################################',
'#..........................................................#',
'#.............................#............................#',
'#.............................#............................#',
'#.............................#............................#',
'#.......S.....................#............................#',
'#.............................#............................#',
'#.............................#............................#',
'#.............................#............................#',
'#.............................#............................#',
'#.............................#............................#',
'#.............................#............................#',
'#.............................#............................#',
'#######.#######################################............#',
'#....#........#............................................#',
'#....#........#............................................#',
'#....##########............................................#',
'#..........................................................#',
'#..........................................................#',
'#..........................................................#',
'#..........................................................#',
'#..........................................................#',
'#...............................##############.............#',
'#...............................#........E...#.............#',
'#...............................#............#.............#',
'#...............................#............#.............#',
'#...............................#............#.............#',
'#...............................###########..#.............#',
'#..........................................................#',
'#..........................................................#',
'############################################################']
test_map = []  # 因为 python 里 string 不能直接改变某一元素, 所以用 test_map 来存储搜索时的地图
#########################################################
class Node_Elem:  # 开放列表和关闭列表的元素类型, parent 用来在成功的时候回溯路径
    def __init__(self, parent, x, y, dist): self.parent, self.x, self.y, self.dist = parent, x, y, dist
class A_Star:
    def __init__(self, s_x, s_y, e_x, e_y, w=60, h=30):  # 注意 w, h 两个参数, 如果你修改了地图, 需要传入一个正确值或者修改这里的默认参数
        self.s_x, self.s_y, self.e_x, self.e_y = s_x, s_y, e_x, e_y
        self.width, self.height = w, h  # 代表地图的宽和高
        self.open, self.close, self.path = [], [], []  # 代表 open, close 集合, 以及最终生成路径的集合
    def find_path(self):  # 查找路径的入口函数
        p = Node_Elem(None, self.s_x, self.s_y, 0.0)  # 构建开始节点
        while True:  # 这里是 ** 开始查找路径的入口 **, 知道找到最优路径才停止, ** 相当于 main 函数 **
            self.extend_round(p)  # 扩展 F 值最小的节点, 将周围 8 个节点遍历, 进行相应操作
            if not self.open: return  # 如果开放列表为空, 则不存在路径, 返回
            idx, p = self.get_best()  # 获取 F 值最小的节点
            if self.is_target(p):  # 判断 p 是否为终点; 找到路径, 生成路径, 返回
                self.make_path(p)  # 向前回溯, 生成路径
                return
            self.close.append(p); del self.open[idx]  # 把此节点压入关闭列表, 并从开放列表里删除
    def make_path(self, p):  # 从结束点回溯到开始点, 开始点的 parent == None
        while p:
            self.path.append((p.x, p.y))
            p = p.parent
    def is_target(self, i): return i.x == self.e_x and i.y == self.e_y
    def get_best(self):  # 获取最小 F 值节点
        best = None
        bv = 1000000  # 如果你修改的地图很大, 可能需要修改这个值, F 初始值
        bi = -1
        for idx, i in enumerate(self.open):  # 同时返回索引和值
            value = self.get_dist(i)  # 获取 F 值
            if value < bv:  # 比以前的更好, 即 F 值更小
                best = i
                bv = value  # 每次调用这个函数, 都会重写一次 bv 的值, 所以初始化要大一点
                bi = idx
        return bi, best  # 返回 index 和 Node_Elem 对象
    def get_dist(self, i):  # 这个公式就是 A* 算法的精华了
        # F = G + H; G 为已经走过的路径长度, H 为估计还要走多远; H() = 欧式距离 * 1.2
        return i.dist + math.sqrt((self.e_x - i.x) * (self.e_x - i.x) + (self.e_y - i.y) * (self.e_y - i.y)) * 1.2
    def extend_round(self, p):  # 可以从 8 个方向走
        xs = (-1, 0, 1, -1, 1, -1, 0, 1)
        ys = (-1,-1,-1,  0, 0,  1, 1, 1)
        for x, y in zip(xs, ys):
            new_x, new_y = x + p.x, y + p.y
            if not self.is_valid_coord(new_x, new_y): continue  # 无效或者不可行走区域, 则忽略
            node = Node_Elem(p, new_x, new_y, p.dist + self.get_cost(p.x, p.y, new_x, new_y))  # 构造新的节点
            if self.node_in_close(node): continue  # 新节点在关闭列表, 则忽略
            i = self.node_in_open(node)  # 判断是否已经在 open 中了
            if i != -1:  # 如果已经在 open 中, 则进行更新
                if self.open[i].dist > node.dist:  # 现在的路径到比以前到这个节点的路径更好; 则使用现在的路径
                    self.open[i].parent = p
                    self.open[i].dist = node.dist
                continue  # 已经在 open 中, 就不用再添加了
            self.open.append(node)  # 如果没在 open 中, 添加进去
    def get_cost(self, x1, y1, x2, y2):  # 上下左右直走, 代价为 1.0, 斜走, 代价为 1.4
        if x1 == x2 or y1 == y2: return 1.0
        return 1.4
    def node_in_close(self, node):  # 判断新生成的 node 是否在 close 中
        for i in self.close:
            if node.x == i.x and node.y == i.y: return True
        return False
    def node_in_open(self, node):  # 判断新生成的 node 是否在 open 中
        for i, n in enumerate(self.open):
            if node.x == n.x and node.y == n.y: return i
        return -1
    def is_valid_coord(self, x, y):  # 判断是否越界 或 有障碍物
        if x < 0 or x >= self.width or y < 0 or y >= self.height: return False
        return test_map[y][x] != '#'
    def get_searched(self):  # 这个函数后面调用, 将走过的路径都标出来
        l = []
        for i in self.open: l.append((i.x, i.y))
        for i in self.close: l.append((i.x, i.y))
        return l
#########################################################
# 下面这些函数都是辅助性质的, 看懂上面的就行了
def print_test_map():  # 打印搜索后的地图
    for line in test_map: print(''.join(line))
def get_start_XY(): return get_symbol_XY('S')
def get_end_XY(): return get_symbol_XY('E')
def get_symbol_XY(s):  # 得到字符 s 的坐标
    for y, line in enumerate(test_map):
        try: x = line.index(s)
        except: continue
        else: break
    return x, y
#########################################################
def mark_path(l): mark_symbol(l, '*')  # 将最优路径标为 *
def mark_searched(l): mark_symbol(l, ' ')  # 将走过的路径标为 空
def mark_symbol(l, s):
    for x, y in l: test_map[y][x] = s
def mark_start_end(s_x, s_y, e_x, e_y):
    test_map[s_y][s_x] = 'S'
    test_map[e_y][e_x] = 'E'
def tm_to_test_map():
    for line in tm: test_map.append(list(line))
def find_path():
    s_x, s_y = get_start_XY()
    e_x, e_y = get_end_XY()
    a_star = A_Star(s_x, s_y, e_x, e_y)
    a_star.find_path()
    searched = a_star.get_searched(); mark_searched(searched)  # 标记已搜索区域
    path = a_star.path;               mark_path(path)          # 标记路径
    print("path length is %d"%(len(path)))
    print("searched squares count is %d"%(len(searched)))
    mark_start_end(s_x, s_y, e_x, e_y)  # 标记开始、结束点
if __name__ == "__main__":
    # 把字符串转成列表
    tm_to_test_map()
    find_path()
    print_test_map()
##################################################################
## 总结:
# 1. A_Star 中的 get_dist 是 f() = g() + h() 的公式; H() = 欧式距离 * 1.2
##################################################################
## A* 过程：
# 1. 将开始节点放入开放列表 (开始节点的 F 和 G 值都视为 0);
# 2. 重复一下步骤:
#    i. 在开放列表中查找具有最小F值的节点,并把查找到的节点作为当前节点;
#    ii. 把当前节点从开放列表删除, 加入到封闭列表;
#    iii. 对当前节点相邻的每一个节点依次执行以下步骤:
#       1. 如果该相邻节点不可通行或者该相邻节点已经在封闭列表中, 则什么操作也不执行, 继续检验下一个节点;
#       2. 如果该相邻节点不在开放列表中, 则将该节点添加到开放列表中, 并将该相邻节点的父节点设为当前节点, 同时保存该相邻节点的 G 和 F 值;
#       3. 如果该相邻节点在开放列表中, 则判断若经由当前节点到达该相邻节点的 G 值是否小于原来保存的 G 值, 若小于, 则将该相邻节点的父节点设为当前节点, 并重新设置该相邻节点的 G 和 F 值.
#    iv. 循环结束条件:
#       当终点节点被加入到开放列表作为待检验节点时, 表示路径被找到, 此时应终止循环;
#       或者当开放列表为空, 表明已无可以添加的新节点, 而已检验的节点中没有终点节点则意味着路径无法被找到, 此时也结束循环;
# 3. 从终点节点开始沿父节点遍历, 并保存整个遍历到的节点坐标, 遍历所得的节点就是最后得到的路径;
