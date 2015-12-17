import re

exp = raw_input("Enter a regular expression: ")
file = open('mbox.txt')
c = 0
for line in file:
    line = line.rstrip()
    if re.search(exp,line):
        c+=1
print 'mbox.txt had',c,'lines that matched',exp
