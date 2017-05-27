#!/bin/bash
########################################
## 系统操作
########################################
alias allproxy='export all_proxy="https://192.168.1.13:8080"'
function bjclip; b64 -e $1 | jclip; end
alias echobool='echo $status'
alias pbjclip='clippaste | xargs -I {} b64 -e {} | jclip'
function cpbjclip; b64 -e $1 | jclip; and clippaste | xargs -I {} b64 -e {} | jclip; end
alias cpgitignore='cp ~/github/jTemplate/src/my.gitignore .gitignore'
alias cman='LANG="zh_CN.utf8" man'
function cps; set tmp1 `pwd`; and set tmp2 "/"; and set tmp3 "$1"; and set tmp $tmp1$tmp2$tmp3; end  # tmp=${tmp1}&{tmp2}&{tmp3}
function cpd; cp $tmp $1; end
alias day="/bin/date '+%Y-%m-%d.%H-%M-%S'"  # "/bin/date '+%Y-%m-%d'"  # 另一种形式
alias dub='du -b'  # ls du 等命令默认以 K 为单位, 很坑
alias dush='du -sh'  # dush 当前目录大小, dush a.txt 文件大小, dush directory 目录大小
alias findname='find -iname'  # exapmle: findname "*.txt"
function ggc; google-chrome http://127.0.0.1:$1; end
alias grep="grep -iI --color=always"  # google: grep exclude binary file || grep ignore spcific directory
function grepf; find -iname $2 | xargs grep -riIn --color=always $1; end  # example: grepf hello "*.md"
alias greps="grep -riIn --color=always"  # example: greps hell
alias grepsd="grep -riIn --color=always --exclude-dir"  # example: grepsd .git hello
alias grepsls='ls | grep'
function pdfgrepinr; pdfgrep -inr $1 *; end
function ju8;
    # iconv -f ISO-8859-1 -t UTF-8 $1 > $1.tmp  # file $1 显示的是 ISO-8859, 但没用
    iconv -f gbk -t utf-8 $1 > $1.tmp  # gbk 中文通用
    mv $1.tmp $1; end  # example: ju8 file, file from Windows
alias ii='clear'  # 因为 C-L 被 tmux 占了(自己设置), cls 又太麻烦, ll 默认是 ls 系列的  # 后来发现不需要了, 只要 Ctrl + A + L, 不要松开 Ctrl  # 再后来 l 又被resize占了...
alias kkm='make clean'
alias llv='ll -v'  # -v 11 不会排在 2 前面了
alias lsv='ls -v'
function md5sumupper; md5sum $1 | tr "a-z" "A-Z"; end  # md5sum <file>
function mkdircd; mkdir $1; and cd $1; end
alias nau='nautilus .'
function shut; shutter -s -e -n -o /home/coder352/Desktop/Another\ link\ to\ Share/$1.jpg; end
# shut 1 就会生成 1.jpg 到指定路径下, 后面不加参数也会交互式截图, 但不会生成文件, Ctrl + Alt + A 生成 tmp.jpg
alias suroot='sudo su root'
alias terminalnew='gnome-terminal --working-directory=`pwd`'
# 这个 unzip 的参数只有 ubuntu 默认有
alias unzipo='unzip -O cp936'  # 对于乱码情况, 最好用 lsar 和 unar
alias unrarx='unrar x'  # 将rar解压到当前文件夹,全路径
alias wgetproxy='wget -e use_proxy=yes -e http_proxy=127.0.0.1:1080'
alias xopen="xdg-open"
# alias zd='youdao'  # 界面有点丑, 但挺快 sudo pip install youdaodict
alias zd='python ~/github/others/ydcv/ydcv.py'  # zd hello, zd 'hello world'
alias fy='sdcv -c'  # sudo apt-get install sdcv

##################################################################
## Program Manage
##################################################################
function killport; sudo kill (sudo lsof -t -i:$1); end
# 下面是查看端口进程
function lsofi; sudo lsof -i :$1; end  # 得到的是 PID, 交给下面 psfp 处理, 用 sudo, 否则显示不全
alias psfp='ps -fp'  # psfp 25 查看 25 号 PID 的程序
function psfplsofi; sudo ps -fp (sudo lsof -t -i :$1); end
alias pse='ps -e'
alias pself='ps -elf'
alias pseg='ps -e | grep -in --color=always'
alias pselfg='ps -elf | grep -in --color=always'
function qkills; ps -ef | grep $1 | awk '{print $2}' | sudo xargs kill -9; end  # qkill python # -elf 会显示好多不需要的进程
function qkills  # qkills python  # elf 会有很多无用信息
    ps -ef | grep $1 | awk '{print $2}' | sudo xargs kill -9  # 有些命令要 root 权限
end  # 很无奈, grep 在双引号里不能用, awk print 在双引号里也不能用
function qkill;  # qkill python  # elf 会有很多无用信息
    ps -ef | grep $1 | awk '{print $2}' | xargs kill -9; end  # 很无奈, grep 在双引号里不能用, awk print 在双引号里也不能用

