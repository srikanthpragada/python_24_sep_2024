
data = "23,33,A44,55,64E"

valid_nums = filter(str.isdigit, data.split(","))
nums = map(int, valid_nums)
print(sum(nums))
