#!/bin/bash
##################################################################
## sleep
date; sleep 3; date; sleep 1m; date
# 默认以 s 为单位, m 表示 minute
##################################################################
## read, 最好拿出去单独执行, 还有很多参数, 慢慢用
read  # 单独命令可以
# 输入进参数
echo -n "Enter your name:"                # 参数 -n 的作用是不换行, echo 默认是换行
read  name                                # 从键盘输入
echo "hello $name,welcome to my program"  # 显示信息
# -p 将上面的简化
read -p "Enter your name:" name1 name2            # 可以连续多个输入
echo "hello $name1 $name2,welcome to my program"  # 显示信息
##################################################################
## at
at now +1 minute <<< 'echo "hello"'  # 在当前的终端看不到
at now +1 minute <<< 'touch abc'
at now +10 minutes <<< "rm -rf /tmp/tobedeleted"
# 下面是多行的
at now +10 minutes <<ENDMARKER
rm -rf /tmp/tobedeleted
echo all done | mail -s 'completion notification' sysadmin@example.com
ENDMARKER
# 执行文件
at now +1 minute -f *.sh
# 查询命令
at -l / atq  # 两个命令都可以查看当前的任务数
atrm 1  # 删除第一个任务; 按 Tab 会自动补全序号
##################################################################
## at 分类符描述
at noon                # 在接下来的正午 12 点运行
at midnight            # 在接下来的凌晨 12 点运行
at teatime             # 下午 4 点
at tomorrow            # 在明天的当前同一时间运行
at noon tomorrow       # 在明天的中午 12 点运行
at next week           # 一周后的当前同一时间运行
at next monday         # 下周一的当前同一时间运行
at fri                 # 周五的当前同一时间运行
at OCT                 # 十月份当前同一时间运行
at 9:00 AM             # 接下来的上午 9 点运行
at 2:30 PM             # 接下来的下午 2:30 运行
at 14:30               # 同上
at 2:30 PM tomorrow    # 同上
at 2:30 PM next month  # 同上
at 2:30 PM Fri         # 同上
at 2:30 PM 3/24        # 同上
at 2:30 PM mar 24      # 同上
at 2:30 PM 3/24/2017   # 同上
at 2:30 PM 24.3.17     # 同上
at now +30 minutes     # 当前时间的 30 分钟后
at now + 1 hour        # 算了, 不解释了
at now + 2 days        # 同上
at 4 PM + 2 days       # 同上
at now + 3 weeks       # 同上
at now + 4 months      # 同上
at now + 5 years       # 同上
