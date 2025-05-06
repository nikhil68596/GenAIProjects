# Project: Password Strength Checker

# Retrieve user input
password = input("Please enter a password: ")
# Define a set of special characters used for the last check
special_characters = set("@#$%^&*()-_=+[]{}|;:'\",.<>?/!")

# Check to for password length less than 8 characters.
if len(password) < 8:
    print("Your password must be at least 8 characters long.")
# Check for 1+ uppercase letters
elif not any(char.isupper() for char in password):
    print("Your password needs at least one uppercase letter.")
# Check for 1+ lowercase letters
elif not any(char.islower() for char in password):
    print("Your password needs at least one lowercase letter.")
# Check for 1+ digits
elif not any(char.isdigit() for char in password):
    print("Your password needs at least one digit.")
# Check for 1+ special characters
elif not any(char in special_characters for char in password):
    print("Your password needs at least one special character.")
else:
    print("Your password is strong! 💪") #Passes all of the checks