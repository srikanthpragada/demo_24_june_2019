class Employee:

    def __init__(self, name, salary, grade=1):
        self.name = name
        self.salary = salary
        self.grade = grade

    def print_details(self):
        print("Name   : ", self.name)
        print("Salary : ", self.salary)
        print("Grade  : ", self.grade)

    def get_salary(self):
        if self.grade == 1:
            return self.salary + self.salary * .30
        else:
            return self.salary + self.salary * .25

    def set_grade(self, grade):
        self.grade = grade


e1 = Employee("Scott",100000,2)
e2 = Employee("Mike",50000)



