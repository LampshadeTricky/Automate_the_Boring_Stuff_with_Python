#! python3

import re

madLibsString = "The ADJECTIVE panda walked to the NOUN and then VERB. \
A nearby NOUN was unaffected by the these events."

regExString = re.compile(r'[A-Z]{2,100}')

while True:
    result = regExString.search(madLibsString)                      # Find first match
    if result == None: break                                        # If no match then exit
    replacement = input(f'Enter a {result.group().lower()}: ')      # Get replacement word
    madLibsString = regExString.sub(replacement, madLibsString, 1)  # replace as you go

print(madLibsString)