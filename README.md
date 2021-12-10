# NFT Provenance Hash Generator
Dead Simple python script to generate an SHA256 Provenance Hash for an NFT series. This assumes your images are named in sequence, `0.png`, `1.png`, etc. (gif, jpg etc. work as well). Should be easy to hack as needed.


1. Edit the following vars:
```python
imgCount     = 10             # <-- How many images are there?
outputFolder = "../renders"   # <-- Where are they?
fmt          = "png"          # <-- What format / file extension?
```

2. Then fire away..
```bash
python3 provenance_hash.py
```

Output will be a series of text files in your `outputFolder`:
* `provenance_hash.txt`  - containing the 'final proof hash'
* `provenance_record.csv`  - .csv file containing image names and sha-256 hashes in order
* `provenance_str.txt`  - containing a concatenated string of the image hashes in order

---
<!-- NOTES -->
### Notes

