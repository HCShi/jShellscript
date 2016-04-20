This is a script of my Ubuntu
## Config the script
```
cd ~
git clone https://github.com/coder352/shellscript.git
sudo vim /etc/bash.bashrc
```
在最后添加下面两句话
```
. /home/coder352/shellscript/myscript
export PATH=/home/coder352/shellscript/bin:$PATH
```
如果用的是zsh的话要在 ~/.zshrc 中添加
执行上面的命令就可以执行了，下面是自己搭建的过程
详细步骤见我的[here](http://blog.csdn.net/u014015972/article/details/50647504)

