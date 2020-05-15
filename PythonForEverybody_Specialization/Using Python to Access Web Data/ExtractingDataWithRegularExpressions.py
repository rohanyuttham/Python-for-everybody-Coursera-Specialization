import re
#fileName = input("Enter the file name: ")
fh=open("regex2.txt")
nums = list()
for line in fh:
    nums = nums + re.findall('[0-9]+',line)

tot=0
for i in nums:
    tot = tot + int(i)
print(tot)
GET http://rancholabs.com/learn/robo101/ HTTP/1.0
