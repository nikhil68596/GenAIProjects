# Assignment: Explore Loops in Python

# Task 1 - Counting Down with Loops

#Request a number from user input 
num = int(input("Please enter a positive number to officially count down: "))
#Check to see if the number is negative.
while num < 0:
    num = int(input("Invalid number, please enter a positive number again: "))
#Performing the count down.
while num > 0:
    print(num, end = " ")
    num -= 1
print("Blast off! 🚀", end = "\n")

# Task 2 - Multiplication Table with for Loops
num = int(input("Please enter a number to generate a multiplication table: "))
#Generating the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}", end=" ")

# Task 3 - Find the Factorial
num = int(input("\nPlease enter a non-negative number in order to find its factorial: "))
#Checking to see if the number is less than 0 for program robustness, invalid factorial.
while num < 0:
    num = int(input("Invalid number, please enter a non-negative number again: "))
# 0! = 1, so the factorial starts off with 1
factorial = 1
#Calculating the factorial.
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}.")