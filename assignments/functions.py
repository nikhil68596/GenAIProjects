# Assignment: About Parameters of Functions

# Task 1: Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.", end= " ")

def add_numbers(num1, num2):
    return num1 + num2

n1, n2 = 5, 10
greet_user("Alice")
print(f"The sum of {n1} and {n2} is {add_numbers(n1,n2)}.\n")

# Task 2: Using Default Parameters
def describe_pet(pet_name, animal_type = "dog"):
    print(f"I have a {animal_type} named {pet_name}.", end = " ")
describe_pet("Buddy")
describe_pet("Whiskers", animal_type = "cat")
print("\n")

# Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:", end = " ")
    for ingredient in ingredients:
        print(f" - {ingredient}", end = " ")
make_sandwich("lettuce", "tomato", "cheese")
print("\n")

# Task 4 - Understanding Recursion
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num, fib_num = 5, 6
factrl = factorial(num)
#For printing out the position for fibonacci.
position = "" 
if fib_num == 1:
    position = "1st"
elif fib_num == 2:
    position = "2nd"
elif fib_num == 3:
    position = "3rd"
else:
    position = f"{fib_num}th"

print(f"Factorial of {num} is {"invalid" if factrl == None else factrl}. The {position} Fibonacci number is {fibonacci(fib_num)}.")