#simple password generator
#a list of all the letters both upper and lower case
import random
letters: list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
# a list of all the symbols
symbols: list= [
    '!', '#', '$', '%', '&', '(', ')', '*', '+'
]
# a list of all the numbers
numbers:list = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

print("Welcome to the PyPassword Generator!")
# ask the user how many letters, symbols and numbers they want in their password
no_letters: int = int(input("How many letter would you like in your password? \n"))
no_symbols: int = int(input("How many symbols would you like? \n"))
no_numbers: int = int(input("How many numbers would you like \n")) 

password = []

for _ in range(no_letters):
    i = random.choice(letters)
    password.append(i)
for _ in range(no_symbols):
    i = random.choice(symbols)
    password.append(i)
for _ in range(no_numbers):
    i = random.choice(numbers)
    password.append(i)

print(password)
random.shuffle(password)
password_string: str = ""

for i in password:
    password_string += i
    
print(password)
print(password_string)