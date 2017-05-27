#!/bin/bash
$cmd splitw -v -p 20 -t $session "pry"  # 创建窗口 1, 并分为上下两个窗格, 其中上窗格占 80% 空间, 运行 Vim, 下窗格占 20% 空间, 运行 Pry
$cmd neww -n mutt -t $session "mutt"    # 创建窗口 2, 运行 Mutt
$cmd set -g automatic-rename-format '#(pwd="#{pane_current_path}"; echo ${pwd####*/})'
