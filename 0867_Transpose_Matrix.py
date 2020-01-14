from unittest import main, TestCase

def transpose(A):
    m, n = len(A), len(A[0])
    transposed = []
    for col in range(n):
        transposed.append([])
        for row in range(m):
            transposed[col].append(A[row][col])
    return transposed

class Test(TestCase):
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

    def assert_matrix_equal(self, A, B):
        self.assertEqual(len(A), len(B))
        self.assertEqual(len(A[0]), len(B[0]))

        for row in range(len(A)):
            for col in range(len(A[0])):
                self.assertEqual(A[row][col], B[row][col])
            
if __name__ == "__main__":
    main()