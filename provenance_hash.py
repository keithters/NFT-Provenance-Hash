import os
import hashlib
from PIL import Image


imgCount     = 10                        # <-- How many images are there?
outputFolder = "../turfmaker/renders"    # <-- Where are they?
fmt          = "png"                     # <-- What format / file extension?

def make_hash():
    i                   = 0
    concatenated_str    = ""
    provenance_hash     = ""

    path = f"{outputFolder}/provenance_hash.txt"
    if os.path.exists(path): os.remove(path)
    f = open(path, 'a')

    record_path = f"{outputFolder}/provenance_record.txt"
    if os.path.exists(record_path): os.remove(record_path)
    rf = open(record_path, 'a')

    str_path = f"{outputFolder}/provenance_str.txt"
    if os.path.exists(str_path): os.remove(str_path)
    sf = open(str_path, 'a')

    while i < imgCount:
        img = Image.open(f"{outputFolder}/{i}.{fmt}")
        hash = hashlib.sha256(img.tobytes()).hexdigest()
        concatenated_str = concatenated_str + hash
        print (hash, file=rf)
        print (hash)
        i = i + 1

    provenance_hash = hashlib.sha256(concatenated_str.encode('utf-8')).hexdigest()
    print(f"Provenance_Hash = {provenance_hash}")
    print(provenance_hash, file=f)
    print(concatenated_str, file=sf)
#---

make_hash()
