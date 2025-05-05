# Project: Number Guessing Game
import random
# Generate a random number
number_to_guess = random.randint(1, 100)
num_of_attempts = 0
while num_of_attempts < 10:
    number = int(input("Guess the number (between 1 and 100): "))
    num_of_attempts += 1
    if number > number_to_guess:
        print("Too high! Try again.")
    elif number < number_to_guess:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed it in {num_of_attempts} attempts!")
        break
if num_of_attempts >= 10:
    print("Game over! Better luck next time!")