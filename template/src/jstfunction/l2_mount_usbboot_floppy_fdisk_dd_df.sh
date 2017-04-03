##################################################################
## 刚插上去的U盘挂载时, 不会提示忙, 只可能会提示权限问题, U 盘(sdb), iso(cdrom), 软盘(fd)
##################################################################
# 五种查看 mount 挂载的命令
sudo fdisk -l  # perfect
df -h  # 这个可以查到 Android 设备挂载到 /run/user/<user-id>/gvfs/ 中
df -ia
mount
cat /etc/mtab
# common steps
mkdir /mnt/usb && mkdir /mnt/cdrom
mount /dev/sdb4 /mnt/usb && mount /dev/cdrom /mnt/cdrom
umount -l /dev/sdb  # 要在挂载点以外的目录执行, -l lazy, just unmount, delete date not immediately
umount -l /dev/cdrom
eject  # 弹出光驱
##################################################################
## install desktop from LiveCD, too interesting
##################################################################
sudo fdisk -l  # check which dev to mount
sudo mount /dev/sda5 /mnt
sudo mount -o bind /dev /mnt/dev  # same to ln -s, but can not use ln -s because of chroot below
sudo mount -o bind /dev/pts /mnt/dev/pts
sudo mount -o bind /proc /mnt/proc
sudo mount -o bind /sys /mnt/sys
sudo cp /etc/resolv.conf /mnt/etc/resolv.conf
sudo chroot /mnt  # set /mnt to new /root
# System Setting -> Network -> Proxy -> Manual, to make apt access the network
apt-get install ubuntu-desktop && exit  # install and exit root
sudo umount /mnt/dev/pts
sudo umount /mnt/dev
sudo umount /mnt/proc
sudo umount /mnt/sys
sudo umount /mnt
##################################################################
## 命令行制作启动盘, 必须切换到 root, 而不是 sudo
##################################################################
su root
cat Ubuntu-amd64.iso > /dev/sdb
cat ubuntu-16.04-desktop-amd64.iso > /dev/sdc1  # 没能干掉老毛桃, 还没试 /dev/sdc
cat ubuntu-16.04-desktop-amd64.iso > /dev/sdc   # 干掉了老毛桃, 却启动不了了
##################################################################
## dd command with usb bootin
##################################################################
dd if=/dev/zero of=test bs=1 count=1024            # 可以根据需要生成指定大小的文件, bs is base on byte
su root
dd if=Ubuntu-amd64.iso of=/dev/sdb1 bs=4M          # 制作 U 盘启动盘
dd if=Ubuntu-amd64.iso of=/dev/cdrom bs=4M         # 制作 CD/DVD 系统盘
dd if=ubuntu-16.04-desktop-amd64.iso of=/dev/sdc1  # 制作 U 盘启动盘, 测试能不能把里面的老毛桃干掉
dd if=ubuntu-16.04-desktop-amd64.iso of=/dev/sdc   # 最后尝试的这个, OK
##################################################################
## dd 软盘
##################################################################
# 创建虚拟软盘镜像文件 下面三条命令中的任意一个可以建立一个虚拟的软盘镜像文件, 结果完全一样
dd if=/dev/zero of=floppy.img bs=1474560 count=1
dd if=/dev/zero of=floppy.img bs=512 count=2880
dd if=/dev/zero of=floppy.img bs=1024 count=1440  # 生成 1.44MB 的一个软盘
# 在软盘镜像文件上建立文件系统 下面两条命令中的任意一个可在软盘镜像上建立文件系统, 可根据需要选择相应的文件系统
mkfs.vfat floppy.img  # 建格式化为vfat文件系统
mkfs.ext2 floppy.img  # 建格式化为ext2文件系统
# 读写建立的软盘镜像
mkdir floppy                     # 在当前文件夹下即可
mount floppy.img floppy -o loop  # 是 -o loop,而不是 -0 loop, 而且一定是 loop
# 如果所用的系统不会自动识别文件系统的话 mount 命令要加上 -t 选项
mount floppy.img floppy -o loop -t vfat  # 如果软盘镜像为vfat文件系统
mount floppy.img floppy -o loop -t ext2  # 如果软盘镜像为ext2文件系统
cp kernel floppy                         # 然后就可以像操作普通文件夹那样对 floppy 文件夹进行操作了, 如将 "kernel" 文件复制到里面
ls floppy                                # 查看其中的文件
umount floppy.img                        # 操作完以后用下列命令将其卸载
# 如果在mount 步骤出现
# mount: unknown filesystem type 'vfat'
# 的提示, 则需要查看并重建
# /lib/modules/2.6.xxx/modules.dep
# 使用用depmod重新生成modules.dep, 重启
##################################################################
## dd 命令详解
##################################################################
# bs 带的参数是一次写入字节数, 可以自己替换更高的数来得到更高的速度,
# 但是真正使用时, 速度的上限还是限于硬件的读写速度
# 比如说, USB2.0 的U盘, 你带入参数 bs=16M, 但是真正得到的读写速度仍然是3M～4M的样子
# if = 输入文件 (或设备名称)
# of = 输出文件 (或设备名称)
# ibs = bytes 一次读取bytes字节, 即读入缓冲区的字节数
# skip = blocks 跳过读入缓冲区开头的ibs*blocks块
# obs = bytes 一次写入bytes字节, 即写入缓冲区的字节数
# bs = bytes 同时设置读/写缓冲区的字节数 (等于设置ibs和obs)
# cbs = byte 一次转换bytes字节
# count=blocks 只拷贝输入的blocks块
# conv = ASCII 把EBCDIC码转换为ASCIl码
# conv = ebcdic 把ASCIl码转换为EBCDIC码
# conv = ibm 把ASCIl码转换为alternate EBCDIC码
# conv = block 把变动位转换成固定字符
# conv = ublock 把固定位转换成变动位
# conv = ucase 把字母由小写转换为大写
# conv = lcase 把字母由大写转换为小写
# conv = notrunc 不截短输出文件
# conv = swab 交换每一对输入字节
# conv = noerror 出错时不停止处理
# conv = sync 把每个输入记录的大小都调到ibs的大小 (用NUL填充)
