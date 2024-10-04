
st = "23 55 6 8 10"

nums = st.split(" ")

total = 0
for v in nums:
    total = total + int(v)

print(total)