# https://github.com/fish-shell/fish-shell/issues/486  # 这里有 alias 的重新定义
# set -xU TERM xterm-256color
# set -xU DEFAULT_USER (whoami)
# set -xU EDITOR /usr/bin/vim
# fish_vi_mode  # deprecated. switch to calling `fish_vi_key_bindings`.
##################################################################
## dircolors
# eval (dircolors ~/.dircolors)  # fish 下不支持 = 赋值, 所以用下面的
if type -fq dircolors and test -e ~/.dircolors
    eval (dircolors -c ~/.dircolors | sed 's/>&\/dev\/null$//')  # 改变 ls 的颜色
end
##################################################################
## 第一次打开 fish, 会使用 tmux
set cmd (which tmux)  # tmux path
set session (whoami)  # session name
eval $cmd has -t $session  # has-session 不存在会报错, 并且返回 1, 存在返回 0
if [ $status -eq 1 ]
    eval $cmd new -d -n normal -s $session         # 最后的 "" 中的都是命令
    eval $cmd set -g automatic-rename-format '#(pwd="#{pane_current_path}"; echo ${pwd####*/})'  # 下面这句话并没有用
    eval $cmd att -t $session                      # 第二个终端就不会进入 tmux 了, 最后才能进入 tmux
end
##################################################################
## Functions
function loop --description "loop <count> <command>"  # loop 3 echo hello
    for i in (seq 1 $argv[1])
        eval $argv[2..-1]  # $argv[2..-1] returns all arguments from the second to the last
    end
end
function alias --description "my alias for fish"  # jalias jhello "echo hello"
    set abbr $argv[1]; set command $argv[2]
    eval "function $abbr; $command; end"
end
function code  # 打开 MS VSCode, 这个好火啊
    set location "$PWD/$argv"
    open -n -b "com.microsoft.VSCode" --args $location
end
function logo  --description "display fish's logo"
    echo '                 '(set_color F00)'___
  ___======____='(set_color FF7F00)'-'(set_color FF0)'-'(set_color FF7F00)'-='(set_color F00)')
/T            \_'(set_color FF0)'--='(set_color FF7F00)'=='(set_color F00)')
[ \ '(set_color FF7F00)'('(set_color FF0)'0'(set_color FF7F00)')   '(set_color F00)'\~    \_'(set_color FF0)'-='(set_color FF7F00)'='(set_color F00)')
 \      / )J'(set_color FF7F00)'~~    \\'(set_color FF0)'-='(set_color F00)')
  \\\\___/  )JJ'(set_color FF7F00)'~'(set_color FF0)'~~   '(set_color F00)'\)
   \_____/JJJ'(set_color FF7F00)'~~'(set_color FF0)'~~    '(set_color F00)'\\
   '(set_color FF7F00)'/ '(set_color FF0)'\  '(set_color FF0)', \\'(set_color F00)'J'(set_color FF7F00)'~~~'(set_color FF0)'~~     '(set_color FF7F00)'\\
  (-'(set_color FF0)'\)'(set_color F00)'\='(set_color FF7F00)'|'(set_color FF0)'\\\\\\'(set_color FF7F00)'~~'(set_color FF0)'~~       '(set_color FF7F00)'L_'(set_color FF0)'_
  '(set_color FF7F00)'('(set_color F00)'\\'(set_color FF7F00)'\\)  ('(set_color FF0)'\\'(set_color FF7F00)'\\\)'(set_color F00)'_           '(set_color FF0)'\=='(set_color FF7F00)'__
   '(set_color F00)'\V    '(set_color FF7F00)'\\\\'(set_color F00)'\) =='(set_color FF7F00)'=_____   '(set_color FF0)'\\\\\\\\'(set_color FF7F00)'\\\\
          '(set_color F00)'\V)     \_) '(set_color FF7F00)'\\\\'(set_color FF0)'\\\\JJ\\'(set_color FF7F00)'J\)
                      '(set_color F00)'/'(set_color FF7F00)'J'(set_color FF0)'\\'(set_color FF7F00)'J'(set_color F00)'T\\'(set_color FF7F00)'JJJ'(set_color F00)'J)
                      (J'(set_color FF7F00)'JJ'(set_color F00)'| \UUU)
                       (UU)'(set_color normal)
end
