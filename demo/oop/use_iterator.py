l  = [1,2,3]

li = iter(l)
while True:
    try:
        v = next(li)
        print(v)
    except StopIteration:
        break




