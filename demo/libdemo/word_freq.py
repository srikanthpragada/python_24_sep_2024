
import re

with open("news.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)

for w in sorted(set(words)):
    if not w.isdigit():
        print(f'{w} - {words.count(w)}')

