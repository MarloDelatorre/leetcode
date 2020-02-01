from math import floor
from typing import List, Tuple
from unittest import TestCase, main

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix: return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = floor(left / 2 + right / 2)
        mid_row, mid_col = convert_1D_to_2D(mid, n)
        mid_num = matrix[mid_row][mid_col]

        if target < mid_num:
            right = mid - 1
        elif target > mid_num:
            left = mid + 1
        else:
            return True
    
    return False

def convert_1D_to_2D(index: int, num_cols: int) -> Tuple[int, int]:
    return (index // num_cols, index % num_cols)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(
            searchMatrix([
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ], 3)
        )

    def test_given_case_2(self):
        self.assertFalse(
            searchMatrix([
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ], 13)
        )

    def test_empty_matrix(self):
        self.assertFalse(searchMatrix([], 0))

    def test_single_value_absent(self):
        self.assertFalse(searchMatrix([[1]], 0))

    def test_single_value_present(self):
        self.assertTrue(searchMatrix([[1]], 1))
    
if __name__ == "__main__":
    main()