import urllib.request
import json


url = input("Enter location: ")
print("Retrieving ", url)
data = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json = json.loads(data)

sum = 0
tot = 0

for comment in json["comments"]:
    sum += int(comment["count"])
    tot += 1

print('Count:', tot)
print('Sum:', sum)