##################################################################
## Network Manage 1.HostScan 2.PortScan(ServerScan) 3.RouteScan
##################################################################
alias myip="ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v 192.168.56.1|grep -v inet6|awk '{print $2}'|tr -d 'addr:'"
alias ncme='netcat -vz localhost 1-1024 2>&1 | grep succeeded'  # 查看 root 端口
alias ncmeall='netcat -vz localhost 1-65535 2>&1 | grep succeeded'  # 查看所有端口
alias netstatantp='netstat -antp'
alias netstatantpg='netstat -antp | grep -in --color=always'
alias netstatanup='netstat -anup'
alias netstatanupg='netstat -anup | grep -in --color=always'
alias nmapme='nmap -v localhost'  # sudo apt-get install nmap
alias pbd='ping www.baidu.com'
alias pggip='ping 8.8.8.8'
alias speedtest='speedtest-cli --simple'  # sudo apt-get install speedtest-cli 测试上传下载速度
alias tcpdump='tcpdump -nn -XSltv'

##################################################################
## Nginx PHP Server
##################################################################
alias cnginx='sudo nginx -p $PWD'
alias snginx='sudo nginx -s stop'
# Ubuntu 直接输入 可执行的 .py 文件不是执行它, 而是打开, 以前 14.04 还不是的啊
# alias mcurl='python ~/github/jShellscript/bin/curl.py'  # 是下面的 py=vi 搞得鬼
# 开启 fgcgi, 用 nginx 和 php 时要开启
alias sfcgi='sudo /usr/bin/spawn-fcgi -a 127.0.0.1 -p 9000 -C 5 -u www-data -g www-data -f /usr/bin/php-cgi7.0 -P /var/run/fastcgi-php.pid'
alias sphpserver='php -S localhost:9999'
alias phpserver='google-chrome http://localhost:9999/'
alias lnsphpmyadmin='sudo ln -s /usr/share/phpmyadmin /home/coder352/web/phpmyadmin'
alias logphpmyadmin='google-chrome localhost/phpmyadmin'
alias clsweb='rm ~/web/*'

# Hexo
alias loghexo='google-chrome http://localhost:4000'

# Python Server
alias pythonsimpleserver="python -m SimpleHTTPServer"  # 开启8000端口
alias python3httpserver='python3 -m http.server'  # open 8000 port

##################################################################
## Python
##################################################################
# alias python='/usr/bin/python2'
# alias python='python3'
# alias bpython='bpython3'
# alias pip='pip3'
# ascii 和 char 之间转换
function pord; python -c "print ord(\"$1\")" }; end  # example: pord A  # 65  # ord(char/unichr)
function pchr; python -c "print chr(int(\"$1\"))"; end  # example: pchr 65  # A  # chr(num)
function punichr; python -c "print unichr(int(\"$1\"))"; end  # example: pchr 65  # A  # unichr(0-65535)
# 进制转换
function phex; python -c "print hex(int(\"$1\"))"; end  # example: phex 16  # 0x10
function pbin; python -c "print bin(int(\"$1\"))"; end  # example: pbin 16  # 0b10000
function poct; python -c "print oct(int(\"$1\"))"; end  # example: poct 16  # 020
function pint16; python -c "print int(\"$1\", 16)"; end  # example: pint16 0x10  # 16  # int('string', base)

# 生成随机字符
# function prans; python -c "import random, string; print ''.join(random.sample(string.ascii_letters + string.digits + '()~!@#$%^&*-+=|\'{}[]:;<>,.?/', $1))"; end  # prans 32
# function pransd; python -c "import random, string; print random.choice(string.ascii_letters) + \
    # ''.join(random.sample(string.ascii_letters + string.digits + '()~!@#$%^&*-+=|\'{}[]:;<>,.?/', int(\"$1\") - 1))"; end  # 以字母开头, pransd 32
# 普通运行
function rpy; python -c "print $1" }; end  # ryp 0xffffd6cc-0xffffd680, 不用带引号
alias pyte='cd ~/Documents/thiscandel; and vim te.py'

# 安装 不用 sudo 权限容易有问题, -H 指定 HOME 目录为目标的, 默认是 阿里源
alias pypyinstall='sudo -H pypy -m pip install'
alias pythoninstall='sudo -H python -m pip install'
alias python3install='sudo -H python3 -m pip install'
alias pipali='pip install --index http://mirrors.aliyun.com/pypi/simple/'

# help package
function pyhelp; python -c "help('$1')"; end  # eg: pyhelp socket, pyhelp argparse

# 代理问题, Missing dependencies for SOCKS support.
alias pipproxyclear='unset all_proxy; and unset ALL_PROXY'
# unset all_proxy
# unset ALL_PROXY

##################################################################
## IDE
##################################################################
alias pycharm='/home/coder352/JetBrains/pycharm-2016.3.2/bin/pycharm.sh'

##################################################################
## JavaScript, ln -s
##################################################################
alias ppw='pug -P -w'  # for pug 实时编译
alias cwc='coffee -wc'  # for coffee 实时编译
alias cbpe='coffee -bpe'

