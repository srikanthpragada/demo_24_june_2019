
count = total = 0

for i in range(1,6):
    try:
        num = int(input("Enter number :"))
        total += num
        count += 1
    except:
        print("Sorry! Invalid number:")


print ("Avreage : ", total / count)

