import unittest

class Solution():
    @staticmethod
    def maxSubArray(nums):
        sum = 0
        max_value = float("-inf") 

        for num in nums:
           sum += num 
           if sum > max_value:
               max_value = sum
           if sum < 0:
               sum = 0

        return max_value if nums else 0

class Test(unittest.TestCase):
    def test_given_case(self):
        self.assertEqual(
            Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
            6
        )

    def test_empty_list(self):
        self.assertEqual(Solution.maxSubArray([]), 0)

    def test_zero_value(self):
        self.assertEqual(Solution.maxSubArray([0]), 0)

    def test_positives_values(self):
        self.assertEqual(Solution.maxSubArray([1,2,3,0,7]), 13)

    def test_negatives_values(self):
        self.assertEqual(Solution.maxSubArray([-2,-3,-1,-5]), -1)

if __name__ == '__main__':
    unittest.main()