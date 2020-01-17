from typing import List
from unittest import TestCase, main

def findLengthOfLCIS(nums: List[int]) -> int:
    if not nums:
        return 0
    
    count = max_count = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1 
            max_count = max(max_count, count)
        else:
            count = 1

    return max_count

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(findLengthOfLCIS([1, 3, 5, 4, 7]), 3)

    def test_given_case_2(self):
        self.assertEqual(findLengthOfLCIS([2, 2, 2, 2, 2]), 1)

    def test_empty_list(self):
        self.assertEqual(findLengthOfLCIS([]), 0)

if __name__ == "__main__":
    main()