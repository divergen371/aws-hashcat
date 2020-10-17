#!/bin/bash

mkdir wordlist
git clone https://github.com/danielmiessler/SecLists.git ~/wordlist/seclists
wget -nH http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2 -O ~/wordlist/rockyou.txt.bz2

cd wordlist
bunzip2 ./rockyou.txt.bz2
cd ~

