import unittest

class Solution():
    @staticmethod
    def majorityElement(nums):
        count = 0
        majority = None
        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority 


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