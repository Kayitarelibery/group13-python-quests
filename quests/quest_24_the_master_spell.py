def ask_for_age():
    return int(input("Enter your age: "))

def can_they_vote(age):
    if age >= 18:
        print("You are old enough to vote!")
    else:
        print("You are not old enough to vote yet.")

age = ask_for_age()
can_they_vote(age)
