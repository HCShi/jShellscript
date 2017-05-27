########################################
## git 相关操作 要被淘汰了 via oh my zsh
########################################
# some repository
alias gis 'git status'
alias gia 'git add .'
alias gial 'git add --all'
alias gicommit 'git commit -m'
alias gilog 'git log --oneline --decorate --graph --all'
alias gipush 'git push origin master'
alias gid 'git diff'  # 工作目录 vs 暂存区 (如果还没 add 进暂存区，则查看文件自身修改前后的差别)
alias gidc 'git diff --cached'  # 暂存区 vs Git仓库 (表示查看已经 add 进暂存区但是尚未 commit 的内容同最新一次 commit 时的内容的差异)
# global
alias gitdep 'git clone --depth 1'  # git shallow clone --depth=1 表示只下载最近一次的版本，使用浅复制可以大大减少下载的数据量
alias gitinfo 'git config --global -l'  # 显示git相关配置信息
alias githttp 'git config --global http.proxy "socks5://127.0.0.1:1080"; and git config --global https.proxy "socks5://127.0.0.1:1080"'  # 只针对 https://github.com/coder352/jvim.git 之类的
alias githttpno 'git config --global --unset http.proxy; and git config --global --unset https.proxy'
alias gitssh 'mv ~/.ssh/jconfig ~/.ssh/config'
alias gitsshno 'mv ~/.ssh/config ~/.ssh/jconfig'
alias gitgit 'git config --global core.gitproxy "git-proxy"'  # 这个的意思是用上面两种代理中的一种
alias gitgitno 'git config --global --unset core.gitproxy'
##### 下面是 Github + Hexo + 七牛云
alias qrsync '~/github/others/qrsync/qrsync'  # 任意目录下执行
