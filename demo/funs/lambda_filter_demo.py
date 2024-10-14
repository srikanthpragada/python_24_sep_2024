nums = [10, 20, 14, 15, 33, 12, 43, 90]

for n in filter(lambda v: v % 2 == 0, nums):  # filter(function, iterable)
    print(n)
