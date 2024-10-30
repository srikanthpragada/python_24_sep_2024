import os

stdir = r"c:\classroom\python24"

allfiles = os.walk(stdir)

count = 0
for (dirname, folders, files) in allfiles:
    for filename in files:
        if filename.endswith(".py"):
            count += 1
            print(dirname  + "\\" + filename)

print(f"Count = {count}")





