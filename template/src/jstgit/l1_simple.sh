#!/bin/bash
git clone https://github.com/coder352/jvim.git vim                 # 重命名
git clone --branch v1.9 https://github.com/ethicalhack3r/DVWA.git  # 下载指定 Tag
git checkout *                                                     # 不小心改了别人的, 这个命令可以恢复
