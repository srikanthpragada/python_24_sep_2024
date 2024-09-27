# Program to take price and calculate net price using 15% discount

data = input("Enter price :")
price = int(data)   # convert str to int
discount = price * 0.15
net_price = price - discount

print('Net price', net_price)
