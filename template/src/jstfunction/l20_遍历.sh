#!/bin/bash

for file in $(ls); do
    echo $file
    if [ -d $file ]; then
        echo $file; cd $file; pwd; cd ..
    fi
    if [ $file == "l4_string.sh" ]; then
        echo "hello world     "$file
    fi
done
