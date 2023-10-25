for number in range(1, 31):
    result = ""
    
    if number % 3 == 0:
        result += "THREE"
    
    if number % 5 == 0:
        result += "FIVE"
    
    if not result:  
        result = str(number)
    
    print(result, end=" ")


print()
