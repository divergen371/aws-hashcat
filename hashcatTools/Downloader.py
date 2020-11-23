import os
import urllib.error
import urllib.request
import sys
import time
from subprocess import CalledProcessError, run
from xtract import xtract
import requests
from bs4 import BeautifulSoup


# def apt_update():
#     update = ["sudo", "apt-get", "-y", "update"]
#     upgrade = ["sudo", "apt-get", "-y", "upgrade"]
#     install1 = [
#         "sudo",
#         "apt-get",
#         "-y",
#         "install",
#         "clinfo",
#         "unzip",
#         "p7zip-full",
#         "python3-pip",
#     ]
#     pip = ["pip3", "install", "psutil", "requests", "beautifulsoup4"]
#     command = [update, upgrade, install1, pip]
#
#     if os.path.isfile("/var/lib/dpkg/lock-frontend"):
#         print("Now dpkg running. Try it in a few minutes:)")
#         sys.exit()
#     else:
#         for c in command:
#             try:
#                 run(c)
#             except CalledProcessError as e:
#                 print(e.output)


def downloadHashcat():
    """
    サイトのレイアウトが変わらない限り最新版をダウンロードする。

    """
    print("Downloading Hashcat...")
    url = "https://hashcat.net/"
    r = requests.get(url)
    html_content = r.text
    parsing_html = BeautifulSoup(html_content, "html.parser")
    id_download = parsing_html.find("div", {"id": "download"})
    link = id_download.findAll("a")[0]
    stuff = link.attrs["href"]
    hashcat_latest = url + stuff[1:]
    save_name = stuff[7:]
    try:
        urllib.request.urlretrieve(hashcat_latest, save_name)
        print("Download complete.")
        time.sleep(2)
    except urllib.error.URLError as urlError:  # 例外処理これでいいのか？
        print(urlError)
    if os.path.isfile(save_name):
        try:
            run(["7z", "x", save_name])
            print("Extracting archive completed:p")
            time.sleep(2)
        except CalledProcessError as e:
            print(e.output)


def downloadWordlist():
    if not os.path.isdir("./wordLists"):
        os.makedirs("./wordLists")

    SecLists = [
        "git",
        "clone",
        "https://github.com/danielmiessler/SecLists.git",
        "./wordLists/secLists",
    ]

    rockyou = [
        "wget",
        "-nH",
        "https://downloads.skullsecurity.org/passwords/rockyou.txt.bz2",
        "-O",
        "./wordLists/rockyou.txt.bz2",
    ]

    dictionaries = [SecLists, rockyou]

    for d in dictionaries:
        try:
            run(d)
            print("Download complete.")
            time.sleep(2)
        except CalledProcessError as e:
            print(e)

    xtract("./wordLists/rockyou.txt.bz2")


if __name__ == "__main__":
    downloadHashcat()
    downloadWordlist()
