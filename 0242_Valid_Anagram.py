import unittest
from collections import Counter

class Solution():
    @staticmethod
    def isAnagram(s, t):
        return Counter(s) == Counter(t)

class Test(unittest.TestCase):
    def test_given_case_1(self):
        self.assertTrue(Solution.isAnagram("anagram", "nagaram"))

    def test_given_case_2(self):
        self.assertFalse(Solution.isAnagram("rat", "car"))

    def test_empty_strings(self):
        self.assertTrue(Solution.isAnagram("", ""))

    def test_empty_non_empty(self):
        self.assertFalse(Solution.isAnagram("", "anagram"))

if __name__ == "__main__":
    unittest.main()