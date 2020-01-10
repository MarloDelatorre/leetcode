import unittest

class Solution():
    @staticmethod
    def findDisappearedNumbers(nums):
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        print(nums)
        return [index + 1 for index, num in enumerate(nums) if num > 0]

class Test(unittest.TestCase):
    def test_given_case(self):
        self.assertListEqual(
            Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]),
            [5, 6]
        )

    def test_single_value(self):
        self.assertListEqual(
            Solution.findDisappearedNumbers([1]),
            []
        )

    def test_all_present(self):
        self.assertListEqual(
            Solution.findDisappearedNumbers([1, 2, 3, 4, 5, 6]),
            []
        )

if __name__ == '__main__':
    unittest.main()