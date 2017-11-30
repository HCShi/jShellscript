#!/bin/bash
# 电脑初始化 git, 用 jPC/git_config
git clone https://github.com/coder352/jvim.git vim                 # 重命名
git clone --branch v1.9 https://github.com/ethicalhack3r/DVWA.git  # 下载指定 Tag
git clone --depth=1 https://github.com/coder352/jvim.git vim       # 只下载最近一次修改后的
git checkout *                                                     # 不小心改了别人的, 这个命令可以恢复
git push origin master
git add .
git add --all
git commmit -m "update"

git tag  # 查看都有哪些标签
git checkout <tag>  # 根据上面查到的标签来切换

git ls-remote  # 查看远端 repository
git remote -v  # 查看远端 repository

##################################################################
## 本地配置
git config --global user.name "Ruipeng Jia"
git config --global user.email 352111644@qq.com
# 添加代理
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
# 修改/添加 远程项目地址
git remote remove oritin
git remote add origin git@github.com:coder352/jVim.git
git remote add origin https://github.com/coder352/jVim.git
