import os
import hashlib
from PIL import Image


imgCount     = 10                        # <-- How many images are there?
outputFolder = "../turfmaker/renders"    # <-- Where are they?
fmt          = "png"                     # <-- What format / file extension?

def make_hash():
    i               = 0
    provenance_hash = ""

    path = f"{outputFolder}/provenance_hash.txt"
    if os.path.exists(path): os.remove(path)
    f = open(path, 'a')

    while i < imgCount:
        img = Image.open(f"{outputFolder}/{i}.{fmt}")
        hash = hashlib.sha256(img.tobytes()).hexdigest()

        f = open(f"{outputFolder}/{i}_hash.txt", 'w')
        print (hash, file=f)

        provenance_hash = provenance_hash + hash
        i = i + 1

    f = open(path, 'a')
    print(provenance_hash, file=f)
#---
make_hash()