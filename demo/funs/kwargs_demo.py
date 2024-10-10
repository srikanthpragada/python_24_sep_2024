def fun(*args, **kwargs):
    for k, v in kwargs.items():
        print(k, v)


fun(a=10, x=1, y=100)
fun(name="Java", version=23)
fun(10, 20)
