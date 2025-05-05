# Assignment: Explore Loops in Python

# Task 1 - Counting Down with Loops
num = int(input("Please enter a positive number to officially count down: "))
while num < 0:
    num = int(input("Invalid number, please enter a positive number again: "))
while num > 0:
    print(num, end = " ")
    num -= 1
print("Blast off! 🚀", end = "\n")

# Task 2 - Multiplication Table with for Loops
num = int(input("Please enter a number to generate a multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}", end=" ")

# Task 3 - Find the Factorial
num = int(input("\nPlease enter a non-negative number in order to find its factorial: "))
while num < 0:
    num = int(input("Invalid number, please enter a non-negative number again: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}.")