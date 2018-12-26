def div42by(divideBy):
    try:
        return 42.0 / divideBy
    except ZeroDivisionError:
        print 'ERROR: You tried to divide by zero'


print div42by(2)
print div42by(12)
print div42by(0)  # ERROR
print div42by(1)
