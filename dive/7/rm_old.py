import sys
import os
import time

_SPD = 86400

def rm_old(dir, ndays):
    target = time.time() - ndays * _SPD

    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            mtime = os.path.getmtime(path)

            if mtime < target: os.remove(path)

if __name__ == "__main__":
    try:
        rm_old(sys.argv[1], int(sys.argv[2]))
    except Exception as ex: print(ex)