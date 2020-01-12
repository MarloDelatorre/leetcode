from collections import deque
from itertools import zip_longest
from unittest import main, TestCase

class Solution():
    @staticmethod
    def addStrings(num1, num2):
        sum = deque()
        carry = 0
        for digit in zip_longest(num1[::-1], num2[::-1], fillvalue=0):
            localSum = int(digit[0]) + int(digit[1]) + carry
            sum.appendleft(str(localSum % 10))
            carry = localSum // 10
        if carry > 0:
            sum.appendleft("1")
        return "".join(sum)

class Test(TestCase):
    def test_single_digit(self):
        self.assertEqual(Solution.addStrings("3", "6"), "9")

    def test_single_digit_overflow(self):
        self.assertEqual(Solution.addStrings("9", "1"), "10")

    def test_zeroes(self):
        self.assertEqual(Solution.addStrings("0", "0"), "0")

    def test_multiple_digits(self):
        self.assertEqual(Solution.addStrings("1347", "18"), "1365")

    def test_multiple_digits_overflow(self):
        self.assertEqual(Solution.addStrings("479", "521"), "1000")

if __name__ == '__main__':
    main()