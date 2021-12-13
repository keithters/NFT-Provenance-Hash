import os
import hashlib

imgCount     = 10                        # <-- How many images are there?
outputFolder = './renders'    # <-- Where are they?
fmt          = "png"                     # <-- What format / file extension?

def make_hash():
    i                   = 0
    concatenated_str    = ""
    provenance_hash     = ""

    path = f"{outputFolder}/provenance_hash.txt"
    if os.path.exists(path): os.remove(path)
    f = open(path, 'a')

    record_csv = f"{outputFolder}/provenance_record.csv"
    if os.path.exists(record_csv): os.remove(record_csv)
    rc = open(record_csv, 'a')

    print ("File Name,SHA-256 HASH", file=rc)

    str_path = f"{outputFolder}/provenance_str.txt"
    if os.path.exists(str_path): os.remove(str_path)
    sf = open(str_path, 'a')

    while i < imgCount:
        with open(f"{outputFolder}/{i}.{fmt}", "rb") as img:
            h = hashlib.sha256()
            data = img.read()
            h.update(data)
            hash = h.hexdigest()
            concatenated_str = concatenated_str + hash
            print (f"{i}.{fmt},{hash}", file=rc)
            print (hash)
            i = i + 1

    provenance_hash = hashlib.sha256(concatenated_str.encode('utf-8')).hexdigest()
    print(f"Provenance_Hash = {provenance_hash}")
    print(provenance_hash, file=f)
    print(concatenated_str, file=sf)
#---

make_hash()
