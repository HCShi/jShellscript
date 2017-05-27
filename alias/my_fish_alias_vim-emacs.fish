##################################################################
## vim 相关操作  进目录是为了退出时能够 git
##################################################################
alias vimq 'vim -u NONE'  # 不加载配置文件
alias vimms 'cd ~/github/jShellscript; and vim my_zsh_alias'
# php.vim 中补全的更新, 中间的括号太乱了
# alias updatephpfunlist 'curl http://www.php.net/manual/en/indexes.functions.php | sed "/class=\"index\"/!d" | grep -oP ">[^<]+</a> - .*</li>" | cut -b2- | sed "s~</a> - ~ ; ~; s~</li>$~~" > php-funclist.txt'
# 下面这句话会在当前目录下生成一个 vim 启动时打开文件的顺序以及事件节点, 可以查看是哪里耗费启动时间
alias vimtimefile 'vim --startuptime timefile the_file_you_want_to_edit'
# 简化配置
alias vimclear 'cp ~/.vimrc.clear ~/.vimrc'
alias vimnormal 'cp ~/.vimrc.normal ~/.vimrc'

##################################################################
## Emacs 相关配置
##################################################################
alias spaceemacscompile 'emacs --batch --eval "(byte-recompile-directory \"~/.spacemacs.d/\" 0)"'  # 最好不要用, 会出现一些奇怪的错误
alias emacscompile 'emacs --batch --eval "(byte-recompile-directory \"~/.emacs.d\" 0)"'  # 直接执行 .el 速度还行, findname "*.elc*" | xargs rm 将 .elc 删除
alias eng 'emacs --debug-init'
alias engq 'emacs --debug-init -q'  # -q 是不加载配置文件
alias enwq 'emacs -nw -q'
alias ens 'emacs --no-site-file --script'  # 执行单独的 .el 文件
# Server
alias ess 'emacs --daemon'  # 开启一个服务端
alias esk 'emacsclient -e "(kill-emacs)"'  # 关闭服务端
# alias esr 'emacsclient -e "(server-start)"'  # 重启服务端, 这个不能用
alias esr 'emacsclient -e "(kill-emacs); and emacs --daemon"'  # 重启服务端
alias eservername 'emacs --eval "(setq server-name $argv[1])" --daemon'  # emacsservername foo; 创建 Name 为 foo 的 Emacs 服务端
alias ecl 'emacsclient'  # ecl a.py; 如果开的是 GUI 界面的服务器, 会进入 GUI; 如果开的是 ess(terminal), 会进入终端
alias vom 'emacsclient -nw'  # vom a.py; fn 退出
alias voms 'emacsclient -nw -s'  # voms foo; 连接 server-name 为 foo 的 emacs 服务器
