# Testing that some of these changes work.
def collatz(theValue):
    if theValue % 2 == 0:
        theValue = theValue // 2
    else:
        theValue = theValue * 3 + 1

    print(str(theValue))
    if theValue != 1:
        collatz(theValue)

print('Enter number:')
try: collatz(int(input()))
except: print('Arrowed!!!')

# Adding some additional code down here
def test(name):
    print(name)