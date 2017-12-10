### zsh 调用关系
先调用 ./zsh/zshrc 文件
再从 ./zsh/zshrc 中依次调用 ./zsh/my_zsh_env  ./zsh/my_zsh_alias ./zsh/my_zsh_rc

### fish 调用关系
先调用 ./config.fish
再通过 ./config.fish 调用 ./fish/my_fish_rc.fish ./fish/my_fish_env.fish ./fish/alias/*

### third-part script
./zsh/zshrc 中标注了第三方的位置, 即: ~/.config/jshellscript/
文件名为 *.sh

./zsh/zshenv 中标注了第三方的位置, 即: ~/.config/jshellscript/
文件名为 *.env


