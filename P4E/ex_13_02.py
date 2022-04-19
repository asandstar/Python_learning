import urllib.request, urllib.parse, urllib.error
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum = 0
c = 0
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    data = urllib.request.urlopen(address, context=ctx).read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)

    for item in info['comments']:
        count = int(item['count'])
        sum = sum + count
        c = c + 1

    print('Count:', c)
    print('Sum:', sum)
