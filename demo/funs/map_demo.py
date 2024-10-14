
data = "23,33, 44,55,64"

def convertToInt(st):
     return int(st) if st.strip().isdigit() else 0

total = sum (map(convertToInt, data.split(",")))
print(total)
