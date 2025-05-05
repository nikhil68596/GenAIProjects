# Project: Eligible Elector
# Request age from user input
age = int(input("Enter your age in years please: "))

# Decide what to do based on the user's age.
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    #If the age is negative -> Invalid age 
    if age <= 0:
        print(f"Oh no, this is an invalid age! Please enter a valid age again!")
    else:
        print(f"Oops! You're not eligible yet. But hey, only {18 - age} more years to go!")