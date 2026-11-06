"""
Filename: numberguessing.py
Author: <Hensel, Oliver>
Created: <11/4/2026>
Instructor: Burgess

"""

import random
#imports random number
rand0m = random.randint(1,100)

e=2

print(rand0m)


while e==2:
    question = input("guess a number 1-100")


    if int (question) > rand0m:
        print("too high")
        e=2
    elif int (question) < rand0m:
        print("too low")
        e=2
    elif int (question) == rand0m:
        print("you guessed the number")
        e=1
