
students = {}

while True:
    rollno =int(input("Enter rollno [0 to stop] :"))
    if rollno == 0:
        break

    marks  = int(input("Enter marks :"))
    students[rollno] = marks


for r,m in sorted(students.items()):
    print(f"{r:5d} {m:3d}")