alias lnsbootstrap='ln -s ~/github/jWeb/CDN/bootstrap .'  # 进项目的根目录执行
alias lnsjquery='ln -s ~/github/jWeb/CDN/jquery .'
alias lnspure='ln -s ~/github/jWeb/CDN/pure .'
alias lnsuikit='ln -s ~/github/jWeb/CDN/uikit .'
alias lnsvue='ln -s ~/github/jWeb/CDN/vue .'
alias lnsd3='ln -s ~/github/jWeb/CDN/d3 .'
alias lnsimage='ln -s ~/github/jImage .'
alias npmhttpfr='sudo npm config set proxy http://192.168.1.13:8080 -g; and sudo npm config set https-proxy http://192.168.1.13:8080 -g'
alias npmhttp='sudo npm config set proxy http://localhost:1080 -g; and sudo npm config set https-proxy http://localhost:1080 -g'
alias npmnohttp='sudo npm config rm proxy -g'
alias cnpm="npm --registry=https://registry.npm.taobao.org \
--cache=$HOME/.npm/.cache/cnpm \
--disturl=https://npm.taobao.org/dist \
--userconfig=$HOME/.cnpmrc"
# npm config get proxy; npm config set proxy null; npm config delete proxy; npm config set https-proxy null; npm config set strict-ssl false
# npm config set registry http://registry.npmjs.org/  # 就是这句和下面那句帮我修复了 npm
# npm cache clean

##################################################################
## mysql, memcache, redis
##################################################################
alias logmysql='mysql -h 127.0.0.1 -u root -p'
alias memcachedme='memcached -d -m 256 -u root -l localhost -c 256 -P /tmp/memcached.pid'  # 开启 Memcached
alias telmemcached='telnet localhost 11211'  # 默认是11211端口
# redis-cli 就可以直接连接本地的数据库了, apt install redis-tools

##################################################################
## Matlab && Octave
##################################################################
alias mmatlabr="matlab -nosplash -nodesktop -r"  # mmatlabr '1 + 2'
alias mmatlab="matlab -nosplash -nodesktop"  # 进入命令行
# alias mmatlabrs; matlab -nosplash -nodesktop -nodisplay -r "$1" }; end  # mmatlabrs 1, 不要后缀, 适合没有图像操作的
function mmatlabrsgui; matlab -r "$1"; end  # mmatlabrsgui 1, 不要后缀, 适合有图形操作的, 会进入图形界面
# -nosplash表示不加载启动界面
# -nodesktop表示不加载GUI界面
# -r表示运行Matlab命令行（MATLAB_command）
# file_base_name表示文件名，但不包含文件扩展名
alias moctave='octave --no-gui'  # 进入命令行, 比 Matlab 友好多了
alias moctaveq='octave --no-gui -q'
# alias moctaver='octave --no-gui'  # 因为 Octave 启动速度非常快, 所以就没有执行单条命令的 alias
alias moctavers='octave --no-gui -q --persist'  # moctavers 1.m, 这个要带后缀
alias moctaversgui='octave -q --persist'  # 带后缀

##################################################################
## player
##################################################################
alias mpa="ls > music.lst; and mplayer -playlist music.lst"
alias mps="mplayer -playlist music.lst"
alias mpm="ls > music.lst"

