l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]

for idx, v1 in enumerate(l1):
    if idx < len(l2):
        print(v1, l2[idx])
    else:
        print(v1, 'None')




