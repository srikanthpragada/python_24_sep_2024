

def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def isodd(num):
    return num % 2 == 1

result = iseven(10)
print(isodd(11), isodd(10))

