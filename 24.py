current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))

price_reduction = ((previous_price - current_price) / previous_price) * 100

if price_reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction:.2f}%")
else:
    print("No need to buy the product. Price reduction is less than 10%.")