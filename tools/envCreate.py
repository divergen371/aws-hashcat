from subprocess import check_call, CalledProcessError
import os
import urllib

update = check_call(["sudo", "apt", "update"], stdout=open(os.devnull, "wb"))
upgrade = check_call(["sudo", "apt", "upgrade"], stdout=open(os.devnull, "wb"))

apt = [update, upgrade]

for comm in apt:
    try:
        comm
    except CalledProcessError as e:
        print(e.output)
