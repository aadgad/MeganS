from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
i = 0
while (i < 3):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print ("That's a positive whole number, try again!")
    else:
        guess = int(guess)
    if (guess == aRandomNumber):
        print ("You are correct!")
        break
    elif (guess < aRandomNumber):
        print ("Guess higher.")
    else:
        print ("Guess lower.")
    i += 1
print ("Sorry, the number was " + str(aRandomNumber))
