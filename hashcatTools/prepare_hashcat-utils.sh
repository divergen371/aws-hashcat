#!/bin/bash

if [ ! -e ~/.utilinstall ]; then
    git clone https://github.com/hashcat/hashcat-utils.git
    cd ./hashcat-utils
    make
fi
