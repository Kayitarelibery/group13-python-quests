# Quest 26: The Simple Calculator
# A calculator that uses functions for each operation and if-elif-else to pick the right one

# --- Define one function for each math operation ---

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b. Handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# --- Main program ---

print("=== Welcome to The Simple Calculator ===\n")

# Ask the user for two numbers and convert them to floats so decimals work
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
print("\nChoose an operation: add, subtract, multiply, divide")
operation = input("Your choice: ").strip().lower()

# Use if-elif-else to call the correct function
if operation == "add":
    result = add(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")
elif operation == "subtract":
    result = subtract(num1, num2)
    print(f"\nResult: {num1} - {num2} = {result}")
elif operation == "multiply":
    result = multiply(num1, num2)
    print(f"\nResult: {num1} * {num2} = {result}")
elif operation == "divide":
    result = divide(num1, num2)
    print(f"\nResult: {num1} / {num2} = {result}")
else:
    # The user typed something that isn't a valid operation
    print("\nInvalid operation. Please choose: add, subtract, multiply, or divide.")
