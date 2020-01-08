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
        actual = Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(actual, 6)

    def test_empty_list(self):
        actual = Solution.maxSubArray([])
        self.assertEqual(actual, 0)

    def test_zero_value(self):
        actual = Solution.maxSubArray([0])
        self.assertEqual(actual, 0)

    def test_positives_values(self):
        actual = Solution.maxSubArray([1,2,3,0,7])
        self.assertEqual(actual, 13)

    def test_negatives_values(self):
        actual = Solution.maxSubArray([-2,-3,-1,-5])
        self.assertEqual(actual, -1)

if __name__ == '__main__':
    unittest.main()