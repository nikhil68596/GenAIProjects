# Assignment: Check your Knowledge on Errors

# Task 1: Understanding Python Exceptions
# Allow the user to enter a number
try:
    num = int(input("Enter a number: "))
    # Once number is valid, move on.
    try:
        final_num = 100 / num
        print(f"100 divided by {num} is {final_num:.2f}")
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Task 2: Types of Exceptions
print("\n") #Making sure to separate each task by new line.

# IndexError: Accessing an invalid list index
try:
    num_list = [12, 4, 35]
    print(num_list[4])  # This will raise an IndexError
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError: Accessing a non-existent key in a dictionary
try:
    my_dict = {"apple": 1.4, "banana": 1.2} #Cost for each item
    print(my_dict["grape"])  # This will raise a KeyError
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError: Adding a string and an integer
try:
    result = "hello" + 5  # This will raise a TypeError
except TypeError:
    print("TypeError occurred! Unsupported operand types.")
    
print("\n")

# Task 3 - Using try...except...else...finally
# Tell user to enter two numbers separately -> check to see if number or not
def division():
    #Validating user input
    try:  
        num1 = int(input("Enter the first number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    try:  
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    
    #Dividing num1 by num2.
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")
    else:
        print(f"The result is {result:.2f}.")
    finally:
        print("This block always executes.")

division() #Performing the division operation.