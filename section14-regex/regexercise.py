import re

pattern = re.compile(r"([a-zA-Z0-9\$%#@\d$]{8,})")
password = 'na$%@123'

a = pattern.fullmatch(password)

if a:
    print("Password is good")
else:
    print("Password at least 8 character")