secret = 7

guess = int(input("Guess the number: "))
while guess != secret:
    print("Wrong, try again.")
    guess = int(input("Guess the number: "))
print("Correct!")
