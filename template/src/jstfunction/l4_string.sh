#!/bin/bash
##################################################################
str="abcdef"
# 取长度
echo ${#str} && expr length $str && expr "$str" : ".*"  # 6; 一般使用第一种
# 查找子串的位置
expr index $str "a" && expr index $str "b" && expr index $str "x" # 1, 2, 0
# 选取子串, 从 x 位置开始向后去 y 个字符
expr substr "$str" 1 3 && expr substr "$str" 2 5 && expr substr "$str" 4 5    # abc, bcdef, def
echo ${str:2} && echo ${str:2:3} && echo ${str:(-6):5} && echo ${str:(-4):3}  # cdef, cde, abcde, cde
# 截取子串, 在键盘布局中, # 总是位于百分号 % 的前面, 所以 # 表示从左边
str="abbc,def,ghi,abcjkl"
echo ${str#a*c}     # ,def,ghi,abcjkl; # 表示从左边截取掉最短的匹配, 这里把 abbc 字串去掉
echo ${str##a*c}    # jkl; ## 表示从左边截取掉最长的匹配, 这里把 abbc,def,ghi,abc 字串去掉
echo ${str#"a*c"}   # abbc,def,ghi,abcjkl 因为 str 中没有 "a*c" 子串
echo ${str##"a*c"}  # abbc,def,ghi,abcjkl 同理
echo ${str#*a*c*}   # ,def,ghi,abcjkl
echo ${str##*a*c*}  # 空
echo ${str#*d*f}    # ,ghi,abcjkl
echo ${str%a*l}     # abbc,def,ghi; % 表示从右边截取最短的匹配
echo ${str%%b*l}    # a; %% 表示从右边截取最长的匹配
echo ${str%a*c}     # abbc,def,ghi,abcjkl
# 字符串替换
str="apple, tree, apple tree"
echo ${str/apple/APPLE}   # 替换第一次出现的 apple
echo ${str//apple/APPLE}  # 替换所有 apple
echo ${str/#apple/APPLE}  # 如果字符串 str 以 apple 开头, 则用 APPLE 替换它
echo ${str/%apple/APPLE}  # 如果字符串 str 以 apple 结尾, 则用 APPLE 替换它
# 比较"
[[ "a.txt" == a* ]]        # 逻辑真 (pattern matching)
[[ "a.txt" =~ .*\.txt ]]   # 逻辑真 (regex matching)
[[ "abc" == "abc" ]]       # 逻辑真 (string comparision)
[[ "11" < "2" ]]           # 逻辑真 (string comparision), 按ascii值比较
# 连接
s1="hello" && s2="world" && echo ${s1}world && echo ${s1}${s2}  # $s1$s2 也行, 但最好加上大括号
##################################################################
## 下面是自己用过的
str="abcdef" && echo ${str:(-6):5}  # abcde
str='hello.java.c' && sub=${str#*.} && echo $sub  # java.c; 从左边开始删除第一次出现子字符串即其左边字符, 保留右边字符
sub=${str##*.} && echo $sub  # c; 从左边开始删除最后一次出现子字符串即其左边字符, 保留右边字符
sub=${str%.*} && echo $sub  # hello.java; 从右边开始删除第一次出现子字符串即其右边字符, 保留左边字符
# 在 vimrc 中 % 已经被占用, 只能用长度截取
sub=${str%%.*} && echo $sub  # hello; 用途是从右边开始删除最后一次出现子字符串即其右边字符, 保留左边字符
## ${string:position} 在$string中, 从位置$position开始提取子串
## ${string:position:length}
sub=${str::-7} && echo $sub  # 去掉后7个字符
