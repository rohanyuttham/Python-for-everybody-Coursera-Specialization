name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    try:
        if line.split()[0]=='From':
            counts[line.split()[5].split(':')[0]]=counts.get(line.split()[5].split(':')[0],0)+1
    except:continue
for k,v in sorted(counts.items()):
    print(k,v)



        

