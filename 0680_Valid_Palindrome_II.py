from unittest import TestCase, main

def validPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return isPalindrome(s[left:right]) or isPalindrome(s[left + 1:right + 1])
        left += 1
        right -= 1
    return True

def isPalindrome(s):
    return s == s[::-1] 

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(validPalindrome("aba"))

    def test_given_case_2(self):
        self.assertTrue(validPalindrome("abca"))

    def test_two_removals(self):
        self.assertFalse(validPalindrome("acbda"))

if __name__ == "__main__":
    main()