########################################
## cd 相关操作
########################################
alias cddel="cd ~/Documents/thiscandel"
alias cdesktop='cd ~/Desktop'  # cddesktop 会和 cddel 冲突
# alias cdhistory="cd `tail -n 2 ~/.zsh_history | head -n 1 | awk '{print $3}'`"
function cdhistory; cd `tail -n 2 ~/.zsh_history | head -n 1 | awk '{print $3}'`; end  # 已弃用, 刚写出来就弃用了
# alias cdhtml="cd /media/coder352/文档/HTML"
alias cdhtml="cd ~/github/Some-Markdown-in-Sublime"
alias cdhtmlhexo="cd ~/github/Some-Markdown-in-Sublime/hexo"
alias cdmythesis="cd ~/Documents/thiscandel/thesis"
alias cdjhexo="cd ~/github/jHexo"
alias cdjhexoothers='cd ~/github/others/Blog_backup'
alias cdjhexoqrsync='cd ~/github/jQrsyncHexo'
alias cdjknowledge='cd ~/github/jKnowledge/'
alias cdjlife='cd ~/github/jLife'
alias cdjpc="cd ~/github/jPC"
alias cdjpcsrc='cd ~/github/jPC/src'
alias cdjpcsrcchromeextend='cd ~/github/jPC/src/Chrome_extend/myExtends'
alias cdjpcsrctmux="cd ~/github/jPC/src/tmux"
alias cdjqlcoder="cd ~/github/jqlcoder"
alias cdjserver="cd ~/github/jServer"
alias cdjshellscript="cd ~/github/jShellscript"
alias cdjshellscriptbin='cd ~/github/jShellscript/bin'
alias cdjshellscriptbinctf='cd ~/github/jShellscript/bin/ctf'
alias cdjshellscriptbintemplate='cd ~/github/jShellscript/bin/template'
alias cdjshellscriptbintemplatesrc='cd ~/github/jShellscript/bin/template/src'
alias cdjshellscripttemplate="cd ~/github/jShellscript/template"
alias cdjshellscripttemplatesrc="cd ~/github/jShellscript/template/src"
alias cdspacemacs="cd ~/.spacemacs.d"
alias cdjspacemacs="cd ~/github/jSpacemacs"
alias cdjspacemacsme="cd ~/github/jSpacemacs/layers/14thcoder"
alias cdjspacemacsmetheme="cd ~/github/jSpacemacs/layers/14thcoder/theme"
alias cdjspacemacsmesnippet="cd ~/github/jSpacemacs/layers/14thcoder/yasnippet"
alias cdjtemplate='cd ~/github/jTemplate'
alias cdjtemplatedatabase="cd ~/github/jTemplate/database"
alias cdjtemplatedatabasemongodb="cd ~/github/jTemplate/database/mongodb"
alias cdjtemplatedatabasemysql="cd ~/github/jTemplate/database/mysql"
alias cdjtemplatedocker='cd ~/github/jTemplate/docker'
alias cdjtemplatepython="cd ~/github/jTemplate/python"
alias cdjtemplatesrc='cd ~/github/jTemplate/src'
alias cdjtemplatetex='cd ~/github/jTemplate/tex'
alias cdjtemplatewebjavascript="cd ~/github/jTemplate/web/javascript"
alias cdjtemplatewebjavascriptwebgl="cd ~/github/jTemplate/web/javascript/webgl"
alias cdjtemplatewebjquery="cd ~/github/jTemplate/web/jquery"
alias cdjtemplatewebphp="cd ~/github/jTemplate/web/php"
alias cdjtemplatewebwebgl="cd ~/github/jTemplate/web/webgl"
alias cdjemacs='cd ~/github/jEmacs/emacsd'
alias cdjemacslisp='cd ~/github/jEmacs/emacsd/lisp'
alias cdjvim="cd ~/github/jVim/vimrc"
alias cdjvimhome="cd ~/.vim/jvim/vimrc"
alias cdjvimlatex="cd ~/github/jVim/ftplugin/latex-suite/templates"
alias cdjvimsnippets="cd ~/github/jVim/UltiSnips"
alias cdjvscode="cd ~/github/jVSCode/User"
alias cdjvscodehome="cd ~/.config/Code/User/"
alias cdjwebtemplatesrc='cd ~/github/jWeb/template/src'
alias cdshare="cd /media/coder352/Documents/Share"
alias cdshareshipin="cd /media/coder352/Documents/Share/视频/"
alias cdshareshiyanlou="cd /media/coder352/Documents/Share/实验楼"
alias cdzshshortcuts="cd ~/.oh-my-zsh/plugins"
alias cdvedio="cd /media/coder352/文档/Share/视频"

# snippets
alias cdvimultisnippets='cd ~/.vim/plugged/vim-snippets/UltiSnips/'  # snippets using UltiSnips format  # 优先级低
alias cdvimsnippets='cd ~/.vim/plugged/vim-snippets/snippets/'  # snippets using snipMate format  # 优先级低
alias cdemacssnippets='cd ~/.emacs.d/elpa/yasnippet*/snippets/'
# 上面还有一个jvimsnippte

# template
# alias cdjpt='cd ~/github/jShellscript/bin/template/src'
# alias cdjptfunction='cd ~/github/jShellscript/bin/template/src/jptfunction'
# alias cdjptnumpy='cd ~/github/jShellscript/bin/template/src/jptnumpy'
# alias cdjstfunction='cd ~/github/jShellscript/template/src/jstfunction'
alias cdnankai='cd /media/coder352/Documents/Share/知识库/nankai/202.113.29.3/nankaisource'

# path
alias cdpythonpath='cd ~/github/jShellscript/bin/pythonpath'
alias cdnodepath='cd ~/github/jShellscript/bin/nodepath'
alias cdlatexpath='cd ~/github/jShellscript/bin/latexpath'
alias cdlatexcls="cd ~/texmf/tex/latex/local"

# Windows
alias cdwendang="cd /media/coder352/文档"

##################################################################
## vim 相关操作  进目录是为了退出时能够 git
##################################################################
alias vimq='vim -u NONE'  # 不加载配置文件
alias vimms="cd ~/github/jShellscript; and vim my_zsh_alias"
# alias vimtmuxshorcuts="cd ~/github/jPC/src/tmux; and vim README.md"
# alias vimzshshortcutgit="cd ~/.oh-my-zsh/plugins/git; and vim git.plugins.zsh"
# php.vim 中补全的更新, 中间的括号太乱了
# alias updatephpfunlist='curl http://www.php.net/manual/en/indexes.functions.php | sed '/class="index"/!d' | grep -oP '>[^<]+</a> - .*</li>' | cut -b2- | sed 's~</a> - ~ ; ~; s~</li>$~~' > php-funclist.txt'
# 下面这句话会在当前目录下生成一个 vim 启动时打开文件的顺序以及事件节点, 可以查看是哪里耗费启动时间
# alias vimtimefile = "vim --startuptime timefile the_file_you_want_to_edit"

# 简化配置
alias vimclear="cp ~/.vimrc.clear ~/.vimrc"
alias vimnormal="cp ~/.vimrc.normal ~/.vimrc"

