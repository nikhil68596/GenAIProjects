# Project: Calculator with Exception Handling

# Step 1: Menu of Recursive Functions
print("Welcome to the Error-Free Calculator!\n")

#Function to find the factorial of a number.
def factorial(n):
    if n < 0: #Invalid factorial for a negative number
        return None
    if n == 0 or n == 1: #Base case
        return 1
    return n * factorial(n - 1) #Recursive step

#Function to find the nth number of the fibonacci sequence.
def fibonacci(n):
    #2 base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) #Recursive step
    
#Present the options for the menu in this continuously executed program (No fractal pattern in this menu)
while True:
    option = int(input("Choose an operation: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit >"))
    print("\n")
    if option == 5: #Exit
        print("Goodbye!")
        break
    elif not (option >= 1 and option <= 5): #Invalid option
        print("Invalid option. Please try again.")
        print("\n")
        continue
    
    #Keep entering the numbers till it's valid.
    while True:
        try:  
            first_num = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    while True:
        try:  
            second_num = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    #Performing the menu options.
    if option == 1: #Addition
        print(f"The sum of {first_num} and {second_num} is {first_num + second_num:.2f}.")
    elif option == 2: #Subtraction
        print(f"The difference between {first_num} and {second_num} is {first_num - second_num:.2f}.")
    elif option == 3: #Multiplication
        print(f"The product of {first_num} and {second_num} is {first_num * second_num:.2f}.")
    elif option == 4: #Division
        try:
            print(f"{first_num} divided by {second_num} is {first_num / second_num:.2f}.")
        except ZeroDivisionError:
            print("Oops! Division by zero is not allowed.")
    print("\n")