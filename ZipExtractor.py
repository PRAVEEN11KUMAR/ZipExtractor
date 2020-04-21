# zipextractor.py

from zipfile import ZipFile

filepath = "F:\python/praveen.zip"
with ZipFile(filepath, "r") as zip:
    zip.printdir()
    zip.extractall()

    
#  zipfile.py

import zipfile

zf = zipfile.ZipFile("praveen.zip", "w")
zf.write("praveen.txt", compress_type=zipfile.ZIP_DEFLATED)
zf.close()
