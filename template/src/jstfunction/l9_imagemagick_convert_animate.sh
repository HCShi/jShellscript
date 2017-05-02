#!/bin/bash
# imagematick 大法好...
##################################################################
## convert 黑科技...
##################################################################
convert -density 300 file.pdf page_%04d.jpg  # 保证质量, %04d 占位
convert -density 300 file.jpg he.pdf
convert *.jpg out.gif               # all images with extension jpg
convert @list.txt out.gif           # list.txt is an image list
convert image-%3d.jpg[1-5] out.gif  # choose image-001.jpg ... image-005.jpg
##################################################################
## animate 专业处理 gif
##################################################################
animate tmp.gif  # 查看 gif 文件; Space 停止/查看下一张; > 加速; < 减速;
