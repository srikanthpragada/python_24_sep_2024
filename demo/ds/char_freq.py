st = "how are you doing today"

for c in sorted(set(st)):
    print(f"{c} - {st.count(c)}", end = ' ')

