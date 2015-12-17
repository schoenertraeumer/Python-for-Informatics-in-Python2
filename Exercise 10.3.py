import string
sp = string.punctuation
space = ' ','\n','\t'
num = ['1','2','3','4','5','6','7','8','9','0']

file = raw_input('Enter File: ')
fhand = open(file)
f = dict()
for line in fhand:
    if len(line)==0: continue
    line = line.lower()
    for word in line:
        if word in space : continue
        if word in num : continue
        if word in sp: continue
        if word in f:
            f[word] +=1
        else:
            f[word]=1
t=list()
for key,val in f.items():
      t.append((val,key))
t.sort()
for (val,key) in t:
    print key,val
