spam = ['hello', 'hi', 'howdy', 'HELLO!']
print spam.index('hello')

ham = ['green', 'eggs', 'ham']
print ham.index('eggs')

index_number = ham.index('eggs') + spam.index('hi')
print index_number

print ham[index_number]
print spam[index_number]


