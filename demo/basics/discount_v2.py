# Program to take price and calculate net price using 15% discount

price = float(input("Enter price :"))
discount = price * 0.15
net_price = price - discount

print(f'Price          {price:8.2f}')
print(f'- Discount     {discount:8.2f}')
print(f'Net price      {net_price:8.2f}')
