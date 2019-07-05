
nums = [10, 20, 39, 45, 60]
names = ["java","Ruby", "Python","c","C#","JavaScript"]

for n in sorted(nums, reverse=True):
    print(n)

# for n in sorted(names, key = len):
#     print(n)

for n in sorted(names, key = str.upper):
    print(n)

d = {1 : 10, 4 : 5, 3:20,2:6}

for t in sorted(d.items(), key = lambda t : t[1]):
    print(t)