##################################################################
## Emacs 相关配置
##################################################################
function spaceemacscompile; emacs --batch --eval '(byte-recompile-directory "~/.spacemacs.d/" 0)'; end  # 最好不要用, 会出现一些奇怪的错误
function emacscompile; emacs --batch --eval '(byte-recompile-directory "~/.emacs.d" 0)'; end  # 直接执行 .el 速度还行, findname "*.elc*" | xargs rm 将 .elc 删除
alias eng='emacs --debug-init'
alias engq='emacs --debug-init -q'  # -q 是不加载配置文件
alias enwq='emacs -nw -q'
alias ens='emacs --no-site-file --script'  # 执行单独的 .el 文件
# Server
alias ess='emacs --daemon'  # 开启一个服务端
alias esk='emacsclient -e "(kill-emacs)"'  # 关闭服务端
# alias esr='emacsclient -e "(server-start)"'  # 重启服务端, 这个不能用
alias esr='emacsclient -e "(kill-emacs); and emacs --daemon"'  # 重启服务端
alias eservername='emacs --eval "(setq server-name \"$1\")" --daemon'  # emacsservername foo; 创建 Name 为 foo 的 Emacs 服务端
alias ecl='emacsclient'  # ecl a.py; 如果开的是 GUI 界面的服务器, 会进入 GUI; 如果开的是 ess(terminal), 会进入终端
alias vom='emacsclient -nw'  # vom a.py; fn 退出
alias voms='emacsclient -nw -s'  # voms foo; 连接 server-name 为 foo 的 emacs 服务器
# 下面几个是调试别人的配置文件时候方便
alias lnsjspacemacs='ln -s ~/github/jSpacemacs ~/.spacemacs.d'
alias lnsjemacs='ln -s ~/.emacs.d.jrp ~/.emacs.d'
alias lnszlspacemacs='ln -s ~/github/others/spacemacs-private ~/.spacemacs.d'
alias lnsmath='ln -s ~/github/jImage/Math .'
alias cdemacslayer='cd ~/.emacs.d/layers/'

##################################################################
## tmux 还没测试
##################################################################
alias tmuxkill="tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill"

##################################################################
## Latex 记录一些常用的 package, 方便查 api
##################################################################
function lnslatex; ln -s ~/github/jShellscript/bin/latexpath/{$1} ~/texmf/tex/latex/local/; end
alias rmlatex="rm *.log & rm *.fmt & rm *.aux & rm *.gz & rm _region_.tex & rm *.toc & rm *.bcf & rm *.lof & rm *.lot & rm *.mintedcmd & rm *.out & rm *.run.xml"
alias rmlatexpdf="rm *.pdf"

alias cdlatexdoc="cd /usr/share/texlive/texmf-dist/doc/latex"
alias latexsheet="texdoc latexcheat"  # 查看常用方法, 2 页
alias latex2e="texdoc latex2e"  # 可以查看 api, 比较全
alias latexfancyhdr="texdoc fancyhdr"

########################################
## git 相关操作 要被淘汰了 via oh my zsh
########################################
# some repository
alias gis="git status"
alias gia="git add ."
alias gial='git add --all'
alias gicommit='git commit -m'
alias gilog='git log --oneline --decorate --graph --all'
alias gipush='git push origin master'
alias girev='git remote -v'
alias gid="git diff"  # 工作目录 vs 暂存区 (如果还没 add 进暂存区，则查看文件自身修改前后的差别)
alias gidc='git diff --cached'  # 暂存区 vs Git仓库 (表示查看已经 add 进暂存区但是尚未 commit 的内容同最新一次 commit 时的内容的差异)
# global
alias gitdep='git clone --depth=1'  # git shallow clone --depth=1 表示只下载最近一次的版本，使用浅复制可以大大减少下载的数据量
alias gitinfo='git config --global -l'  # 显示git相关配置信息
alias githttp="git config --global http.proxy 'socks5://127.0.0.1:1080'; and git config --global https.proxy 'socks5://127.0.0.1:1080'"  # 只针对 https://github.com/coder352/jvim.git 之类的
alias githttpno="git config --global --unset http.proxy; and git config --global --unset https.proxy"
alias gitssh='mv ~/.ssh/jconfig ~/.ssh/config'
alias gitsshno='mv ~/.ssh/config ~/.ssh/jconfig'
alias gitgit='git config --global core.gitproxy "git-proxy"'  # 这个的意思是用上面两种代理中的一种
alias gitgitno='git config --global --unset core.gitproxy'
##### 下面是 Github + Hexo + 七牛云
alias qrsync="~/github/others/qrsync/qrsync"  # 任意目录下执行

##################################################################
## Java && Opengl
##################################################################
alias eclipse='~/eclipse/java-neon2/eclipse/eclipse'
alias javac="javac -J-Dfile.encoding=utf8"
function opengl; g++ $1 -o gl -lGL -lGLU -lglut; and ./gl; end  # example: grepf hello "*.md"
#alias opengl='g++ -o gl -lGL -lGLU -lglut'  # 文件名必须放前面

