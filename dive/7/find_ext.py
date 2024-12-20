import os
import sys

def find_ext(dir, ext):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                print(os.path.join(root, file))

if __name__ == "__main__":
    try:
        find_ext(sys.argv[1], sys.argv[2])
    except Exception as ex: print(ex)