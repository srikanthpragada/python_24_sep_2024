# Calculate net amount with 20% discount

qty = int(input("Enter qty :"))
price = int(input("Enter price :"))

amount = qty * price
discount = amount * 20 // 100
net_amount = amount - discount

print(f"Amount       {amount:8}")
print(f"- Discount   {discount:8}")
print(f"Net Amount   {net_amount:8}")