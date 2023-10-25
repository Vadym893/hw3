userNum = int(input("write how much of nums are you interested in: "))
output = ""
for j in range(0,userNum):
    num = j
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) != 0:
                output+=f"{num} " 
                break
print(output)