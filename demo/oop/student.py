class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("James")
s1.age = 20
print(s1.__dict__)

print(hasattr(s1, 'age'))



