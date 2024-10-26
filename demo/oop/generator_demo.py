def numbers(start, end):
    for n in range(start, end + 1):
        yield n


g = numbers(10, 15)
print(type(g))

print(next(g))
print(next(g))
