import os
import json
import csv

def get_size(path : str) -> int:
    if os.path.isfile(path): return os.path.getsize(path)

    tot = 0
    for dir, _, files in os.walk(path):
        for file in files:
            current_path = os.path.join(dir, file)
            tot += os.path.getsize(current_path)

    return tot;

def traverse(dir : str) -> list:
    res = []

    for root, dirs, files in os.walk(dir):
        for name in dirs + files:
            current_path = os.path.join(root, name)
            res.append(
                {
                    "name" : name,
                    "path" : current_path,
                    "type" : "dir" if os.path.isdir(current_path) else "file",
                    "size" : get_size(current_path),
                    "parent" : os.path.basename(root),
                }
            )
    
    return res

def to_json(data, file):
    with open(file, "w") as _file:
        json.dump(data, _file)

def to_csv(data, file):
    with open(file, "w") as _file:
        writer = csv.DictWriter(_file, fieldnames=["name", "path", "type", "size", "parent"])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    dir = os.getcwd()
    
    # print(traverse(dir))
    to_csv(traverse(dir), os.path.join(dir, "_test.csv"))