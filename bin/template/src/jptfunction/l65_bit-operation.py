#!/usr/bin/python3
# coding: utf-8
##################################################################
## "0b" 或者 "-0b" 开头的字符串来表示二进制
print(0b101)  # 5
print(-0b101)  # -5
##################################################################
## bin() 整数转二进制
print(bin(5))   # 0b101
print(bin(-8))  # -0b1000
##################################################################
## << 左移
print(0b11 << 2)  # 12, 即 0b1100
print(5 << 2)     # 20, 即 0b10100
print(-5 << 2)    # -20
print(5 << 64)    # 92233720368547758080L
##################################################################
## >>  右移
print(0b11 >> 1)  # 1, 即 0b1
print(5 >> 1)     # 2, 即 0b10
print(-8 >> 3)    # -1
##################################################################
## | 位或
print(0b110 | 0b101)   # 7, 即 0b111
print(-0b001 | 0b101)  # -1
##################################################################
## & 位与
print(0b110 & 0b011)  # 2, 即 0b010
##################################################################
## ^ 位异或
print(0b111 ^ 0b111)  # 0
print(0b100 ^ 0b111)  # 3
##################################################################
## ~ 非
print(~0b101)  # -6, 即 -0b110
print(~-3)     # 2, 即 0b10
##################################################################
## 总结
# 1. 左移操作相当于乘以 2**n, 以5 << 3为例, 相当于 5(2*3), 结果为 40
# 2. 负数的左移相对来说就比较复杂, 以 -2 << 2 为例, -2 的
#     原码是 10000000000000000000000000000010 (32 位系统), 其
#     补码为 11111111111111111111111111111110,
#     左移为 11111111111111111111111111111000, 再转化
#     原码为 10000000000000000000000000001000, 也就是 -8, 也就是-2*(2**2)=-8
# 3. 左移超过32位或者64位 (根据系统的不同) 自动转化为long类型
