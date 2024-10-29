# read all lines from file
with open("test.txt", "rt") as f:
    lines = f.readlines()

# write back all non-blank lines
with open("test.txt", "wt") as f:
    for line in lines:
        if len(line.strip()) > 0:
            f.write(line)

