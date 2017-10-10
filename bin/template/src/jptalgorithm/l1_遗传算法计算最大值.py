#!/usr/bin/python3
# coding: utf-8
# [算法参考](https://www.zhihu.com/question/23293449/answer/120530793)
# [概念参考](http://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_fundamentals.htm)
# 求解函数 f(x) = x + 10 * sin(5 * x) + 7 * cos(4 * x) 在区间 [0, 9] 的最大值
import math
import random
import operator
class GA():
    def __init__(self, length, count):
        self.length = length  # 染色体长度, 本题目设置为 17
        self.count = count  # 种群中的染色体数量, 设置为 300
        self.population = self.gen_population(length, count)  # 随机生成初始种群
    def evolve(self, retain_rate=0.2, random_select_rate=0.5, mutation_rate=0.01):
        # 对当前一代种群依次进行选择、交叉并生成新一代种群, 然后对新一代种群进行变异
        parents = self.selection(retain_rate, random_select_rate)  # 选择
        self.crossover(parents)                                    # 交叉
        self.mutation(mutation_rate)                               # 变异
    def gen_chromosome(self, length):  # 随机生成长度为 length 的染色体, 每个基因的取值是 0 或 1
        chromosome = 0
        for i in range(length): chromosome |= (1 << i) * random.randint(0, 1)  # 这里用一个 bit 表示一个基因
        return chromosome
    def gen_population(self, length, count):  # 获取初始种群 (一个含有 count 个长度为 length 的染色体的列表)
        return [self.gen_chromosome(length) for i in range(count)]  # 生成 300 个长度为 17 的 chromosome
    def fitness(self, chromosome):  # 计算适应度, 将染色体解码为 0~9 之间数字, 代入函数计算; 因为是求最大值, 所以数值越大, 适应度越高
        x = self.decode(chromosome)  # 先进行解码, x 返回的是 [0, 9] 之间的数字
        return x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)  # 带入原公式, 返回函数值
    def selection(self, retain_rate, random_select_rate):
        # 先对适应度从大到小排序, 选出存活的染色体
        # 再进行随机选择, 选出适应度虽然小, 但是幸存下来的个体
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]  # [(f(x), chromosome)], 根据 f(x) 排序, 取 chromosome
        graded = [x[1] for x in sorted(graded, reverse=True)]  # 因为是求最大值, 所以反向排序, 排完序后 f(x) 就没用了, 只取 chromosome
        retain_length = int(len(graded) * retain_rate)  # 根据存活率, 选出适应性强的染色体
        parents = graded[:retain_length]  # 选出排名靠前的
        for chromosome in graded[retain_length:]:  # 选出适应性不强, 但是幸存的染色体, 就是从剩下的中间随机选择一些
            if random.random() < random_select_rate: parents.append(chromosome)
        return parents
    def crossover(self, parents):
        # 染色体的交叉、繁殖, 生成新一代的种群, 新出生的孩子, 最终会被加入存活下来的父母之中, 形成新一代的种群
        children = []
        target_count = len(self.population) - len(parents)  # 需要繁殖的孩子的量, 也就是上一轮淘汰的数量
        while len(children) < target_count:  # 开始根据需要的量进行繁殖
            male = random.randint(0, len(parents) - 1)  # 男性的索引
            female = random.randint(0, len(parents) - 1)  # 女性的索引, 从中挑出两个数
            if male != female:  # 只要两个数不同, 就进行交叉
                cross_pos = random.randint(0, self.length)  # 随机选取交叉点, self.length 是 17, 染色体长度
                mask = 0  # 生成掩码, 方便位操作
                for i in range(cross_pos): mask |= (1 << i)  # 00000011111111, 类似于种
                male, female = parents[male], parents[female]
                child = ((male & mask) | (female & ~mask)) & ((1 << self.length) - 1)  # 孩子将获得父亲在交叉点前的基因和母亲在交叉点后 (包括交叉点) 的基因
                children.append(child)
        self.population = parents + children  # 经过繁殖后, 孩子和父母的数量与原始种群数量相等, 在这里可以更新种群
    def mutation(self, rate):  # 变异; 对种群中的所有个体, 随机改变某个个体中的某个基因
        for i in range(len(self.population)):
            if random.random() < rate:  # 这里的变异率 rate 比较小, 为 0.01
                j = random.randint(0, self.length-1)
                self.population[i] ^= 1 << j
    def decode(self, chromosome): return chromosome * 9.0 / (2**self.length - 1)  # 解码染色体, 将二进制转化为属于 [0, 9] 的实数
    def result(self):  # 获得当前代的最优值, 这里取的是函数取最大值时 x 的值
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded, reverse=True)]
        return ga.decode(graded[0])
if __name__ == '__main__':
    ga = GA(17, 300)  # 染色体长度为 17, 种群数量为 300
    # 设定解的精度为小数点后 4 位, 将解空间划分为 (9-0)×(1e+4)=90000 个等分; 2^16<90000<2^17, 需要 17 位二进制数来表示这些解
    for x in range(200): ga.evolve()  # 200 次进化迭代
    print(ga.result())  # 7.856726507007652
##################################################################
## 总结:
# 1. 遗传算子: selection -> crossover ->  mutation; 选择, 交叉, 变异, 这三个是核心函数
# 2. 对于本问题, 我们可以采用以下公式来解码: x = 0 + decimal(chromosome)×(9-0)/(2^17-1)
#    decimal(): 将二进制数转化为十进制数
#    一般化解码公式: x = lower_bound + decimal(chromosome)×(upper_bound-lower_bound)/(2^chromosome_size-1)
#    f(x), x∈ [lower_bound, upper_bound]
#    lower_bound: 函数定义域的下限
#    upper_bound: 函数定义域的上限
#    chromosome_size: 染色体的长度
# 3. 求最大值, 设置较大的交叉率, 较小的变异率; 本题目中没有考虑交叉率, 默认都会交叉
# 4. GA 是全局的类, 并没有针对与各个 chromosome 的类
