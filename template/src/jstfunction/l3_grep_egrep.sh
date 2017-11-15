#!/bin/bash
# 具体讲解见: Regular_express_grep_sed.md, 这里之总结常用的
##################################################################
## grep i: (ignore-case) q: (quiet,suppress_normal_output) E: (extend regular_express)
##      r: (recursive) I: (without_binary_file) n: (print_line_number) v: (anti-select)
##################################################################
echo "I love China 521" | grep -n --color=always '[[:lower:]]'  # 查找小写字母, 高亮显示找到的
echo "I love China 521" | grep -n --color=always '[[:digit:]]'  # 查找数字
# 开头和结尾
echo "#hello world" | grep -n '^#'  # 查询以 # 开头的, 居然没有高亮
echo "thejrp dr for the^" | grep -n '^the'  # 以 the 开头的
echo "dr for ^[the dr]" | grep -n '^[the dr]'  # 以 the 或 dr 开头的
echo "hello for d$ world" | grep -n 'd$'  # 查找以 d 字母结尾的行
echo "hello \n \n world no white line" | grep -vn '^$'  # 查找不是空行的
cat /etc/passwd | head -n 5 | grep -nv '^$' | grep -nv '^#'  # 过滤到空行和注释行
# 字符组匹配
grep -n '^[A-Z]' regular_express.txt  # 表示以大写字母开头的行
grep -n 't[ae]st' regular_express.txt  # 查找"tast"或者"test"两个字符串
grep -n '[^go]oog' regular_express.txt  # 查找 "[^go]oog" 是指字符 "oog" 前面不能为 g 或者 o
# . 和 *
grep -n 'a.ou.' regular_express.txt  # 查找 a？ou？类型的字符, 只能表示一个字符
grep -n --color=always 'e*' regular_express.txt  # 允许空字符, 打印所有文本
# 限定连续字符范围{}
grep -n 'o\{2\}' regular_express.txt  # 结果与命令 grep -n 'ooo*' regular_express.txt 的结果相同
grep -n 'go\{2,5\}g' regular_express.txt  # 查找 g 后面接 2 到 5 个 o，然后再接 g 的字符串
# 未完待续
##################################################################
## grep 常用命令
alias greps="grep -riIn --color=always"  # example: greps hell
greps hello */l*  # 在 jptfun 上级目录中搜索所有的 l* 开头的文件中的 'hello'
