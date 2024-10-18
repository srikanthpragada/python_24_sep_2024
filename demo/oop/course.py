class Course:
    # Constructor
    def __init__(self, title, fee=10000):
        # Object Attributes
        self.title = title
        self.fee = fee

    # Methods
    def getnetfee(self):
        return self.fee * 1.18

    def show(self):
        print(f"Title = {self.title}")
        print(f"Fee = {self.fee}")


# Create an object
c1 = Course('Python')
c2 = Course("Power BI", 8000)
c3 = Course(fee = 15000, title = "Data Science")

print(c1.getnetfee())  # call method
c1.show()

#print(c1.fee)

