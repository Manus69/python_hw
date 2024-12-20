import os
import sys

def batch_rename(dir, name, ndigits, old_extension, new_extension) -> int:
    files = [x for x in os.listdir(dir) if x.endswith(old_extension)]

    count = 0
    format_str = f"{{:0{ndigits}d}}"

    for idx, fname in enumerate(files):
        count += 1
        base_name = os.path.splitext(fname)[0]
        new_name = f"{base_name}_{name}_{format_str.format(idx)}.{new_extension}"
        os.rename(os.path.join(dir, fname), os.path.join(dir, new_name))

    return count

if __name__ == "__main__":
    try:
        batch_rename(* sys.argv[1:])
    except Exception as ex: print(ex)