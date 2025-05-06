# Project: Password Strength Checker

# Retrieve user input
password = input("Please enter a password: ")
# Define a set of special characters used for the last check
special_characters = set("@#$%^&*()-_=+[]{}|;:'\",.<>?/!")
failed_checks = set() #List of failed checks for the string.

# Check to for password length less than 8 characters.
if len(password) < 8:
    failed_checks.add("at least 8 characters")
# Check for 1+ uppercase letters
if not any(char.isupper() for char in password):
    failed_checks.add("at least one uppercase letter")
# Check for 1+ lowercase letters
if not any(char.islower() for char in password):
    failed_checks.add("at least one lowercase letter")
# Check for 1+ digits
if not any(char.isdigit() for char in password):
    failed_checks.add("at least one digit")
# Check for 1+ special characters
if not any(char in special_characters for char in password):
    failed_checks.add("at least one special character")

#If the user passed all of the checks -> strong password
if len(failed_checks) == 0:
    print("Your password is strong! 💪") #Passes all of the checks
else:
    #Print the first check
    result = f"Your password needs {failed_checks.pop()}"
    #If there is still at least one failed check.
    if len(failed_checks) > 0:
        failed_checks_list = list(failed_checks) #To peform substring operations.
        result += f", {', '.join(failed_checks_list[:-1])}, and {failed_checks_list[-1]}"
    print(result)