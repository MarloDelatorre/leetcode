import unittest

MAX_INT = 2**31 - 1

class Solution():
    @staticmethod
    def isPalindrome(x):
        if x < 0:
            return False 

        try:
            reversed_x = Solution.reverse(x)
            return reversed_x == x
        except:
            return False

    @staticmethod
    def reverse(x):
        reversed_integer = 0

        while x > 0:
            reversed_integer = reversed_integer * 10 + x % 10 
            x //= 10

        if reversed_integer > MAX_INT:
            raise ValueError('Could not reverse integer due to overflow')

        return reversed_integer

        
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