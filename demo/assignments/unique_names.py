
st = "Jack,Mark,Bill,Gary,Kevin,Mark,Jack,Scott"
names = st.split(",")
print(names)

unames = set(names)
print(unames)

for name in sorted(unames):
    print(name)




