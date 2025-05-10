# Simple pizza delivery calculator
size: str = input("What size of pizza do you want? S,M, or L? ").strip().title()
pepperoni: str = input("Do you want pepperoni in your pizza? Y or N ").strip().title()
extra_cheese: str = input("Do you want extra cheese? Y or N").strip().title()

total_bill: int = 0

while True:
    if size == "S":
        total_bill += 15
        print(total_bill)
        break
    elif size == "M":
        total_bill += 20
        break
    elif size == "L":
        total_bill += 25
        break
    else:
        print("Invalid input try again")
        size= input("What size of pizza do you want? S,M, or L? ").strip().title()

while True: 
    if pepperoni == "Y":
        if size == "S":
            total_bill += 2
            print(total_bill)
        else:
            total_bill += 3
        break
    elif pepperoni == "N":
        break
    else:
        print("Invalid input try again")
        pepperoni = input("Do you want pepperoni in your pizza? Y or N ").strip().title()
     
while True: 
    if extra_cheese == "Y":
        total_bill += 1
        break
    elif extra_cheese == "N":
        break
    else:
        print("Invalid input try again")
        extra_cheese = input("Do you want extra cheese? Y or N").strip().title()

print(f"Your total bill is ${total_bill}, Thank you for shoping with us")