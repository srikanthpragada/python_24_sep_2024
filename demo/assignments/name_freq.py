
st = "Jack,Mark,Bill,Gary,Kevin,Mark,Jack,Scott,Bill,Jack"
names = st.split(",")   # List of str
unames = set(names)     # Set of str
for name in unames:
    print(f"{name:10}  -  {names.count(name):2}")





