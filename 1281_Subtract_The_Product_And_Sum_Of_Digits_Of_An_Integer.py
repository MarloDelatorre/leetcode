from unittest import main, TestCase
from functools import reduce
import operator

def subtractProductAndSum(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    digit_sum = sum(digits)
    digit_product = reduce(operator.mul , digits) if digits else 0
    return digit_product - digit_sum

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(subtractProductAndSum(234), 15)

    def test_given_case_2(self):
        self.assertEqual(subtractProductAndSum(4421), 21)

    def test_zero(self):
        self.assertEqual(subtractProductAndSum(0), 0)

    def test_large_number(self):
        self.assertEqual(subtractProductAndSum(12345), 105)

if __name__ == '__main__':
    main()