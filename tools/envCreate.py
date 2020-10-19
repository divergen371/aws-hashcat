import os
import sys
import urllib.request
from subprocess import CalledProcessError, run

import requests
from bs4 import BeautifulSoup


def apt_update():
    update = ["sudo", "apt-get", "-y", "update"]
    upgrade = ["sudo", "apt-get", "-y", "upgrade"]
    install1 = ["sudo", "apt-get", "-y", "install", "clinfo", "unzip", "p7zip-full"]
    pip = ["pip3", "install", "psutil", "requests", "beautifulsoup4"]
    command = [update, upgrade, install1, pip]

    if os.path.isfile("/var/lib/dpkg/lock-frontend"):
        print("Now dpkg running. Try it in a few minutes:)")

    else:
        for c in command:
            try:
                run(c)
            except CalledProcessError as e:
                print(e.output)


def downloader():
    """
    subprocessでwget使ったほうが早いと思うけど練習がてらということで。

    """
    url = "https://hashcat.net/"
    r = requests.get(url)
    html_content = r.text
    parsing_html = BeautifulSoup(html_content, "html.parser")
    download = parsing_html.find("div", "download")
    link = download.find_all("a")[0]
    stuff = link.attrs["href"]
    hashcat_latest = link + stuff[1:]
    save_name = stuff[7:]
    urllib.request.urlretrieve(hashcat_latest, save_name)
    if os.path.isfile(save_name):
        try:
            run(["7z", "x", save_name])
        except CalledProcessError as e:
            print(e.output)
