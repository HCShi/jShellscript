#!/bin/bash
# Path to Oh My Fish install.
set -q XDG_DATA_HOME
  and set -gx OMF_PATH "$XDG_DATA_HOME/omf"
  or set -gx OMF_PATH "$HOME/.local/share/omf"
# Load Oh My Fish configuration.
source $OMF_PATH/init.fish
##################################################################
## Proxy (/etc/environment 可以 System -> Network -> Proxy 生成, 也可以手动添加, 手动添加要去掉 set -gx)
##################################################################
# set -gx ALL_PROXY "https://192.168.1.13:8080/"  # 可以是小写
# set -gx HTTP_PROXY "http://192.168.1.13:8080/"
# set -gx HTTPS_PROXY "https://192.168.1.13:8080/"
# set -gx FTP_PROXY "ftp://192.168.1.13:8080/"
# set -gx SOCKS_PROXY "socks://192.168.1.13:8080/"
##################################################################
## /etc/bash.bashrc
##################################################################
set -gx GREP_COLOR '01;37;46'   # color grep matches 蓝底白字加粗
set -gx LD_LIBRARY_PATH $LD_LIBRARY_PATH /usr/local/lib
set -gx PATH /home/$USER/github/jLife/bin $PATH
set -gx PATH /home/$USER/github/jShellscript/bin $PATH
set -gx PATH /home/$USER/github/jShellscript/bin/ctf $PATH
set -gx PATH /home/$USER/github/jShellscript/bin/game $PATH

# 各种尝试了用 python 修改父进程的环境以后发现 alias 不能用, 只能在这里修改了, 每个目录下放一个脚本...
# 其实用 `` 来使用那些命令就可以切换目录了, 但还是不够方便
set -gx PATH /home/$USER/github/jShellscript/bin/template $PATH  # for python
source /home/$USER/github/jShellscript/bin/alias_fish /home/$USER/github/jShellscript/bin/template/
set -gx PATH /home/$USER/github/jShellscript/template $PATH      # for shellscript
source /home/$USER/github/jShellscript/bin/alias_fish /home/$USER/github/jShellscript/template/
set -gx PATH /home/$USER/github/jTemplate/lisp/elisp $PATH       # for elisp
source /home/$USER/github/jShellscript/bin/alias_fish /home/$USER/github/jTemplate/lisp/elisp/
set -gx PATH /home/$USER/github/jTemplate/latex $PATH            # for latex
source /home/$USER/github/jShellscript/bin/alias_fish /home/$USER/github/jTemplate/latex/
set -gx PATH /home/$USER/github/jWeb/template $PATH              # for html, css, js, jquery ...
source /home/$USER/github/jShellscript/bin/alias_fish /home/$USER/github/jWeb/template/

set -gx PATH /home/$USER/github/others/ctf-tools/bin $PATH
# set -gx PATH /usr/local/texlive/2016/bin/x86_64-linux $PATH
set -gx PYTHONPATH /home/$USER/github/jShellscript/bin/pythonpath $PYTHONPATH
set -gx PYTHONPATH /home/$USER/github/jShellscript/bin/template/src/jptsdn $PYTHONPATH  # for SDN
set -gx NODE_PATH $HOME/github/jShellscript/bin/nodepath/ $NODE_PATH
set -gx JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64 $JAVA_HOME
set -gx HISTCONTROL ignorespace  # 前面带空格的命令不记录到历史
# set -gx LC_ALL "en_US.UTF-8"
# set -gx LC_CTYPE "en_US.UTF-8"
set -gx LC_CTYPE zh_CN.UTF-8  # emacs GUI 输入中文要用这个, 终端里本来就可以输入中文, 放到 /etc/environment (Ubuntu 16.04 后才有的文件)
# set -gx HTTP_PROXY 'http://192.168.1.13:8080'  # 编辑 System Setting -> Network -> proxy 会自动保存到 /etc/environment
# set -gx EDITOR vim  # 加上这个以后好多 emacs 的快捷键用不了
##################################################################
## django & virtualenv & virtualenvwrapper & conda & pyenv; 最终选择的是 anaconda
##################################################################
set -gx WORKON_HOME $HOME/.virtualenvs  # python-virtualenvwrapper 环境变量
set -gx PROJECT_HOME $HOME/workspace    # virtualenvwrapper 的工作路径, mkproject 使用
# 下面的 source 用 virtualenvwrapper 的时候取消注释, 用 miniconda3 的时候要注释掉, 而且 source 启动很慢
# source /usr/share/virtualenvwrapper/virtualenvwrapper.sh  # 这条命令之后才能使用 mkvirtualenv 等命令
set -gx PATH /home/$USER/anaconda3/bin $PATH  # for anaconda
# set -gx PATH /home/$USER/miniconda3/bin $PATH   # for miniconda, 就是靠环境变量把我系统的 python 覆盖掉的
# set -gx PYENV_ROOT "$HOME/.pyenv"   # pyenv 用到的环境变量
# set -gx PATH $PYENV_ROOT/bin $PATH  # pyenv 可执行文件
# eval "$(pyenv init -)"             # enable shims and autocompletion, 安装 pyenv 后, 将这两句话取消注释
# eval "$(pyenv virtualenv-init -)"
##################################################################
## Latex, 这个好像不起作用, ~/texmf/tex/latex/local/ 默认放在这里
##################################################################
set -gx TEXINPUTS ".:~/github/jShellscript/bin/latexpath:"  # 前边那个点可以不加, 最后 : 必须写; 存放 .cls, .sty 文件的地方; 这行其实不起作用 OnO
# ln -s ~/github/jShellscript/bin/latexpath/14thcoder_thesis.cls ~/texmf/tex/latex/local/14thcoder_thesis.cls
# 每次调试哪个文件就这样软连接一下, 调试好以后就删除软连接, 然后执行 ./config 把整个目录复制过去
##################################################################
## nvm, source 启动有点慢, 用的时候在打开; n(目前嫌弃 nvm 使我的 shell 启动速度太慢)
##################################################################
set -gx NVM_DIR "$HOME/.nvm"  # install.sh will clone the nvm repository to ~/.nvm
# 去 zsh 里面看一下, 这里删掉了好多...
set -gx N_PREFIX $HOME/.node_n  # for n
set -gx PATH $HOME/.node_n/bin $PATH  # 这样才能覆盖掉系统的, 如果用默认的 N_PREFIX /usr/local 就不用这个 PATH 了
set -gx NODE_PATH $HOME/.node_n/lib/node_modules $NODE_PATH
##################################################################
## Go env
##################################################################
# set -gx GOPATH $HOME/workspace
# set -gx PATH $PATH $GOPATH/bin
##################################################################
## UTF8
##################################################################
# 和 Docker 容器不兼容
# LANG "en_US.UTF-8"
# LC_COLLATE "en_US.UTF-8"
# LC_CTYPE "en_US.UTF-8"
# LC_MESSAGES "en_US.UTF-8"
# LC_MONETARY "en_US.UTF-8"
# LC_NUMERIC "en_US.UTF-8"
# LC_TIME "en_US.UTF-8"
# LC_ALL "en_US.UTF-8"
