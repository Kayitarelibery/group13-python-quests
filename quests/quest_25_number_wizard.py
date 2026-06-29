# Quest 25: The Number Wizard
# Upgraded guessing game that tells the user if their guess is too high or too low

import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

print("=== Welcome to The Number Wizard! ===")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?\n")

guessed = False  # Track whether the user has guessed correctly

# Keep looping until the user guesses correctly
while not guessed:
    user_input = input("Enter your guess: ")
    guess = int(user_input)  # Convert the input string to an integer

    if guess < secret_number:
        print("Too low! Try a higher number.\n")
    elif guess > secret_number:
        print("Too high! Try a lower number.\n")
    else:
        # The guess is correct
        print(f"You got it! The secret number was {secret_number}. Well done, Wizard!")
        guessed = True  # Exit the loop
