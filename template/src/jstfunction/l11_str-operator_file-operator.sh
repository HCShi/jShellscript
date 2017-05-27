#!/bin/bash
##################################################################
## 字符串运算符
# =	  检测两个字符串是否相等
# !=  检测两个字符串是否不相等
# -z  检测字符串长度是否为 0
# -n  检测字符串长度是否不为 0
if [ "$1"  != "" ]; then echo $1; fi  # quotes around $x, because if $x is empty, you'll get if [ == "valid" ]... which is a syntax error

##################################################################
## 文件测试运算符
# -b file	检测文件是否是块设备文件
# -c file	检测文件是否是字符设备文件
# -d file	检测文件是否是目录
# -f file	检测文件是否是普通文件(既不是目录, 也不是设备文件)
# -g file	检测文件是否设置了 SGID 位
# -k file	检测文件是否设置了粘着位(Sticky Bit)
# -p file	检测文件是否是有名管道
# -u file	检测文件是否设置了 SUID 位
# -r file	检测文件是否可读
# -w file	检测文件是否可写
# -x file	检测文件是否可执行
# -s file	检测文件是否为空(文件大小是否大于0)
# -e file	检测文件(包括目录)是否存在
# -L file   检测文件是否是 symlinks
file="/home/coder352/.zshrc"
# if  [[ -d $file && ! -L $file ]]; then  # 确定是文件, 并且不是软连接
if [ -r $file ]; then echo "文件可读"
else echo "文件不可读"
fi
if [ -w $file ]; then echo "文件可写"
else echo "文件不可写"
fi
