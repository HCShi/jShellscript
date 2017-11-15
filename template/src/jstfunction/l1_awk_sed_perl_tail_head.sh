#!/bin/bash
##################################################################
## awk (awk + action)
# 读入有'\n'换行符分割的一条记录, 然后将记录按指定的域分隔符划分域, 填充域, **$0则表示所有域**, $1表示第一个域, $n表示第n个域
# -F 指定分隔符, 默认域分隔符是"空白键" 或 "[tab]键"
last -n 5 | awk  '{print $1}'  # 只显示最近登录的5个帐号
cat /etc/passwd | awk -F ':' '{print $1}'  # 显示/etc/passwd的账户, -F指定域分隔符为':'
cat /etc/passwd | awk -F ':' '{print $1"\t"$7}'  # 显示/etc/passwd的账户和账户对应的shell,而账户与shell之间以tab键分割
cat /etc/passwd | awk -F ':' 'BEGIN {print "name, shell"}  {print $1","$7} END {print "blu, /bin/nosh"}'  # 账户与shell之间以逗号分割, 在所有行添加列名name,shell,在最后一行添加"blu,/bin/nosh"
# 先执行BEGING, 然后读取文件, 读入有 /n 换行符分割的一条记录, 然后将记录按指定的域分隔符划分域, 填充域, 最后执行END操作
awk -F : '/root/' /etc/passwd  # 搜索/etc/passwd有root关键字的所有行
# 这种是 pattern 的使用示例, 匹配了 pattern(这里是root)的行才会执行action(没有指定action, 默认输出每行的内容)
awk -F : '/^root/' /etc/passwd  # 搜索支持正则, 例如找root开头的
awk -F : '/root/{print $7}' /etc/passwd  # 搜索/etc/passwd有root关键字的所有行, 并显示对应的shell
awk -F : '{print "filename:" FILENAME ",linenumber:" NR ",columns:" NF ",linecontent:"$0}' /etc/passwd  # 统计/etc/passwd:文件名, 每行的行号, 每行的列数, 对应的完整行内容
awk -F : '{printf("filename:%10s,linenumber:%s,columns:%s,linecontent:%s\n",FILENAME,NR,NF,$0)}' /etc/passwd  # 使用printf替代print,可以让代码更加简洁
ifconfig wlan0 | awk '/inet addr/{gsub(/addr:/,"");print $2}'  # 输出无线网IP地址
##################################################################
## tail & head & sed & awk
cat filename | tail -n +3000 | head -n 1000  # 从第3000行开始, 显示1000行, 即显示3000~3999行
cat filename | head -n 3000 | tail -n +1000  # 显示1000行到3000行
echo '(+ 1 2)' | mit-scheme | tail -n +12 | head -n -3  # 前 12 行是没用的 startup report of versions and copyrights
# 后三行是 valediction, 都省略掉
# tail -n 1000: 显示最后1000行
# tail -n +1000: 从1000行开始显示, 显示1000行以后的
# head -n -1000: 最后1000行过滤掉
# head -n 1000: 显示前面1000行
sed -n '5,10p' filename  # 这样你就可以只查看文件的第5行到第10行
tail -n 2 ~/.zsh_history | head -n 1 | awk '{print $3}'  # 倒数第二行的路径

## sed 删除指定行
sed '42d' test.txt > test2.txt  # 删除 42 from test.txt and save to test2.txt; 前后的文件名一定不能相同, 否则全删光了
sed '1,42d' test.txt > test2.txt  # 删除 1-42
sed '1,4d;7,8d' tmp  # 删除 1-4, 7-8 行
##################################################################
## head 应用
head -n 100 filename.csv > tmp.csv  # 对大文件的操作, 先截取小文件来测试
head -n 7105 filename.csv | tail -n 1  # 查看第 7105 行数据
##################################################################
## sed perl 处理字符串
sed -i -- 's/bar/bar/g' *  # 将当前路径所有文件替换, 没有递归效果, sed 不能加 e
perl -i -pe 's/bar/bar/gc' ./*  # 将当前路径所有文件替换, 没有递归效果 (加 e 和不加一样)
# perl 那个比较好用
uptime | awk '{print $3}' | sed 's/,//'
