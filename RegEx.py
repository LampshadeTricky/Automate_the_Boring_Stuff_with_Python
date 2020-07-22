import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 at my office.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.findall(message)
print(mo)