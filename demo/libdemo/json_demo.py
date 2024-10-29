import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Larry Page", 45)
print(json.dumps(p.__dict__))
