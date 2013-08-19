# reversebinary.py

def main():
    '''Reverse numbers in binary.

    For instance, the binary representation of 13 is 1101, and reversing it
    gives 1011, which corresponds to the number 11.
    '''

    decimal_in      = read_input()
    reversed_binary = to_reversed_binary(decimal_in)
    decimal_out     = to_decimal(reversed_binary)

    print decimal_out

def read_input():
    '''Return a string representation of an integer value'''
    decimal_in = raw_input()
    return decimal_in

def to_reversed_binary(decimal_in):
    '''Convert a decimal value to its reversed binary (as strings)'''
    # Input validation
    try:
        value = int(decimal_in)
    except ValueError:
        print 'You must enter an integer N where 1 <= N <= 1000000000.'
        exit(0)
    if not 1 <= value <= 1000000000:
        raise OutOfRangeError

    # Build a reversed binary representation of a decimal value
    reversed_binary = ''
    while value != 0:
        # "remainder" will be 0 or 1--the bit to use in the binary string
        remainder = value % 2
        value /= 2 # Integer division
        # Append the bit on the right of the string, building it in reverse
        # to avoid unnecessary conversions later
        reversed_binary += str(remainder)
    return reversed_binary

def to_decimal(reversed_binary):
    '''Convert a binary value to its decimal representation (as strings)'''
    decimal = 0
    # Scan "reversed_binary" from right to left, building "decimal" using the
    # binary -> decimal formula (if a given bit == 1, add to a running summation
    # the base we're converting from raised to that bit's position).
    for i in range(0, len(reversed_binary)):
        if reversed_binary[-i-1] == '1':
            decimal += 2 ** i
    return str(decimal) 

# For input validation
class OutOfRangeError(ValueError): pass

if __name__ == '__main__':
    main()
