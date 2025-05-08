# Simple Caesar cipher encryption and decryption program.

# ASCII art for the cipher program

ASCII_CIPHER = """ 
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           """

# List of lowercase letters used for encryption and decryption
letters: list[str] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

# Function to encrypt a message using Caesar cipher
def encrypt(message, shift):
    """
    Encrypts the given message by shifting each letter by the specified amount.
    :param message: The message to encrypt.
    :param shift: The number of positions to shift each letter.
    :return: The encrypted message.
    """
    encrypted_message: str = ""
    shifted_position = 0
    # Loop through each character in the message
    for i in message:
        # If the character is a space, add it directly to the encrypted message
        if i == " ":
            encrypted_message += " "
        else:
            # Loop through the list of letters to find the character
            for j in range(len(letters)):
                if i == letters[j]:
                    # Calculate the shifted position and wrap around if necessary
                    shifted_position = j + shift
                    shifted_position %= len(letters)  # Ensure the position wraps around
                    encrypted_message += letters[shifted_position]

            # If the character is not in the letters list (e.g., numbers or symbols), add it as is
            if i not in letters:
                encrypted_message += i
    return encrypted_message

# Function to decrypt a message using Caesar cipher
def decrypt(message, shift):
    """
    Decrypts the given message by reversing the Caesar cipher shift.
    :param message: The encrypted message to decrypt.
    :param shift: The number of positions to shift each letter back.
    :return: The decrypted message.
    """
    shifted_position = 0
    decrypted_message: str = ""
    # Loop through each character in the message
    for i in message:
        # If the character is a space, add it directly to the decrypted message
        if i == " ":
            decrypted_message += " "
        else:
            # Loop through the list of letters to find the character
            for j in range(len(letters)):
                if i == letters[j]:
                    # Calculate the shifted position and wrap around if necessary
                    shifted_position = j - shift
                    shifted_position %= len(letters)  # Ensure the position wraps around
                    decrypted_message += letters[shifted_position]
            # If the character is not in the letters list (e.g., numbers or symbols), add it as is
            if i not in letters:
                decrypted_message += i
    return decrypted_message

# Main program loop to allow the user to repeatedly encode or decode messages
go_again: bool = True  # Flag to control whether the program should continue running
while go_again:
    print(ASCII_CIPHER)  # Display the ASCII art banner
    # Ask the user whether they want to encode or decode a message
    user_choice: str = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").strip().lower()
    # Get the message to encode or decode
    message: str = input("Type your message: \n").strip().lower()
    # Get the shift value for the Caesar cipher
    shift: int = int(input("Type the shift number: \n").strip())
    
    # Perform the chosen operation (encode or decode)
    if user_choice == "encode":
        print(f"Here's the encoded result: {encrypt(message, shift)}")  # Call the encrypt function
    elif user_choice == "decode":
        print(f"Here's the decoded result: {decrypt(message, shift)}")  # Call the decrypt function
    else:
        print("Invalid choice. Try again.")  # Handle invalid input for the operation choice
    
    # Ask the user if they want to run the program again
    try_again: str = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").strip().lower()
    
    # Validate the user's input for whether to continue or exit
    while True:
        if try_again == "yes":
            break  # Exit the inner loop and restart the main loop
        elif try_again == "no":
            go_again = False  # Set the flag to False to exit the main loop
            break
        else:
            # Handle invalid input for the try_again prompt
            print("Invalid choice. Please type 'yes' or 'no'.")
            try_again: str = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").strip().lower()

