from typing import List
from unittest import TestCase, main

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = int(left / 2 + right / 2)
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_given_case_2(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_answer_in_left(self):
        self.assertEqual(search([7, 0, 1, 2, 4, 5, 6], 0), 1)

    def test_answer_in_right(self):
        self.assertEqual(search([7, 0, 1, 2, 4, 5, 6], 5), 5)

    def test_first_number(self):
        self.assertEqual(search([7, 0, 1, 2, 4, 5, 6], 7), 0)
    
    def test_last_number(self):
        self.assertEqual(search([7, 0, 1, 2, 4, 5, 6], 6), 6)

if __name__ == "__main__":
    main()