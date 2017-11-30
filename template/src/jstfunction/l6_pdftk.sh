#!/bin/bash
##################################################################
## pdftk PDF 分割/合并/旋转 利器
##################################################################
# output 的名字不能和 输入文件 的名字相同
# 合并
pdftk 1.pdf 2.pdf 3.pdf cat output 123.pdf                   # 指定文件合并
pdftk *.pdf cat output all.pdf                               # 所有 PDF 合并, 不包含子目录
pdftk *.pdf 1.4\ HTTP与Cookie/1.4+HTTP与Cookie.pdf 3.1\ SQL注入/3.1+SQL注入.pdf cat output all.pdf  # 手动指定子目录

pdftk full-pdf.pdf cat 12-15 output outfile_p12-15.pdf       # 取中间 12-15 一部分
pdftk A=in.pdf cat A1-10 A15 A17 output out.pdf              # 分段裁剪
pdftk A=1.pdf B=2.pdf C=pdf cat A1-2 B2-3 C3 output abc.pdf  # 多个不同页面合并
# 旋转
# Acceptable keywords, for example: "even" or "odd".  To rotate pages, use: "north" "south" "east" "west" "left" "right" or "down"
pdftk in.pdf cat 1east 2-end output out.pdf  # 旋转第一页, 其他页不变, east 指顺时针, left 指逆时针
pdftk in.pdf cat 1east output out.pdf  # 旋转第一页, 其他页删除

pdftk a.pdf output b.pdf owner_pw pass  # 加密 (128位)
pdftk a.pdf output b.pdf user_pw pass   # 加访问密码
pdftk a.pdf input_pw pass output b.pdf  # 解密
pdftk a.pdf output b.pdf uncompress     # 解压
pdftk a.pdf output b.pdf compress       # 压缩
pdftk a.pdf output b.pdf                # 修复
pdftk a.pdf cat 1-end output b.pdf      # 切割
pdftk a.pdf burst                       # 分解成单页
