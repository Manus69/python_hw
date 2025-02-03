import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

_LOGFNAME = ".log.log"
Info = namedtuple("Info", ["name", "ext", "is_dir", "parent"])
logging.basicConfig(filename=_LOGFNAME, level=logging.INFO, format="%(asctime)s - %(message)s")

def _Info_str(info):
    ext = "n/a" if info.ext is None else info.ext
    dir = "dir" if info.dir else "file"

    return f"{info.name}, {ext}, {dir}, {info.parent}"

def get_info(path):
    if not os.path.isdir(path): raise FileNotFoundError()

    parent = os.path.basename(os.path.abspath(path))

    for item in os.listdir(path):
        _path = os.path.join(path, item)

        if os.path.isdir(_path):
            info = Info(name=item, ext=None, is_dir=True, parent=parent)
        else:
            name, ext = os.path.splitext(item)

            info = Info(name=name, ext=ext, is_dir=False, parent=parent)

        logging.info(_Info_str(info))

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("dir", type=str, help="dir path")

    path = parser.parse_args().dir
    try:
        get_info(path)
        print(f"Info logged to {_LOGFNAME}")
    except Exception as ex: print(ex)


