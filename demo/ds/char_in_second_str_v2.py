# Print chars in first string that are present in second string without duplicates
fs = "java"
ss = "oracle"

for c in set(fs):
    if c in ss:
        print(c)
