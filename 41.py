import random
Pin_code = str(input("write your pincode: "))
if len(Pin_code)!=4:
    print("it must have been 4 digits!")
    exit()
print("Three options available: ")
print("1. To check if the PIN code is valid.")
print("2. To generate a new random 4 digit PIN code")
print("3. To exit the program")
option = int(input())
flag=0
while True:
    if option == 1:
        flag=0
        for i in range(3):
            if flag==0:
                print("Please enter your PIN Code again after",3-i,"attempts left")
                pin_check = input()
                if(pin_check==Pin_code):
                    print("Your PIN Code is correct!")
                    flag=1
                    break
                elif pin_check!=Pin_code:
                    print("Your PIN is incorec!")
                if 3-i==1 and flag==0:
                    print("sir, your card is blocked, enjoy the day")
                    exit()
    elif option==2:
        new_password=random.randint(1000,9999)
        print(f"Your new password is {new_password}")
        Pin_code=str(new_password)
    else :
        exit()
    print("Three options available: ")
    print("1. To check if the PIN code is valid.")
    print("2. To generate a new random 4 digit PIN code")
    print("3. To exit the program")
    option = int(input())
