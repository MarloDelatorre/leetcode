from typing import List
from unittest import main

from testutil import MatrixTestCase

def setZeroes(matrix: List[List[int]]) -> None:
    first_row = False
    first_col = False
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 0:
                if row == 0:
                    first_row = True
                if col == 0:
                    first_col = True
                matrix[row][0] = 0
                matrix[0][col] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if first_row:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0

    if first_col:
        for row in range(len(matrix)):
            matrix[row][0] = 0

    return matrix

class Test(MatrixTestCase):
    def test_given_case_1(self):
        self.assert_matrix_equal(
            setZeroes([
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ]),
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]
            ]
        )

    def test_given_case_2(self):
        self.assert_matrix_equal(
            setZeroes([
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]
            ]),
            [
                [0, 0, 0, 0],
                [0, 4, 5, 0],
                [0, 3, 1, 0]
            ]
        )

    def test_given_case_3(self):
        self.assert_matrix_equal(
            setZeroes([
                [1, 1, 1],
                [0, 1, 2]
            ]),
            [
                [0, 1, 1],
                [0, 0, 0]
            ]
        )

if __name__ == "__main__":
    main()