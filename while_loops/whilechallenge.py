#!/usr/bin/env python3
"""Jurassic Park Trivia | Solution"""

# Question 1

attempt1 = 0
attempt2 = 0

while attempt1 < 3: 
    question1 = input("In Jurassic Park, what kind of dinosaur is the star attraction? ")
# Check if the answer is correct (case-insensitive)
    if question1.lower() in ["t-rex", "trex", "tyrannosaurus rex"]:
        print("Correct! The T-Rex is the star attraction!")
        break
    else:
        print("Sorry, that's not correct. The correct answer is T-Rex.")
        attempt1 += 1

# Question 2
while attempt2 < 3:
    question2 = input("What type of DNA was used to fill the gaps in the dinosaur genome? ")

# Check if the answer is correct (case-insensitive)
    if question2.lower() == "frog":
        print("Correct! Frog DNA was used to fill the gaps in the genome!")
        break
    else:
        print("Sorry, that's not correct. The correct answer is Frog.")
        attempt2 += 1

