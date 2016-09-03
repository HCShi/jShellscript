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


