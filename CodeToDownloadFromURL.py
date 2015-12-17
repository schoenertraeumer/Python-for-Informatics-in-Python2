import urllib
from bs4 import BeautifulSoup

url = 'http://www.py4inf.com/code/'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tags = soup('a')
for tag in tags:
    t = tag.get('href', None)
    if t.endswith('.txt'):
        doc = url+t
        file = urllib.urlopen(doc)
        temp = ''
        for line in file:
            temp+=line
        new = open(t,'w')
        new.write(temp)
        
print 'end'
