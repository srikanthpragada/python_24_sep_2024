# Print chars in first string that are present in second string without duplicates
fs = "java"
ss = "oracle"

chars = []
for c in fs:
    if c in ss and c not in chars:
        print(c)
        chars.append(c)

