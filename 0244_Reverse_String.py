import unittest

class Solution():
    @staticmethod
    def reverseString(s):
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return s

class Test(unittest.TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            Solution.reverseString(["h","e","l","l","o"]),
            ["o","l","l","e","h"]
        )
    
    def test_given_case_2(self):
        self.assertListEqual(
            Solution.reverseString(["H","a","n","n","a","h"]),
            ["h","a","n","n","a","H"]
        )

    def test_empty_list(self):
        self.assertListEqual(
            Solution.reverseString([]),
            []
        )

    def test_single_value(self):
        self.assertListEqual(
            Solution.reverseString(["k"]),
            ["k"]
        )

if __name__ == "__main__":
    unittest.main()