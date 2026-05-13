#!/usr/bin/env python3

import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number 1-10: "))

if guess == secret_number:
    print('You won!')
else:
    print('you loose!')


