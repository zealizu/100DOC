#simple rock paper scissors game
import random
ASCII_ROCK = """

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
ASCII_PAPER = """

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
ASCII_SCISSORS = """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

while True:
    computer_move:str = random.choice(["rock", "paper", "scissors"])
    player_move:str = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors \npress q to quit\n").strip().lower()
    if computer_move == "rock":
        if player_move == "0":
            print(ASCII_ROCK)
            print("Computer choose: ")
            print(ASCII_ROCK)
            print("It's a draw")
        elif player_move == "1":
            print(ASCII_PAPER)
            print("Computer choose: ")
            print(ASCII_ROCK)
            print("You win")
        elif player_move == "2":
            print(ASCII_SCISSORS)
            print("Computer choose: ")
            print(ASCII_ROCK)
            print("You lose")
        elif player_move == "q":
            print("Thank you for playing")
            exit()
    elif computer_move == "paper":
        if player_move == "0":
            print(ASCII_ROCK)
            print("Computer choose: ")
            print(ASCII_PAPER)
            print("You lose")
        elif player_move == "1":
            print(ASCII_PAPER)
            print("Computer choose: ")
            print(ASCII_PAPER)
            print("It's a draw")
        elif player_move == "2":
            print(ASCII_SCISSORS)
            print("Computer choose: ")
            print(ASCII_PAPER)
            print("You win")
        elif player_move == "q":
            print("Thank you for playing")
            exit()
    elif computer_move == "scissors":
        if player_move == "0":
            print(ASCII_ROCK)
            print("Computer choose: ")
            print(ASCII_SCISSORS)
            print("You win")
        elif player_move == "1":
            print(ASCII_PAPER)
            print("Computer choose: ")
            print(ASCII_SCISSORS)
            print("You lose")
        elif player_move == "2":
            print(ASCII_SCISSORS)
            print("Computer choose: ")
            print(ASCII_SCISSORS)
            print("It's a draw")
        elif player_move == "q":
            print("Thank you for playing")
            exit()