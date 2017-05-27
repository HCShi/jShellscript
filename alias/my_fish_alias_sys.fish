########################################
## 系统操作
########################################
alias allproxy 'export all_proxy="https://192.168.1.13:8080"'
alias bjclip 'b64 -e $argv[1] | jclip'
alias echobool 'echo $status'
alias pbjclip 'clippaste | xargs -I {} b64 -e {} | jclip'
alias cpbjclip 'b64 -e $argv[1] | jclip; and clippaste | xargs -I {} b64 -e {} | jclip'
alias cpgitignore 'cp ~/github/jTemplate/src/my.gitignore .gitignore'
alias cman 'LANG="zh_CN.utf8" man'
alias cps 'set tmp1 (pwd); set tmp2 "/"; set tmp3 $argv[1]; set tmp $tmp1$tmp2$tmp3'
alias cpd 'cp $tmp $argv[1]'
alias day '/bin/date "+%Y-%m-%d.%H-%M-%S"'  # "/bin/date '+%Y-%m-%d'"  # 另一种形式
alias dub 'du -b'  # ls du 等命令默认以 K 为单位, 很坑
alias dush 'du -sh'  # dush 当前目录大小, dush a.txt 文件大小, dush directory 目录大小
alias findname 'find -iname'  # exapmle: findname "*.txt"
alias ggc 'google-chrome http://127.0.0.1:$argv[1]'
# alias grep 'grep -iI --color=always'  # google: grep exclude binary file || grep ignore spcific directory; 在 fish 中会死循环
alias grepf 'find -iname $argv[2] | xargs grep -riIn --color=always $argv[1]'  # example: grepf hello "*.md"
alias greps 'grep -riIn --color=always $argv[1]'  # example: greps hell
alias grepsd 'grep -riIn --color=always --exclude-dir $argv[1]'  # example: grepsd .git hello
alias grepsls 'ls | grep'
alias pdfgrepinr 'pdfgrep -inr $argv[1] *'
function ju8
    # iconv -f ISO-8859-1 -t UTF-8 $argv[1] > $argv[1].tmp  # file $argv[1] 显示的是 ISO-8859, 但没用
    iconv -f gbk -t utf-8 $argv[1] > $argv[1].tmp  # gbk 中文通用
    mv $argv[1].tmp $argv[1]  # example: ju8 file, file from Windows
end
alias ii 'clear'  # 因为 C-L 被 tmux 占了(自己设置), cls 又太麻烦, ll 默认是 ls 系列的  # 后来发现不需要了, 只要 Ctrl + A + L, 不要松开 Ctrl  # 再后来 l 又被resize占了...
alias kkm 'make clean'
alias llv 'll -v'  # -v 11 不会排在 2 前面了
alias lsv 'ls -v'
alias md5sumupper 'md5sum $argv[1] | tr "a-z" "A-Z"'  # md5sum <file>
alias mkdircd 'mkdir $argv[1]; cd $argv[1]'
alias nau 'nautilus .'
alias shut 'shutter -s -e -n -o /home/coder352/Desktop/Another\ link\ to\ Share/$argv[1].jpg'
# shut 1 就会生成 1.jpg 到指定路径下, 后面不加参数也会交互式截图, 但不会生成文件, Ctrl + Alt + A 生成 tmp.jpg
alias suroot 'sudo su root'
alias terminalnew 'gnome-terminal --working-directory=`pwd`'
# 这个 unzip 的参数只有 ubuntu 默认有
alias unzipo 'unzip -O cp936'  # 对于乱码情况, 最好用 lsar 和 unar
alias unrarx 'unrar x'  # 将rar解压到当前文件夹,全路径
alias wgetproxy 'wget -e use_proxy=yes -e http_proxy=127.0.0.1:1080'
alias xopen 'xdg-open'
# alias zd 'youdao'  # 界面有点丑, 但挺快 sudo pip install youdaodict
alias zd 'python ~/github/others/ydcv/ydcv.py'  # zd hello, zd 'hello world'
alias fy 'sdcv -c'  # sudo apt-get install sdcv
