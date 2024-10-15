g = 1


def f1():
    e = 2   # Enclosing var
    print("F1")

    # Local function
    def f2():
        l = 3   # local var
        e = 20
        print("Local function")
        print(g, e, l)

    f2()


f1()
