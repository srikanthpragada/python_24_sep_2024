# Print all prime numbers in the given range
import sys

start = 1
end = int(sys.argv[1])

def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
             return False

    return True


for n in range(start, end + 1):
    if isprime(n):
        print(n, end = ' ')


