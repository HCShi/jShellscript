#!/bin/bash
##################################################################
## apt-get
# http://askubuntu.com/questions/100503/how-are-packages-suggested-and-what-is-the-difference-between-extra-and-new-pack
# There are three basic ways an Ubuntu package can depend or pull in other packages:
#
# Depends - this is a hard dependency, the program you are installing requires this other package to run. If you try to uninstall one of these packages, your program will be uninstalled with it.
# Recommends - this is a package the is needed or recommended for normal use of the program you are installing, but the program will work without it. By default Ubuntu will install these (unless disabled with --no-install-recommends) but it won't complain if you remove them later on.
# Suggests - this is a package that can enhance the program you are installing but is not considered a part of normal use. These packages are not installed by default (unless enabled with --install-suggests) and would be considered like a "hey, you might find these interesting" from the package developer.
# By default, Ubuntu installs packages marked as depends and recommends, and all these will be listed as extra packages, unless you specified some of them explicitly on the command line.
#
# Packages marked as NEW are all the packages that are about to be installed, i.e. the packages specified on the command line and all extra packages.
sudo apt check             # 检查是否有损坏的依赖
sudo apt list --installed  # 查看已经安装的包, 这个很厉害
sudo apt install -f        # 修复依赖关系(depends) 的命令, 就是假如你的系统上有某个 package 不满足依赖条件, 这个命令就会自动修复

sudo apt-cache search {package}    # 搜索包, 查看那些可安装
sudo apt-cache show {package}      # 获取包的相关信息, 如说明、大小、版本等
sudo apt-cache depends {package}   # 查看有哪些依赖项
sudo apt-cache rdepends {package}  # 查看该包被哪些包依赖

sudo add-apt-repository ppa:teejee2008/ppa  # 添加第三方
sudo apt-get install ppa-purge
sudo ppa-purge ppa:teejee2008/ppa

sudo apt-file search filename   # 查找 filename 属于哪个软件包
sudo apt-file list packagename  # 列出软件包的内容
sudo apt-file update            # 更新 apt-file 的数据库

sudo apt install {package}              # 安装上一步查看到的, 会去下载
sudo apt install {package} --reinstall  # 重新安装包
sudo apt source {package}               # 下载该包的源代码
sudo apt build-dep {package}            # 安装相关的编译环境

sudo apt remove {package}              # 删除包
sudo apt remove --purge {package}      # 删除包, 包括删除配置文件等
sudo apt purge {package}               # 同上
sudo apt autoremove --purge {package}  # 删除包及其依赖的软件包 + 配置文件等
sudo apt clean                       # 清理下载文件的存档
apt-get autoclean                    # 只清理过时的包

sudo apt update           # 更新源
sudo apt upgrade -u       # 更新已安装的包
sudo apt dist-upgrade     # 升级系统
sudo apt dselect-upgrade  # 使用 dselect 升级
##################################################################
## dpkg, Debian package 的简写
# 通常情况下, linux 会这样放软件的组件:
# 程序的文档   -> /usr/share/doc
# 程序         -> /usr/share
# 程序的启动项 -> /usr/share/apps
# 程序的语言包 -> /usr/share/locale
dpkg -L softwarename         # 查询软件的安装位置, 这里的软件名就是你 apt-get install 后面的那个名字
dpkg -l | grep name* | more  # 查询所有软件, list all package
dpkg -s softname             # 查询软件的相关信息
dpkg -i sogoupinyin_2.0.deb  # 安装软件
dpkg -L sougoupinyin         # 列出与该包先关联的文件,查看软件安装到什么地方,在/user/share
dpkg -l sougoupinyin         # 显示包的版本
dpkg -r sougoupinyin         # 移除软件 (保留配置)
dpkg -P package              # 移除软件 (不保留配置)
dpkg -s package              # 查找包的详细信息
dpkg -c package.deb          # 列出 deb 包的内容
dpkg --unpack package.deb    # 解开 deb 包的内容
dpkg -S keyword              # 搜索所属的包内容
dpkg --configure package     # 配置包
dpkg --listfile softname     # 查看系统中输入软件的文件

dpkg -l | grep -i ftp
rpm -qa | grep -i *ftp*  # redhat 用这个

## 有道词典安装...
wget youdao-dict_1.1.0-0-ubuntu_amd64.deb  # 2015 年更新
mkdir youdao-dict
sudo dpkg -X youdao-dict_1.1.0-0-ubuntu_amd64.deb youdao-dict  # 把该 deb 包解压到 youdao-dict 目录
sudo dpkg -e ./youdao-dict_1.1.0-0-ubuntu_amd64.deb youdao-dict/DEBIAN  # 解压 deb 包中的 control 信息 (包的依赖就写在这个文件里面)
sudo vi ./youdao-dict/DEBIAN/control  # 编辑 control 文件, 删除 Depends 里面的 gstreamer0.10-plugins-ugly
sudo dpkg-deb -b youdao-dict youdaobuild.deb  # 重新打包
sudo gdebi youdaobuild.deb  # 安装重新打包的安装包; 已经安装 gdebi 包管理器, 可以使用如下命令安装, 自动解决依赖问题
# 下面使用 dpkg 进行安装, 可能还会报错, 用 apt install -f 来修复即可
sudo dpkg -i youdaobuild.deb  # 会报错
sudo apt install -f  # 出现缺少的依赖使用如下命令安装所需依赖
sudo dpkg -i youdaobuild.deb  # 依赖安装完成后再次键入如下命令进行安装
