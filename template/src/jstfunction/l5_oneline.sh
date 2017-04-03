#!/bin/bash
# Oh-my-shell
for i in {1..12}; do for j in $(seq 1 $i); do echo -ne $i x $j=$((i*j))\t;done; echo;done  # 9x9 乘法表
(){:|:&}:  # Fork 炸弹: 以指数级的自乘, 直到所有的系统资源都被利用了或者系统挂起, 运行它之前关掉并保存其它所有程序和文件
while true; do echo "$(date '+%D %T' | toilet -f term -F border --gay)"; sleep 1; done  # 提供彩色的日期和文件

mkdir -p my-project/{src,doc}  # 创建工程目录
cat > hello.c  # 紧接着在终端里面输入代码, 最后另起一行, C-d 结束输入
