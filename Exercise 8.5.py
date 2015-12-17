file = raw_input('Enter file: ')
t = list()
fhand = open(file,'r')
c = 0
for line in fhand:
    if line.startswith('From'):
        c+=1
        line = line.split()
        print line[1]
print 'There were',c,'lines in the file with From as the first word'
