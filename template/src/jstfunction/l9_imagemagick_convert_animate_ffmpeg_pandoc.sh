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
## ffmpeg: A complete, cross-platform solution to record, convert and stream audio and video.
## 剪切
ffmpeg -i input.mkv -ss 00:00:00 -t 00:06:03 -acodec copy -vcodec copy output.mkv  # 这样写不需要重新编码, 即时完成...
ffmpeg -i input.mkv -ss 00:00:00 -t 00:06:03 -async 1 cut.mkv  # 这样写会重新编码, 很慢
# -ss 指定从什么时间开始
# -t 指定需要截取多长时间, 这里指截取 6 分钟长的视频
# -i 指定输入文件
# 处理的时候要把原视频关掉
## 拼接
ffmpeg -i concat:"part1_1.mkv|part1_2.mkv" -c copy part1.mkv  # 显示指定, 但可能拼接的不好, 中间会出现丢失; 先用 ffmpeg 转成 mpeg; 还是用下面的
ffmpeg -f concat -i list.txt -c copy part1.mkv  # 将要合并的文件写到字符文件里
# 文件中这样写, 前面的 file 一定要写
file 'part1_1.mkv'
file 'part1_2.mkv'

## 嵌入字幕
ffmpeg -i subtitle.srt subtitle.ass  # 将 .srt 文件转换成 .ass 文件
ffmpeg -i subtitle.ass subtitle.srt  # 将 .ass 文件转换成 .srt 文件
ffmpeg -i tmp.mkv -vf subtitles=tmp.ssa out.mkv  # 嵌入 SSA 字幕到视频文件
ffmpeg -i video.avi -vf "ass=subtitle.ass" out.avi  # 嵌入 ASS 字幕到视频文件
ffmpeg -i video.avi -vf subtitles=subtitle.srt out.avi  # 单独 SRT 字幕

## 嵌入在 MKV 等容器的字幕, 类似于视频转换
ffmpeg -i video.mkv -vf subtitles=video.mkv out.avi  # 将 video.mkv 中的字幕(默认)嵌入到 out.avi 文件
ffmpeg -i video.mkv -vf subtitles=video.mkv:si=1 out.av  # 将 video.mkv 中的字幕(第二个)嵌入到 out.avi 文件

## 实战...
## 国科大英语 A, 期末, 阿甘正传, 配音, out.mkv 是上面将 ssa 字母嵌进去以后的输出文件, 这里剪切就是输入文件
ffmpeg -i out.mkv -ss 00:04:25 -t 00:01:01 -acodec copy -vcodec copy part1_1.mkv
ffmpeg -i out.mkv -ss 00:05:59 -t 00:00:41 -acodec copy -vcodec copy part1_2.mkv
ffmpeg -i out.mkv -ss 00:13:25 -t 00:02:14 -acodec copy -vcodec copy part2.mkv
ffmpeg -i out.mkv -ss 01:32:15 -t 00:02:00 -acodec copy -vcodec copy part3.mkv
ffmpeg -i out.mkv -ss 01:39:00 -t 00:02:20 -acodec copy -vcodec copy part4.mkv
ffmpeg -i out.mkv -ss 01:57:26 -t 00:01:30 -acodec copy -vcodec copy part5.mkv
ffmpeg -i out.mkv -ss 02:00:00 -t 00:03:22 -acodec copy -vcodec copy part6.mkv
## 将前两个拼接
ffmpeg -i concat:"part1_1.mkv|part1_2.mkv" -c copy part1.mkv
ffmpeg -f concat -i list.txt -c copy .mp4

##################################################################
## pandoc
## /usr/share/pandoc/data/templates, 官方提供的模板在这里
# Markdown - Html
pandoc in.md -o out.html
pandoc in.md -c style.css out.html  # 添加 css 样式
pandoc -s -H style.css in.md -o out.html  # 将 css 嵌入到 html 里面, 方便传输
pandoc -s --self-contained -c style.css in.md -o out.html  # 这个命令不但会把 css 文件嵌入到 html 中, 它会把所有外部文件全部压缩进单个 html 文件中, 包括图片、视屏、音乐等

# Markdown - PDF
pandoc in.md -o out.pdf  # 中文会报错, 默认是 pdflatex, 不支持中文
pandoc in.md -o out.pdf --latex-engine=xelatex  # 中文部分全是空白, 还要用下面的命令
pandoc in.md -o out.pdf --latex-engine=xelatex -V mainfont=SimSun  # 中文完全是没有断行的; 还要用下面的命令
pandoc in.md -o out.pdf --latex-engine=xelatex -V mainfont="Adobe Song Std"  # 我电脑中没有 SimSun
pandoc in.md -o out.pdf --latex-engine=xelatex --template=pm-template.latex  # Perfect !!

# Org - PDF
pandoc in.org -o out.pdf --latex-engine=xelatex --template=pm-template.latex  # 先暂时用这个, 有时间写自己的模板
pandoc -o out.pdf --latex-engine=xelatex --data-dir=~/github/jshellscript/bin/latexpath --template=pm-template.latex tmp.org  # 指定模板位置
# 后来上面那句话又失效了, 直接在本地建立目录吧...
mkdir -p ~/.pandoc/templates
pandoc -D latex > ~/.pandoc/templates/default.latex
cd ~/.pandoc/templates
cp ~/github/jShellscript/bin/latexpath/pm-template.latex .
# 如果用 ln -s 软连接过去的话, 不能先用 mkdir 创建目录

# Org - Docx; 转换 PDF 很烦, 但是转换成其他的就很简单了
pandoc -o out.docx Big-Project_Paper.org  # 原始模板挺好的..., 其实是自己还不会整理 docx 模板...

# Html - Org; 经常从网上扒一些 Html, 然后转成 org
pandoc -f html+tex_math_dollars+tex_math_single_backslash -t org in.html -o out.org  # 主要解决 $ ^ _ 前面会自动加 \
