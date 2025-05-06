#simple hangman game
import random
#ASCII art for hangman
ASCII_HANGMAN = [r"""+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""", r"""+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",r"""+---+
  |   |
  O   |
 /|\  |
      |
      |
=========""","""+---+
  |   |
  O   |
 /|   |
      |
      |
=========""",r"""+---+
  |   |
  O   |
  |   |
      |
      |
=========""",r"""+---+
  |   |
  O   |
      |
      |
      |
=========""",r""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/"""]
#list of words to guess
words = [
    "apple", "banana", "orange", "table", "chair",
    "pencil", "school", "laptop", "window", "bottle",
    "garden", "kitchen", "mirror", "pillow", "basket"
]
#randomly select a word from the list
word = random.choice(words)
#number of lives
lives = 6
#create a list of underscores for the guessed word
guess_word_list = []
guess_word = ""
#loop through the word and create a list of underscores
for character in word:
    guess_word_list.append("_")
#join the list of underscores into a string
for i in guess_word_list:
    guess_word += i
def check_win():
    """Check if the player has won the game"""
    for i in guess_word_list:
        if i == "_":
            return False
    return True

#main game loop
print(ASCII_HANGMAN[6])
while True:
    print(f"Word to guess: {guess_word}")
    #ask the player to guess a letter
    guessed_letter: str = input("Guess a letter: ").strip().lower()
    found: bool = False
    
    #loops through the word and checks if the guessed letter is in the word
    for i in range(len(word)):
        if word[i] == guessed_letter:
    #if th guessed letter is in the word, update the list of underscores
            guess_word_list[i] = guessed_letter
            found = True
     
    #if the guessed letter is in the word update string usiing the updated list      
    if found is True:
        print("Correct Guess") 
        guess_word = ""
        #loops through the updated list and joins the letters to form the guessed word
        for i in guess_word_list:
            guess_word += i
        print(guess_word)
    else:
        #if the guessed letter is not in the word, reduce the number of lives
        #and print the hangman ASCII art
        lives -= 1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        print(ASCII_HANGMAN[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    #if the player has no lives left, end the game
    if lives == 0:
        print("***********************IT WAS jawbreaker! YOU LOSE**********************")
        exit()
    #if the player has guessed the word, end the game
    if check_win():
        print("***********************YOU WON!***********************")
        print(f"THE WORD WAS {word.upper}")
        exit()