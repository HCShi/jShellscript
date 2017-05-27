#!/bin/bash
# 1. 等号左右不能有空格 2. 两个 for 可以嵌套 3. 两个 while 或者 for-while 嵌套不可以, 但 while-for 可以嵌套
# 4. 而且 !/bin/bash 的声明必须放在第一行, 否则会提示循环不能执行
##################################################################
## useradd passwd adduser (后面还有 for while 添加用户)
# sudo useradd -m hadoop -s /bin/bash  # 这条命令创建了可以登陆的 hadoop 用户, 并使用 /bin/bash 作为 shell -m 是添加家目录
# sudo passwd hadoop  # 添加 用户密码
# sudo adduser hadoop sudo  # 可为 hadoop 用户增加管理员权限, 方便部署, 避免一些对新手来说比较棘手的权限问题
# 最后注销当前用户（点击屏幕右上角的齿轮, 选择注销）, 在登陆界面使用刚创建的 hadoop 用户进行登陆
##################################################################
## for while, 可以用换行去掉分号
for x in one two three four; do echo number $x; done
for x in ./*; do echo $(basename $x) is a file living in ./; done
for thing in "$@"; do echo you typed ${thing}; done
for j in $(seq 1 5); do echo $j; done
for (( i=1; i<=5; i++ )); do echo "i=$i"; done
echo "变量自增"
i=0;
while [ $i -lt 10 ]; do
    echo $i; i=`expr $i + 1`; let i+=1; ((i++)); i=$[$i+1]; i=$(( $i + 1 ))
done
# cat /etc/passwd  # 显示当前用户群
echo "添加用户: "
for((i=1;i<=4;i++)); do
    for((j=1;j<=30;j++)); do
        if [ $j -le 9 ]; then USERNAME=jsjclassI${i}str0${j}
        else USERNAME=jsjclassI${i}stu${j}; fi
        # useradd $USERNAME  # 增加用户
        # userdel -r $USERNAME  # 删除用户
        # echo $USERNAME
    done
    if [ $i == 3 ]; then
        echo break; break
    fi
done
