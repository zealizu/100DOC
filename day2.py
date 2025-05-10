#simple tip calculator
print("Welcome to the tip calculator !")
total_bill : float = float(input("What was the total bill? $"))
tip : float = float(input("How much tip would you like to give? 10, 12, or 15? "))/100
total_people : int = int(input("How many people to split the bill? "))
each_persons_bill: float =  (total_bill + (total_bill * tip))/total_people
print(f"Each person should pay: ${each_persons_bill:.2f}")