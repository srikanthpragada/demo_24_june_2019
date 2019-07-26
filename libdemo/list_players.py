import re
from datetime import datetime

f = open("players.txt")

players = {}

today = datetime.today()
for line in f:
    parts = line.strip("\n").split(',')
    if len(parts) < 2:
        continue

    try:
        dob = datetime.strptime(parts[1],'%d-%m-%Y')
        years = (today - dob).days // 365
        players[parts[0]] = years
    except:
        pass

for name,age in sorted(players.items(),key=lambda t : t[1]):
    print(f"{name:15} {age}")

