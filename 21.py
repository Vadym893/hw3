first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if first_number > second_number:
    first_number, second_number = second_number, first_number

print(f"Numbers in ascending order: {first_number}, {second_number}")