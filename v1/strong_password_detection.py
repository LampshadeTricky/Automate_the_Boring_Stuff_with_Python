#! python3

import re

REGEX = re.compile(r'\d+[^0-9a-zA-Z]*[A-Z]+[^0-9a-zA-Z]*[a-z]+')


def is_strong_password(password):
    print(re.search(REGEX, ''.join(sorted(password))))
    return len(password) >= 8 and bool(re.search(REGEX, ''.join(sorted(password))))


assert is_strong_password('abc!@#123ABC<>/.,{}\\|') is True
assert is_strong_password('abc123ABC') is True
assert is_strong_password('aA1') is False
assert is_strong_password('!@#$%^&*(') is False
assert is_strong_password('<A<b<2<<') is True
assert is_strong_password('x1y2z3TT') is True