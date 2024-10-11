names = ['java', 'Python', 'C#', 'c', 'javascript']


def containsupper(st) -> bool:
    for c in st:
        if c.isupper():
            return True

    return False


for n in filter(containsupper, names):
    print(n)
