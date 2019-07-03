
students = {}

while True:
    rollno =int(input("Enter rollno [0 to stop] :"))
    if rollno == 0:
        break

    marks  = int(input("Enter marks :"))
    if rollno in students:
        students[rollno].append(marks)
    else:
        students[rollno] = [marks]


for r,m in sorted(students.items()):
    print(f"{r:5d} {m}")


