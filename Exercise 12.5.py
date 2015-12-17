import socket
import re
url = raw_input("Enter URL : ")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = url.split('/')
port = port[2]
mysock.connect((port,80))
mysock.send('GET '+url+' HTTP/1.0\n\n')
doc=''
while 1:
   data = mysock.recv(5120)
   if (len(data) < 1): break
   doc += data

pos = doc.find("\r\n\r\n")
print doc[pos+4:]
