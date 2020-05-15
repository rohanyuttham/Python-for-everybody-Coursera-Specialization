name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    try:
        if line.split()[0]=='From':
            counts[line.split()[1]]=counts.get(line.split()[1],0)+1
    except:continue

maxkey=None
maxvalue=None
for k,v in counts.items():
    if maxkey is None or v>=maxvalue:
        maxvalue=v
        maxkey=k
print(maxkey,maxvalue)
        				

