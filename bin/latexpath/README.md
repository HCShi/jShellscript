### Description
``` zsh
jltfunction 中没有用这里的, jLatex 这个 repository 中会用到这里的
.sty 可以 SPC m b 直接进行编译...
.sty 中使用 \documentclass{} 和 \begin{document} 也没关系, 不会影响被调用...
.sty 中复用的代码段用 \input{} 引入
```
``` zsh
./thuthesis.cls  # 清华大学模板
./swfcthesis.cls  # 西南林业大学 王晓林 教程用的模板

./14thcoder_math.cls  # 弃用, 改用 .sty, 但还有参考价值
./14thcoder_math_manual.sty  # 数学笔记的模板

./14thcoder_slide_metropolis.sty  # slide 模板

./14thcoder_thesis_upc.cls  # 石油大学毕设模板, 自己设计的, 虽然最后没有用
./14thcoder_thesis_pages.sty  # 分模块的设计, 将各个页面在这里定义
./14thcoder_thesis_variables.sty  # 将变量在这里定义

./14thcoder_ucas_matrix-analysis.sty  # 国科大 矩阵分析与应用 课程作业模板

./part_*_*  # 将各部分分离出来重用; 名称分为三部分, part_位置/属性_功能
./part_class_*  # 第一行, 在被调用时要注释掉
./part_normal-*  # 优先引用
# 中间是一些不冲突的配置
./part_my-*      # 靠后引用
./part_main_*  # 最后一行, 被调用时不必注释掉
```
### 调用 .sty 方法
``` zsh
1. 调用 .sty 文件
    \usepackage{14thcoder_ucas_matrix-analysis}  % 不加末尾的 .sty 后缀
    \blinddocument  % 生成一段随机的文本, 放到 document 中; \usepackage{blindtext} 已经在这里引入了
2. Debug/Test .sty file
    将第一个 \input{} 取消注释, 因为一个 .tex 中只能有一个 \documentclass{}
```
