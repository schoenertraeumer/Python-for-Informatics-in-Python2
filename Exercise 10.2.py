file = raw_input('Enter File: ')
fhand = open(file)
t = list()
for line in fhand:
    if line.startswith('From'):
        line = line.split()
        if len(line)>=5:
            str = line[5]
            str = str.split(':')
            t.append((str[0],str[1]))
t.sort()
for (i,j) in t:
    print i,j
