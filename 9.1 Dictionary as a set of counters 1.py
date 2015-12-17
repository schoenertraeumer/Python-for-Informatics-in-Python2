#file = raw_input('Enter File: ')
e = ['a','b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = list() 
c=0
for i in e:
    e[c] = ord(e[c])
    c+=1
pos = max(e)
for i in range(0,pos):
    print i
    
