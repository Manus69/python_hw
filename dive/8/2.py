import json

def merge_json(in_files, out_file):
    data = []
    for file in in_files:
        with open(file, "r") as f:
            current = json.load(f)
            data.extend(current)

    with open(out_file, "w") as f:
        json.dump(data, f)

