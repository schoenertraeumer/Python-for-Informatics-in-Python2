import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    try:
        address = raw_input('Enter location: ')
        if len(address) < 1 : break

        url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
        
        uh = urllib.urlopen(url)
        data = uh.read()
        

        js = json.loads(str(data))
        

        code = js["results"][0]["address_components"][3]["short_name"]
        print 'Country Code: ',code
    except:
            print 'Country Code, Not available'
            continue
