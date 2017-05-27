##################################################################
## 1. .zip file, lsar unar
lsar file.zip  # 如果显示没有乱码就可以直接解压, 对 Windows 上的 zip 效果特别好, 没有乱码
unar file.zip
lsar -e GB18308 file.zip  # 如果上面显示有乱码, 指定编码方式查看
unar -e GB18308 file.zip
##################################################################
## 2. gzip bzip tar
# gzip [-cdtv#] filename
# bzip2 [-cdkzv] 文件名  # gzip 的升级, 大部分操作相同
ls /etc > list          # 为下面提供文件
gzip -v1 list           # 压缩等级 1, 越高压缩的越好, 默认是 6, v 参数是显示具体信息
gzip -c list > list.gz  # 保留原文件, 没有重定向则是输出到屏幕
gzip -t list            # 测试是否是压缩文件
gzip -d list.gz         # 解压
bzip2 -k list           # 保留源文件
tar -jcv -f filename.tar.bz2 filename  # 使用 j 参数, 是将文件先打包, 再压缩进行 bz2 压缩, z 是 gzip
tar -jxv -f filename.tar.bz2 -C path   # 指定解压路径
tar -jcv -f list.tar.bz2 list          # 将 list 进行压缩
tar xvzf filename.tar.gz               # 解压到当前目录, 以后经常用到

