num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if num_products > 2:
    total_price = num_products * product_price
    discount = (total_price * 0.25)  
    amount_to_pay = total_price - discount
else:
    amount_to_pay = num_products * product_price
print(f"Amount to pay: {amount_to_pay:.2f}")