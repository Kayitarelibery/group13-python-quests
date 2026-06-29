# Quest 14: The Logical Gatekeeper
# Goal: use "and" to check two conditions at once

age = int(input("Enter your age: "))
gold = int(input("Enter how much gold you have: "))

if age >= 18 and gold >= 20:
    print("You may enter the club.")
else:
    print("You cannot enter the club.")
