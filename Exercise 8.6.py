t = list()
while 1:
       try:
           number = raw_input('Enter a number: ')
           if number=='done': break
           number = float(number)
           t.append(number)
           
       except:
           print 'Error, enter a numeric input'
           continue
print 'Maximum:',max(t)
print 'Minimum:',min(t)

       
