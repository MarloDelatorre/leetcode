import unittest

class Solution():
    @staticmethod
    def isPalindrome(s):
        s = s.lower()

        left = 0
        right = len(s) - 1
        while True:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left >= right:
                break

            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True


class Test(unittest.TestCase):
    def test_given_cases(self):
        cases = {
            "A man, a plan, a canal: Panama": True,
            "race a car": False,
        }
        for input, expected_output in cases.items():
            self.assertEqual(Solution.isPalindrome(input), expected_output)

    def test_non_alnum_on_ends(self):
        self.assertTrue(Solution.isPalindrome("+_,race+,car+,-."))

    def test_empty_string(self):
        self.assertTrue(Solution.isPalindrome(""))

    def test_only_non_alnum(self):
        self.assertTrue(Solution.isPalindrome("+-."))

    def test_plain_palindrome(self):
        self.assertTrue(Solution.isPalindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(Solution.isPalindrome("not a palindrome"))

if __name__ == '__main__':
    unittest.main()
        