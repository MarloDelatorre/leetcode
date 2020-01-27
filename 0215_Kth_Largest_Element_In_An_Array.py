from heapq import heapify, heappop
from typing import List
from unittest import TestCase, main

def findKthLargest(nums: List[int], k: int) -> int:
    heapify(nums := [-num for num in nums])
    for _ in range(k - 1):
        heappop(nums)
    return -nums[0]

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_given_case_2(self):
        self.assertEqual(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

if __name__ == "__main__":
    main()
