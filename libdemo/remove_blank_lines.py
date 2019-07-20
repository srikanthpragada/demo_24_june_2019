
f = open("names.txt","rt")

lines = []
for l in f:
    l = l.strip('\n')
    if len(l.strip(' ')) > 0:
        lines.append(l)


f.close()

f = open("names.txt","wt")

for l in lines:
    f.write(l + "\n")

f.close()
