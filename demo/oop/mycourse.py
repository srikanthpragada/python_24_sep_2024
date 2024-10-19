class MyCourse:
    # Class attribute or static attributes
    taxrate = 12
    # Constructor
    def __init__(self, title, fee=10000):
        # Object Attributes
        self.title = title
        self.fee = fee

    # Methods
    def getnetfee(self):
        return self.fee + (self.fee * MyCourse.taxrate / 100)

    def show(self):
        print(f"Title = {self.title}")
        print(f"Fee = {self.fee}")

    @staticmethod
    def getTaxrate():
        return  MyCourse.taxrate


# Create an object
c1 = MyCourse('Python')

print(MyCourse.getTaxrate())

print(c1.getnetfee())  # call method
c1.show()


