nums = [[], []]

for i in range(1, 6):
    n = int(input("Enter a number :"))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)

print(nums)
