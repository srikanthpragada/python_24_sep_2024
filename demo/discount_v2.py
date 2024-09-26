# Program to take price and calculate net price using 15% discount

price = float(input("Enter price :"))
discount = price * 0.15
net_price = price - discount

print('Price         ', price)
print('- Discount    ', discount)
print('Net price     ', net_price)
