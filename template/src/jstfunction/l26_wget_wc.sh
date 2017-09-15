#!/bin/bash
##################################################################
## wc
ls | wc -l  # 求输出行数 带着 . 和 ..
wc whoiswoldy.txt  # 0 1 5586640 whoiswoldy.txt, 0行, 1个词, 55586640个字符, 也就说文件里只有一个大字符串, 字符数是千万级
##################################################################
## wget 强大的功能
wget -r -p -np -mk http://xxx.edu.cn
# -r 表示递归下载,会下载所有的链接,不过要注意的是,不要单独使用这个参数,因为如果你要下载的网站也有别的网站的链接,wget也会把别的网站的东西下载下来,所以要加上-np这个参数,表示不下载别的站点的链接.
# -np 表示不下载别的站点的链接.
# -k 表示将下载的网页里的链接修改为本地链接.
# -p 获得所有显示网页所需的元素,比如图片什么的.
# -m 镜像
wget -r -p -np -mk http://netedu.xauat.edu.cn/jpkc/netedu/jpkc/gdsx/  # 爬取西安建筑科技大学的数学网站
wget -r -p -np -mk -w 1 -X "*video*" http://netedu.xauat.edu.cn/jpkc/netedu/jpkc/gdsx/  # 发现 video 太大了
# -X exclude directory
wget -r -p -np -mk -X "*video*" http://netedu.xauat.edu.cn/jpkc/netedu/jpkc/gdsx/  # -w 1 太慢了, 受不了, 适合晚上
# 最终使用的, 还是不好用 -X 碰到 video 就直接退出了, 不会往后面的爬取
wget -r -p -np -U --spider -mk -X /jpkc/netedu/jpkc/gdsx/video/ http://netedu.xauat.edu.cn/jpkc/netedu/jpkc/gdsx/
wget -r -p -np -U --spider -mk http://netedu.xauat.edu.cn/jpkc/netedu/jpkc/gdsx/  # -X 并没有卵用

wget -A html,pdf http://www.ccs.neu.edu -U Mozilla -r -w 5 --spider -D northeastern.edu,ccs.neu.edu
# -A 爬虫接受的link类型, 如果不是-A指定的类型, 爬虫不会crawl
# -U 在爬虫的HTTP请求中, 加入User-Agent类型, 以模拟真实浏览器访问。很多网站禁止无User-Agent类型的HTTP请求。
# -r Recursive模式, 爬虫会分析当前页面所包含的link, 作为之后crawl的种子。据说同时使用-nv -r会更加稳定。
# -w 指定访问页面的间隔, 过频访问会让爬虫变得不友好
# --spider 打开spider模式, 即爬虫模式, 使得爬虫不保存访问过的页面至本地
# --D 指定Domain Lists, 指定爬虫只访问指定的域名下的页面
