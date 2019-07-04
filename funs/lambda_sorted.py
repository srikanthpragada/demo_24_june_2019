
nums = [10, 20, 39, 45, 60]
names = ["Java","Ruby", "Python","C","C#","JavaScript"]

for n in sorted(nums, reverse=True):
    print(n)

# for n in sorted(names, key = len):
#     print(n)

for n in sorted(names, key = lambda n : n[0:3] ):
    print(n)


