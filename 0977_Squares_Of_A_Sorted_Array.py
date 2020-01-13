from unittest import main, TestCase

class Solution():
    @staticmethod
    def sortedSquares(A):
        sorted_squares = []

        for i in range(len(A)):
            A[i] *= A[i]

        positive_index = 0
        negative_index = -1
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                positive_index = i
                negative_index = i - 1
        
        while positive_index < len(A) or negative_index >= 0:
            if positive_index >= len(A):
                sorted_squares.append(A[negative_index])
                negative_index -= 1
            elif negative_index < 0:
                sorted_squares.append(A[positive_index])
                positive_index += 1
            elif A[positive_index] <= A[negative_index]:
                sorted_squares.append(A[positive_index])
                positive_index += 1
            else:
                sorted_squares.append(A[negative_index])
                negative_index -= 1

        return sorted_squares

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            Solution.sortedSquares([-4, -1, 0, 3, 10]),
            [0, 1, 9, 16, 100]
        )

    def test_given_case_2(self):
        self.assertListEqual(
            Solution.sortedSquares([-7, -3, 2, 3, 11]),
            [4, 9, 9, 49, 121]
        ) 

    def test_single_value(self):
        self.assertListEqual(
            Solution.sortedSquares([4]),
            [16]
        )

    def test_all_negative(self):
        self.assertListEqual(
            Solution.sortedSquares([-7, -4, -3, -1]),
            [1, 9, 16, 49]
        )

if __name__ == "__main__":
    main()