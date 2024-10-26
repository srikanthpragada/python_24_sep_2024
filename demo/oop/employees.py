from abc import ABC, abstractmethod


# Abstract class
class Employee(ABC):
    def __init__(self, name, desg):
        self.name = name
        self.desg = desg

    def setdesg(self, newdesg):
        self.desg = newdesg

    # Abstract Method
    @abstractmethod
    def getsalary(self):
        pass


class Consultant(Employee):
    def __init__(self, name, desg, hours, rate):
        super().__init__(name, desg)
        self.hours = hours
        self.rate = rate

    def getsalary(self):
        return self.hours * self.rate

class SalariedEmployee(Employee):
    def __init__(self, name, desg, salary):
        super().__init__(name, desg)
        self.salary = salary 

    def getsalary(self):
        return self.salary


class Trainee(Employee):
    def __init__(self, name, desg):
        super().__init__(name, desg)

    def getsalary(self):
        return 5000


#e = Employee("James", "Tester")

c = Consultant("Jack", "DBA", 10, 2000)
c.setdesg("Oracle DBA")
print(c.getsalary())

t = Trainee("Scott", "Programmer")
print(t.getsalary())

# print(isinstance(c, Employee))
# print(isinstance(c, Consultant))
# print(issubclass(Consultant, Employee))
# print(issubclass(Consultant, str))
