### zsh 调用关系
先调用 zshrc 文件
再从 zshrc 中依次调用 ./my_zsh_env  ./my_zsh_alias ./my_zsh_rc

### fish 调用关系
先调用 ./config.fish
再通过 ./config.fish 调用 ./my_fish_rc.fish ./my_fish_env.fish ./alias/*

### third-part script
./zshrc 中标注了第三方的位置, 即: ~/.config/jshellscript/
文件名为 *.sh

