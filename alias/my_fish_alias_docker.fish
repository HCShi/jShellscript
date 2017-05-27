##################################################################
# Docker 简写完以后仍然可一 Tab 补全
##################################################################
# docker d 开头
alias dattach 'docker attach'
alias dcp 'docker cp'
# alias dfimage "docker run -v /var/run/docker.sock:/var/run/docker.sock --rm centurylink/dockerfile-from-image"
alias dexecit 'docker exec -i -t'  # dexecit ubuntu /bin/bash 在已经运行的 container 上在开一个 bash
alias dimages 'docker images'  # 查看所有镜像
alias dinspect 'docker inspect'
alias dinspectfid "docker inspect -f '{{.Id}}'"
alias dinspectfimage "docker inspect -f '{{.Config.Image}}'"
alias dinspectfip "docker inspect -f '{{.NetworkSettings.IPAddress}}'"
alias dinspectfport "docker inspect -f '{{.NetworkSettings.Ports}}'"
alias dkill 'docker kill'
alias dkilla 'docker kill (docker ps -q)'
alias dnetworkinspect 'docker network inspect'
alias dnetworkinspectf "docker network inspect -f '{{range $con :=.IPAM.Config}} {{$con.Subnet}} {{end}}'"  # 不知道为什么错
alias dps 'docker ps'  # 后台运行容器
alias dpsa 'docker ps -a'  # 后台所有容器
alias dpull 'docker pull'
alias drm 'docker rm'
alias drma 'docker rm (docker ps -a -q)'
alias drmi 'docker rmi'
alias drunit 'docker run -i -t'
alias drunitrm 'docker run -i -t --rm'  # -it 分开写, 要不然就没有补全了
alias drunitrmp 'docker run -i -t --rm -p 80:80 -p 3306:3306'
alias drunitrmsh 'docker run -i -t --rm $argv[1] /bin/bash'  # 只要 run 后面 加 sh 或 /bin/bash, 就能进入 CLI
alias dstart 'docker start -i'  # 打开一个已经关闭的容器
alias dstop 'docker stop'

# docker-compose dc 开头
alias dcps 'docker-compose ps'
alias dcstop 'docker-compose stop'
alias dcup 'docker-compose up'
alias dcupd 'docker-compose up -d'

# 一些 Offical 操作 doc 开头
# ubuntu, debian 等操作系统直接 drunitrm 就行了
alias docdvwa 'docker run -d -p 80:80 -p 3306:3306 -e MYSQL_PASS="root" citizenstig/dvwa'
alias docsqli 'docker run -d -p 80:80 -p 3306:3306 -e MYSQL_PASS="root" tuxotron/audi_sqli'

alias docmysql "docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -i -t --rm mysql:5.7 /bin/bash -c \
    'nohup service mysql start && /bin/bash'"  # 据说 Docker 只能运行一个进程, 呵呵..., 这个是打开服务器, 并进入 CLI
alias docmysqlserver "docker run --name some-mysql \
    -v /home/coder352/Documents/thiscandel/share:/j \
    -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7"  # 启动 Mysql 服务端, 端口 3306, Server 是打不开 CLI 的
# 后台默认执行 mysqld --verbose --help, server端其实不用挂 share, client 端挂就行了
# mysql -h 127.0.0.1 -u root -p 就可以通过 host 连接 mysql, 或者如果没装 mysql-client 的话, 用下面那条 alias
# 要等会才能连上, 等后台服务起来了
# alias logmysql mysql -h 127.0.0.1 ...
# alias docmysqlcli 'exec docker run -it \
#     -v /home/coder352/Documents/thiscandel/share:/j \
#     --link some-mysql:mysql --rm mysql:5.7 sh -c \
#     "mysql -h (docker inspect -f "{{.NetworkSettings.IPAddress}}" some-mysql) -P 3306 -u root -proot"'  # 在已经打开的 docker 上开 Client
# 上面最外层一定要用单引号, -proot, 好尴尬, 这个第一次用的时候会退出, 在打开就好了

alias docredis 'docker run -p 6379:6379 --name some-redis -d redis:3'

# 这里使用的 打开SSH服务 的方法, 跟 exec 的方法不太一样了
alias docredhat 'docker run --name some-redhat9 -p 2233:22 -i -t -d apiemont/redhat9 /bin/bash -c \
    "echo "root:jk" | chpasswd; \
    /usr/sbin/sshd -D"'  # echo -e "jk\njk" | passwd root --stdin  # 这种修改密码的方法改的密码竟然不是 jk
# alias docredhatssh 'ssh root@(docker inspect -f "{{.NetworkSettings.IPAddress}}" some-redhat9)'
alias docredhatssh 'ssh -p 2233 root@localhost'  # 和上面那种方法相同, 两种写法, 也可以用 sshdocker(只适用于一个 container)

alias docmssql "docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=My@Super@Secret' -p 1433:1433 -d microsoft/mssql-server-linux"
alias docmssqlcli "sqlcmd -S localhost -U SA -P 'My@Super@Secret'"  # Install: https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools#ubuntu

alias docdjango 'docker run --name some-django-app -v "$PWD":/usr/src/app -w /usr/src/app -p 8000:8000 -d django bash -c "pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000"'

alias docmininet 'docker run -i -t --privileged barbaracollignon/ubuntu-mininet'  # mininet 不加 privileged 就无法用 sudo mn

alias docjubuntuv 'docker run -i -t --privileged --rm -v /home/coder352/:/home/coder352/ -u coder352 -w /home/coder352 coder352/ubuntu:16.04'
alias docjubuntu 'docker run -i -t --privileged --rm -u coder352 -w /home/coder352 coder352/ubuntu:16.04'
# alias docjubuntualias 'docker run -i -t --privileged -u coder352 -w /home/coder352 --rm \
#     -v /home/coder352/.config/shellscript/my_zsh_alias:/home/coder352/my_zsh_alias \
#     coder352/ubuntu:16.04 /bin/bash -c "echo \". /home/coder352/my_zsh_alias\" >> /home/coder352/.bashrc \'
# alias docjubuntuvim 'docker run -i -t --privileged --rm --name some-ubuntu-vim \
#     -v /home/coder352/Documents/thiscandel/vim/vimrc:/home/coder352/.vimrc:rw \
#     -v /home/coder352/.config/shellscript/my_zsh_alias:/home/coder352/my_zsh_alias:ro \
#     -v /home/coder352/Documents/thiscandel/vim:/home/coder352/.vim:rw \
#     coder352/ubuntu:16.04 /bin/bash -c "echo \". /home/coder352/my_zsh_alias\" >> /home/coder352/.bashrc; \
#     mkdir /var/run/sshd; \
#     chmod 0755 /var/run/sshd; \
#     service ssh start; \
#     cd /home/coder352; \
#     su coder352"'
# /usr/sbin/sshd -D, 这个在 Ubuntu 中不好用, 而且不用 /bin/bash, 只有第一个 -v 可以实时同步, 其他的只能在　container 中写才能同步
