#!/bin/bash
for file in *; do  # * 表示当前路径所有文件和目录, */ 表示所有目录
    echo $file
done
for file in ../jstgit/*; do  # 可以切换路径, 但末尾必须是 * 或者 */
    echo $file
done
