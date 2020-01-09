import unittest
from collections import Counter

class Solution():
    @staticmethod
    def majorityElement(nums):
        return Counter(nums).most_common(1)[0][0]

class Test(unittest.TestCase):
    def test_given_case_1(self):
        self.assertEqual(
            Solution.majorityElement([3, 2, 3]),
            3
        )

    def test_given_case_2(self):
        self.assertEqual(
            Solution.majorityElement([2, 2, 1, 1, 1, 2, 2]),
            2
        )

    def test_single_value(self):
        self.assertEqual(
            Solution.majorityElement([1]),
            1
        )

if __name__ == "__main__":
    unittest.main()