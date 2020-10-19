from subprocess import run, CalledProcessError
import os, sys
import urllib

update = ["sudo", "apt-get", "-y", "update"]
upgrade = ["sudo", "apt-get", "-y", "upgrade"]
install1 = ["sudo", "apt-get", "-y", "install", "clinfo", "unzip", "p7zip-full"]
pip = ["pip3", "install", "psutil"]


command = [update, upgrade, install1, pip]

if os.path.isfile("/var/lib/dpkg/lock-frontend"):
    print("Now dpkg running. Try it in a few minutes:)")

else:
    for c in command:
        try:
            res = run(c, stdout=sys.stdout)
        except CalledProcessError as e:
            print(e.output)
