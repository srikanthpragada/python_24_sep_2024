# keyword only args
def wish(*, name, message):
    print(message, name)


#wish('Steve', "Hello")
wish(message="Hi", name="Jack")  # keyword
