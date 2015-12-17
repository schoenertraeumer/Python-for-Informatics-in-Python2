import re

c = 0
s = 0

file = raw_input('Enter file:')
fhand = open(file).read()
find = re.findall("New Revision: ([0-9]+)",fhand)
c = 0
s = 0
for i in find:
    i = float(i)
    c += 1
    s += i
print s/c
