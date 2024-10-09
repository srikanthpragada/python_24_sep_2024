def wish(*names, message = 'Hello'):
    for n in names:
        print(message, n)


wish('Larry', 'Scott', message =  "Hi")
wish('Ben', 'Tom', "Harry", message = "Good Bye")









