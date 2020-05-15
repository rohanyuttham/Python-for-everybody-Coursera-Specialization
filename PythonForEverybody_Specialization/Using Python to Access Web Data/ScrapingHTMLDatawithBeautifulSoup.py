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
Sum=0
Count=0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    Sum+=int(tag.contents[0])
    Count=Count+1
print('Count',Count)
print('Sum',Sum)
