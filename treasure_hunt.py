#simple treasure hunt game
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("""Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. where do you want to go?""")
#this prompts users for their first answer 
first_choice: str = input('\tType "left" or right\n').strip().title()

while True:
    if first_choice == "Right":
        print("You fell into a hole. Game Over.")
        exit()
    elif first_choice == "Left":
        print("You've come to a lake. There's an island in the middle of the lake.")
        break
    else:
        print("Invalid answer. Try again")
        first_choice= input('\tType "left" or right\n').strip().title()

second_choice: str = input('\t Type "wait" to wait for a boat. Type "swim" to swim across \n').strip().title()

while True:
    if second_choice == "Wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        break
    elif second_choice == "Swim":
        print("You get attacked by an angry trout. Game Over.")
        exit()
    else:
        print("Invalid answer. Try again")
        second_choice = input('\t Type "wait" to wait for a boat. Type "swim" to swim across \n').strip().title()

third_choice: str = input("\t One red, one yellow and one blue. Which colour do you choose? \n").strip().title()

while True:
    if third_choice == "Red":
        print("It's a room full of fire. Game Over.")
        exit()
    elif third_choice == "Blue":
        print("You enter a room of beasts. Game Over.")
        exit()
    elif third_choice == "Yellow":
        print("You found the treasure! You Win!")
        exit()
    else: 
        print("Invalid answer. Try again")
        third_choice = input("\t One red, one yellow and one blue. Which colour do you choose? \n").strip().title()