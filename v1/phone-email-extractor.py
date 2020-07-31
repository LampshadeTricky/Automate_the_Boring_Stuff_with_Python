#1 python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegEx = re.compile(r'''(
    # 212-555-1212, 555-1212, (415) 555-1212, 555-1212 ext/ext./x 12345
    (\d{3} | \(\d{3}\))?            # area code (optional)
    (\s|‐|\.)?                      # first separator
    (\d{3})                         # first three digits
    (\s|‐|\.)                       # second separator
    (\d{4})                         # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension number (optional)
    )''', re.VERBOSE)

# Create a regex for email addresses
emailRegEx = re.compile(r'''
    [a-zA-Z0-9_.+]+  # username
    @               # @
    [a-zA-Z0-9_.+]+  # domain name
    ''', re.VERBOSE)
# Get text from clipboard
text = pyperclip.paste()

# TODO: extract email/phone from text
extractedPhone = phoneRegEx.findall(text)
extractedEmail = emailRegEx.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

allEmailAddresses = []
for emailAddress in extractedEmail:
    allEmailAddresses.append(emailAddress)

results = 'Phone Numbers:\n>' + \
          '\n>'.join(allPhoneNumbers) + \
          '\n\n' + \
          'Email Addresses:\n>' + \
          '\n>'.join(allEmailAddresses)

# Copy extracted email/phone to clipboard
pyperclip.copy(results)