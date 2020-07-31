#! python3
# commaCode.py - Write a function that takes a list value as an argument and 
# returns a string with all the items separated by a comma and a space, with 
# and inserted before the last item. For example, passing the previous spam 
# list to the function would return 'apples, bananas, tofu, and cats'. But 
# your function should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']

def commaList(theList):    
    return ', '.join(theList[:-1]) + ', and ' + theList[-1]

print(commaList(spam))