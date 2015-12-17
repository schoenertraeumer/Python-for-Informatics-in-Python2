import os
from os.path import join
d = dict()
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.mp3'):
            thefile = os.path.join(dirname,filename)
            size = os.path.getsize(thefile)
            if size in d:
                d[size] += thefile
                print size,d[size]
            else:
                d[size] = thefile
