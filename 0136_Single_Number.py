import unittest
from collections import Counter

class Solution():
    @staticmethod
    def singleNumber(nums):
        single = 0
        for num in nums:
            single ^= num
        return single

class Test(unittest.TestCase):
    def test_given_case_1(self):
        self.assertEqual(
            Solution.singleNumber([2, 2, 1]),
            1
        )

    def test_given_case_2(self):
        self.assertEqual(
            Solution.singleNumber([4, 1, 2, 1, 2]),
            4
        )
    
    def test_single_value(self):
        self.assertEqual(
            Solution.singleNumber([1]),
            1
        )

if __name__ == "__main__":
    unittest.main()