from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
Count = 0
Sum = 0
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('class', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    nStr = ""
    nStr = nStr.join(tag.contents[0])
    tag.contents[0] = int(nStr)
    Count = Count + 1
    Sum = Sum + tag.contents[0]

print("Count ", Count)
print("Sum ", Sum)
