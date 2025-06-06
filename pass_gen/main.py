import random
import pyperclip
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# List of possible characters for the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Randomly determine the number of letters, symbols, and numbers in the password
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def generate_pass():
    """
    Generates a random password using letters, symbols, and numbers.
    Fills the password entry field with the generated password and copies it to the clipboard.
    """
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)  # Shuffle to ensure randomness
    password = "".join(password_list)
    pass_input.delete(0, END)  # Clear the password entry field
    pass_input.insert(0, password)  # Insert the generated password
    pyperclip.copy(password)  # Copy the password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    """
    Saves the website, username/email, and password to a text file after validation.
    Shows a warning if any field is empty and asks for confirmation before saving.
    """
    web_user_input = web_input.get().strip().title()
    name_user_input = name_input.get()
    pass_user_input = pass_input.get()
    
    # Check for empty fields
    if len(web_user_input) == 0 or len(name_user_input) == 0 or len(pass_user_input) == 0:
        messagebox.showwarning(
            title="Empty Field Detected",
            message="You canot have any empty fields, Please try again"
        )
    else:
        # Ask for confirmation before saving
        is_ok = messagebox.askokcancel(
            title=web_user_input,
            message=f"These are the details entered: \nEmail/Username: {name_user_input}\nPassword: {pass_user_input}\nis it okay to save? "
        )
        if is_ok:
            # Save the details to a file
            with open("100DOC/pass_gen/data.txt", "a") as file:
                file.write(f"{web_user_input} | {name_user_input} | {pass_user_input} \n")
                web_input.delete(0, END)  # Clear website entry
                pass_input.delete(0, END)  # Clear password entry

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)  # Add padding around the window

# Create and place the logo image
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="100DOC/pass_gen/logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# Website label and entry
web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)
web_input = Entry(width=38)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()  # Focus cursor on website entry

# Email/username label and entry
name_label = Label(text="Email/Username: ")
name_label.grid(row=2, column=0)
name_input = Entry(width=38)
name_input.grid(row=2, column=1, columnspan=2)
name_input.insert(0, "Zealizu@gmail.com")  # Default email

# Password label and entry
pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)
pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)

# Generate password button
gen_pass = Button(text="Generate Password", command=generate_pass)
gen_pass.grid(row=3, column=2)

# Add/save button
add_btn = Button(text="Add", width=36, command=save_pass)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()  # Start the Tkinter event loop