from typing import List
from unittest import TestCase, main

def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    r1x1, r1y1, r1x2, r1y2 = rec1
    r2x1, r2y1, r2x2, r2y2 = rec2

    return r2x2 > r1x1 and r2x1 < r1x2 and r2y1 < r1y2 and r2y2 > r1y1

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))

    def test_given_case_2(self):
        self.assertFalse(isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))

    def test_horizontal_edges(self):
        self.assertFalse(isRectangleOverlap([0, 0, 1, 1], [0, 1, 1, 2]))

    def test_horizontal_overlap(self):
        self.assertTrue(isRectangleOverlap([0, 0, 2, 1], [1, 0, 3, 1]))

    def test_vertical_edges(self):
        self.assertFalse(isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))

    def test_vertical_overlap(self):
        self.assertTrue(isRectangleOverlap([0, 0, 1, 2], [0, 1, 1, 3]))

if __name__ == "__main__":
    main()