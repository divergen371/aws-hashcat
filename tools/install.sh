#!/bin/bash

if [ -e /var/lib/dpkg/lock-forntend ]; then
    echo "dpkg running come back in a few minutes:)"
    exit 255
fi

if [ ! -e ~/.updatefin ]; then
    sudo apt update
    sudo apt upgrade
    sudo apt install clinfo unzip p7zip-full
    #sudo apt install build-essential linux-headers-$(uname -r)
    pip3 install psutil
    touch ~/.updatefin

    echo "update completed"
    exit 1
fi

echo "Download hashcaaaat"
wget https://hashcat.net/files/hashcat-6.1.1.7z
7z x hashcat-6.1.1.7z
