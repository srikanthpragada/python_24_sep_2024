l  = [1,2,3]

li = l.__iter__()  # get iterator
while True:
    try:
        v = li.__next__()  # get next element
        print(v)
    except StopIteration:
        break




