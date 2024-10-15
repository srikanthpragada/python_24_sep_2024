names = ["Bill123", "larry838", "ben343", "Kevin111", "Jack939"]


for n in sorted(names, key = lambda s : int(s[-3:])):
    print(n)
