# Project: About Menu

# Step 1: Menu of Recursive Functions
print("Welcome to the Recursive Artistry Program!\n")

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
    option = int(input("Choose an option: \n1. Calculate Factorial \n2. Find Fibonacci \n3. Exit >"))
    if option == 1: #Calculate factorial
        num = int(input("Enter a number to find its factorial:"))
        factl = factorial(num)
        print(f"The factorial of {num} is {"invalid" if factl == None else factl}.")
    elif option == 2: #Calculate fibonacci
        num = int(input("Enter a number to find it's number in the fibonacci sequence:"))
        fib = fibonacci(num)
        position = "" 
        if num == 1:
            position = "1st"
        elif num == 2:
            position = "2nd"
        elif num == 3:
            position = "3rd"
        else:
            position = f"{num}th"
        print(f"The {position} Fibonacci number is {fib}.")
    elif option == 3: #Exit the program
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")