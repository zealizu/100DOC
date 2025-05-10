# Simple coffee machine program

# Menu dictionary containing the details of each drink
# Each drink has its required ingredients and cost
MENU: dict = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Resources dictionary to track the available ingredients and money in the machine
resources: dict = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Dictionary to store the value of each type of coin
money_value: dict = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# Function to calculate the total money inserted by the user
def check_funds(money, money_value, have_funded):
    """
    Calculates the total money inserted by the user.
    :param money: Dictionary containing the number of each type of coin inserted.
    :param money_value: Dictionary containing the value of each type of coin.
    :param have_funded: Boolean indicating whether the user has inserted coins.
    :return: The total amount of money inserted.
    """
    if have_funded:
        user_money = 0
        for i in money_value:
            user_money += money[i] * money_value[i]  # Multiply the number of coins by their value
        return user_money
    else:
        return 0

# Function to handle the transaction and check if the machine can make the drink
def handle_transaction(money, item, resources, user_choice):
    """
    Handles the transaction for the selected drink.
    :param money: The total money inserted by the user.
    :param item: The selected drink from the menu.
    :param resources: The available resources in the machine.
    :param user_choice: The name of the selected drink.
    """
    if item["cost"] > money:
        # If the user doesn't insert enough money, refund the money
        print("Sorry that's not enough money. Money refunded.")
    else:
        # Check if the ingredients are sufficient to make the drink
        is_ingredient_enough: bool = False
        insufficient_item: str = ""
        sufficient_items: list = []
        for i in item["ingredients"]:
            if item["ingredients"][i] > resources[i]:
                # If any ingredient is insufficient, set the flag to False
                is_ingredient_enough = False
                insufficient_item = i
                break
            else:
                # If the ingredient is sufficient, add it to the list
                is_ingredient_enough = True
                sufficient_items.append(i)
        if is_ingredient_enough:
            # Deduct the used ingredients from the resources
            for i in sufficient_items:
                resources[i] -= item["ingredients"][i]
            # Add the cost of the drink to the machine's money
            resources["money"] += item["cost"]
            print(f"Here is your {user_choice} ☕️")
            # If the user inserted more money than required, return the change
            if money > item["cost"]:
                print(f"Here is ${money - item['cost']:.2f} in change")
        else:
            # If ingredients are insufficient, refund the money
            print(f"Sorry there is not enough {insufficient_item}.\nYour money has been refunded")

# Main program loop
while True:
    # Reset the money dictionary for each transaction
    money: dict = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    # Ask the user for their choice of drink
    user_choice: str = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    have_funded: bool = False  # Flag to indicate whether the user has inserted coins

    # If the user selects a drink
    if user_choice in ["espresso", "latte", "cappuccino"]:
        print("Please insert coins.")
        # Ask the user to insert coins
        for i in money:
            money[i] = int(input(f"How many {i}?: "))
        have_funded = True  # Set the flag to True after coins are inserted
        user_money = check_funds(money, money_value, have_funded)  # Calculate the total money inserted
        handle_transaction(user_money, MENU[user_choice], resources, user_choice)  # Handle the transaction
    elif user_choice == "report":
        # Display the current resources in the machine
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif user_choice == "off":
        # Turn off the machine
        exit()
    else:
        # Handle invalid input
        print("Invalid input")