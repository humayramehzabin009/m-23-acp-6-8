from tkinter import *
import re
import random
import string

# Function to check password strength
def check_password():
    password = ent_password.get()

    # Initialize strength criteria
    length = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Determine password strength
    if all([length, has_upper, has_lower, has_digit, has_special]):
        lbl_result["text"] = "Strong Password"
        lbl_result["fg"] = "green"
    elif length and (has_upper or has_lower) and (has_digit or has_special):
        lbl_result["text"] = "Moderate Password"
        lbl_result["fg"] = "orange"
    else:
        lbl_result["text"] = "Weak Password"
        lbl_result["fg"] = "red"

# Function to generate a random password
def generate_password():
    length = 12  # Default password length
    characters = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
    password = ''.join(random.choice(characters) for _ in range(length))
    ent_password.delete(0, END)
    ent_password.insert(0, password)
    check_password()  # Automatically check the strength of the generated password

# Set up the main window
window = Tk()
window.title("Password Generator & Strength Checker")
window.geometry("400x300")
window.resizable(False, False)

# Create widgets
Label(window, text="Enter Password:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
ent_password = Entry(window, show="*", font=("Arial", 12), width=20)
ent_password.grid(row=0, column=1, padx=10, pady=10)

btn_check = Button(window, text="Check Strength", command=check_password, font=("Arial", 12))
btn_check.grid(row=1, column=0, padx=10, pady=10)

btn_generate = Button(window, text="Generate Password", command=generate_password, font=("Arial", 12))
btn_generate.grid(row=1, column=1, padx=10, pady=10)

lbl_result = Label(window, text="", font=("Arial", 14))
lbl_result.grid(row=2, column=0, columnspan=2, pady=20)

# Run the application
window.mainloop()
