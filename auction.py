# This is a secret auction program where multiple users can place bids, and the program determines the highest bidder.

import os

# ASCII art for the auction hammer
ASCII_HAMMER = r'''
             ___________
            /          /
           /__________/
          |"""""""""""|_.-._,.---------.,_.-._
          |           | | |             | |   '-.
          |           |_| |_           _| |_..-'
          |___________| '-' '---------' '-' 
          )"""""""""""(
         /_____________\
       .---------------.
      /_________________\
'''

# Function to clear the terminal screen
def clear_terminal():
    """
    Clears the terminal screen.
    Works for both Windows (cls) and macOS/Linux (clear).
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# Dictionary to store bid information (name as key, bid amount as value)
bid_info: dict = {}

# Display the ASCII art for the auction
print(ASCII_HAMMER)

# Variables to track the highest bidder and their bid amount
highest_bidder_amount = 0
highest_bidder_name = ""

# Main loop to collect bids
while True:
    # Ask the user for their name and bid amount
    name: str = input("What is your name: ").strip().title()
    bid_amount: int = int(input("What is your bid: $").strip())

    # Check if the name has already been used
    if name in bid_info:
        print("That name has been taken already")
    else:
        # Add the bid to the dictionary
        bid_info[name] = bid_amount

        # Ask if there are other bidders
        other_bid: str = input("Are there any other bidders? Type 'yes' or 'no'. \n").strip().lower()
        if other_bid == "yes":
            # Clear the terminal for the next bidder
            clear_terminal()
        elif other_bid == "no":
            # Exit the loop if no more bidders
            break
        else:
            # Handle invalid input for the other_bid prompt
            print("Invalid answer")
            exit()

# Determine the highest bidder
for i in bid_info:
    if bid_info[i] > highest_bidder_amount:
        highest_bidder_amount = bid_info[i]
        highest_bidder_name = i

# Announce the winner
print(f"The winner is {highest_bidder_name} with a bid of ${highest_bidder_amount}")