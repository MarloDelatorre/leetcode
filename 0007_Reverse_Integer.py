import unittest

MAX_INT = 2**31 - 1

class Solution():
    @staticmethod
    def reverse(x):
        abs_value = abs(x)
        reversed_integer = 0

        while abs_value > 0:
            remainder = abs_value % 10
            abs_value //= 10
            reversed_integer *= 10
            reversed_integer += remainder

        if reversed_integer > MAX_INT:
            return 0
        return reversed_integer if x >= 0 else -reversed_integer

class Test(unittest.TestCase):
    def test_given_case_1(self):
        self.assertEqual(Solution.reverse(123), 321)

    def test_given_case_2(self):
        self.assertEqual(Solution.reverse(-123), -321)

    def test_given_case_3(self):
        self.assertEqual(Solution.reverse(120), 21)

    def test_single_positive(self):
        self.assertEqual(Solution.reverse(3), 3)

    def test_single_negative(self):
        self.assertEqual(Solution.reverse(-7), -7)

    def test_zero(self):
        self.assertEqual(Solution.reverse(0), 0)

    def test_positive_overflow(self):
        self.assertEqual(Solution.reverse(MAX_INT), 0)

    def test_negative_overflow(self):
        self.assertEqual(Solution.reverse(-1 * MAX_INT), 0)

    def test_zero_in_middle(self):
        self.assertEqual(Solution.reverse(901000), 109)

if __name__ == '__main__':
    unittest.main()