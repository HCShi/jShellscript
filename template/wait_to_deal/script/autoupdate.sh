#!/bin/bash
# Name:autoupdate.sh
# This is a ShellScript For Auto Update Hexo Blog

hexoDir="/home/wwwroot/mritd.me"
updateCommand="git pull"
updatetime=`date "+%Y-%m-%d %T"`

#Swich Dir
cd $hexoDir
#Update Site
$updateCommand &>> update.log

if [ $? -eq 0 ]; then
 echo "$updatetime 更新成功！" &>> update.log
else
 echo "$updatetime 更新失败! " &>> update.log
fi
