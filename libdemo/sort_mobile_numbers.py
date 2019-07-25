import re

f = open("mobiles.txt","rt")
mobiles = set()

for line in f:
    phones = re.findall(r'\d+',line)
    for p in phones:
        if len(p) == 10:
            mobiles.add(p)


f.close()
print(sorted(mobiles))
