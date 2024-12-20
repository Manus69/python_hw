import os
import zipfile
import sys

def zip_dir(dir, fname):

    with zipfile.ZipFile(fname, 'w', zipfile.ZIP_DEFLATED) as arch:
        for root, dirs, files in os.walk(dir):
            for file in files:
                path = os.path.join(root, file)
                arch.write(path, os.path.relpath(path, dir))

if __name__ == "__main__":
    try:
        zip_dir(sys.argv[1], sys.argv[2])
    except Exception as ex: print(ex)