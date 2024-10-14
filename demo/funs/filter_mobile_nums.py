data = ["399393999", "3939119333", "39929198333", "2918231212", "93939a9439"]


def isMobile(st):
    return st.isdigit() and len(st) == 10


# for m in filter(isMobile, data):
#     print(m)

for m in filter(lambda v: v.isdigit() and len(v) == 10, data):
    print(m)
