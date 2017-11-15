#!/bin/bash
##################################################################
## eval
eval "echo hello"
eval "ls"
eval "echo 'hello world'"  # 可以嵌套
eval ls  # 可以不加引号
##################################################################
## echo
echo -e -n "\x11\x22" > tmp  # 直接写 16 进制
## 有一个题目要上传一个 jpg 文件: 1. 后缀为 php, jpg 文件默认的开头是 FFD8 (16进制)
echo -e -n "\xFF\xD8" > jiaruipeng.php  # 这里不能直接用 echo "FFD8" > jiaruipeng.php
xxd jiaruipeng.php  # 查看是否写进去了
##################################################################
## -e -n
# 参考: https://linux.cn/article-3948-1.html
# -n 不输出末尾的换行符; -e 启用反斜线转义; \b 退格; \\ 反斜线
# \n 新行; \r 回车; \t 水平制表符; \v 垂直制表符
## 不用带 ""
echo Tecmint is a community of Linux Nerds
## 变量
x=10
echo The value of variable x = $x
## -e
echo -e "Tecmint \bis \ba \bcommunity \bof \bLinux \bNerds"
# TecmintisacommunityofLinuxNerds  # '-e'后带上'\b'会删除字符间的所有空格, Linux 中的选项 '-e' 扮演了转义字符反斜线的翻译器
echo "Tecmint \bis \ba \bcommunity \bof \bLinux \bNerds"  # Tecmint \bis \ba \bcommunity \bof \bLinux \bNerds
echo -e "Tecmint \nis \na \ncommunity \nof \nLinux \nNerds"  # '-e' 后面的带上 '\n' 行会在遇到的地方作为新的一行
echo "Tecmint \nis \na \ncommunity \nof \nLinux \nNerds"
echo -e "Tecmint \tis \ta \tcommunity \tof \tLinux \tNerds"  # '-e' 后面跟上 '\t' 会在空格间加上水平制表符
echo -e "\n\tTecmint \n\tis \n\ta \n\tcommunity \n\tof \n\tLinux \n\tNerds"  # 也可以同时使用换行 '\n' 与水平制表符 '\t'
echo -e "\vTecmint \vis \va \vcommunity \vof \vLinux \vNerds"  # '-e' 后面跟上 '\v' 会加上垂直制表符
echo -e "\n\vTecmint \n\vis \n\va \n\vcommunity \n\vof \n\vLinux \n\vNerds"  # 也可以同时使用换行 '\n' 与垂直制表符 '\v'
# /r 覆盖掉开头字符
echo -e "Tecmint \ris a community of Linux Nerds"  # '-e' 后面跟上 '\r' 来指定输出中的回车符;(LCTT 译注：会覆写行开头的字符)
# is a community of Linux Nerds
echo -e "Tecmint is a community \cof Linux Nerds"  # Tecmint is a community  # '-e' 后面跟上 '\c' 会抑制输出后面的字符并且最后不会换新行
## -n
echo -n "Tecmint is a community of Linux Nerds"
# '-n' 会在 echo 完后不会输出新行
echo -e "Tecmint is a community of \aLinux Nerds"  # Tecmint is a community of Linux Nerds  # '-e'后面跟上'\a'选项会听到声音警告
## *
echo *  # 使用 echo 命令打印所有的文件和文件夹(ls 命令的替代)
##################################################################
## 9x9 表
for i in $(seq 1 10)
do
    for (( j=1; j<=$i; j++ ))
    #for j in $(seq 1 $i)
    do
        echo -ne $i x $j=$((i*j)) \\t
    done
    echo
done
