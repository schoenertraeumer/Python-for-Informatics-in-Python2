file = raw_input('Enter file: ')
fhand = open(file,'r')
words = dict()
for line in fhand:
    line = line.split()
    for word in line:
        if word not in words:
            words[word] = 1
print words
str = raw_input('Enter string: ')
if str in words:
    print str,'is in dictionary'
else:
    print str,'is not in dictionary'
    

       
