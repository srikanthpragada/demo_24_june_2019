ln = 0
while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num > ln:
        ln = num

print("Largest number : ", ln)