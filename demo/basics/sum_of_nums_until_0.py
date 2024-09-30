total = 0
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num < 0:  # Negative
        continue

    total += num

print(total)
