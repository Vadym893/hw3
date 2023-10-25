number = str(input("Write first number: "))
sum = 0
i=1
while number.upper() !="STOP":
    sum += int(number)
    i+=1
    number = str(input(f"Write {i} number: "))
print(f"Quantity: {i} , Sum: {sum} , Mean: {round(float(sum/i),2)}")