from heapq import heapify, heappush, heappop
from typing import List
from unittest import TestCase, main

class KthLargest():
    def __init__(self, k: int, nums: List[int]):
        self._mins = nums[:]
        self._k = k
        heapify(self._mins)
        while len(self._mins) > k:
            heappop(self._mins)

    def add(self, val: int):
        heappush(self._mins, val)
        while len(self._mins) > self._k:
            heappop(self._mins)
        return self._mins[0]

class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._kth_largest = KthLargest(3, [4,5,8,2])

    def test_add_values(self):
        cases = [(3, 4), (5, 5), (10, 5), (9, 8), (4, 8)]
        for value, expected in cases:
            with self.subTest(value):
                self.assertEqual(self._kth_largest.add(value), expected)

if __name__ == "__main__":
    main()