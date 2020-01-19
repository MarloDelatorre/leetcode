from typing import List
from unittest import TestCase, main

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    two_back = nums[0]
    one_back = max(nums[1], two_back)

    for i in range(2, len(nums)):
        two_back, one_back = one_back, max(nums[i] + two_back, one_back)

    return max(two_back, one_back)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(rob([1, 2, 1, 1]), 4)

    def test_given_case_2(self):
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)

    def test_no_houses(self):
        self.assertEqual(rob([]), 0)

    def test_one_house(self):
        self.assertEqual(rob([4]), 4)

    def test_two_houses(self):
        self.assertEqual(rob([1, 2]), 2)

    def test_should_skip_two_houses(self):
        self.assertEqual(rob([2, 1, 1, 4]), 6)
    
if __name__ == "__main__":
    main()