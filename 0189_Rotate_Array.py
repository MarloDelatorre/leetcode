from typing import List
from unittest import TestCase, main

def rotate(nums: List[int], k: int) -> None:
    k %= len(nums) or 1
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums

def reverse(nums: List[int], start, end) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            rotate([1, 2, 3, 4, 5, 6, 7], 3),
            [5, 6, 7, 1, 2, 3, 4]
        )

    def test_given_case_2(self):
        self.assertListEqual(
            rotate([-1, -100, 3, 99], 2),
            [3, 99, -1, -100]
        )

    def test_empty_list(self):
        self.assertEqual(rotate([], 4), [])

if __name__ == "__main__":
    main()