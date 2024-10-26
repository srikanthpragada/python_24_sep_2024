def primes(start, end):
    start = start + 1 if start % 2 == 0 else start
    for n in range(start, end + 1, 2):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            yield n



g = primes(150, 200)
print(next(g))
print(next(g))

# for n in g:
#     print(n)


