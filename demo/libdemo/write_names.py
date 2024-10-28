# Write names into names.txt

names = ['Ben', 'Kevin', 'Larry', 'Scott', "Jackson"]

f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close()
