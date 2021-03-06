from unittest import main
from testutil import MatrixTestCase

def transpose(A):
    m, n = len(A), len(A[0])
    transposed = []
    for col in range(n):
        transposed.append([])
        for row in range(m):
            transposed[col].append(A[row][col])
    return transposed

class Test(MatrixTestCase):
    def test_given_case_1(self):
        transposed = transpose([
            [1, 2 ,3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        expected = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        self.assert_matrix_equal(transposed, expected)

    def test_given_case_2(self):
        transposed = transpose([
            [1, 2, 3],
            [4, 5, 6]
        ])
        expected = [
            [1, 4],
            [2, 5],
            [3, 6]
        ]
        self.assert_matrix_equal(transposed, expected)

    def test_single_value(self):
        self.assert_matrix_equal([[1]], [[1]])

if __name__ == "__main__":
    main()