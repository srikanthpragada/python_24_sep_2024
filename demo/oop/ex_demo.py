
st = "10"

try:
    n = int(st)
    print(100 // n)
except ValueError as ex:
    print("Error --> " + str(ex))
else:
    print("Okay")
# except Exception as ex:
#     print("Error ->" + str(ex))
finally:
    print("Finally")

print("Done")