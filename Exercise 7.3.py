try:
    file = raw_input("Enter the file name: ")
    if file=='na na boo boo':
        print "NAN NA BOO BOO TO YOU - You have been punk'd!"
    else:
        c=0
        fhand = open(file)
        for line in fhand:
            c+=1
        print 'There were',c,'subjects lines in',file
except:
    print 'File cannot be opened:',file