########################################
## SDN Floodlight Ryu Mininet
########################################
alias fltg='google-chrome http://localhost:8080/ui/index.html'
alias flt="cd ~/github/floodlight/; and java -jar target/floodlight.jar"  # http://localhost:8080/ui/index.html 是 Floodlight 1.2 的主页
# net.floodlightcontroller.forwarding.Forwarding,\  # 下面两个命令中 noforwarding 是将这就话注释掉, 额, 好像只能删掉
alias cnf="cd ~/github/floodlight/src/main/resources/; and cp floodlightdefault.properties.noforwarding floodlightdefault.properties; and cd ~"
alias cff="cd ~/github/floodlight/src/main/resources/; and cp floodlightdefault.properties.forwarding floodlightdefault.properties; and cd ~"
alias rum="ryu-manager --verbose"
alias cdru="cd ~/github/ryu/ryu/app"
alias cdjtemplatepythonsdnryu="cd ~/github/jTemplate/python/sdn/ryuapp/"
alias cdjtemplatepythonmininet="cd ~/github/jTemplate/python/sdn/mininet"
# Mininet
alias sshxm="ssh -X mininet@192.168.56.101"  # scpmip 是将本机的 IP 传给 Mininet, scpm 是传文件到 Mininet
# sudomn 在 shellscript/bin 中有一个
# sudomn() { sudo mn --custom $1 --topo mytopo --controller=remote,ip=127.0.0.1,port=6653 --link tc,bw=10,delay=1ms --mac }
function sudomn; sudo mn --custom $1 --topo mytopo --controller=remote,ip=127.0.0.1,port=6653 --mac; end
# ovs-vsctl
alias ovsc='sudo ovs-vsctl'
alias ovscab='sudo ovs-vsctl add-br'
alias ovscdb='sudo ovs-vsctl del-br'
alias ovscap='sudo ovs-vsctl add-port'
alias ovscdp='sudo ovs-vsctl del-port'
alias ovscsc='sudo ovs-vsctl set-controller'

########################################
## SSH SCP
########################################
# VPS
alias sshaliyun="ssh root@115.28.247.19"  # 管理终端密码 367692
alias sshbanwagong="ssh root@45.78.9.29 -p 28484"
alias sshkali="ssh root@192.168.56.105" # passwd: asd
alias sshredhat="ssh root@192.168.56.101" # passwd: 123456
alias sshruanjianbei="ssh jrp@211.87.185.53 -p 22222" # passwd: Yr1Uwud6yH87kcJ8
alias sshteacher="ssh r12@121.251.254.208" # username: root; passwd: 123456
alias sshtencent='ssh root@115.159.88.186'
alias sshdocker='ssh root@(docker inspect -f "{{.NetworkSettings.IPAddress}}" (docker ps -a -q))'
# alias sshxm="ssh mininet@192.168.56.101" 因为要把本机IP传过去，所以写成可执行文件了
# 很坑的把另一台虚拟机也是192.168.56.101的也设置了sshkey，然后mininet就不能公钥登陆了，还得重设

# SCP
function scpm; scp $1 mininet@192.168.56.101:~/; end  # 向mininet传送
function scpbm; scp mininet@192.168.56.101:$1 $2; end  # 向回传
function scpbanwagong; scp -P 28484 $1 root@45.78.9.29:$2; end  # 带端口的
function scpbbanwagong; scp -P 28484 root@45.78.9.29:$1 $2; end  # 带端口的
function scpaliyun; scp $1 root@115.28.247.19:$2; end
# exp: scpaliyun filename  或者  scpaliyun filename .  第二个是加了一个路径, 默认就是 . 家目录
function scpbaliyun; scp root@115.28.247.19:$1 $2; end
function scptencent; scp $1 root@115.159.88.186:$2; end
function scpbtencent; scp root@115.159.88.186:$1 $2; end

# Proxy
# alias sshrdoc='ssh -CNR 1080:localhost:1080 coder352@(docker inspect -f "{{.NetworkSettings.IPAddress}}" some-ubuntu-vim)'  # 这种方法太针对性了
alias sshrdoc='ssh -CNR 1080:localhost:1080 coder352@(docker inspect -f "{{.NetworkSettings.IPAddress}}" (docker ps -q))'

########################################
## Shadowsocks 后面两个是统计和显示流量 + Kcptun 加速
########################################
alias sslog='tail /var/log/shadowsocks.log'
# 搬瓦工自带 python
alias stass="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.python.json -d start; and exit"  # 这样默认是全局的, -d 会在后台运行
alias stoss="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.python.json -d stop; and exit"
alias restass='sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.python.json -d stop; and sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.python.json -d start; and exit'
# 搬瓦工 go
alias stassgo="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.go.json -d start; and exit"
alias stossgo="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.go.json -d stop; and exit"
alias stassgokcptun="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.go_kcptun.json -d start; and exit"
alias stossgokcptun="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.go_kcptun.json -d stop; and exit"
alias stassgokcptunall='stakcp stassgokcptun'  # OnO...
# kcptun 参考 断流: https://github.com/xtaci/kcptun/issues/218
# 手动参数设定: https://github.com/xtaci/kcptun/issues/137
alias stakcp='nohup ~/Downloads/client_linux_amd64 -r "45.78.9.29:18384" -l ":11080" -mode fast2 -mtu 512 >/dev/null 2>&1 &'
# 有时候不行了就改 mtu, 512, 1024 两个换着来
# function stakcp() { nohup ~/Downloads/client_linux_amd64 -r "45.78.9.29:18383" -l ":11080" -mode fast2 -mtu 256 >/dev/null 2>&1 & }
alias showkcp="ps -ef | grep client_linux_amd64 | grep -v grep | awk '{print $2}'"  # 这里原意是只输出 PID, 可还是会输出整个命令, 也还行
# function stokcp() { kill `ps -ef | grep client_linux_amd64 | grep -v grep | awk '{print $2}'` }  # 直接 stokcp 既可以执行函数了
# shadowsocksR
alias stassr='sudo python ~/github/others/shadowsocks/shadowsocks/local.py -s 45.78.9.29 -p 443 -k 6irwnc8jck -m aes-256-cfb -d start'  # 后台运行
alias stossr='sudo python ~/github/others/shadowsocks/shadowsocks/local.py -d stop'  # 停止
# 别人的免费
alias stassy="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.yzy.json -d start; and exit"
alias stossy="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.yzy.json -d stop; and exit"
alias stassother="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.json -d start; and exit"
alias stossother="sudo -S sslocal -c ~/.config/jshadowsocks/shadowsocks.json -d stop; and exit"
#alias cstass="sudo sslocal -s 45.78.9.29 -p 443 -b 127.0.0.1 -l 1080 -k MzBhMDU4YT -m aes-256-cfb -t 500 --fast-open -d start -v"

