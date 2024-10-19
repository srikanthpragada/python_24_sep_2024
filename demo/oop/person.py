class Person:
    def __init__(self, name, email):
        self.name = name
        # private attribute
        self.__email = email

    def getemail(self):
        return self.__email

p1 = Person("Garry", "garry@gmail.com")
print(p1.__dict__)

print(p1._Person__email)

