#!/bin/bash
# Usage: $source ./l10_basename_dirname_if_$_bool.sh 1 2 3
##################################################################
## dirname 命令可以直接获取路径对应的目录名
## basename 命令可以直接获取路径名最后的文件名
str=`pwd` && basename $str  # jstfunction
dirname $str  # /home/coder352/github/jShellscript/template/src
# $$  # Shell 本身的 PID(ProcessID)
# $!  # Shell 最后运行的后台 Process 的 PID
# $?  # 最后运行的命令的结束代码(返回值)
# $-  # 使用 Set 命令设定的 Flag 一览
# $*  # 所有参数列表; 如 "$*" 用「"」括起来的情况、以"$1 $2 … $n" 的形式输出所有参数
# $@  # 所有参数列表; 如 "$@" 用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数
# $#  # 添加到 Shell 的参数个数
# $0  # Shell 本身的文件名
# $n  # 添加到 Shell 的各参数值; $1 是第 1 参数、$2 是第 2 参数
$0  # /home/coder352/github/jShellscript/template/src/jstfunction/l4_string_basename_dirname.sh: line 54: /home/coder352/github/jShellscript/template/src/jstfunction/l4_string_basename_dirname.sh
name=`basename $0 .sh` && echo $name  # l4_string_basename_dirname; 获取文件名
basename $0 && basename $0 .sh  # l4_string_basename_dirname.sh, l4_string_basename_dirname
##################################################################
# 1. if 与 [ 之间必须有空格; 2. [ ] 与判断条件之间也必须有空格; 3. ] 与 ; 之间不能有空格
name=`basename $0 .sh`
if [ $# -ne 2 -a $# -ne 3 ]; then  # $# 表示添加到命令的参数的个数, -a 与运算, -o 或运算
    echo "Usage: $name value1 value2"
    echo "       $name value1 value2 value3 "
    exit 1
fi
if [ $# -eq 2 ]; then echo "two args: $1, $2"
else echo "three args: $1 $2 $3"
fi
if [ $# -eq 2 ]; then
    if [ $1 -gt $2 ]; then echo "$1 > $2"
    elif [ $1 -lt $2 ]; then echo "$1 < $2 "
    else echo "$1 = $2"
    fi
else
    if [ $1 -ge $2 -a $1 -ge $3 ]; then echo "$1 >=$2 , $1 >=$3"
    elif [ $1 -ge $2 -a $1 -lt $3 ]; then echo "$1 >=$2 ，$1 < $3"
    elif [ $1 -lt $2 ] && [ $1 -ge $3 ]; then echo "$1 < $2, $1 >= $3"
    else echo "$1 < $2, $1 < $3"
    fi
fi
