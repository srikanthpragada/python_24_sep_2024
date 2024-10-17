# Print all prime numbers in the given range
import sys

if len(sys.argv) < 3:
    print("Sorry! Missing arguments!")
    print("Usage: Python prime_numbers_v2.py start end")
    exit()  # Terminate program

start = int(sys.argv[1])
end = int(sys.argv[2])


def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


# if start is even then add 1 so that we start with odd
if start % 2 == 0:
    start += 1

for n in range(start, end + 1, 2):
    if isprime(n):
        print(n, end=' ')
