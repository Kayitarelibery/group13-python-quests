#!usr/bin/env python3

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote.")
elif age < 18:
    print("You can not vote")
else:
    print("Invalid input")

