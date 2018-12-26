print 'How many cats do you have?'
numCats = raw_input()
try:
    if int(numCats) >= 4:
        print 'That is a lot of cats'
    if int(numCats) < 0:
        print 'You cannot have negative cats.'
    else:
        print 'That is not many cats. You should adopt more cats.'
except ValueError:
    print 'You did not enter a number. Please try again.'


