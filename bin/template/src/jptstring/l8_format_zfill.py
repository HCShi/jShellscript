#!/usr/bin/python3
# coding: utf-8
##################################################################
## format, 另外还有 list 里面的格式化
# format 和 %
print('hello {}, {}'.format('jrp', 'beijing'), ('hello %s, %s' % ('jrp', 'beijing')))  # hello jrp, beijing hello jrp, beijing

# 特殊字符
print(r'\\\\t')  # r 内部字符串不转义
print(b'A' == 'A', b'A' == b'\x41')  # False, True
print('''hello
    world'''); print('hello\nworld')  # 两种换行方式

# 保留小数位数, 可以用 {:.2} 或者 %.2f
print('hello [%.2f, %.2f]"' % (1/3, 2/3))  # [0.33, 0.67];
print('hello {:.2}, {:.2}'.format(1/3, 2/3))  # hello 0.33, 0.67
print('hello [%f, %f]"' % (round(1/3, 2), round(2/3, 2)))  # [0.330000, 0.670000]; round(x, n) 比较尴尬

print(bin(6))  # 0b110
print(bin(6)[2:])  # 110
# What can i do if i want to show 6 as 00000110 instead of 110
# 方法一: zfill()
print(bin(6)[2:].zfill(8))  # 00000110
# 方法二: format(<the_integer>, "<0><width_of_string><format_specifier>")
print(format(6, "08b"))  # 00000110
# 方法三:
print('{0:08b}'.format(6))  # 00000110
# {} places a variable into a string
# 0 takes the variable at argument position 0
# : adds formatting options for this variable (otherwise it would represent decimal 6)
# 08 formats the number to eight digits zero-padded on the left
# b converts the number to its binary representation
print('{0:08}'.format(6))  # 00000006
# 方法四: %0*d
print('%0*d' % (8, int(bin(6)[2:])))  # 00000110; Python 好神奇
# 方法五: rjust()
print(bin(6)[2:].rjust(8, '0'))  # 00000110
