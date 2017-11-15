#!/bin/bash
# imagematick 大法好...; imagematick 安装好以后包括 convert, animate
##################################################################
## convert 黑科技...
convert -density 300 file.pdf page_%04d.jpg  # 保证质量, %04d 占位, 对于多页的会分页, 很烦; 使用 150 可以把作业给那些 想抄作业的...
convert tmp-%d.jpg[0-3] tmp.pdf  # choose tmp-0.jpg, ..., tmp-3.jpg; 不要用 %1d

convert -density 300 file.jpg he.pdf
convert *.jpg out.gif               # all images with extension jpg
convert @list.txt out.gif           # list.txt is an image list
convert image-%3d.jpg[1-5] out.gif  # choose image-001.jpg ... image-005.jpg
##################################################################
## animate 专业处理 gif
animate tmp.gif  # 查看 gif 文件; Space 停止/查看下一张; > 加速; < 减速;

##################################################################
## pandoc
pandoc in.md -o out.html
pandoc in.md -c style.css out.html  # 添加 css 样式
pandoc -s -H style.css in.md -o out.html  # 将 css 嵌入到 html 里面, 方便传输
pandoc -s --self-contained -c style.css in.md -o out.html  # 这个命令不但会把 css 文件嵌入到 html 中, 它会把所有外部文件全部压缩进单个 html 文件中, 包括图片、视屏、音乐等

pandoc in.md -o out.pdf  # 中文会报错, 默认是 pdflatex, 不支持中文
pandoc in.md -o out.pdf --latex-engine=xelatex  # 中文部分全是空白, 还要用下面的命令
pandoc in.md -o out.pdf --latex-engine=xelatex -V mainfont=SimSun  # 中文完全是没有断行的; 还要用下面的命令
pandoc in.md -o out.pdf --latex-engine=xelatex -V mainfont="Adobe Song Std"  # 我电脑中没有 SimSun
pandoc in.md -o out.pdf --latex-engine=xelatex --template=pm-template.latex  # Perfect !!

pandoc in.org -o out.pdf --latex-engine=xelatex --template=pm-template.latex  # 先暂时用这个, 有时间写自己的模板
pandoc -o out.pdf --latex-engine=xelatex --data-dir=~/github/jshellscript/bin/latexpath --template=pm-template.latex tmp.org  # 指定模板位置
