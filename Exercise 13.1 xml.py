import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    try:
        address = raw_input('Enter location: ')
        if len(address) < 1 : break

        url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

        uh = urllib.urlopen(url)
        data = uh.read()

        tree = ET.fromstring(data)


        results = tree.findall('result')
        
        code = results[0][6][1].text
        print 'Country Code: ',code
    except:
        print "Country Code, Not Available"
