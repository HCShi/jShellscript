#!/bin/bash
# sed 1975 年诞生, 全名: Stream Editor
# awk 1977 年诞生
##################################################################
## awk (awk + action)
# 读入有 '\n' 换行符分割的一条记录, 然后将记录按指定的域分隔符划分域, 填充域, **$0 则表示所有域**, $1 表示第一个域, $n 表示第 n 个域
# -F 指定分隔符, 默认域分隔符是"空白键" 或 "[tab] 键"
last -n 5 | awk  '{print $1}'  # 只显示最近登录的 5 个帐号
cat /etc/passwd | awk -F ':' '{print $1}'  # 显示/etc/passwd 的账户, -F 指定域分隔符为':'
cat /etc/passwd | awk -F ':' '{print $1"\t"$7}'  # 显示/etc/passwd 的账户和账户对应的 shell,而账户与 shell 之间以 tab 键分割
cat /etc/passwd | awk -F ':' 'BEGIN {print "name, shell"}  {print $1","$7} END {print "blu, /bin/nosh"}'  # 账户与 shell 之间以逗号分割, 在所有行添加列名 name,shell,在最后一行添加"blu,/bin/nosh"
# 先执行 BEGING, 然后读取文件, 读入有 /n 换行符分割的一条记录, 然后将记录按指定的域分隔符划分域, 填充域, 最后执行 END 操作
awk -F : '/root/' /etc/passwd  # 搜索/etc/passwd 有 root 关键字的所有行
# 这种是 pattern 的使用示例, 匹配了 pattern(这里是 root)的行才会执行 action(没有指定 action, 默认输出每行的内容)
awk -F : '/^root/' /etc/passwd  # 搜索支持正则, 例如找 root 开头的
awk -F : '/root/{print $7}' /etc/passwd  # 搜索/etc/passwd 有 root 关键字的所有行, 并显示对应的 shell
awk -F : '{print "filename:" FILENAME ",linenumber:" NR ",columns:" NF ",linecontent:"$0}' /etc/passwd  # 统计/etc/passwd:文件名, 每行的行号, 每行的列数, 对应的完整行内容
awk -F : '{printf("filename:%10s,linenumber:%s,columns:%s,linecontent:%s\n",FILENAME,NR,NF,$0)}' /etc/passwd  # 使用 printf 替代 print,可以让代码更加简洁
ifconfig wlan0 | awk '/inet addr/{gsub(/addr:/,"");print $2}'  # 输出无线网 IP 地址
##################################################################
## sed
## sed 处理文件
## sed 删除指定行
sed '42d' test.txt > tmp    # 删除 42 from test.txt and save to test2.txt; 前后的文件名一定不能相同, 否则全删光了
sed '1,42d' test.txt > tmp  # 删除 1-42
sed '1,4d;7,8d' tmp         # 删除 1-4, 7-8 行

sed "s/my/your/g" tmp       # 全局替换
sed "s/mathjax//g;s/MathJax//g;s/mathJax//g" tmp.html > he.html  # 替换 mathjax, 虽然替换成功了, 但是没什么用

sed -e '/abc/d' tmp         # 删除含有 abc 的行
sed -e '/abc/d;/efg/d' tmp     # 删除含有 abc 或 efg 的行
sed -e '/mathJax/d;/MathJax/d;/mathjax/d' tmp.html > out.html  # 删掉含 MathJax 的行, 删掉了, 但是没什么用

## sed perl 处理字符串
sed -i -- 's/bar/bar/g' *  # 将当前路径所有文件替换, 没有递归效果, sed 不能加 e
perl -i -pe 's/bar/bar/gc' ./*  # 将当前路径所有文件替换, 没有递归效果 (加 e 和不加一样)
# perl 那个比较好用
uptime | awk '{print $3}' | sed 's/,//'
##################################################################
## tail & head
cat filename | tail -n +3000 | head -n 1000  # 从第 3000 行开始, 显示 1000 行, 即显示 3000~3999 行
cat filename | head -n 3000 | tail -n +1000  # 显示 1000 行到 3000 行
echo '(+ 1 2)' | mit-scheme | tail -n +12 | head -n -3  # 前 12 行是没用的 startup report of versions and copyrights
# 后三行是 valediction, 都省略掉
# tail -n 1000: 显示最后 1000 行
# tail -n +1000: 从 1000 行开始显示, 显示 1000 行以后的
# head -n -1000: 最后 1000 行过滤掉
# head -n 1000: 显示前面 1000 行
sed -n '5,10p' filename  # 这样你就可以只查看文件的第 5 行到第 10 行
tail -n 2 ~/.zsh_history | head -n 1 | awk '{print $3}'  # 倒数第二行的路径

## head 应用
head -n 100 filename.csv > tmp.csv  # 对大文件的操作, 先截取小文件来测试
head -n 7105 filename.csv | tail -n 1  # 查看第 7105 行数据
##################################################################
## tr
# -d, --delete            delete characters in SET1, do not translate
echo "hello world" | tr -d 'hello'  # wrd
xdotool getmouselocation | awk '{print $1}' | tr -d 'x:'  # 输出当前鼠标的 x 坐标
