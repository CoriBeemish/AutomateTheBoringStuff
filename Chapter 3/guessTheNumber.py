# This is a guess the number game.
# Written by: Cori Beemish
# Written on: December 26th, 2018

import random

print 'Hello! What is your name?'
name = raw_input()
secretNumber = random.randint(1,20)
print 'Well, ' + name + ', I am thinking of a number between 1 and 20.'
guess_number = 6

for guessesTaken in range(1, 7):
    print 'Take a guess!'
    guess = int(input())
    guess_number -= 1
    if guess < secretNumber:
        print 'Your guess is too low! Number of guesses left: ' + str(guess_number) + '.'
    elif guess > secretNumber:
        print 'Your guess it too high! Number of guesses left: ' + str(guess_number) + '.'
    else:
        break  # This condition is the correct number!


if guess == secretNumber:
    print 'Good job ' + name + '! You got it! You guessed the correct number! Number of guesses left: ' + str(guess_number) + '.'
else:
    print 'Nope. The number was ' + str(secretNumber)  # This prints when you've run out of guesses
