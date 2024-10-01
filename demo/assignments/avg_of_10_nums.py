
count = total = 0
for n in range(10):
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    total += num
    count += 1

print(f"Total = {total//count}")