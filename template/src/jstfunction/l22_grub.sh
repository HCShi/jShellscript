#!/bin/bash
# 参考: https://askubuntu.com/questions/192621/grub-rescue-prompt-repair-grub

# First thing is we have to start our OS only then after we can fix grub.
# to start OS-->
error: unknown filesystem.
Entering rescue mode...
grub rescue>

# When u see such error first we have to check for “Filesystem” is ext2'
grub rescue> ls  # type 'ls' and hit enter to see drive partition.
(hd0) (hd0,msdos6) (hd0,msdos5) (hd0,msdos4) ...   # you will see such things

# this are our drives now we have to check which one is ext2.
grub rescue>ls (hd0,msdos6)
error: disk 'hd,msdos6' not found.

# go for another drives until you get "Filesystem is ext2".
grub rescue>ls (hd0,msdos5)
error: disk 'hd,msdos5' not found.
grub rescue>ls hd0,msdos2)
(hd0,msdos2): Filesystem is ext2        # this is what we want

# now set the path
grub rescue>set boot=(hd0,msdos2)
grub rescue>set prefix=(hd0,msdos6)/boot/grub
grub rescue>insmod normal
grub rescue>normal

# Now just fix grub by following command on any ubuntu
sudo grub-install /dev/sda
sudo apt-get update
# to update grub
sudo apt-get upgrade
# make sure you must update grub after login into OS
