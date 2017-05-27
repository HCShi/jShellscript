########################################
## SSH SCP
########################################
# VPS
alias sshaliyun 'ssh root@115.28.247.19'  # 管理终端密码 367692
alias sshbanwagong 'ssh root@45.78.9.29 -p 28484'
alias sshkali 'ssh root@192.168.56.105'  # passwd: asd
alias sshredhat 'ssh root@192.168.56.101'  # passwd: 123456
alias sshruanjianbei 'ssh jrp@211.87.185.53 -p 22222'  # passwd: Yr1Uwud6yH87kcJ8
alias sshteacher 'ssh r12@121.251.254.208'  # username: root; passwd: 123456
alias sshtencent 'ssh root@115.159.88.186'
alias sshdocker 'ssh root@(docker inspect -f "{{.NetworkSettings.IPAddress}}" (docker ps -a -q))'
# alias sshxm 'ssh mininet@192.168.56.101' 因为要把本机IP传过去，所以写成可执行文件了
# 很坑的把另一台虚拟机也是192.168.56.101的也设置了sshkey，然后mininet就不能公钥登陆了，还得重设

# SCP
alias scpm 'scp $argv[1] mininet@192.168.56.101:~/'  # 向mininet传送
alias scpbm 'scp mininet@192.168.56.101:$argv[1] $argv[2]'  # 向回传
alias scpbanwagong 'scp -P 28484 $argv[1] root@45.78.9.29:$argv[2]'  # 带端口的
alias scpbbanwagong 'scp -P 28484 root@45.78.9.29:$argv[1] $argv[2]'  # 带端口的
alias scpaliyun 'scp $argv[1] root@115.28.247.19:$argv[2]'
# exp: scpaliyun filename  或者  scpaliyun filename .  第二个是加了一个路径, 默认就是 . 家目录
alias scpbaliyun 'scp root@115.28.247.19:$argv[1] $argv[2]'
alias scptencent 'scp $argv[1] root@115.159.88.186:$argv[2]'
alias scpbtencent 'scp root@115.159.88.186:$argv[1] $argv[2]'

# Proxy
# alias sshrdoc 'ssh -CNR 1080:localhost:1080 coder352@(docker inspect -f "{{.NetworkSettings.IPAddress}}" some-ubuntu-vim)'  # 这种方法太针对性了
alias sshrdoc 'ssh -CNR 1080:localhost:1080 coder352@(docker inspect -f "{{.NetworkSettings.IPAddress}}" (docker ps -q))'
