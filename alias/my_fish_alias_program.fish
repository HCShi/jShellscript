alias pycharm '/home/coder352/JetBrains/pycharm-2016.3.2/bin/pycharm.sh'
alias eclipse '~/eclipse/java-neon2/eclipse/eclipse'
##################################################################
## Python
##################################################################
# ascii 和 char 之间转换
alias pord 'python -c "print ord(\"$argv[1]\")" }'  # example: pord A  # 65  # ord(char/unichr)
alias pchr 'python -c "print chr(int(\"$argv[1]\"))"'  # example: pchr 65  # A  # chr(num)
alias punichr 'python -c "print unichr(int(\"$argv[1]\"))"'  # example: pchr 65  # A  # unichr(0-65535)
# 进制转换
alias phex 'python -c "print hex(int(\"$argv[1]\"))"'  # example: phex 16  # 0x10
alias pbin 'python -c "print bin(int(\"$argv[1]\"))"'  # example: pbin 16  # 0b10000
alias poct 'python -c "print oct(int(\"$argv[1]\"))"'  # example: poct 16  # 020
alias pint16 'python -c "print int(\"$argv[1]\", 16)"'  # example: pint16 0x10  # 16  # int('string', base)

# 生成随机字符
# alias prans 'python -c "import random, string; print ''.join(random.sample(string.ascii_letters + string.digits + '()~!@#$%^&*-+=|\'{}[]:;<>,.?/', $argv[1]))"'  # prans 32
# alias pransd 'python -c "import random, string; print random.choice(string.ascii_letters) + \
    # ''.join(random.sample(string.ascii_letters + string.digits + '()~!@#$%^&*-+=|\'{}[]:;<>,.?/', int(\"$argv[1]\") - 1))"'  # 以字母开头, pransd 32
# 普通运行
alias rpy 'python -c "print $argv[1]" }'  # ryp 0xffffd6cc-0xffffd680, 不用带引号
alias pyte 'cd ~/Documents/thiscandel; and vim te.py'

# 安装 不用 sudo 权限容易有问题, -H 指定 HOME 目录为目标的, 默认是 阿里源
alias pypyinstall 'sudo -H pypy -m pip install'
alias pythoninstall 'sudo -H python -m pip install'
alias python3install 'sudo -H python3 -m pip install'
alias pipali 'pip install --index http://mirrors.aliyun.com/pypi/simple/'

# help package
alias pyhelp 'python -c "help(\"$argv[1]\")"'  # eg: pyhelp socket, pyhelp argparse

# 代理问题, Missing dependencies for SOCKS support.
alias pipproxyclear 'unset all_proxy; and unset ALL_PROXY'
# unset all_proxy
# unset ALL_PROXY

##################################################################
## JavaScript, ln -s
##################################################################
alias ppw 'pug -P -w'  # for pug 实时编译
alias cwc 'coffee -wc'  # for coffee 实时编译
alias cbpe 'coffee -bpe'

alias lnsbootstrap 'ln -s ~/github/jWeb/CDN/bootstrap .'  # 进项目的根目录执行
alias lnsjquery 'ln -s ~/github/jWeb/CDN/jquery .'
alias lnspure 'ln -s ~/github/jWeb/CDN/pure .'
alias lnsuikit 'ln -s ~/github/jWeb/CDN/uikit .'
alias lnsvue 'ln -s ~/github/jWeb/CDN/vue .'
alias lnsd3 'ln -s ~/github/jWeb/CDN/d3 .'
alias lnsimage 'ln -s ~/github/jImage .'
alias npmhttpfr 'sudo npm config set proxy http://192.168.1.13:8080 -g; and sudo npm config set https-proxy http://192.168.1.13:8080 -g'
alias npmhttp 'sudo npm config set proxy http://localhost:1080 -g; and sudo npm config set https-proxy http://localhost:1080 -g'
alias npmnohttp 'sudo npm config rm proxy -g'
alias cnpm 'npm --registry=https://registry.npm.taobao.org \
    --cache=$HOME/.npm/.cache/cnpm \
    --disturl=https://npm.taobao.org/dist \
    --userconfig=$HOME/.cnpmrc'
# npm config get proxy; npm config set proxy null; npm config delete proxy; npm config set https-proxy null; npm config set strict-ssl false
# npm config set registry http://registry.npmjs.org/  # 就是这句和下面那句帮我修复了 npm
# npm cache clean

##################################################################
## Java && Opengl
##################################################################
alias javac 'javac -J-Dfile.encoding=utf8'
alias opengl 'g++ $argv[1] -o gl -lGL -lGLU -lglut; ./gl'  # example: grepf hello '*.md'
# alias opengl 'g++ -o gl -lGL -lGLU -lglut'  # 文件名必须放前面
