class Student:
    def __init__(self, name):
        self.name = name

    @property
    def fullname(self):
        return self.name.upper()


s1 = Student("James")
s1.age = 20
print(s1.fullname)  # Property

print(s1.__dict__)

print(hasattr(s1, 'age'))
delattr(s1, 'age')
print(s1.__dict__)

# print(s1.age)
setattr(s1, 'age', 10)
print(getattr(s1, 'age', 0))
