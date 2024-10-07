names = ['Scott', "Steve", 'Richards', "Jack", "Martin"]


chars = set()   # Empty set
for name in names:
     chars  = chars | set(name)

print(chars)


