def iseven(n):
    return n % 2 == 0


nums = [10, 20, 39, 45, 60]

for n in filter(iseven, nums):
    print(n)

for n in filter(lambda n: n % 2 != 0, nums):
    print(n)
