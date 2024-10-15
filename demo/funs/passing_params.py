
def zero(num:int) -> None:
    print(id(num))
    num = 0
    print(id(num))


a = 100
print(id(a))
zero(a)
print(a)

