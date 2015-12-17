file = raw_input('Enter File: ')
fhand = open(file)
mail = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.split()
        if len(line)>=2:
            word = line[1]
            if word in mail:
                mail[word] += 1
            else:
                mail[word] = 1
t = list()
for key,val in mail.items():
    t.append((val,key))
t.sort(reverse=True)
print t[0][1],t[0][0]



