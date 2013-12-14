# Reversed Binary Numbers

def reversed_binary(decimal):
    '''Return a decimal number as if its binary value were reversed.

    For instance, the binary representation of 13 is 1101, and reversing it
    gives 1011, which corresponds to the number 11.
    '''

    # An example of reversed_binary(47):
    #     bin(47) returns '0b101111'
    #     '0b101111'[:1:-1] returns its last downto 2nd char, i.e. reverses it
    #     int('111101', 2) converts the base 2 string to an int.

    return int(bin(decimal)[:1:-1], 2)

if __name__ == '__main__':
    print reversed_binary(int(raw_input()))

# Bonus: this entire program can fit comfortably on one line:
# print int(bin(int(raw_input()))[:1:-1], 2)
