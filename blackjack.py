# Simple Blackjack Game
import random

# ASCII art for the Blackjack game
ASCII_BLACK_JACK = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/     """

# List of cards in the deck (11 represents Ace, 10 represents face cards)
cards: list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to draw a random card for a player
def get_card(player):
    return player.append(random.choice(cards))

# Main game loop
while True:
    # Dictionary to store the hands of the player and the computer
    hands: dict = {
        "player": [],
        "computer": []
    }

    # Ask the user if they want to play a game of Blackjack
    play_game: str = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
    if play_game == "y":
        print(ASCII_BLACK_JACK)  # Display the ASCII art

        # Deal one card to the computer and two cards to the player
        get_card(hands["computer"])
        for _ in range(2):
            get_card(hands["player"])

        # Display the player's cards and the computer's first card
        print(f"""
\tYour cards: {hands['player']}, current score: {sum(hands['player'])} 
\tComputer's first card: {hands['computer'][0]}""")

        # Player's turn
        while True:
            # Check if the player has a Blackjack
            if sum(hands["player"]) == 21:
                print(f"""
\tYour final hand: {hands['player']}, final score: {sum(hands['player'])}
\tComputer's final hand: {hands['computer']}, final score: {sum(hands['computer'])}
Win with a Blackjack 😎""")
                break
            else:
                # Ask the player if they want another card
                another_card: str = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
                if another_card == "y":
                    # Draw another card for the player
                    get_card(hands["player"])
                    print(f"""
\tYour cards: {hands['player']}, current score: {sum(hands['player'])} 
\tComputer's first card: {hands['computer'][0]}""")

                    # Handle Ace (11) if the player's score exceeds 21
                    if 11 in hands["player"] and sum(hands["player"]) > 21:
                        index = hands["player"].index(11)
                        hands["player"][index] = 1

                    # Check if the player went over 21
                    if sum(hands["player"]) > 21:
                        print(f"""
\tYour final hand: {hands['player']}, final score: {sum(hands['player'])}
\tComputer's final hand: {hands['computer']}, final score: {sum(hands['computer'])}
You went over. You lose 😭""")
                        break
                elif another_card == "n":
                    # Computer's turn
                    while sum(hands["computer"]) < 17:
                        get_card(hands["computer"])

                        # Handle Ace (11) for the computer if its score exceeds 21
                        while 11 in hands["computer"] and sum(hands["computer"]) > 21:
                            index = hands["computer"].index(11)
                            hands["computer"][index] = 1

                    # Final results
                    print(f"""
\tYour final hand: {hands['player']}, final score: {sum(hands['player'])}
\tComputer's final hand: {hands['computer']}, final score: {sum(hands['computer'])}""")

                    # Determine the winner
                    player_score = sum(hands["player"])
                    computer_score = sum(hands["computer"])

                    if computer_score > 21:
                        print("Opponent went over. You win 😁")
                    elif player_score > computer_score:
                        print("You win 😁")
                    elif player_score < computer_score:
                        print("You lose 😤")
                    else:
                        print("It's a draw! 😐")
                    break  # End the game
                else:
                    # Handle invalid input
                    print("Invalid input")
                    break

    elif play_game == "n":
        # Exit the game if the player chooses not to play
        print("Bye Bye")
        exit()
    else:
        # Handle invalid input for starting the game
        print("Invalid input")