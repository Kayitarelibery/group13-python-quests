# Quest 30: The Reflective Scribe
# This file revisits three previous quests and adds detailed comments
# explaining what each part of the code does and WHY it is written that way.

# ===========================================================================
# QUEST 27 REVISITED: FizzBuzz
# ===========================================================================

print("=== FizzBuzz (Revisited with Comments) ===\n")

# range(1, 101) generates numbers starting at 1 and stopping BEFORE 101,
# giving us exactly 1 through 100. This is how Python's range works.
for number in range(1, 101):

    # We check for divisibility by BOTH 3 and 5 first.
    # If we checked 3 alone first, a number like 15 would print "Fizz"
    # and never reach the FizzBuzz check. Order matters here.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")   # e.g. 15, 30, 45 ...

    elif number % 3 == 0:
        # % is the modulo operator — it gives the remainder of division.
        # If remainder is 0, the number divides evenly, so it's a multiple.
        print("Fizz")       # e.g. 3, 6, 9 ...

    elif number % 5 == 0:
        print("Buzz")       # e.g. 5, 10, 20 ...

    else:
        # None of the special conditions matched, so just print the number.
        print(number)

print()  # Blank line for readability between sections

# ===========================================================================
# QUEST 26 REVISITED: The Simple Calculator
# ===========================================================================

print("=== Simple Calculator (Revisited with Comments) ===\n")

# Each arithmetic operation gets its own function.
# This follows the DRY principle: if we need to change how division works,
# we only change it in ONE place (inside divide()), not everywhere.

def add(a, b):
    return a + b       # Return the sum to the caller

def subtract(a, b):
    return a - b       # Return the difference to the caller

def multiply(a, b):
    return a * b       # Return the product to the caller

def divide(a, b):
    # Guard clause: division by zero is mathematically undefined.
    # We check for it before dividing to avoid a ZeroDivisionError crash.
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b       # Return the quotient to the caller

# float() allows the user to enter decimals (e.g. 3.5), not just whole numbers.
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print("Operations: add, subtract, multiply, divide")
operation = input("Choose operation: ").strip().lower()
# .strip() removes accidental spaces; .lower() makes it case-insensitive
# so "ADD" and "add" both work.

# if-elif-else routes the inputs to the correct function.
# The else at the bottom is a safety net for any unexpected input.
if operation == "add":
    print(f"Result: {add(num1, num2)}")
elif operation == "subtract":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "divide":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Unknown operation. Please type add, subtract, multiply, or divide.")

print()

# ===========================================================================
# QUEST 29 REVISITED: The Code Breaker
# ===========================================================================

print("=== Code Breaker (Revisited with Comments) ===\n")

SECRET_CODE = 42    # Storing the code in a named constant makes it easy to change later.
MAX_ATTEMPTS = 3    # Same idea — change this one number to adjust the difficulty.

print(f"You have {MAX_ATTEMPTS} attempts to guess the secret code.\n")

# range(1, MAX_ATTEMPTS + 1) gives us [1, 2, 3].
# We start at 1 (not 0) so the displayed attempt number is human-friendly.
for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"Attempt {attempt} of {MAX_ATTEMPTS}:")

    # int() converts the string from input() into an integer
    # so we can compare it with == to the integer SECRET_CODE.
    guess = int(input("Enter your guess: "))

    if guess == SECRET_CODE:
        print(f"\n✅ Correct! The secret code was {SECRET_CODE}. You cracked it!")
        break   # break exits the for loop immediately — no more attempts needed.
    else:
        remaining = MAX_ATTEMPTS - attempt  # Calculate how many tries are left.
        if remaining > 0:
            print(f"❌ Wrong! You have {remaining} attempt(s) remaining.\n")
        else:
            # This block only runs on the LAST wrong attempt (remaining == 0).
            print(f"\n❌ Wrong again! All {MAX_ATTEMPTS} attempts used.")
            print(f"The secret code was {SECRET_CODE}. Better luck next time!")
