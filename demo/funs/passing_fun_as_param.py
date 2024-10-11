
def task(operation, a, b):
    print(operation(a,b))

def add(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return n1 * n2

task(add, 10, 20)
task(mul, 10, 20)

