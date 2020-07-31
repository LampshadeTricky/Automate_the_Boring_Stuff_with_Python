#! python3

import re

def regexStrip(theString, stripChar='\s'):
    theRegex = re.compile(f'^({stripChar})*|({stripChar})*$')
    stripContext = theRegex.sub('', theString)
    return stripContext

print(regexStrip('SpamEggsSpam','Spam'))
print(regexStrip('SpamSpamSpam$Eggs$SpamSpamSpam','Spam'))
print(regexStrip('    Eggs    '))
print(regexStrip('   $ Eggs $   '))