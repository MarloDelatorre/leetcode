import unittest

class Solution():
    @staticmethod
    def twoSum(nums, target):
        numToIndex = {}
        for i, num in enumerate(nums):
            if (diff := target - num) in numToIndex:
                return [numToIndex[diff], i]
            numToIndex[num] = i

        raise Exception("Input must contain a solution")

class Test(unittest.TestCase):
    def test_given_case(self):
        self.assertEqual(
            Solution.twoSum([2, 7, 11, 15], 9),
            [0, 1],
        )

    def test_not_same_index(self):
        actual = Solution.twoSum([2, 7, 2, 15], 4)
        self.assertNotEqual(actual, [0, 0])
        self.assertEqual(actual, [0, 2])

    def test_min_len(self):
        self.assertEqual(
            Solution.twoSum([2, 1], 3),
            [0, 1],
        )

if __name__ == '__main__':
    unittest.main()