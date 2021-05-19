import re

pattern = re.compile('search this')
string = 'search this inside of this text please!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())
# print(a)
# print(b)
# print(c)