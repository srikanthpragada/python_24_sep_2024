nums = [10, 20, 14, 15, 33, 12, 43, 90]


def iseven(n) -> bool:
    #print('Value', n)
    return n % 2 == 0


for n in filter(iseven, nums):  # filter(function, iterable)
    print(n)
