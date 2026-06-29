#!usr/bin/env python3

score = int(input("Enter your score (0-100): "))

if score >= 90 and score <=100:
    print("A")
elif score >= 80 and score <=89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
else:
    print("Needs Improvement")
