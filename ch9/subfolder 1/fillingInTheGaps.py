#! python3
# fillingInTheGaps.py - Write a program that finds all files with a given 
# prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and 
# locates any gaps in the numbering (such as if there is a spam001.txt and 
# spam003.txt but no spam002.txt). Have the program rename all the later files 
# to close this gap.

# Only matches where there is a single number between the prefix and the suffix.

import os, re, shutil

searchString = r'(spam)(\d*)(\.txt)'

# Set folder names
os.chdir('c:\\users\\jonat\\documents\\python\\' + \
        'Automate_the_Boring_Stuff_with_Python\\ch9')
rootFolder = os.getcwd()

# Get list of filenames that match search string pattern
regEx = re.compile(searchString)
fileList = regEx.findall(str(os.listdir()))

# Start file counter
counter = 1

for fileName in fileList:
    prefix = fileName[0]
    suffix = fileName[2]

    oldPath = os.path.join(rootFolder, prefix + str(fileName[1]) + suffix)
    newPath = os.path.join(rootFolder, prefix + str(counter) + suffix)
    shutil.move(oldPath, newPath)

    counter += 1