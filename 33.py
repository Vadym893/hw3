decimal_number = int(input("Enter decimal number: "))
original_number = decimal_number  

binary_number = ""
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number = decimal_number // 2

print(f"{original_number}(10) = {binary_number}(2)")