file = raw_input('Enter File: ')
fhand = open(file)
day = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.split()
        if len(line)>=2:
            word = line[1]
            if word in day:
                day[word] += 1
            else:
                day[word] = 1

largest =None
for j in day.values():
    if largest is None or j > largest :
        largest  = j
print day.keys()[day.values().index(largest)],largest
