
f = open("salaries.txt","wt")

while True:
    name = input("Enter department name [end to stop] :")
    if name == 'end':
        break

    f.write(name)
    while True:
        salary = int(input("Enter salary [0 to stop] :"))
        if salary == 0:
            break

        f.write("," + str(salary))

    f.write("\n")

f.close()



