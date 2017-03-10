This is a script of my Ubuntu

## Install
先安装 zsh
见 jPC/pc_config

## Config the script
read the config
下面是自己搭建的过程
详细步骤见我的[here](http://blog.csdn.net/u014015972/article/details/50647504)

## for server
mkdir ~/github && cd github && git clone https://github.com/coder352/shellscript
./config
vim ~/.zshrc
:%s/coder352/servername

## 调用关系
先调用 zshrc 文件
再从 zshrc 中依次调用 ./mybashrc ~/.config/jshellscript(第三方,没有该目录就不会调用) ./mybashrc ./myzshrc

## third-part script
朕在 ./zshrc 中标注了第三方的位置, 即: ~/.config/jshellscript/
文件名为 *.sh

## 科普 各种 profile 的作用
我们可以明白的是：针对于用户的配置，应该将配置信息写入~/.bashrc文件
1. /etc/profile:为系统的每个用户设置环境信息,当用户第一次登录,文件被执行.从/etc/profile.d目录的配置文件中搜集shell的设置.默认调用/etc/bash.bashrc
2. /etc/bashrc:为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取.
3. ~/.bash_profile:每个用户都可使用该文件输入专用于自己使用的shell信息,用户登录时,文件仅执行一次!默认情况下,设置一些环境变量,执行用户的.bashrc文件
4. ~/.bashrc:该文件包含专用于你的bash shell的bash信息。
5. ~/.bash_logout:当每次退出系统(退出bash shell)时,执行该文件.
