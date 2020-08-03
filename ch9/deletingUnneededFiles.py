#! python3
# deletingUnneededFiles.py - It’s not uncommon for a few unneeded but humongous 
# files or folders to take up the bulk of the space on your hard drive. If 
# you’re trying to free up room on your computer, you’ll get the most bang for 
# your buck by deleting the most massive of the unwanted files. But first you 
# have to find them. Write a program that walks through a folder tree and 
# searches for exceptionally large files or folders—say, ones that have a file 
# size of more than 100MB. (Remember, to get a file’s size, you can use 
# os.path.getsize() from the os module.) Print these files with their absolute 
# path to the screen.

import os, send2trash

# Set folder names
os.chdir('c:\\users\\jonat\\documents\\python\\' + \
        'Automate_the_Boring_Stuff_with_Python\\ch9')
        
rootFolder = os.getcwd()

deleteCount = 0
bytesSaved = 0

for folderName, subfolders, filenames in os.walk(rootFolder):
    for filename in filenames:

        filePath = os.path.join(folderName, filename)
        fileSize = os.path.getsize(filePath)

        if fileSize > 100 * 1048576:
            # send2trash.send2trash(filePath)
            print('Deleting: ' + filePath)
            deleteCount += 1
            bytesSaved += fileSize

print(f'{deleteCount} files have been removed.')
print(f'{bytesSaved} bytes have been saved.')