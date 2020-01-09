import unittest
from collections import Counter

class Solution():
    @staticmethod
    def firstUniqChar(s):
        freq = Counter(s)
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i 

        return -1

class Test(unittest.TestCase):
    def test_given_case1(self):
        self.assertEqual(Solution.firstUniqChar("leetcode"), 0)

    def test_given_case2(self):
        self.assertEqual(Solution.firstUniqChar("loveleetcode"), 2)

    def test_empty_string(self):
        self.assertEqual(Solution.firstUniqChar(""), -1)

    def test_single_char(self):
        self.assertEqual(Solution.firstUniqChar("k"), 0)

    def test_no_unique(self):
        self.assertEqual(Solution.firstUniqChar("eell"), -1)

if __name__ == '__main__':
    unittest.main()
