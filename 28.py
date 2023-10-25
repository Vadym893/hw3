ean_13_number = input("Enter EAN-13 article number: ")

if len(ean_13_number) == 13 and ean_13_number.isdigit():
    print("Article number is correct")
    if ean_13_number[:3] == "590":
        print("Article manufactured in Poland")
    else:
        print("Article not manufactured in Poland")
else:
    print("Invalid EAN-13 article number. It should consist of 13 digits.")
