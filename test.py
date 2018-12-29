from fractions import Fraction
import unittest

import fractionfun

class TestFractionStringFunctions(unittest.TestCase):
    def roundtrip(self, value):
        fraction = fractionfun.mixed_number_to_fraction(value)
        new_value = fractionfun.fraction_to_mixed_number_string(fraction)
        self.assertEqual(value, new_value)

    def test_zero(self):
        self.roundtrip("0")

    def test_whole(self):
        self.roundtrip("5")

    def test_fraction(self):
        self.roundtrip("1/2")

    def test_mixed(self):
        self.roundtrip("1_1/2")

    def test_negative_whole(self):
        self.roundtrip("-5")

    def test_negative_fraction(self):
        self.roundtrip("-1/2")

    def test_negative_mixed(self):
        self.assertEqual("-1_1/2", fractionfun.fraction_to_mixed_number_string(Fraction(-3, 2)))
        self.roundtrip("-1_1/2")

if __name__ == '__main__':
    unittest.main()