# reversebinary.py

def main():
    decimal_in      = read_input()
    reversed_binary = to_reversed_binary(decimal_in)
    decimal_out     = to_decimal(reversed_binary)

    display_results(decimal_out)

def read_input():
    '''Return a string representation of an integer value'''
    decimal_in = raw_input()
    return decimal_in

def to_reversed_binary(decimal_in):
    '''Convert a decimal value to its reversed binary (as strings)'''
    value = int(decimal_in)
    if not 1 <= value <= 1000000000:
        raise OutOfRangeError
    reversed_binary = ''
    while value != 0:
        remainder = value % 2
        value /= 2
        reversed_binary += str(remainder)
    return reversed_binary

def to_decimal(reversed_binary):
    pass

def display_results(decimal_out):
    pass

class OutOfRangeError(ValueError): pass

if __name__ == '__main__':
    main()
