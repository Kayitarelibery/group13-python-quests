#!usr/bin/env python3

direction = input("Do you go left or right? ")

if direction == "left":
    action = input("Do you swim or wait? ")
    if action == "swim":
        print("You found a treasure!")
    else:
        print("You found no treasure!")
else:
    print("You wander off and never find anything interesting.")
