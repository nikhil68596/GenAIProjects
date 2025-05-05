# Assignment: Exploring Python Concepts

# Task 1: Variables: Your First Python Intro
def task1():
    name = "Nikhil"
    age = 21
    height = 5.92
    # Print out the message properly.
    print(f"Hey there, my name is {name}! I'm {age} years old and {height} feet tall.")

# Task 2: Operators: Playing with Numbers
def task2():
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
def task3():
    number = input("Enter a number: ")
    # Rules to account for when deciding whether the user has entered a valid number.
    condition1 = not (number.count('.') > 1) # Whether string/number has two decimal points -> Invalid
    condition2 = number.startswith('-') and number[1:].replace('.', '').isdigit() # Negative numbers
    condition3 = number.replace('.', '', 1).isdigit() # Positive numbers
    while not (condition1 and (condition2 or condition3)):
        number = input("Enter a valid number: ")
    
    number = float(number)

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

if __name__ == "__main__":
    # Call each one of the tasks separately
    task1()
    task2()
    task3()
