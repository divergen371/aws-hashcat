#!/bin/bash

if [ ! -e ~/.dependinstall ]; then
    # キャプチャしたパケットをhashcatおよびjohn the ripperで解析するためのパケット変換ツール。
    git clone https://github.com/ZerBea/hcxtools.git
    cd ./hcxtools.sh
    make
    sudo make install
    touch ~/.dependinstall
fi

rm ~/.dependinstall
