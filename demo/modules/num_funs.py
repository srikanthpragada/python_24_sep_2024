# numeric functions

def iseven(n):
    return n % 2 == 0

def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
             return False

    return True


def ispositive(n):
    return  n > 0

