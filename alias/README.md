### bash/zsh
``` zsh
# alias 等号左右不能有空格
# oneko & # 打开终端出现一只小猫
# alias 后面用 "" 才能用 $1; 更新: alias 不支持 $1 $2, 请直接使用函数
```
### fish
``` zsh
'' 后面才能用 $argv[1]
```
和 zsh/bash 区别:
``` zsh
# 1. && -> ; and
# 2. test() 这些命令暂时注释了, 不支持 test() 写法
# 3. $? -> $status  # 上一个命令的返回值, 0 为正常返回, 1 为错误
# 4. cpd(){cp $tmp $1} 这类的命令不能用了 function cpd; cp $tmp $1; end
# 5. $(pwd)/`pwd` -> (pwd)  # 这种使用返回值的
# 6. $var -> {$var}
# 7. $1 -> $argv[1]
```
