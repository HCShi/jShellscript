#!/bin/bash
eval "echo hello"
eval "ls"
eval "echo 'hello world'"  # 可以嵌套
eval ls  # 可以不加引号