alias lsofi1080='sudo lsof -i:1080'
alias staiptall="sudo iptables -I OUTPUT -s 127.0.0.1 -p tcp --sport 1080"
alias showipt="sudo iptables -n -v -L -t filter |grep -i 'spt:1080' |awk -F' ' '{print $2}'"
# 设置防火墙, 每次开机后要重设
alias staipt="sudo iptables -A INPUT -p tcp -s 0/0 --sport 1080 -d 45.78.9.29 --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT; and
sudo iptables -A INPUT -p tcp -s 0/0 --sport 1080 -d 45.78.9.29 --dport 443 -m state --state ESTABLISHED,RELATED -j ACCEPT; and
sudo iptables -A OUTPUT -p tcp -s 45.78.9.29 --sport 443 -d 0/0 --dport 1080 -m state --state ESTABLISHED -j ACCEPT"
alias iptsta='sudo iptables -L -n | grep 1080'

##################################################################
# Docker 简写完以后仍然可一 Tab 补全
##################################################################
# docker d开头
alias dattach='docker attach'
alias dcp='docker cp'
# alias dfimage="docker run -v /var/run/docker.sock:/var/run/docker.sock --rm centurylink/dockerfile-from-image"
alias dexecit='docker exec -i -t'  # dexecit ubuntu /bin/bash 在已经运行的 container 上在开一个 bash
alias dimages='docker images'  # 查看所有镜像
alias dinspect='docker inspect'
alias dinspectfid="docker inspect -f '{{.Id}}'"
alias dinspectfimage="docker inspect -f '{{.Config.Image}}'"
alias dinspectfip="docker inspect -f '{{.NetworkSettings.IPAddress}}'"
alias dinspectfport="docker inspect -f '{{.NetworkSettings.Ports}}'"
alias dkill='docker kill'
alias dkilla='docker kill (docker ps -q)'
alias dnetworkinspect='docker network inspect'
alias dnetworkinspectf="docker network inspect -f '{{range $con :=.IPAM.Config}} {{$con.Subnet}} {{end}}'"  # 不知道为什么错
alias dps='docker ps'  # 后台运行容器
alias dpsa='docker ps -a'  # 后台所有容器
alias dpull='docker pull'
alias drm='docker rm'
alias drma='docker rm (docker ps -a -q)'
alias drmi='docker rmi'
alias drunit='docker run -i -t'
alias drunitrm='docker run -i -t --rm'  # -it 分开写, 要不然就没有补全了
alias drunitrmp='docker run -i -t --rm -p 80:80 -p 3306:3306'
function drunitrmsh; docker run -i -t --rm $1 /bin/bash; end  # 只要 run 后面 加 sh 或 /bin/bash, 就能进入 CLI
alias dstart='docker start -i'  # 打开一个已经关闭的容器
alias dstop='docker stop'

# docker-compose dc开头
alias dcps='docker-compose ps'
alias dcstop='docker-compose stop'
alias dcup='docker-compose up'
alias dcupd='docker-compose up -d'

# 一些 Offical 操作 doc开头
# ubuntu, debian 等操作系统直接 drunitrm 就行了
alias docdvwa='docker run -d -p 80:80 -p 3306:3306 -e MYSQL_PASS="root" citizenstig/dvwa'
alias docsqli='docker run -d -p 80:80 -p 3306:3306 -e MYSQL_PASS="root" tuxotron/audi_sqli'

alias docmysql="docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -i -t --rm mysql:5.7 /bin/bash -c \
    'nohup service mysql start && /bin/bash'"  # 据说 Docker 只能运行一个进程, 呵呵..., 这个是打开服务器, 并进入 CLI
alias docmysqlserver="docker run --name some-mysql \
    -v /home/coder352/Documents/thiscandel/share:/j \
    -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7"  # 启动 Mysql 服务端, 端口 3306, Server 是打不开 CLI 的
