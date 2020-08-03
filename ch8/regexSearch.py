#! python3
# regexSearch.py - Write a program that opens all .txt files in a folder and 
# searches for any line that matches a user-supplied regular expression. The 
# results should be printed to the screen.

import os, re

os.chdir('c:\\users\\jonat\\documents\\python\\Automate_the_Boring_Stuff_with_Python\\ch8')
folderName = os.getcwd()
txtList = [files for files in os.listdir() if files.endswith('.txt')]

searchString = r'summer'
regEx = re.compile(searchString)

for fileName in txtList:
    theFile = open(os.path.join(folderName, fileName))

    searchText = theFile.read()
    theFile.close()

    checkString = regEx.search(searchText)
    if checkString != None:
        print(f'{os.path.join(folderName, fileName)} ' + \
              'contains the string you want.')