amount = int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {amount} in coins:")

coins_5 = amount // 5
amount %= 5

coins_2 = amount // 2
amount %= 2

coins_1 = amount

print(f"5 zł - {coins_5}")
print(f"2 zł - {coins_2}")
print(f"1 zł - {coins_1}")
