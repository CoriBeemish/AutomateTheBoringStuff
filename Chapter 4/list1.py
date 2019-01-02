# Author: Cori Beemish
# Date: December 27th, 2018

spam = ['cat', 'bat', 'rat', 'elephant']
print spam  # ['cat', 'bat', 'rat', 'elephant']
print spam[2]  # rat
print spam[-1]  # elephant

spam[0] = 'Hello'
print spam  # ['Hello', 'bat', 'rat', 'elephant']

spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print spam  # ['Hello', 'CAT', 'DOG', 'MOUSE', 'elephant']

print spam[1:]  # ['CAT', 'DOG', 'MOUSE', 'elephant']

del spam[-1]
print spam  # ['Hello', 'CAT', 'DOG', 'MOUSE']

print list(spam[1])  # ['C', 'A', 'T']
print 'CAT' in spam  # True


