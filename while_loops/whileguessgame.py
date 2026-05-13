#!/usr/bin/env python3

import random

secret_number = random.randint(1, 10)
guess = 0        
while guess != secret_number:
    guess = input("Guess a number 1-10: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('invalid guess, try again')
        continue

    if guess == secret_number:
        print('You won!')
        break
    else:
        print('guess again!')


