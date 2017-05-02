#!/bin/bash
# Oh-my-shell
for i in {1..12}; do for j in $(seq 1 $i); do echo -ne $i x $j=$((i*j))\t;done; echo;done  # 9x9 乘法表
(){:|:&}:  # Fork 炸弹: 以指数级的自乘, 直到所有的系统资源都被利用了或者系统挂起, 运行它之前关掉并保存其它所有程序和文件
while true; do echo "$(date '+%D %T' | toilet -f term -F border --gay)"; sleep 1; done  # 提供彩色的日期和文件

mkdir -p my-project/{src,doc}  # 创建工程目录, 不能有逗号
cat > hello.c  # 紧接着在终端里面输入代码, 最后另起一行, C-d 结束输入

# 一行命令下载图片
for i in {1..10}; do curl "http://me2-sex.lofter.com/tag/美媛馆?page="$i |grep -o "http://imglf.*.jpg" |xargs wget -P lofter -t 10 -T 30 -N||break;done;

# ed  # GNU 标准编辑器
# red

# Python
python -c "import matplotlib; print(matplotlib.get_backend())"  # Qt5Agg
pydoc dict  # 查看 dict 类的方法
pydoc __builtin__  # 查看 __builtin__ 方法
python -c "import asyncore; help(asyncore)"  # 帮助文档
python -c "import asyncore; print(dir(str))"  # 属性
