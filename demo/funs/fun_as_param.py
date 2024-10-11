
def fun(task, value):
    task(value)  # print('Hello')

def upper(value):
    print(value.upper())

# Pass a function as parameter
fun(print, 'Hello')
fun(upper, "Good Morning")







