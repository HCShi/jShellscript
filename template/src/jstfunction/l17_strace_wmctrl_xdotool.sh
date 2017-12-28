#!/bin/bash
##################################################################
## strace
# 修改了 /etc/hosts 以后, sudo 变得非常慢, 于是查到了这个命令
# Is one of the files/directories it needs to read on a networked mount, or is it somehow triggering reading from a slow usb device?
sudo strace -r -o trace.log sudo echo hi
# Each line will start with the time taken since entering the previous syscall

##################################################################
## wmctrl
## 下面这几个目前还不可以, 但没有硬性需求, 先放一放...
lyx && wmctrl -r LyX -e 0,0,0,800,600  # 打开 lyx, 并指定将 lyx 放到左上角; 这样写不行, 还没找到好的方法
lyx && wmctrl -r :ACTIVE: -e 0,0,0,800,600  # 打开 lyx, 将刚刚激活的窗口(lyx) 放到左上角
wmctrl -lG  # 查看当前的窗口数量及大小, 名称; 用名称就可以来调用窗口, 哈哈...
# 0x02e0000a  0 0    0    1366 768  localhost Desktop   # 这个可以看出来屏幕的分辨率, 这样就可以设置为右半屏幕
# 0x0140000a  0 0    0    1366 768  localhost jPC-tmux  # 我的 Terminal
lyx && wmctrl -r :ACTIVE: -e 0,683,0,683,768  # 打开 lyx, 将刚刚激活的窗口(lyx) 放到左上角
# 计算像素的时候最好把 Launcher 隐藏了...

## 直接用名字很好使...
wmctrl -r l2_GD_Gradient-Descent.pdf -e 0,683,0,683,768  # 用 zathura 打开 pdf, 然后放到右边

# 参数解释太长, 放下面
# -m                   Show information about the window manager and about the environment.
# -l                   List windows managed by the window manager.
# -d                   List desktops. The current desktop is marked with an asterisk.
# -s <DESK>            Switch to the specified desktop.
# -a <WIN>             Activate the window by switching to its desktop and raising it.
# -c <WIN>             Close the window gracefully.
# -R <WIN>             Move the window to the current desktop and activate it.
# -r <WIN> -t <DESK>   Move the window to the specified desktop.
# -r <WIN> -e <MVARG>  Resize and move the window around the desktop.
#                      The format of the <MVARG> argument is described below.
# -r <WIN> -b <STARG>  Change the state of the window. Using this option it's possible for example to make the window maximized,
#                      minimized or fullscreen. The format of the <STARG> argument and list of possible states is given below.
# -r <WIN> -N <STR>    Set the name (long title) of the window.
# -r <WIN> -I <STR>    Set the icon name (short title) of the window.
# -r <WIN> -T <STR>    Set both the name and the icon name of the window.
# -k (on|off)          Activate or deactivate window manager's "showing the desktop" mode. Many window managers do not implement this mode.
# -o <X>,<Y>           Change the viewport for the current desktop.
#                      The X and Y values are separated with a comma.
#                      They define the top left corner of the viewport.
#                      The window manager may ignore the request.
# -n <NUM>             Change number of desktops.
#                      The window manager may ignore the request.
# -g <W>,<H>           Change geometry (common size) of all desktops.
#                      The window manager may ignore the request.
# -h                   Print help.
##################################################################
## xdotool
xdotool getmouselocation | awk '{print $1}' | tr -d 'x:'  # 输出当前鼠标的 x 坐标
