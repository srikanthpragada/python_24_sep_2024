total = 0

for n in range(5):
    try:
        num = int(input("Enter a number :"))
        total += num
    except ValueError:
        print("Invalid Number")

print(total)
