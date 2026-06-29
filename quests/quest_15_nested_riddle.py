# Quest 15: The Nested Riddle
# Goal: use an if statement inside another if statement

direction = input("Do you go left or right? ")

if direction == "left":
    action = input("Do you swim or wait? ")
    if action == "swim":
        print("You found a treasure chest!")
    else:
        print("You wait and nothing happens.")
else:
    print("You wander off and get lost.")
