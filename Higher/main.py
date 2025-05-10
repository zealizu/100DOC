# Simple higher or lower game in Python
import random
from game_data import data  # Import the data containing the game options
from art import logo, vs  # Import ASCII art for the game

# Function to randomly select data from the game_data
def get_data():
    """
    Selects a random entry from the game data and formats it for display.
    :return: A list containing the formatted string for display and the follower count.
    """
    choice = random.choice(data)  # Randomly select an entry from the data
    # Format the selected data into a string and include the follower count
    choice_list = [f"{choice['name']}, a {choice['description']}, from {choice['country']}.", choice["follower_count"]]
    return choice_list

# Function to check if the user's choice is correct
def check_win(a, b, user_choice):
    """
    Compares the follower counts of two options and checks if the user's choice is correct.
    :param a: Follower count of option A.
    :param b: Follower count of option B.
    :param user_choice: The user's choice ('a' or 'b').
    :return: True if the user's choice is correct, False otherwise.
    """
    if a > b and user_choice == "a":  # User chose A and A has more followers
        return True
    elif b > a and user_choice == "b":  # User chose B and B has more followers
        return True
    else:
        return False  # User's choice is incorrect

# Function to prompt the user for their choice
def prompt_user(a, b):
    """
    Displays the two options to the user and prompts them to choose one.
    :param a: Formatted string for option A.
    :param b: Formatted string for option B.
    :return: The user's choice ('a' or 'b').
    """
    print(f"Compare A: {a}\n\n")  # Display option A
    print(vs)  # Display the "vs" ASCII art
    print(f"Against B: {b}")  # Display option B
    user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    if user_choice not in ["a", "b"]:  # Validate the user's input
        print("\nInvalid choice\n")
        exit()  # Exit the program if the input is invalid
    return user_choice

# Display the game logo
print(logo)

# Initialize the score and the first two options to compare
score: int = 0
compare1: list = get_data()  # Get the first random option
compare2: list = get_data()  # Get the second random option

# Prompt the user for their choice and start the game loop
user_choice: str = prompt_user(compare1[0], compare2[0])
while check_win(compare1[1], compare2[1], user_choice):  # Continue as long as the user is correct
    score += 1  # Increment the score for a correct answer
    print(f"You're right! Current score: {score}.")
    compare1 = compare2  # Move the second option to the first position
    compare2 = get_data()  # Get a new random option for the second position
    user_choice = prompt_user(compare1[0], compare2[0])  # Prompt the user again

# Clear the screen and display the final score when the user is wrong
print("\n" * 40)  # Clear the screen by printing multiple newlines
print(logo)  # Display the game logo again
print(f"Sorry, that's wrong. Final score: {score}")  # Display the user's final score


