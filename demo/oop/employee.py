
class Employee:
    def __init__(self, name, basicSalary, grade = 'a'):
        self.name = name
        self.basicSalary = basicSalary
        self.grade = grade

    def show(self):
        print(f"Name          : {self.name}")
        print(f"Basic Salary  : {self.basicSalary}")
        print(f"Grade         : {self.grade}")

    def getSalary(self):
        if self.grade == 'a':
            return  self.basicSalary * 1.3
        else:
            return self.basicSalary * 1.2

e1 = Employee("Richards", 50000)
print(e1.getSalary())

