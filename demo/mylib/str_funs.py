
def hasdigit(st):
    for c in st:
        if c.isdigit():
            return True

    return False

def countupper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count