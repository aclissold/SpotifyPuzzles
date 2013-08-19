# reversebinarytest.py
# -*- coding: utf-8 -*-

# Your task will be to write a program for reversing numbers in binary. For
# instance, the binary representation of 13 is 1101, and reversing it gives
# 1011, which corresponds to number 11.
# 
# Input
#
# The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.
# 
# Output
#
# Output one line with one integer, the number we get by reversing the binary
# representation of N.

import unittest
import reversebinary

known_values = (
        ('1', '1'),
        ('2', '10'),
        ('3', '11'),
        ('4', '100'),
        ('5', '101'),
        ('6', '110'),
        ('7', '111'),
        ('8', '1000'),
        ('16', '10000'),
        ('32', '100000'),
        ('64', '1000000'),
        ('437', '110110101'),
        ('8439', '10000011110111'),
        ('34989', '1000100010101101'),
        ('918574', '11100000010000101110'),
        ('1238974', '100101110011110111110'),
        ('43289709', '10100101001000110001101101'),
        ('900654068', '110101101011101110001111110100'),
        ('1000000000', '111011100110101100101000000000')
    )

class TestToReversedBinary(unittest.TestCase):


    def test_to_reversed_binary_known_values(self):
        '''to_reversed_binary should return reversed binary versions of ints'''
        for decimal, binary in known_values:
            expected = binary[::-1]
            found = reversebinary.to_reversed_binary(decimal)
            self.assertEqual(expected, found)

    def test_to_reversed_binary_out_of_range(self):
        '''to_reversed_binary should fail for !(1 <= N <= 1000000000)'''
        for value in ('-1', '0', '1000000001'):
            self.assertRaises(reversebinary.OutOfRangeError,
                    reversebinary.to_reversed_binary, value)


class TestToDecimal(unittest.TestCase):
    def test_to_decimal_known_values(self):
        for known_decimal, binary in known_values:
            found_decimal = reversebinary.to_decimal(binary)
            self.assertEqual(known_decimal, found_decimal)


if __name__ == '__main__':
    unittest.main()
