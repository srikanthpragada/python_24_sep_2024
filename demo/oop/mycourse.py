class MyCourse:
    # Constructor
    def __init__(self, title, fee=10000):
        # Object Attributes
        self.title = title
        self.fee = fee
        self.taxrate = 12

    # Methods
    def getnetfee(self):
        return self.fee + (self.fee * self.taxrate / 100)

    def show(self):
        print(f"Title = {self.title}")
        print(f"Fee = {self.fee}")


# Create an object
c1 = MyCourse('Python')

print(c1.getnetfee())  # call method
c1.show()


