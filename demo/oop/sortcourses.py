class Course:
    # Constructor
    def __init__(self, title, fee=10000):
        # Object Attributes
        self.title = title
        self.fee = fee

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f"{self.title} - {self.fee}"

    def __gt__(self, other):
        return  self.title > other.title
    

# Create an object
courses = [Course("Python", 10000), Course("FSWD", 15000),
           Course("Power BI", 8000), Course("Data Science",20000)]

# for c in sorted(courses):
#     print(c)

for c in sorted(courses, key = lambda c : c.fee):
    print(c)

