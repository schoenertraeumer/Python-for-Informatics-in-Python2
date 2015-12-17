file = raw_input('Enter File: ')
fhand = open(file)
day = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.split()
        if len(line)>=3:
            word = line[2]
            if word in day:
                day[word] += 1
            else:
                day[word] = 1
print day
            
