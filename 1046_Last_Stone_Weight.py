from heapq import heapify, heappush, heappop
from unittest import main, TestCase

class Solution():
    @staticmethod
    def lastStoneWeight(stones):
        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            stone_y, stone_x = heappop(heap), heappop(heap)
            if stone_x != stone_y:
                heappush(heap, stone_y - stone_x)

        return -heappop(heap) if heap else 0

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(Solution.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)

    def test_empty_case(self):
        self.assertEqual(Solution.lastStoneWeight([]), 0)

    def test_all_same_values(self):
        self.assertEqual(Solution.lastStoneWeight([2, 2, 2, 2]), 0)

if __name__ == '__main__':
    main()