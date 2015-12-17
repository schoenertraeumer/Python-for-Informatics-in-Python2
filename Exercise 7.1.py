file = raw_input("Enter file: ")
fhand = open(file,'r')
for line in fhand:
    print line.upper()
