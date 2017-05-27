#!/bin/bash
##################################################################
## clipcopy clippaste; 这两个不是 bash 命令, 所以 emacs 中不能识别, 内部其实调用的是 xclip
echo "hello" | clipcopy  # 要复制出去运行, 在哪里都能粘贴
clippaste  # 将系统粘贴板的内容打印出来
##################################################################
## xclip
echo "world" | xclip  # 复制进系统粘贴板, 只有 xclip -o 能粘贴出来
echo "jrp" | xclip -in -selection clipboard  # 这个在哪都能粘贴出来
xclip -o  # 将粘贴板中的动西打印出来
