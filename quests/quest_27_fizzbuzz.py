# Quest 27: The FizzBuzz Test
# Classic challenge: print numbers 1-100 with special rules for multiples of 3 and 5

print("=== FizzBuzz ===\n")

for number in range(1, 101):  # Loop through 1 to 100 inclusive

    if number % 3 == 0 and number % 5 == 0:
        # Multiple of BOTH 3 and 5 — must check this FIRST before the other two
        print("FizzBuzz")
    elif number % 3 == 0:
        # Multiple of 3 only
        print("Fizz")
    elif number % 5 == 0:
        # Multiple of 5 only
        print("Buzz")
    else:
        # Not a multiple of 3 or 5, just print the number
        print(number)
