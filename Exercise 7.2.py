
file = raw_input("Enter file: ")
fhand = open(file)
sum = 0
c = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        num = float(line[pos+1:])
        sum += num
        c += 1
avg = sum/c
print 'Average spam confidence:',avg
