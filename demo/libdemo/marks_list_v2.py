
f = open("marks.txt", "rt")

for line in f.readlines():
    name, *marks = line.split(",")
    valid_marks = list(filter(lambda v : v.strip().isdigit(), marks))

    # if no marks found then skip this line
    if len(valid_marks) == 0:
        continue

    total = sum(map(int, valid_marks))
    print(f"{name} - {total} - {total/len(valid_marks):.2f}")

f.close()


