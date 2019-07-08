import sys

num = int(sys.argv[1])

size = 20
if len(sys.argv) > 2:
    size = int(sys.argv[2])

for i in range(1,size + 1):
    print(f"{num:5}  * {i:2} = {num * i:5}")