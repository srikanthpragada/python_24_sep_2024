import re

with open("sample.txt", "rt") as f:
    contents = f.read()

newcontent = re.sub(' +', ' ', contents)
newcontent = re.sub(r'\n+', r'\n', newcontent)
print(newcontent)

# with open("sample.txt", "wt") as f:
#     f.write(newcontent)

