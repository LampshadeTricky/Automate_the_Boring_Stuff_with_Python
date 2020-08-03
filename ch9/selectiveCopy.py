#! python3
# selectiveCopy.py - Write a program that walks through a folder tree and 
# searches for files with a certain file extension (such as .pdf or .jpg). Copy 
# these files from whatever location they are in to a new folder.

import os, shutil

selectedExtensions = ['jpg', 'png', 'gif']

# Set folder names
os.chdir('c:\\users\\jonat\\documents\\python\\Automate_the_Boring_Stuff_with_Python\\ch9')
folderName = os.getcwd()
subFolder = os.path.join(folderName, 'subfolder')
if not os._exists(subFolder):
    os.mkdir(subFolder)

fileList = [files for files in os.listdir() if files[-3:] in selectedExtensions]

for fileName in fileList:
    sourceFile = os.path.join(folderName, fileName)
    destinationFile = os.path.join(subFolder, fileName)    
    shutil.copy(sourceFile, destinationFile)