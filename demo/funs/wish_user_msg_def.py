# Function with argument or parameter

def wish(name = "Guest", message = 'Hello'):
    print(message, name)


wish()
wish('Van', "Hi")    # positional
wish('Steve')
wish(name = 'Tom')
wish(message = 'Hi')






