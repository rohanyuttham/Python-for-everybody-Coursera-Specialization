fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
	try:
		if line.split()[0]=='From':
			print(line.split()[1])
			count = count+1
	except: 
		continue

print("There were", count, "lines in the file with From as the first word")

