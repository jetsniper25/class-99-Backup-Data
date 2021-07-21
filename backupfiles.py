import os
import shutil
source=input("Enter the source folder name who's backup you want")
destination=input("Enter the destination folder where you want to keep the backup")
source=source+"/"
destination=destination+"/"
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.move((source+file),destination)