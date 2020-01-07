import unittest

MAX_INT = 2**31 - 1

class Solution():
    @staticmethod
    def isPalindrome(x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False 

        reversed_second_half = 0
        while x > reversed_second_half:
            reversed_second_half = reversed_second_half * 10 + x % 10
            x //= 10

        return x == reversed_second_half or x == reversed_second_half // 10
        
class Test(unittest.TestCase):
    def test_given_case1(self):
        self.assertTrue(Solution.isPalindrome(121))

    def test_given_case2(self):
        self.assertFalse(Solution.isPalindrome(-121))

    def test_given_case3(self):
        self.assertFalse(Solution.isPalindrome(10))

    def test_overflow(self):
        self.assertFalse(Solution.isPalindrome(MAX_INT))

if __name__ == '__main__':
    unittest.main()