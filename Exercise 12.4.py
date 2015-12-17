import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
c=0
tags = soup('p')
for tag in tags:
    c = c+1
print 'Number of paragraphs',c
