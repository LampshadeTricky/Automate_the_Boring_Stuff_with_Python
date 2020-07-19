# Testing that some of these changes work.
def collatz(theValue):
    if theValue % 2 == 0:
        theValue = theValue // 2
    else:
        theValue = theValue * 3 + 1

    print(str(theValue))
    if theValue != 1:
        collatz(theValue)

# Adding some additional code down here
def welcome_message(name):
    print('Welcome, ' + name + '!')

welcome_message('JonBrown')
print('Enter number:')
try: collatz(int(input()))
except: print('Arrowed!!!')