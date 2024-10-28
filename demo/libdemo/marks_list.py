
f = open("marks.txt", "rt")

for line in f.readlines():
    name, *marks = line.split(",")
    #print(name, marks)
    total = sum(map(int, marks))
    print(f"{name} - {total} - {total/len(marks):.2f}")

f.close()


