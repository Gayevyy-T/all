#!/bin/bash

> oldFiles.txt

files=$(grep ' jane ' ~/data/list.txt | cut -d ' ' -f3)
for f in $files; do
        if test -e ~/$f; then
                echo $HOME$f >> oldFiles.txt;     #$HOME$f == ~/$f
        fi
done
