# fish_vi_mode  # deprecated. switch to calling `fish_vi_key_bindings`.
function fish_user_key_bindings
    fish_vi_key_bindings  # enter into vim-mode
    bind -M insert \ej accept-autosuggestion  # Alt + j
    # bind -M insert \el execute  # 回车的快捷键
    bind -M insert \cp history-search-backward  # Ctrl + p
    bind -M insert \cn history-search-forward
    bind -M insert -m default fj force-repaint
    bind -M insert -m default jj execute  # 回车的快捷键, 不好的是会进入 normal 模式
    # bind -M insert -m default fl end-of-line
end
# set -g fish_key_bindings my_key_bindings
# fish_user_key_bindings isn't used with vi bindings, it's only used with the default bindings.
# If you want custom bindings with vi mode, you should do something like

