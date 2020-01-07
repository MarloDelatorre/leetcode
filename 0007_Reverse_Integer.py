import unittest

MAX_INT = 2**31 - 1

class Solution():
    @staticmethod
    def reverse(x):
        positive = x >= 0
        abs_value = abs(x)
        num_places = Solution.count_places(abs_value)
        reversed_integer = 0

        while abs_value != 0 and abs_value % 10 == 0:
            abs_value //= 10

        while num_places > 0:
            remainder = abs_value % 10
            abs_value //= 10

            reversed_integer += remainder * 10**(num_places - 1)
            num_places -= 1

        if reversed_integer > MAX_INT:
            return 0

        if not positive:
            reversed_integer *= -1

        return reversed_integer 

    @staticmethod
    def count_places(x):
        count = 0
        while x != 0 and x % 10 == 0:
            x //= 10

        while x > 0:
            count += 1
            x //= 10
        return count

class Test(unittest.TestCase):
    def test_given_case_1(self):
        actual = Solution.reverse(123)
        self.assertEqual(actual, 321)

    def test_given_case_2(self):
        actual = Solution.reverse(-123)
        self.assertEqual(actual, -321)

    def test_given_case_3(self):
        actual = Solution.reverse(120)
        self.assertEqual(actual, 21)

    def test_single_positive(self):
        actual = Solution.reverse(3)
        self.assertEqual(actual, 3)

    def test_single_negative(self):
        actual = Solution.reverse(-7)
        self.assertEqual(actual, -7)

    def test_zero(self):
        actual = Solution.reverse(0)
        self.assertEqual(actual, 0)

    def test_positive_overflow(self):
        actual = Solution.reverse(MAX_INT)
        self.assertEqual(actual, 0)

    def test_negative_overflow(self):
        actual = Solution.reverse(-1 * MAX_INT)
        self.assertEqual(actual, 0)

    def test_zero_in_middle(self):
        actual = Solution.reverse(901000)
        self.assertEqual(actual, 109)

if __name__ == '__main__':
    unittest.main()