#!/bin/bash

if [ -e /var/lib/dpkg/lock-forntend ]; then
    echo "dpkg running come back in a few minutes:)"
    exit 255
fi

if [ ! -e ~/.updatefin ]; then
    sudo apt update
    sudo apt upgrade
    sudo apt install clinfo unzip p7zip-full python3-pip
    #sudo apt install build-essential linux-headers-$(uname -r)
    pip3 install psutil requests beautifulsoup4
    touch ~/.updatefin

    echo "update completed"
fi
rm  ~/.updatefin


python3 ./Downloader.py
