# Write names into names.txt

names = ['Ben', 'Kevin', 'Larry', 'Scott', "Jackson"]

with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")


