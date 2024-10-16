g = 1


def f1():
    e = 2   # Enclosing var
    print("F1")
    global g
    g = 10 
    # Local function
    def f2():
        l = 3   # local var
        nonlocal e
        e = 20
        print("Local function")
        print(g, e, l)

    f2()


f1()
