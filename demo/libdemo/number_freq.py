
f = open("numbers.txt", "rt")

freq = {}
for line in f.readlines():
    nums = line.strip().split(",")

    for n in nums:
        count = freq.get(n, 0)
        count += 1
        freq[n] = count


f.close()

print(freq)


