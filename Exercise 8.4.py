file = raw_input('Enter file: ')
t = list()
fhand = open(file)
for line in fhand:
    line = line.split()
    for word in line:
        if word not in t: t.append(word)
t.sort()
print t
