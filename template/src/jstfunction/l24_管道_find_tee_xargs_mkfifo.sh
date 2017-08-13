##################################################################
## 1. 类管道命令
ls | wc -l  # 后一个命令在前一个的基础上运行
ls > test  # 重定向, 写入
# tee: read from standard input and write to standard output and files.
# Copy standard input to each FILE, and also to standard output. If a FILE is -, copy again to standard output
seq 5 | tee a b  # stdout 有输出, 新建两个文件 a b, 内容和输出一样
echo 'hello' | tee - - - - -  # 有几个 - 重复几次, zsh 中不好用

find -name *.py | xargs grep asdf  # 作为参数, 找 py 结尾的文件中的字符串
findname "*.db" | xargs rm  # 删除子文件的指定文件
findname "*sqlmap*" | xargs -I {} cp {} ~/del  # 将 xargs 的结果作为第一个参数, 第一个 {} 是声明占位符
echo `python -c "print 'a'*24"`  # `` 将命令执行结果不变的返回  # aaaaaaaaaaaaaaaaaaaaaaaa
find / -name virtualenvwrapper.sh  # 全局查找, 很给力
##################################################################
## 2. mkfifo
mkfifo pipe1  # 创建管道
ls -l pipe1  # prw-rw-r-- 1 coder352 coder352 0 Nov 17 20:31 pipe1, p 表示是管道, 大小为 0, 且一直为 0, 不占用本地磁盘
# 开启两个终端
ls -l > pipe1
cat < pipe1  # 两个命令的顺序可以反
# cat Usage: cat [OPTION]... [FILE]..., 默认是读文件, 但是 pipe1 就相当于文件
cat tmp
cat < tmp  # tmp 为普通文件, 这两行效果相同
