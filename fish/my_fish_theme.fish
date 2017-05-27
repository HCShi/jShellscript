##################################################################
## bobthefish
# https://github.com/oh-my-fish/theme-bobthefish  # 这里有详细的命令
# set -g theme_powerline_fonts no  # 没安装 powerline-font 时执行
# set -g theme_nerd_fonts yes  # 安装了 nerd-font 后执行, 但是不太好看
set -g theme_color_scheme solarized-light
set fish_greeting ""  # remove greeting; 这个对默认的管用, 对 bobthefish 要用下面的
set fish_greeting 'Talk is cheap. Show me the code.'
function fish_greeting; end

##################################################################
## right; 默认是时间和时区
function fish_right_prompt
    # set last_status $status
    # set_color $fish_color_cwd
    # printf '%s' (prompt_pwd)
    set_color normal
    # printf '%s ' (__fish_git_prompt)
    printf '%s' (eval uptime | awk -F ',' '{print $2}')
    set_color normal
    # uname -nmsr  # bobthefish 默认使用的这三行
    # uptime
    # set_color normal
end

##################################################################
## Git status
# set normal (set_color normal)
# set magenta (set_color magenta)
# set yellow (set_color yellow)
# set green (set_color green)
# set red (set_color red)
# set gray (set_color -o black)
# # Fish git prompt
# set __fish_git_prompt_showdirtystate 'yes'
# set __fish_git_prompt_showstashstate 'yes'
# set __fish_git_prompt_showuntrackedfiles 'yes'
# set __fish_git_prompt_showupstream 'yes'
# set __fish_git_prompt_color_branch yellow
# set __fish_git_prompt_color_upstream_ahead green
# set __fish_git_prompt_color_upstream_behind red
# # Status Chars
# set __fish_git_prompt_char_dirtystate '⚡'
# set __fish_git_prompt_char_stagedstate '→'
# set __fish_git_prompt_char_untrackedfiles '☡'
# set __fish_git_prompt_char_stashstate '↩'
# set __fish_git_prompt_char_upstream_ahead '+'
# set __fish_git_prompt_char_upstream_behind '-'
# function fish_right_prompt
#     # set last_status $status
#     # set_color $fish_color_cwd
#     # printf '%s' (prompt_pwd)
#     set_color normal
#     printf '%s ' (__fish_git_prompt)
#     set_color normal
# end