# 后台默认执行 mysqld --verbose --help, server端其实不用挂 share, client 端挂就行了
# mysql -h 127.0.0.1 -u root -p 就可以通过 host 连接 mysql, 或者如果没装 mysql-client 的话, 用下面那条 alias
# 要等会才能连上, 等后台服务起来了
# alias logmysql = mysql -h 127.0.0.1 ...
# alias docmysqlcli='exec docker run -it \
#     -v /home/coder352/Documents/thiscandel/share:/j \
#     --link some-mysql:mysql --rm mysql:5.7 sh -c \
#     "mysql -h (docker inspect -f "{{.NetworkSettings.IPAddress}}" some-mysql) -P 3306 -u root -proot"'  # 在已经打开的 docker 上开 Client
# 上面最外层一定要用单引号, -proot, 好尴尬, 这个第一次用的时候会退出, 在打开就好了

alias docredis='docker run -p 6379:6379 --name some-redis -d redis:3'

# 这里使用的 打开SSH服务 的方法, 跟 exec 的方法不太一样了
alias docredhat='docker run --name some-redhat9 -p 2233:22 -i -t -d apiemont/redhat9 /bin/bash -c \
    "echo "root:jk" | chpasswd \
    && /usr/sbin/sshd -D"'  # echo -e "jk\njk" | passwd root --stdin  # 这种修改密码的方法改的密码竟然不是 jk
# alias docredhatssh='ssh root@(docker inspect -f "{{.NetworkSettings.IPAddress}}" some-redhat9)'
alias docredhatssh='ssh -p 2233 root@localhost'  # 和上面那种方法相同, 两种写法, 也可以用 sshdocker(只适用于一个 container)

alias docmssql="docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=My@Super@Secret' -p 1433:1433 -d microsoft/mssql-server-linux"
alias docmssqlcli="sqlcmd -S localhost -U SA -P 'My@Super@Secret'"  # Install: https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools#ubuntu

alias docdjango='docker run --name some-django-app -v "$PWD":/usr/src/app -w /usr/src/app -p 8000:8000 -d django bash -c "pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000"'

alias docmininet='docker run -i -t --privileged barbaracollignon/ubuntu-mininet'  # mininet 不加 privileged 就无法用 sudo mn

alias docjubuntuv='docker run -i -t --privileged --rm -v /home/coder352/:/home/coder352/ -u coder352 -w /home/coder352 coder352/ubuntu:16.04'
alias docjubuntu='docker run -i -t --privileged --rm -u coder352 -w /home/coder352 coder352/ubuntu:16.04'
# alias docjubuntualias='docker run -i -t --privileged -u coder352 -w /home/coder352 --rm \
#     -v /home/coder352/.config/shellscript/my_zsh_alias:/home/coder352/my_zsh_alias \
#     coder352/ubuntu:16.04 /bin/bash -c "echo \". /home/coder352/my_zsh_alias\" >> /home/coder352/.bashrc \'
# alias docjubuntuvim='docker run -i -t --privileged --rm --name some-ubuntu-vim \
#     -v /home/coder352/Documents/thiscandel/vim/vimrc:/home/coder352/.vimrc:rw \
#     -v /home/coder352/.config/shellscript/my_zsh_alias:/home/coder352/my_zsh_alias:ro \
#     -v /home/coder352/Documents/thiscandel/vim:/home/coder352/.vim:rw \
#     coder352/ubuntu:16.04 /bin/bash -c "echo \". /home/coder352/my_zsh_alias\" >> /home/coder352/.bashrc \
#     && mkdir /var/run/sshd \
#     && chmod 0755 /var/run/sshd \
#     && service ssh start \
#     && cd /home/coder352 \
#     && su coder352"'
# /usr/sbin/sshd -D, 这个在 Ubuntu 中不好用, 而且不用 /bin/bash, 只有第一个 -v 可以实时同步, 其他的只能在　container 中写才能同步

########################################
# 渗透 & Ctf & Tools
########################################
# ctf-tools 中的
alias burpsuite='java -jar ~/github/others/ctf-tools/burpsuite/burp.jar'
alias stegsolve='~/github/others/ctf-tools/stegsolve/bin/stegsolve.jar'
#alias sqlmap="python /usr/bin/sqlmap/sqlmap.py"
alias sqlmap="python ~/github/others/ctf-tools/sqlmap/bin/sqlmap.py"
alias sqlmapub="python ~/github/others/ctf-tools/sqlmap/bin/sqlmap.py --current-user --current-db"

function strflag; strings $1 | grep $2; end  # strflag <filename> flag, <filename> 不能使用 *
alias gephi='~/github/others/gephi-0.9.1/bin/gephi'

########################################
# 无线AP
########################################
# alias stawf="echo '$mypassword' | sudo ap-hotspot start"  # Ubuntu 16.04 已经不好用了
# alias stowf="echo '$mypassword' | sudo ap-hotspot stop"
alias mcreate_ap="sudo create_ap wlp3s0 wlp3s0 jrp 123456jrp"  # github, oblique/create_ap 有安装步骤

##################################################################
## tips
##################################################################
alias ascii='man 7 ascii'
alias msources='man 5 sources.list'

##################################################################
## Others: VIBes(法国高科)
##################################################################
alias vibesviewer='~/miniconda3/pkgs/vibes-bin-0.2.2a1-0/bin/VIBes_viewer'

##################################################################
## 零碎的
##################################################################
alias jpasswordqq='jpassword qq | jclip'
