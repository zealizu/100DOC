# Simple Calculator Program

# Function to handle calculations based on the operator
def handle_calculation(first_number: float, second_number: float, operator: str) -> float:
    """
    Performs the calculation based on the given operator.
    :param first_number: The first number in the calculation.
    :param second_number: The second number in the calculation.
    :param operator: The operator to use for the calculation (+, -, *, /).
    :return: The result of the calculation.
    """
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        try: 
            # Handle division and check for division by zero
            return first_number / second_number
        except ZeroDivisionError:
            print("You cannot divide by zero")
            exit()
    else:
        # Handle invalid operators
        print("Invalid operator.")
        return 0.0

# Start a new calculation
first_number = float(input("What's the first number?: ").strip())

# Loop to ensure the user selects a valid operator
while True:
    operator = input("+\n-\n*\n/\nPick an operation: ").strip()
    if operator in ["+", "-", "*", "/"]:
        break
    print("Invalid operator, please try again.")

# Get the second number and perform the calculation
second_number = float(input("What's the next number?: ").strip())
result = handle_calculation(first_number, second_number, operator)
print(f"{first_number} {operator} {second_number} = {result}")

# Continue calculating with the result or start a new calculation
while True:
    continue_calc = input(f"\nType 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").strip().lower()
    if continue_calc == "y":
        # Loop to ensure the user selects a valid operator for the next calculation
        while True:
            operator = input("+\n-\n*\n/\nPick an operation: ").strip()
            if operator in ["+", "-", "*", "/"]:
                break
            print("Invalid operator, please try again.")
        # Get the next number and update the result
        next_number = float(input("What's the next number?: ").strip())
        result = handle_calculation(result, next_number, operator)
        print(f"Result: {result}")
    elif continue_calc == "n":
        # Exit the program if the user chooses to start a new calculation
        exit()
    else:
        # Handle invalid input for continuing or restarting
        print("Invalid input. Please enter 'y' or 'n'.")
