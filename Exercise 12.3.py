import urllib
try:
    url = raw_input("Enter URL: ")
    file = urllib.urlopen(url)
    fhand = file.read()
    c = 0
    data = ''
    for i in fhand:
        c += 1
        data += i
    print data[:3001]
    print "Number of characters:",c
except:
    print 'Error, enter a valid URL'
    
