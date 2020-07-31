#! python3
# strongPasswordDetection.py - Write a function that uses regular expressions 
# to make sure the password string it is passed is strong. A strong password is 
# defined as one that is at least eight characters long, contains both 
# uppercase and lowercase characters, and has at least one digit. You may need 
# to test the string against multiple regex patterns to validate its strength.

import re

strongPasswordRegex = re.compile(r'^(?=.*\d)(?=.*[A-Z])\w{8,}$')

def checkPasswordStrength(thePassword):
    searchResults = strongPasswordRegex.search(thePassword)
    return searchResults

passwords = ['12345', 'Asc11R0ad', 'TheyCallMeStarLord', 'TheyCallMeStarL0rd', 'N01Ca77541MStarL0rd']
for password in passwords:
    if checkPasswordStrength(password):
        print(f'{password} is good.')
    else:
        print(f'Don\'t use {password}. It\'s not strong enough.')