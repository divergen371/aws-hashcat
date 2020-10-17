#!/bin/bash

sudo apt update
sudo apt upgrade
sudo apt install clinfo unzip p7zip-full
sudo apt install build-essential linux-headers-$(uname -r)
pip3 install psutil
