class Person:
    def __init__(self, name, email):
        self.name = name
        # private attribute
        self.__email = email

    def getemail(self):
        return self.__email

    def __str__(self):
        return f"{self.name} - {self.__email}"

    def __lt__(self, other):
        # print("__lt__")
        return self.name < other.name


p1 = Person("Garry", "garry@gmail.com")
print(p1.__dict__)
print(p1._Person__email)

people = [Person("Tom", "tom@yahoo.com"),
          Person("Jack", "jack@google.com"),
          Person("Larry", "larry@gmail.com")]

for p in sorted(people):
    print(p)
