f = open("marks.txt", "rt")

students = {}

for line in f:
    rollno, marks = line.strip("\n").split(",")

    if rollno in students:
        students[rollno] += int(marks)
    else:
        students[rollno] = int(marks)

print(students)
