# This is a guess the number game.
import random

print 'Hello! What is your name?'
name = raw_input()
secretNumber = random.randint(1,20)
print 'Well, ' + name + ', I am thinking of a number between 1 and 20.'

for guessesTaken in range(1, 7):
    print 'Take a guess!'
    guess = int(input())
    if guess < secretNumber:
        print 'Your guess is too low!'
    elif guess > secretNumber:
        print 'Your guess it too high!'
    else:
        break  # This condition is the correct number!


if guess == secretNumber:
    print 'Good job ' + name + '! You got it! You guessed the correct number!'
else:
    print 'Nope. The number was ' + str(secretNumber)  # This prints when you've run out of guesses
