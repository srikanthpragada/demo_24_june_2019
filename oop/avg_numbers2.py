count = total = 0

while True:
    try:
        num = int(input("Enter number :"))
        total += num
        count += 1
        if count == 5:
            break
    except:
        print("Sorry! Invalid number:")


print ("Avreage : ", total / 5)

