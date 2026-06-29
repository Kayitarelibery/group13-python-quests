# Quest 29: The Code Breaker
# Allow a user 3 attempts to guess the secret code (42).
# Give feedback on each guess and stop on a correct guess or after 3 failed attempts.

SECRET_CODE = 42  # The secret code the user must guess
MAX_ATTEMPTS = 3  # Total number of allowed attempts

print("=== The Code Breaker ===\n")
print(f"You have {MAX_ATTEMPTS} attempts to guess the secret code.\n")

for attempt in range(1, MAX_ATTEMPTS + 1):  # attempt goes 1, 2, 3
    print(f"Attempt {attempt} of {MAX_ATTEMPTS}:")
    user_input = input("Enter your guess: ")
    guess = int(user_input)  # Convert the string input to an integer

    if guess == SECRET_CODE:
        # Correct guess — congratulate and stop the loop immediately
        print(f"\n✅ Correct! The secret code was {SECRET_CODE}. You cracked it!")
        break  # Exit the for loop early
    else:
        # Wrong guess — give feedback
        remaining = MAX_ATTEMPTS - attempt  # How many tries are left
        if remaining > 0:
            print(f"❌ Wrong! You have {remaining} attempt(s) remaining.\n")
        else:
            # No attempts left — reveal the code
            print(f"\n❌ Wrong again! You've used all {MAX_ATTEMPTS} attempts.")
            print(f"The secret code was {SECRET_CODE}. Better luck next time!")
