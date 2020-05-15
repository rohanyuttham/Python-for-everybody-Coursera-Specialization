import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input("Enter location: ")
print('Retrieving',location)

xml = urllib.request.urlopen(location).read()
print('Retrieved', len(xml), 'characters')


tree = ET.fromstring(xml)
#print(stuff)
lst = tree.findall('comments/comment')

# print(lst)
print('Count:',len(lst))
Sum=0
for nodes in lst:
    num = nodes.find('count').text
    Sum=Sum+int(num)

print('Sum:',Sum)
