import os
import sys
import pathlib
import zipfile
dirName = input("Enter Directory name that you want to backup : ")
if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exists")
    sys.exit(0)
curDirectory = pathlib.Path(dirName)
number = 1
while True:
    zipFilename = os.path.basename(curDirectory) + '_' + str(number) + '.zip'
    if not os.path.exists(zipFilename):
        break
    number = number + 1
print(f'Creating {zipFilename}...')
with zipfile.ZipFile(zipFilename, mode="w") as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(curDirectory))
if os.path.isfile(zipFilename):
    print("Archive", zipFilename, "created successfully")
else:
    print("Error in creating zip archive")
