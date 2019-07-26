import re

f = open("persons.txt")

persons = {}

for line in f:
    name = re.search('[a-zA-z ]+',line)
    if name is None:
        continue

    mobile = re.search('\d+',line)
    if mobile is None:
        continue

    persons[name.group().strip(' ')] = mobile.group()


for name,mobile in sorted(persons.items()):
    print(f"{name:15} {mobile}")

