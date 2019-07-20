import os
import sys

root = "."

if len(sys.argv) < 2:
    pattern = input("Enter pattern :")
else:
    pattern = sys.argv[1]


if len(sys.argv) > 2:
    root = sys.argv[2]

for (name,dirs,files) in os.walk(root):
    for f in files:
        if f.find(pattern) >= 0:
            print( name + "\\" + f)






