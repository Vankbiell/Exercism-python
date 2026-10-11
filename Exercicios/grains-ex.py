number = 70
def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return  print(2 ** (number - 1))
    '''return print(1 << (number - 1)) meio utilizando o método de Bitwise Shift'''
square(number)

def total():
    return print((2 ** 64) - 1)

total()

