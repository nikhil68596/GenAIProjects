# Assignment: Exploring Python Concepts

# Task 1: Variables: Your First Python Intro
name = "Nikhil"
age = 21
height = 5.92
# Print out the message properly.
print(f"Hey there, my name is {name}! I'm {age} years old and {height} feet tall.")

# Task 2: Operators: Playing with Numbers
num1 = 25
num2 = 4

# Addition
print(f"The sum of {num1} and {num2} is {num1 + num2}")

# Subtraction
print(f"The difference when {num2} is subtracted from {num1} is {num1 - num2}")

# Multiplication
print(f"The product of {num1} and {num2} is {num1 * num2}")

# Division
print(f"The quotient when {num1} is divided by {num2} is {num1 / num2}")

# Task 3 - Conditional Statements: The Number Checker
number = float(input("Enter a number: "))
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")