#! python3
# collazSequence.py - Write a function named collatz() that has one parameter 
# named number. If number is even, then collatz() should print number // 2 and 
# return this value. If number is odd, then collatz() should print and return 
# 3 * number + 1. Then write a program that lets the user type in an integer 
# and that keeps calling collatz() on that number until the function returns 
# the value 1.

def collaz(theNumber):
    if theNumber == 1:
        return 1
    elif theNumber % 2 == 0:
        theNumber = theNumber // 2
    elif theNumber % 2 == 1:
        theNumber = 3 * theNumber + 1
    
    print(theNumber)
    return collaz(theNumber)

# Main program
print('Enter a number to sequence: ')
theNumber = int(input())
collaz(theNumber)