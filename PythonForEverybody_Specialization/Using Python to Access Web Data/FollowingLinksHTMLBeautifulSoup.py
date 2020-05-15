import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter Count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
print("Retrieving:",url)
tags = soup('a')
#print(tags[position].contents[0])

i=0
while True:
    nurl=tags[position-1].get('href',None)
    print("Retrieving:",nurl)
    nhtml = urllib.request.urlopen(nurl,context=ctx).read()
    nsoup=BeautifulSoup(nhtml,'html.parser')
    tags=nsoup('a')
    #print(tags[position].contents[0])
    i=i+1
    if i==count: break
