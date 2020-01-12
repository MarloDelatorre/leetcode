from unittest import main, TestCase
from collections import deque
from itertools import zip_longest

class Solution():
    @staticmethod
    def addBinary(a, b):
        binary_sum = deque()
        carry = 0

        for digits in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            digit_a, digit_b = int(digits[0]), int(digits[1])
            local_sum = digit_a + digit_b + carry
            binary_sum.appendleft(str(local_sum % 2))
            carry = local_sum >> 1 
        
        if carry & 1:
            binary_sum.appendleft("1")

        return "".join(binary_sum) 

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(Solution.addBinary("11", "1"), "100")

    def test_given_case_2(self):
        self.assertEqual(Solution.addBinary("1010", "1011"), "10101")

    def test_zero_case(self):
        self.assertEqual(Solution.addBinary("0", "0"), "0")

if __name__ == "__main__":
    main()