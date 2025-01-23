import json
import csv

def json_csv(jfile, cfile):
    try: 
        with open(jfile, "r") as _jfile:
            data = json.load(_jfile)
        
        with open(cfile, "w") as _cfile:
            writer = csv.DictWriter(_cfile)
            writer.writeheader()
            writer.writerows(data)
        
    except Exception as ex: raise ex
