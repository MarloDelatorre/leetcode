from unittest import TestCase

class MatrixTestCase(TestCase):
    def assert_matrix_equal(self, A, B):
        self.assertEqual(len(A), len(B))
        self.assertEqual(len(A[0]), len(B[0]))

        for row in range(len(A)):
            for col in range(len(A[0])):
                self.assertEqual(A[row][col], B[row][col])