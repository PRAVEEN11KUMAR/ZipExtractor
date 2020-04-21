from zipfile import ZipFile

filepath = "F:\python/praveen.zip"
with ZipFile(filepath, "r") as zip:
    zip.printdir()
    zip.extractall()
